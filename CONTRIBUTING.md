# Contributing to Lumix

We love your input! We want to make contributing to this project as easy and transparent as possible.

## Development Process

1. Fork the repo and create your branch from `main`.
2. If you've added code, add tests.
3. Ensure the test suite passes (`pytest`).
4. Make sure your code follows the existing style (we use `black`).
5. Issue that pull request!

## Adding a New Converter

1. Create a new folder under `lumix/` with the name of your converter (e.g., `myconverter`).
2. Implement at least:
   - `__init__.py`
   - `convert.py` – the core conversion logic.
   - `parser.py` – CLI parsing and localization.
3. Add tests in `tests/test_myconverter.py`.
4. Update the language maps in `lumix/cli/main.py` (add entries for each language).
5. Add an example script in `examples/example_myconverter.sh`.
6. Run `pytest` to verify everything works.

## Reporting Bugs

Use the issue tracker. Include as much detail as possible: version, OS, steps to reproduce.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
