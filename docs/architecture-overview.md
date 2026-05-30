# Architecture Overview

## 1. Purpose of This Document

This document explains the architecture of the Yin-Yang Oscillation Control Protocol.

The protocol is designed as a control-layer extension for reasoning systems based on the Yin-Yang Five-Phase model. It does not replace the core reasoning protocol. Instead, it defines a separate layer for tuning oscillation, convergence, amplitude thresholds, and rebalance behavior.

In simple terms:

```text
Core Protocol = reasoning structure
Oscillation Control Protocol = dynamic tuning layer
```

## 2. Architectural Position

The Yin-Yang Five-Phase Reasoning Protocol defines the basic reasoning structure:

```text
Five phases
Dynamic metrics
Yin-Yang balancing
Claim boundaries
Core reasoning behavior
```

The Yin-Yang Oscillation Control Protocol extends that foundation by defining how dynamic reasoning behavior may be observed, bounded, and adjusted over time.

```text
Yin-Yang Five-Phase Reasoning Protocol
        |
        | defines the reasoning structure
        v
Yin-Yang Oscillation Control Protocol
        |
        | defines dynamic control behavior
        v
Oscillation tuning / convergence optimization
```

This separation keeps the parent protocol stable while allowing more detailed control-layer experimentation in a dedicated repository.

## 3. Why a Separate Control Layer Is Needed

A reasoning protocol can define phases, metrics, and balancing behavior, but dynamic reasoning systems may still fluctuate.

Those fluctuations may appear as:

```text
Excessive phase intensity
Premature convergence
Delayed convergence
Repeated instability
Overcorrection
Unstable rebalance timing
Persistent oscillation
```

If all of these behaviors are added directly to the parent protocol, the parent repository becomes too heavy.

Therefore, this repository treats oscillation control as a dedicated layer.

```text
Parent repository:
Defines the structure.

This repository:
Tunes the movement of that structure.
```

The metaphor is simple: the parent protocol defines the body; this protocol defines the posture control.

## 4. Layer Model

The architecture can be understood as a layered model.

```text
Layer 0: Input / Reasoning Context
        |
Layer 1: Five-Phase Reasoning Structure
        |
Layer 2: Yin-Yang Balance Evaluation
        |
Layer 3: Dynamic Metrics
        |
Layer 4: Oscillation Control
        |
Layer 5: Convergence / Rebalance Decision
        |
Layer 6: Output / Stabilized Reasoning State
```

This repository mainly focuses on Layer 4 and Layer 5.

## 5. Core Components

### 5.1 Oscillation Period

The oscillation period defines the observed or expected cycle length of reasoning-state fluctuation.

It helps determine how often stability should be evaluated.

```text
Short period = faster evaluation
Long period  = greater tolerance for natural fluctuation
```

### 5.2 Amplitude Threshold

The amplitude threshold defines how much deviation is acceptable before corrective behavior may be triggered.

```text
Low threshold  = sensitive correction
High threshold = greater fluctuation tolerance
```

This parameter helps prevent uncontrolled reasoning-state drift.

### 5.3 Convergence Window

The convergence window defines the acceptable range within which reasoning behavior may be considered stable enough to proceed.

```text
Below window = insufficient stability
Inside window = acceptable convergence
Above window = possible over-convergence
```

The goal is not to force certainty, but to define a bounded stability range.

### 5.4 Rebalance Interval

The rebalance interval defines how frequently the control layer evaluates whether phase-level or Yin-Yang rebalance is required.

```text
Short interval = frequent rebalance checks
Long interval  = more continuity before intervention
```

### 5.5 Overcorrection Limit

The overcorrection limit prevents a correction action from becoming a new source of instability.

This is important because excessive correction can create secondary oscillation.

```text
Instability
   ↓
Too much correction
   ↓
New instability
```

The overcorrection limit exists to avoid this loop.

### 5.6 Phase Stability Score

The phase stability score represents the observed stability of a reasoning phase over a defined evaluation interval.

