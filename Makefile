.DEFAULT_GOAL := help
.PHONY: install-dev-deps install-deps dev-deps deps help lint test tox

SHELL := /bin/bash

install-dev-deps: dev-deps  ## Sync dev requirements
	pip-sync requirements.txt dev-requirements.txt

install-deps: deps  ## Sync requirements
	pip-sync requirements.txt

deps:  ## Compile requirements
	pip install --upgrade pip pip-tools
	pip-compile requirements.in

dev-deps: deps  ## Compile dev requirements
	pip-compile dev-requirements.in


coverage:  ## Run tests with coverage
	python -m coverage erase
	python -m coverage run --include=src/twtrexcs/* -m pytest -ra
	python -m coverage report -m

lint:  ## Lint and static-check
	python -m flake8 src/twtrexcs/
	python -m pylint --disable=C0305 --output-format=colorized src/twtrexcs/
	python -m mypy src/twtrexcs/

test:  ## Run tests
	python -m pytest -x

tox:   ## Run tox
	python -m tox

help: ## Show help message
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
	run.sh
