# Changelog

All notable changes per release. Versions follow [semver](https://semver.org).

## v1.0.5 — 2026-08-01

CI/infrastructure only. No code in this repo changed — the whole diff since v1.0.4 is under `.github/workflows/`.

- Split the pipeline: building and publishing stay in `pipeline.yml`, and everything that leaves the host now lives in its own file beside it.
- The repo is mirrored to Codeberg as well as GitLab.
- The repo is archived to the Wayback Machine, Software Heritage and archive.org.
- Issues opened on either mirror are copied back to GitHub every six hours, and closed here when the original closes.
- Pull requests are switched off on both mirrors — they are force-pushed from GitHub, so anything merged there would be destroyed by the next sync. Issues and forking stay enabled.

## v1.0.4 — 2026-07-27

- Fixed the README's Codex subsection, which was missing its install command. It now reads `codex plugin add supervisor-config-gen@psyb0t` right after the marketplace-add line.
- Clarified that the skill's invocation form depends on how it was picked up: installed via the marketplace it's `$supervisor-config-gen:supervisor-config-gen`; auto-detected from a repo's own `.agents/skills/` it's plain `$supervisor-config-gen`.

## v1.0.3 — 2026-07-27

- Added Claude Code and Codex plugin manifests (`.agents/.claude-plugin/plugin.json`, `.agents/.codex-plugin/plugin.json`) so the existing ClawHub skill installs natively in both clients via the shared `psyb0t/agents` marketplace.
- Added an "Agent integrations" section to the README with install commands for Claude Code, Codex, and the OpenClaw skill.

## v1.0.2 — 2026-07-27

- Added a GitHub Actions CI status badge to the README.

## v1.0.1 — 2026-07-27

Add README status badges.

- Added self-hosted version and license badges (rendered as SVGs on the `badges` branch by the `create-badges` CI job, no third-party render service). Wired a badges job into pipeline.yml.
