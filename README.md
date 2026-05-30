# Yin-Yang Oscillation Control Protocol v0.1

A control-layer extension for oscillation tuning, convergence windows, and dynamic rebalance behavior in Yin-Yang Five-Phase reasoning systems.

## Status

```text
Version: v0.1.0-draft
Status: Initial repository scaffold
Layer: Control Optimization Layer
Parent Protocol: Yin-Yang Five-Phase Reasoning Protocol
```

This repository defines an extension layer for controlling oscillation, convergence behavior, amplitude thresholds, and rebalance timing in reasoning systems based on the Yin-Yang Five-Phase model.

The goal is not to replace the core reasoning protocol, but to provide a dedicated control layer for tuning dynamic behavior after the core phase structure has already been defined.

## Purpose

The Yin-Yang Five-Phase Reasoning Protocol defines the basic reasoning structure:

```text
Phase structure
Dynamic metrics
Yin-Yang balancing
Claim boundaries
Core reasoning behavior
```

This repository focuses on what comes after that foundation:

```text
Oscillation control
Convergence windows
Amplitude thresholds
Rebalance intervals
Overcorrection limits
Phase stability scoring
Adaptive convergence behavior
```

In short:

```text
Core Protocol = reasoning structure
Oscillation Control Protocol = dynamic tuning layer
```

## Why This Repository Exists

The original Yin-Yang Five-Phase Reasoning Protocol reached a stable core form through the following progression:

```text
v0.1.0 = Five-Phase reasoning skeleton
v0.1.1 = Validation foundation
v0.2.0 = Dynamic control metrics
v0.3.0 = Yin-Yang Balancer
v0.3.1 = Documentation and claim-boundary polish
```

After v0.3.1, the core protocol became sufficiently stable as a foundation.

However, further additions such as oscillation tuning, convergence optimization, amplitude control, and adaptive rebalance behavior would make the core repository too heavy.

Therefore, this repository separates those concerns into a dedicated control-layer extension.

## Conceptual Relationship

```text
Yin-Yang Five-Phase Reasoning Protocol
        |
        | defines:
        | - phases
        | - metrics
        | - balancing logic
        | - reasoning structure
        v

Yin-Yang Oscillation Control Protocol
        |
        | defines:
        | - oscillation tuning
        | - convergence windows
        | - amplitude thresholds
        | - rebalance timing
        | - stability scoring
        v

Dynamic Control Optimization Layer
```

## Core Concepts

### Oscillation Period

Defines the observed or expected cycle length of reasoning-state fluctuation.

### Amplitude Threshold

Defines how much deviation is acceptable before a correction or rebalance is triggered.

### Convergence Window

Defines the acceptable range within which a reasoning process may be considered stable enough to proceed.

### Rebalance Interval

Defines how frequently the system should evaluate whether phase-level or Yin-Yang rebalance is required.

### Overcorrection Limit

Prevents the system from overreacting to instability and creating new instability through excessive correction.

### Phase Stability Score

Provides a measurable indicator of whether a phase remains stable over time.

### Oscillation Decay

Describes whether instability decreases, persists, or expands across reasoning cycles.

### Adaptive Convergence

Allows convergence behavior to adjust depending on reasoning context, phase intensity, and system stability.

## Repository Structure

```text
yin-yang-oscillation-control-protocol-v0.1/
├── README.md
├── spec/
│   └── oscillation-control-protocol-v0.1.yaml
├── schemas/
│   └── oscillation-control.schema.json
├── examples/
│   ├── convergence-window.example.yaml
│   ├── amplitude-threshold.example.yaml
│   └── rebalance-interval.example.yaml
├── docs/
│   ├── architecture-overview.md
│   ├── relationship-to-yin-yang-five-phase.md
│   ├── oscillation-tuning.md
│   ├── convergence-window.md
│   └── claim-boundaries.md
├── scripts/
│   └── validate_specs.py
├── CHANGELOG.md
├── CITATION.cff
└── LICENSE
```

## Start Here

Recommended reading order:

1. `README.md`
2. `docs/architecture-overview.md`
3. `docs/relationship-to-yin-yang-five-phase.md`
4. `spec/oscillation-control-protocol-v0.1.yaml`
5. `examples/convergence-window.example.yaml`
6. `docs/claim-boundaries.md`

## Design Principles

This protocol follows several basic design principles:

```text
Separate structure from control.
Tune behavior without rewriting the core protocol.
Prefer stability over forced convergence.
Prevent excessive correction.
Treat oscillation as a signal, not merely as noise.
Keep claims bounded and implementation-neutral.
```

## Scope

This repository defines a control-layer specification.

It may be used for:

```text
Reasoning-system tuning
Multi-phase reasoning stability analysis
Dynamic rebalance design
Convergence behavior modeling
AI reasoning architecture documentation
Protocol-level experimentation
```

It does not claim to provide:

```text
A complete AI safety system
A consciousness model
A production-ready runtime
A guaranteed reasoning optimizer
A replacement for empirical evaluation
```

## Claim Boundaries

This project is a conceptual and structural protocol specification.

It is intended to describe possible control-layer behavior in reasoning systems. It does not claim that any specific AI system currently implements these mechanisms internally.

Any implementation should be tested independently and evaluated in its own technical context.

## Relationship to the Parent Protocol

This repository depends conceptually on the Yin-Yang Five-Phase Reasoning Protocol.

The parent protocol defines the reasoning structure.
This repository defines how that structure may be dynamically tuned.

```text
Parent:
Yin-Yang Five-Phase Reasoning Protocol

Extension:
Yin-Yang Oscillation Control Protocol
```

The two repositories should be read as complementary layers, not as competing specifications.

## License

This project is released under the MIT License.

## Citation

If you use or reference this specification, please cite this repository.

A formal `CITATION.cff` file will be added as part of the v0.1.0 release structure.

## Current Development Stage

```text
v0.1.0-draft
Initial repository scaffold and conceptual positioning.
```

Planned next steps:

```text
1. Add core YAML specification
2. Add JSON Schema validation
3. Add minimal examples
4. Add architecture documentation
5. Add validation script
6. Prepare v0.1.0 release
```

