# Oscillation Tuning

## 1. Purpose of This Document

This document explains the concept of oscillation tuning in the Yin-Yang Oscillation Control Protocol.

Oscillation tuning refers to the process of observing, bounding, and adjusting reasoning-state fluctuation over time.

The purpose is not to eliminate all fluctuation.
The purpose is to distinguish useful movement from destabilizing instability.

In this protocol:

```text
Oscillation is treated as a signal, not merely as noise.
```

## 2. What Oscillation Means

In a reasoning system, oscillation refers to repeated fluctuation in reasoning state, phase intensity, balance condition, or convergence behavior.

Oscillation may appear as:

```text
A reasoning process repeatedly shifting between phases
A balance state moving back and forth between Yin and Yang emphasis
A system approaching convergence and then drifting away
A correction action creating new instability
A reasoning process failing to settle within an acceptable window
```

Not all oscillation is harmful.

Some oscillation may indicate exploration, comparison, or healthy uncertainty.
Excessive oscillation, however, may indicate instability or lack of control.

## 3. Why Oscillation Tuning Is Needed

A reasoning protocol may define a stable structure, but dynamic reasoning behavior can still fluctuate.

Without oscillation tuning, the system may suffer from:

```text
Premature convergence
Delayed convergence
Excessive phase dominance
Repeated rebalancing
Overcorrection
Unstable reasoning loops
Weak stability detection
```

Oscillation tuning provides a structured way to observe when fluctuation is acceptable and when intervention may be required.

## 4. Core Oscillation Parameters

This protocol defines three primary oscillation-related parameters:

```text
oscillation_period
amplitude_threshold
oscillation_decay
```

Each parameter captures a different aspect of dynamic behavior.

```text
oscillation_period  = how long the fluctuation cycle is
amplitude_threshold = how large the fluctuation may become
oscillation_decay   = whether fluctuation is shrinking or expanding
```

Together, these parameters provide a basic model for evaluating reasoning-state movement.

## 5. Oscillation Period

### Definition

`oscillation_period` defines the observed or expected cycle length of reasoning-state fluctuation.

It answers the question:

```text
How many reasoning cycles does it take for the fluctuation pattern to repeat or become evaluable?
```

### Example

```yaml
oscillation_period:
  value: 4
  unit: "reasoning_cycle"
```

This means that the system evaluates fluctuation across a four-cycle reasoning pattern.

### Interpretation

```text
Short oscillation period
= faster fluctuation, quicker evaluation, higher sensitivity

Long oscillation period
= slower fluctuation, more tolerance, delayed evaluation
```

A short period may be useful when rapid instability must be detected.

A long period may be useful when the reasoning process needs room to explore before being judged unstable.

## 6. Amplitude Threshold

### Definition

`amplitude_threshold` defines the maximum acceptable deviation from the target balance state before corrective behavior may be considered.

It answers the question:

```text
How much fluctuation is acceptable before the system should respond?
```

### Example

```yaml
amplitude_threshold:
  value: 0.30
  unit: "normalized_deviation"
```

This means that observed deviation above `0.30` may trigger a watch state or rebalance decision.

### Interpretation

```text
Low threshold
= sensitive control, earlier correction

High threshold
= tolerant control, later correction
```

A threshold that is too low may cause excessive correction.

A threshold that is too high may allow instability to continue too long.

## 7. Oscillation Decay

### Definition

`oscillation_decay` describes whether fluctuation is decreasing, persisting, or increasing over repeated reasoning cycles.

It answers the question:

```text
Is the oscillation moving toward stability or away from it?
```

### Example

```yaml
oscillation_decay:
  value: 0.18
  unit: "normalized_decay_rate"
```

This means that oscillation is decreasing and the reasoning state may be moving toward stability.

### Interpretation

```text
Negative value = oscillation is expanding
Zero value     = oscillation is persistent
Positive value = oscillation is decaying
```

In general:

```text
Positive decay is usually stabilizing.
Zero decay may require monitoring.
Negative decay may indicate instability.
```

## 8. Combined Evaluation

Oscillation tuning should not rely on one parameter alone.

A more useful evaluation combines period, amplitude, and decay.

Example:

```yaml
observed_state:
  oscillation_period: 3
  observed_amplitude: 0.42
  amplitude_threshold: 0.30
  oscillation_decay: -0.12
```

Interpretation:

```text
The oscillation is recurring quickly.
The observed amplitude exceeds the threshold.
The oscillation is expanding rather than decaying.
```

