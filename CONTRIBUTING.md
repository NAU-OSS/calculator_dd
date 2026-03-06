# Contributing Guide

Thank you for your interest in contributing to Calculator DD. This document describes how to contribute, our expectations for code and community, and practical steps for reporting issues or proposing features.

## Table of contents

- How to contribute
- Reporting bugs
- Proposing new features
- Pull request workflow
- Code style & formatting
- Testing requirements
- Documentation standards
- Community guidelines & expectations
- Maintainer process
- Contact

## How to contribute

1. Check existing issues and pull requests to avoid duplication.
2. For bugs or small improvements: open an issue with a clear title and steps to reproduce.
3. For new features or larger changes: open an issue to discuss scope before implementing.
4. Fork the repository and create a branch: `git checkout -b feat/short-description`.
5. Make changes, add tests and documentation, and run the test suite.
6. Push your branch to your fork and open a Pull Request (PR) against `main`.
7. Link related issues in the PR description and provide a short summary of changes and rationale.

## Reporting bugs

When reporting a bug, include:
- A clear descriptive title.
- Steps to reproduce the problem.
- Expected and actual behavior.
- Environment (OS, Python version).
- Minimal reproducible code or test case.
- Any error messages and stack traces.

Use the issue template (if present) when opening a bug report.

## Proposing new features

- Open an issue describing the proposed feature, motivation, and usage examples.
- Describe alternatives considered and backwards compatibility impact.
- For larger changes, create a short design doc or RFC and link it in the issue.
- Wait for community or maintainer feedback before investing significant implementation time.

## Pull request workflow

- Base PRs against `main`.
- One logical change per PR; keep commits focused and amend or squash when appropriate.
- Include tests covering new behavior and update documentation/examples.
- Follow the PR template if present; include testing steps and compatibility notes.
- Address review comments in a timely manner; maintainers may request changes.
- PRs will be reviewed for correctness, style, tests, and documentation.

## Code style & formatting

- Follow Python idioms and PEP 8 (https://www.python.org/dev/peps/pep-0008/).
- Use black for formatting and isort for imports where applicable.
- Prefer clear, simple, and well-named abstractions.
- Add or update type hints where helpful.
- Use pre-commit hooks if configured; run linters locally before opening PRs.

## Testing requirements

- Write unit tests for new functionality and bug fixes.
- Tests should live in `tests/` and use the same test framework as the project (unittest/pytest).
- Ensure tests run locally: `python -m unittest discover -s tests` (or `pytest` if configured).
- Aim to keep tests deterministic and fast.
- CI will run tests on PRs; fix any failures before merging.

## Documentation standards

- Document public functions, classes, and modules with clear docstrings.
- Update README.md with user-facing changes and usage examples.
- Add examples under `examples/` for non-trivial features.
- Keep change notes for user-impacting changes (CHANGELOG or release notes if maintained).

## Community guidelines & expectations

- Be respectful, patient, and constructive in discussions.
- Follow the project's Code of Conduct (see CODE_OF_CONDUCT.md).
- Give clear, actionable feedback when reviewing others’ work.
- Welcome new contributors; help mentor and explain rationale when rejecting or requesting changes.

## Maintainer process

- Maintainers will review issues and PRs, prioritize work, and merge contributions that meet quality standards.
- The maintainers may close or redirect issues that are duplicates, out of scope, or lack necessary information.
- Security-related reports should be made privately if necessary; see the repository metadata for security contact.

## Contact

- Repository: https://github.com/NAU-OSS/calculator_dd
- Issues: https://github.com/NAU-OSS/calculator_dd/issues
- Pull requests: https://github.com/NAU-OSS/calculator_dd/pulls

Thank you for contributing!