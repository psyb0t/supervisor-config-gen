# Changelog

All notable changes per release. Versions follow [semver](https://semver.org).

## v1.0.3 — 2026-07-27

- Added Claude Code and Codex plugin manifests (`.agents/.claude-plugin/plugin.json`, `.agents/.codex-plugin/plugin.json`) so the existing ClawHub skill installs natively in both clients via the shared `psyb0t/agents` marketplace.
- Added an "Agent integrations" section to the README with install commands for Claude Code, Codex, and the OpenClaw skill.

## v1.0.2 — 2026-07-27

- Added a GitHub Actions CI status badge to the README.

## v1.0.1 — 2026-07-27

Add README status badges.

- Added self-hosted version and license badges (rendered as SVGs on the `badges` branch by the `create-badges` CI job, no third-party render service). Wired a badges job into pipeline.yml.
