.PHONY: all ensure-uv install version

UV_INSTALLED := $(shell command -v uv)

all: version

ensure-uv:
ifndef UV_INSTALLED
		@echo "Installing the uv package manager and dev requirements."
		python -m pip install --upgrade pip
		python -m pip install --upgrade uv 
endif

version: ensure-uv 
	uv run happystudy --version

test: ensure-uv 
	uv run pytest

check-version: ensure-uv 
	uv run invoke check-version

tag-release: ensure-uv 
	uv run invoke tag-release

bump-version: ensure-uv 
	uv version --bump patch | tail -n 1 | sed 's/^Bumping/Bump/'
