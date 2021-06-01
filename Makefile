.DEFAULT_GOAL := help
.PHONY: install-dev-deps install-deps help lint test tox

SHELL := /bin/bash

install-dev-deps: install-deps  ## Sync dev requirements
	poetry install

install-deps:  ## Sync requirements
	poetry install --no-dev

coverage:  ## Run tests with coverage
	poetry run coverage erase
	poetry run coverage run --include=src/twtrexcs/* -m pytest -ra
	poetry run coverage report -m

lint:  ## Lint and static-check
	poetry run flake8 src/twtrexcs/
	poetry run pylint --disable=C0305 --output-format=colorized src/twtrexcs/
	poetry run mypy src/twtrexcs/

test:  ## Run tests
	poetry run pytest -x

tox:   ## Run tox
	poetry run tox

help:  ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done

twit:  ## Post in Twitter
	source ./.env && poetry run twtrexcs
