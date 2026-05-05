# reachy-mini-app

[![CI](https://github.com/nolte/reachy-mini-app/actions/workflows/ci.yml/badge.svg)](https://github.com/nolte/reachy-mini-app/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)

A Reachy Mini behavior package built on the Pollen Robotics / Hugging Face
[`reachy_mini`](https://github.com/pollen-robotics/reachy-mini) SDK.

> Status: scaffolding. The repository layout was initialized from the
> `nolte/claude-shared` `project-structure` spec; behaviors will land under
> `src/reachy_mini_app/`.

## Quickstart

```bash
task setup    # install dev + docs dependencies, register pre-commit hooks
task lint     # run linters (Ruff)
task test     # run the test suite (pytest)
task docs     # build the MkDocs documentation locally
```

## Documentation

Full documentation lives under [`docs/`](./docs/) and is published from
[`mkdocs.yml`](./mkdocs.yml).

## Specifications

Project-level specifications live under [`spec/`](./spec/).

## License

Apache-2.0 — see [`LICENSE`](./LICENSE).
