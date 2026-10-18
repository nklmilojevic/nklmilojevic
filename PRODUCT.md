# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

GitHub profile README (`README.md` in the `nklmilojevic/nklmilojevic` repo), rendered by GitHub's Markdown sanitizer: no CSS, no scripts, limited HTML. Visuals are hand-authored SVG files committed to the repo, served in light and dark variants through `<picture>` + `prefers-color-scheme`. A scheduled GitHub Action regenerates the SVGs with live data (star counts, latest release tags). No third-party stats widgets.

## Users

Two audiences, tools first:

1. Developers who land here from sofka or thurm (a star, an issue, a release link) and want to know what else this person builds, how to install it, and where to follow it.
2. Engineers, peers and candidates who want to know who Nikola is: CTO at MailerLite, based in Belgrade, building tools for Kubernetes and terminal workflows.

## Product Purpose

The profile is the front door to Nikola's open-source work. Success: a visitor understands within one screen what sofka and thurm are, clicks through to one of them (site, install, download), and leaves knowing the person behind them.

## Positioning

A CTO who still ships daily: sofka (1.7k+ stars, Rust Kubernetes TUI) and thurm (native macOS terminal for coding agents) are actively released, often several times a week. The profile shows work, not claims.

## Capabilities and Constraints

- Featured projects: **sofka** (https://sofka.rs, Rust, kube-rs + ratatui, Flux/Argo built in, incident view, signed Linux packages + Homebrew) and **thurm** (native macOS terminal for Apple silicon, persistent sessions via `thurmd`, coding-agent status, remote sessions, `thurm` CLI; docs at https://docs.thurm.rs; iPhone/iPad app in `thurm-ios`).
- Other repos (Lodge, home, nix-config, flakes) are not featured; a link to the full repo list is enough.
- GitHub strips `<style>`, `<script>`, and most attributes from the README itself. SVG loaded via `<img>` may carry its own CSS and SMIL/CSS animation but cannot load external fonts or resources and has no interactivity; links live on the wrapping `<a>`.
- Must read correctly in GitHub light and dark themes and at mobile widths (GitHub mobile web scales images to column width).

## Brand Commitments

- sofka's identity: named after Sophie, a Russian Blue who watches the screen; Serbian short form of Sophia.
- Website: https://nikola.milojevic.me. X/Twitter: @nklmilojevic.
- Title: CTO @ MailerLite. Location: Belgrade, Serbia.

## Evidence on Hand

- sofka: star count, release cadence (v0.31.x as of 2026-10), `docs/demo.gif`, `docs/sophie.png` in the sofka repo, live site sofka.rs.
- thurm: releases (v0.8.x as of 2026-10), screenshots under `docs/public/screenshots/` in the thurm repo, DMG download link.
- No testimonials, user counts, or company metrics beyond what GitHub reports. Do not invent any.

## Product Principles

1. Work before biography: the tools lead, the person is one line.
2. Every number on the page is live or absent; nothing hand-typed that goes stale.
3. One click to the useful thing: install, download, or site.
4. Quiet enough to sit next to the GitHub UI, specific enough that it could only be this profile.
