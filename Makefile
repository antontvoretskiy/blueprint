SHELL := /bin/bash

ENV_FILE ?= .env.local
COMPOSE_ENV := $(if $(wildcard $(ENV_FILE)),--env-file $(ENV_FILE),--env-file .env.example)
COMPOSE := docker compose $(COMPOSE_ENV)

.PHONY: init doctor config up down restart ps logs smoke clean

init:
	@if [[ ! -f "$(ENV_FILE)" ]]; then cp .env.example "$(ENV_FILE)"; echo "created $(ENV_FILE)"; else echo "$(ENV_FILE) already exists"; fi

doctor: init
	@set -euo pipefail; \
	set -a; source "$(ENV_FILE)"; set +a; \
	project="$${COMPOSE_PROJECT_NAME:-blueprint-dev}"; \
	bind_host="$${BLUEPRINT_BIND_HOST:-127.0.0.1}"; \
	owned_ports="$$(docker ps --filter "label=com.docker.compose.project=$${project}" --format '{{.Ports}}' 2>/dev/null || true)"; \
	project_containers="$$(docker ps --filter "label=com.docker.compose.project=$${project}" --format '{{.Names}}' 2>/dev/null || true)"; \
	failed=0; \
	check_port() { \
		name="$$1"; port="$$2"; \
		if lsof -nP -iTCP:"$${port}" -sTCP:LISTEN >/tmp/blueprint-port-check 2>/dev/null; then \
			if grep -q ":$${port}->" <<<"$${owned_ports}"; then \
				printf "  ok   %-12s %s:%s already owned by %s\n" "$${name}" "$${bind_host}" "$${port}" "$${project}"; \
			else \
				printf "  fail %-12s %s:%s is already in use\n" "$${name}" "$${bind_host}" "$${port}"; \
				sed 's/^/       /' /tmp/blueprint-port-check; \
				failed=1; \
			fi; \
		else \
			printf "  ok   %-12s %s:%s free\n" "$${name}" "$${bind_host}" "$${port}"; \
		fi; \
	}; \
	echo "Blueprint environment"; \
	echo "  project: $${project}"; \
	echo "  bind:    $${bind_host}"; \
	echo; \
	echo "Port check"; \
	check_port app "$${BLUEPRINT_APP_PORT:-3231}"; \
	check_port api "$${BLUEPRINT_API_PORT:-8231}"; \
	check_port postgres "$${BLUEPRINT_POSTGRES_PORT:-55461}"; \
	check_port redis "$${BLUEPRINT_REDIS_PORT:-6406}"; \
	check_port mailpit_web "$${BLUEPRINT_MAILPIT_WEB_PORT:-8046}"; \
	check_port mailpit_smtp "$${BLUEPRINT_MAILPIT_SMTP_PORT:-1046}"; \
	rm -f /tmp/blueprint-port-check; \
	echo; \
	echo "Docker namespace check"; \
	if [[ -n "$${project_containers}" ]]; then \
		echo "  ok   compose project '$${project}' is active and namespaced"; \
	else \
		echo "  ok   compose project '$${project}' is not active yet"; \
	fi; \
	if docker network ls --format '{{.Name}}' 2>/dev/null | grep -Fxq "$${project}_blueprint"; then \
		echo "  ok   network '$${project}_blueprint' exists and is namespaced"; \
	else \
		echo "  ok   network '$${project}_blueprint' is not active yet"; \
	fi; \
	if docker volume ls --format '{{.Name}}' 2>/dev/null | grep -Eq "^$${project}_(postgres-data|redis-data)$$"; then \
		echo "  ok   project volumes exist and are namespaced"; \
	else \
		echo "  ok   project volumes are not active yet"; \
	fi; \
	if [[ "$${failed}" -ne 0 ]]; then \
		echo; \
		echo "Doctor failed: change the port values in $(ENV_FILE) before starting the stack."; \
		exit 1; \
	fi; \
	echo; \
	echo "Doctor passed."

config: init
	@$(COMPOSE) config --quiet

up: init config
	@$(COMPOSE) up -d --build

down:
	@$(COMPOSE) down

restart: down up

ps:
	@$(COMPOSE) ps

logs:
	@$(COMPOSE) logs -f --tail=100

smoke:
	@set -a; source "$(ENV_FILE)"; set +a; \
	curl -fsS "http://$${BLUEPRINT_BIND_HOST}:$${BLUEPRINT_APP_PORT}/" >/dev/null; \
	curl -fsS "http://$${BLUEPRINT_BIND_HOST}:$${BLUEPRINT_API_PORT}/" >/dev/null; \
	echo "smoke ok: app=$${BLUEPRINT_BIND_HOST}:$${BLUEPRINT_APP_PORT}, api=$${BLUEPRINT_BIND_HOST}:$${BLUEPRINT_API_PORT}"

clean:
	@$(COMPOSE) down --volumes --remove-orphans