It may be used as one input in convergence or rebalance decisions.

```text
0.0 = unstable
0.5 = partially stable
1.0 = highly stable
```

### 5.7 Oscillation Decay

Oscillation decay describes whether fluctuation decreases, persists, or expands over repeated reasoning cycles.

```text
Negative value = oscillation is expanding
Zero value     = oscillation is persistent
Positive value = oscillation is decaying
```

### 5.8 Adaptive Convergence

Adaptive convergence allows convergence behavior to adjust depending on context, phase intensity, and observed stability.

This prevents the system from applying the same convergence rule to every reasoning situation.

## 6. Control Flow

A simplified control flow looks like this:

```text
Reasoning state observed
        |
Measure phase stability
        |
Measure amplitude
        |
Measure oscillation decay
        |
Check convergence window
        |
Check rebalance interval
        |
Evaluate overcorrection risk
        |
Return control decision
```

Possible control decisions include:

```text
stable
watch
rebalance_required
overcorrection_risk
```

## 7. Rebalance Behavior

When instability is detected, the control layer may recommend bounded rebalance behavior.

Allowed actions include:

```text
reduce_phase_intensity
increase_context_review
delay_convergence
expand_convergence_window
narrow_convergence_window
lower_correction_strength
increase_rebalance_interval
decrease_rebalance_interval
```

These actions are intended to tune behavior, not override the parent protocol.

The control layer must not:

```text
override_parent_protocol_structure
force_single_phase_dominance
erase_claim_boundaries
claim_model_internal_state
skip_validation_when_required
```

## 8. Relationship to the Parent Protocol

The parent protocol defines the stable conceptual foundation.

```text
Yin-Yang Five-Phase Reasoning Protocol
= Core reasoning structure
```

This repository defines a dynamic extension.

```text
Yin-Yang Oscillation Control Protocol
= Control optimization layer
```

The two protocols are complementary.

```text
Parent = structure
Extension = movement control
```

The parent protocol should remain readable and stable.
This repository may evolve more actively as control parameters, examples, and validation structures are refined.

## 9. Design Principles

This architecture follows several principles.

```text
Separate structure from control.
Treat oscillation as signal, not merely noise.
Prefer bounded adjustment over forced correction.
Avoid overcorrection.
Do not claim internal AI model behavior.
Keep the protocol implementation-neutral.
Preserve the parent protocol's claim boundaries.
```

These principles are important because the protocol is intended as a specification layer, not as a claim about any specific AI system.

## 10. Claim Boundaries

This architecture does not claim that any specific AI model internally performs oscillation control.

It does not claim to be:

```text
A complete AI safety system
A consciousness model
A production runtime
A guaranteed optimizer
A replacement for empirical evaluation
```

It may be used as:

```text
A conceptual specification
A documentation structure
A control-layer model
A validation target
A basis for experimentation
```

Any implementation should be tested independently.

## 11. Example Architecture

A minimal implementation may follow this structure:

```text
Input reasoning state
        |
Extract observed metrics
        |
Compare with control parameters
        |
Evaluate stability
        |
Apply rebalance decision if needed
        |
Return stabilized reasoning state
```

A more advanced implementation may include:

```text
Adaptive convergence
Phase-specific thresholds
Historical oscillation tracking
Context-sensitive rebalance intervals
Overcorrection monitoring
```

## 12. Summary

The Yin-Yang Oscillation Control Protocol separates dynamic control behavior from the core reasoning protocol.

It exists because reasoning systems may need more than structure. They may also need a way to observe, tune, and stabilize movement over time.

In short:

```text
The parent protocol defines the reasoning skeleton.
This protocol defines the control rhythm.
```

The architecture is intentionally modest, bounded, and implementation-neutral.

Its purpose is not to claim that a system is intelligent, conscious, or safe.
Its purpose is to define a structured language for discussing oscillation, convergence, and rebalance behavior in Yin-Yang Five-Phase reasoning systems.
