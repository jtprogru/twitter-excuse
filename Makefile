
SHELL := /bin/bash


install-dev-deps: dev-deps
	pip-sync requirements.txt dev-requirements.txt

install-deps: deps
	pip-sync requirements.txt

deps:
	pip install --upgrade pip pip-tools
	pip-compile requirements.in

dev-deps: deps
	pip-compile dev-requirements.in

lint:
	flake8 --config ./.flake8 --show-source --statistics src

test:
	cd src && pytest -x

twit:
	run.sh
