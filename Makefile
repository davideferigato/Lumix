# Makefile per Lumix

.PHONY: help install install-dev test lint format clean docker-build publish

help:
	@echo "Available targets:"
	@echo "  install      : install in production mode"
	@echo "  install-dev  : install in editable mode with dev dependencies"
	@echo "  test         : run pytest with coverage"
	@echo "  lint         : run flake8 (if installed)"
	@echo "  format       : run black and isort"
	@echo "  clean        : remove __pycache__, .pytest_cache, dist, etc."
	@echo "  docker-build : build Docker image"
	@echo "  publish      : build and upload to PyPI (requires PyPI token)"

install:
	pip install .

install-dev:
	pip install -e .[dev]

test:
	pytest tests/ --cov=lumix --cov-report=term-missing

lint:
	flake8 lumix/ tests/

format:
	black lumix/ tests/
	isort lumix/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .coverage htmlcov/ dist/ build/ *.egg-info/

docker-build:
	docker build -t lumix .

publish:
	rm -rf dist/ build/ *.egg-info
	python -m build
	twine upload dist/*