This may result in:

```yaml
decision:
  status: "rebalance_required"
  reason: >
    Observed amplitude exceeds the configured threshold and oscillation
    decay is negative.
```

## 9. Tuning Modes

Oscillation tuning may be configured according to different control modes.

### Conservative Mode

```yaml
mode: "conservative"
amplitude_threshold: 0.40
rebalance_interval: 5
overcorrection_limit: 0.25
```

Conservative mode allows more natural fluctuation and applies gentler correction.

It is useful when stability should be preserved without frequent intervention.

### Balanced Mode

```yaml
mode: "balanced"
amplitude_threshold: 0.30
rebalance_interval: 3
overcorrection_limit: 0.40
```

Balanced mode is the recommended default for general experimentation.

It attempts to balance responsiveness and stability.

### Responsive Mode

```yaml
mode: "responsive"
amplitude_threshold: 0.20
rebalance_interval: 2
overcorrection_limit: 0.55
```

Responsive mode reacts quickly to instability.

It may be useful in highly dynamic contexts, but it carries a higher risk of overcorrection.

## 10. Overcorrection Risk

Oscillation tuning must avoid excessive correction.

A common failure pattern is:

```text
Instability detected
        ↓
Correction applied too strongly
        ↓
New instability created
        ↓
Further correction applied
        ↓
Oscillation increases
```

This protocol uses `overcorrection_limit` to reduce that risk.

Example:

```yaml
overcorrection_guard:
  enabled: true
  overcorrection_limit: 0.40
  proposed_correction_strength: 0.35
  status: "within_limit"
```

If correction strength exceeds the limit, the control layer should reduce correction intensity.

## 11. Healthy Oscillation vs. Destabilizing Oscillation

Not all fluctuation should be suppressed.

Healthy oscillation may include:

```text
Exploring multiple interpretations
Comparing competing phase tendencies
Maintaining uncertainty before convergence
Allowing context to mature
```

Destabilizing oscillation may include:

```text
Repeated contradiction without resolution
Increasing amplitude over time
Negative oscillation decay
Frequent rebalance failure
Premature or forced convergence
```

The goal is not to create a motionless reasoning system.

The goal is to create a system that can move without losing balance.

## 12. Relationship to Convergence

Oscillation tuning is closely related to convergence.

A reasoning process should not be considered stable merely because it stops moving.
It should be considered stable when movement has entered an acceptable range.

```text
No movement is not always stability.
Bounded movement may be stability.
```

This is why oscillation tuning works together with the convergence window.

```text
Oscillation tuning observes movement.
Convergence window defines acceptable stability.
Rebalance behavior responds when movement becomes unstable.
```

## 13. Implementation-Neutral Design

This protocol does not require a specific implementation.

An implementation may calculate oscillation using:

```text
phase-level scores
balance-state changes
metric deltas
cycle-to-cycle deviation
historical stability tracking
context-specific thresholds
```

The protocol only defines the structural vocabulary and expected boundaries.

It does not claim that any specific AI model internally measures oscillation in this way.

## 14. Example Decision Flow

A simplified oscillation tuning flow may look like this:

```text
Observe reasoning state
        |
Measure phase stability
        |
Measure observed amplitude
        |
Compare with amplitude threshold
        |
Evaluate oscillation decay
        |
Check overcorrection risk
        |
Return stability decision
```

Possible results:

```text
stable
watch
rebalance_required
overcorrection_risk
```

## 15. Claim Boundaries

This document describes a conceptual control structure.

It does not claim:

```text
That any specific AI model internally performs oscillation tuning
That oscillation tuning guarantees better reasoning
That this protocol is a complete AI safety system
That this protocol proves internal model states
That this protocol replaces empirical testing
```

Allowed claims are more modest:

```text
This protocol defines a possible oscillation-control structure.
This protocol provides terminology for reasoning-state fluctuation.
This protocol may support documentation, experimentation, or validation.
```

## 16. Summary

Oscillation tuning is the process of managing reasoning-state fluctuation without eliminating useful movement.

The three core concepts are:

```text
oscillation_period  = timing of fluctuation
amplitude_threshold = acceptable size of fluctuation
oscillation_decay   = direction of fluctuation over time
```

Together, they help determine whether a reasoning process is stable, should be watched, or requires rebalance.

In short:

```text
The goal is not to stop movement.
The goal is to keep movement within balance.
```
