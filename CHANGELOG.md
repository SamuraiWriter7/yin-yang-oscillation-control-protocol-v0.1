# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight versioning model during the early draft phase.

## [Unreleased]

### Planned

* Prepare the first tagged release as `v0.1.0`.
* Finalize the initial protocol specification.
* Finalize example validation coverage.
* Add or refine documentation if needed before release.

## [0.1.0-draft] - 2026-05-31

### Added

* Initial repository scaffold for the Yin-Yang Oscillation Control Protocol.
* `README.md` with project purpose, repository scope, parent protocol relationship, and recommended reading order.
* Core protocol specification:

  * `spec/oscillation-control-protocol-v0.1.yaml`
* JSON Schema for validation:

  * `schemas/oscillation-control.schema.json`
* Example configuration documents:

  * `examples/convergence-window.example.yaml`
  * `examples/amplitude-threshold.example.yaml`
  * `examples/rebalance-interval.example.yaml`
* Documentation files:

  * `docs/architecture-overview.md`
  * `docs/relationship-to-yin-yang-five-phase.md`
  * `docs/oscillation-tuning.md`
  * `docs/convergence-window.md`
  * `docs/claim-boundaries.md`
* Validation script:

  * `scripts/validate_specs.py`
* GitHub Actions workflow:

  * `.github/workflows/validate-oscillation-control.yml`

### Defined

* Initial control-layer concepts:

  * `oscillation_period`
  * `amplitude_threshold`
  * `convergence_window`
  * `rebalance_interval`
  * `overcorrection_limit`
  * `phase_stability_score`
  * `oscillation_decay`
  * `adaptive_convergence`
* Initial control actions:

  * `continue_without_rebalance`
  * `soft_rebalance`
  * `hard_rebalance`
  * `delay_convergence`
  * `enter_observation_window`
* Initial default profiles:

  * `conservative`
  * `balanced`
  * `responsive`

### Validation

* Added validation flow for:

  * Core protocol YAML
  * Example YAML files
  * Required example metadata
  * Required parent protocol metadata
  * Required decision and claim-boundary fields
* Confirmed validation compatibility for:

  * `convergence-window.example.yaml`
  * `amplitude-threshold.example.yaml`
  * `rebalance-interval.example.yaml`

### Documentation

* Established the relationship between this repository and the parent Yin-Yang Five-Phase Reasoning Protocol.
* Clarified that this repository functions as a Control Optimization Layer rather than a replacement for the core protocol.
* Added claim boundaries to prevent overstatement of conceptual protocol behavior.

### Notes

This draft separates oscillation tuning and convergence optimization from the parent reasoning protocol.

The parent repository defines the reasoning structure.
This repository defines a control-layer extension for dynamic tuning, convergence behavior, amplitude thresholds, rebalance timing, and stability evaluation.

## Versioning Notes

```text
0.1.0-draft = Initial draft scaffold and validation foundation
0.1.0       = First stable initial release
```

## Release Philosophy

This project is intended to remain implementation-neutral.

It defines structural concepts and validation-ready protocol examples, but it does not claim that any existing AI system internally implements these mechanisms.

The core principle is:

```text
Structure first.
Control second.
Claims bounded.
Validation required.
```
