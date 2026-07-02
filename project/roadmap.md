# Roadmap

This file is the work queue governed by `spec/project/roadmap/`. Each entry is a
level-3 heading followed by a `yaml` code block (`id`, `title`, `detail`,
`outcomes`, `target_sprint`, `mvp`, `status`, in that order) and a free-text
body. `roadmap-plan` and `roadmap-refine` own the detail level and the status
lifecycle; do not hand-edit those fields here.

Entries carry monotonically increasing IDs starting at `R-1`, never reused.
Outcome IDs (`O-n` in `goals.md`) are an independent counter.

The MVP is minimal: a behaviour package on the `reachy_mini` SDK that runs at
least one behaviour and is distributable as a Hugging Face app. R-1 shipped
before the planning suite and is recorded retroactively as `status: done`. The
repository stays experimental, so further behaviours are post-MVP.

## Phase 1 — Runnable behaviour app

### R-1 — Reachy Mini behaviour package on the reachy_mini SDK

```yaml
id: R-1
title: Reachy Mini behaviour package on the reachy_mini SDK
detail: fine
outcomes: [O-1, O-2]
target_sprint: 1
mvp: true
status: done
```

The behaviour package built on the Pollen Robotics / Hugging Face `reachy_mini`
SDK that runs at least one robot behaviour (for example dance-to-music) on the
Reachy Mini and is distributable as a Hugging Face app. Capability
`reachy-mini-behavior-app` in `project/portfolio.yml`.

## Phase 2 — More behaviours (post-MVP)

### R-2 — Additional robot behaviours

```yaml
id: R-2
title: Additional robot behaviours
detail: backlog
outcomes: [O-1]
target_sprint: null
mvp: false
status: proposed
```

Further packaged behaviours beyond the first. Post-MVP while the repository
stays an experimental playground.
