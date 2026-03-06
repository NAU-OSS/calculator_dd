# Calculator DD

A small, well-tested Python calculator library and learning project that demonstrates clear project structure, automated testing, and contribution workflows. Designed as a friendly place for beginners to learn open source contribution practices while providing a simple, useful library for arithmetic operations.

## Table of Contents

- [Project overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Quick start and usage](#quick-start-and-usage)
- [Development setup](#development-setup)
- [Testing](#testing)
- [Project status & roadmap](#project-status--roadmap)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Contact & community](#contact--community)

## Project overview

`Calculator DD` provides a minimal, modular calculator implemented in `src/` with a focused test suite in `tests/`. The goal is educational and production-sensible: easy to read, simple to extend, and suitable for demonstrating CI, code review, and contribution processes.

## Features

- Basic arithmetic: `add`, `subtract` (core functions)
- Clean module layout (`src/` and `tests/`)
- Unit tests and usage examples
- Contribution guidelines and a welcoming Code of Conduct

## Installation

Clone the repository and create an isolated Python environment (Windows example):

```bash
git clone https://github.com/NAU-OSS/calculator_dd.git
cd calculator_dd
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt  # optional for development tools
```

No external dependencies are required for the core calculator. If `requirements.txt` is present it contains development/test dependencies.

## Quick start and usage

Import the library and call functions directly:

```python
from src.calculator import add, subtract

print(add(2, 3))       # 5
print(subtract(10, 4)) # 6
```

For interactive exploration:

```bash
.\.venv\Scripts\activate
python
>>> from src.calculator import add
>>> add(1,2)
```

## Development setup

Recommended contributor workflow:

1. Fork the repository on GitHub.
2. Create a feature branch: `git checkout -b feat/your-feature`.
3. Implement changes and add tests under `tests/`.
4. Run tests and linters locally.
5. Open a Pull Request describing the change and linking any related issue.

Suggested dev tools: `pre-commit`, `black`, `flake8`, and CI workflows in `.github/workflows/`.

## Testing

Run the full test suite with unittest discovery:

```bash
python -m unittest discover -s tests
```

If `pytest` is added, run:

```bash
pytest
```

## Project status & roadmap

**Status:** Active — small educational project.

Planned improvements:

- Expand operations: multiply, divide, power
- Add robust input validation and error handling
- Provide a CLI wrapper for quick calculations
- Add `examples/` and developer tutorials
- Add CI checks and coverage reporting

If you plan to work on an item, open an issue or claim a task labeled `good first issue`.

## Contributing

We welcome contributions of all sizes:

- Read `CONTRIBUTING.md` for process and style guidelines.
- Open an issue to discuss major changes before implementing.
- Write tests for new behavior and ensure all tests pass.
- Keep commits small and focused; use meaningful commit messages.

Maintainers will review PRs and provide constructive feedback.

## Code of Conduct

This project follows a Code of Conduct to foster an open, welcoming community. See `CODE_OF_CONDUCT.md` for details.

## License

This project is provided under the MIT License. See `LICENSE` for full license text.

## Contact & community

Use GitHub Issues and Pull Requests for support and contributions:

- Repository: https://github.com/NAU-OSS/calculator_dd
- Issues: https://github.com/NAU-OSS/calculator_dd/issues
- Pull requests: https://github.com/NAU-OSS/calculator_dd/pulls

When the project grows we'll add chat channels (Slack/Discord) or a mailing list and link them here.