# Audiences — Reachy Mini App

<!--
Produced following spec/project/audience-identification/. Audiences are derived
from the repository's README and purpose, not invented. Do not add audiences
without first declaring the bounded context.
-->

## Bounded context

A Reachy Mini behavior package built on the Pollen Robotics / Hugging Face
reachy_mini SDK, packaging robot behaviours that run on the Reachy Mini and
distributed as a Hugging Face app. The repository is currently a playground
project.

**Inside the boundary**

- The behavior package under `reachy_mini_app/`
- The Hugging Face static app surface (`index.html`, `style.css`)

**Outside the boundary**

- The `reachy_mini` SDK and the Reachy Mini hardware/runtime
- Hugging Face Spaces hosting

## Audiences

Each entry: label, relationship category, interaction surface, expectation,
documentation `track` (per spec/project/docs-audience-tracks/), status, criticality.

### Direct consumers

- **Reachy Mini owner / maker** — _category_: direct-consumer ·
  _surface_: the deployed behaviours on the robot and the Hugging Face app ·
  _expects_: working behaviours (for example dance-to-music) that run on the Reachy Mini ·
  _track_: `user-docs` · _status_: `assumed` · _criticality_: primary

### Contributors / maintainers

- **Maintainer (`nolte`)** — _category_: contributor ·
  _surface_: the package source, the Hugging Face app, the specs under `spec/` ·
  _expects_: a runnable app and readable conventions ·
  _track_: `developer-docs` · _status_: `assumed` · _criticality_: primary
- **Claude Code as co-author** — _category_: contributor ·
  _surface_: `CLAUDE.md`, `.claude/` ·
  _expects_: deterministic conventions ·
  _track_: `developer-docs` · _status_: `assumed` · _criticality_: secondary

### Indirect audiences

- **reachy_mini SDK (Pollen Robotics / Hugging Face)** — _category_: indirect ·
  _surface_: the SDK APIs this package builds on ·
  _expects_: (without knowing) correct SDK usage ·
  _track_: `developer-docs` · _status_: `assumed` · _criticality_: secondary

## Revisit triggers

Re-run `audience-identify revisit` when any of the following changes:

- The app graduates from playground to a maintained, released behaviour package.
- A second robot platform or SDK is targeted.
