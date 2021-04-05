
SHELL := /bin/bash


install-deps: deps
	pip-sync requirements.txt

deps:
	pip install --upgrade pip pip-tools
	pip-compile requirements.in

lint:
	flake8 --config ./.flake8 --show-source --statistics src

test:
	cd src && pytest -x

twit:
	run.sh