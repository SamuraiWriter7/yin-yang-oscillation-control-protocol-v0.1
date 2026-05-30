# Convergence Window

## 1. Purpose of This Document

This document explains the concept of the convergence window in the Yin-Yang Oscillation Control Protocol.

The convergence window defines the acceptable stability range within which a reasoning process may be considered sufficiently stable to continue, pause, or finalize.

The purpose is not to force certainty.

The purpose is to define a bounded zone where reasoning behavior is stable enough, without requiring artificial stillness.

```text id="x3m9q1"
Convergence does not mean perfect certainty.
Convergence means bounded stability.
```

## 2. What a Convergence Window Is

A convergence window is a defined range used to evaluate whether a reasoning state has become stable enough over time.

It usually includes:

```text id="y8n2fd"
lower_bound
upper_bound
minimum_duration
```

Example:

```yaml id="wv7d8c"
convergence_window:
  lower_bound: 0.65
  upper_bound: 0.90
  minimum_duration: 2
  unit: "reasoning_cycle"
```

This means:

```text id="v5qz7k"
The stability score should remain between 0.65 and 0.90
for at least 2 reasoning cycles
before the state is treated as sufficiently converged.
```

## 3. Why a Window Is Needed

Reasoning systems can fail in two opposite ways.

They may fail by not converging enough:

```text id="ds3yra"
The reasoning process remains unstable.
The system continues shifting without resolution.
The phase balance keeps drifting.
```

They may also fail by converging too strongly or too early:

```text id="nh4xfd"
The reasoning process becomes fixed too soon.
Alternative interpretations are ignored.
The system prematurely closes uncertainty.
```

The convergence window prevents both extremes.

```text id="m5egzl"
Too little convergence = instability
Too much convergence   = premature fixation
Windowed convergence   = bounded stability
```

## 4. Core Fields

### 4.1 lower_bound

`lower_bound` defines the minimum stability score required before a reasoning state may be considered sufficiently stable.

Example:

```yaml id="khmk3b"
lower_bound: 0.65
```

If the phase stability score is below this value, the system may remain in a watch state or require further balancing.

### 4.2 upper_bound

`upper_bound` defines the upper edge of the acceptable convergence range.

Example:

```yaml id="dmmt1h"
upper_bound: 0.90
```

If a stability score rises above this value too quickly or too rigidly, the system may be over-converging.

This does not always mean failure, but it may indicate that the reasoning process has become too fixed.

### 4.3 minimum_duration

`minimum_duration` defines how long the reasoning state must remain inside the convergence window before it is treated as stable.

Example:

```yaml id="qelc1n"
minimum_duration: 2
unit: "reasoning_cycle"
```

This prevents the system from treating a brief stable moment as true convergence.

## 5. Basic Interpretation

The convergence window can be interpreted as follows:

```text id="i880bg"
Below lower_bound:
  The reasoning state is not stable enough.

Inside the window:
  The reasoning state may be treated as sufficiently stable.

Above upper_bound:
  The reasoning state may be over-converged or prematurely fixed.
```

A stable reasoning process does not need to become motionless.
It only needs to remain within acceptable bounds.

## 6. Relationship to Phase Stability Score

The convergence window is usually evaluated against `phase_stability_score`.

Example:

```yaml id="svd2v2"
phase_stability_score: 0.74

convergence_window:
  lower_bound: 0.65
  upper_bound: 0.90
```

In this example, the score is inside the convergence window.

```text id="wbhn8b"
0.65 <= 0.74 <= 0.90
```

This means the reasoning state may be considered stable, assuming other conditions are also satisfied.

## 7. Relationship to Oscillation Decay

A reasoning state may be inside the convergence window but still unstable if oscillation is expanding.

For this reason, convergence should be evaluated together with `oscillation_decay`.

Example:

```yaml id="n70b7b"
phase_stability_score: 0.74
oscillation_decay: 0.18
```

Interpretation:

```text id="cwlaom"
The stability score is inside the convergence window.
Oscillation is decaying.
The reasoning state may be treated as stable.
```

Counter-example:

```yaml id="qj1d68"
phase_stability_score: 0.74
oscillation_decay: -0.20
```

Interpretation:

```text id="j9hyk2"
The stability score is inside the convergence window,
but oscillation is expanding.
The state should be watched or re-evaluated.
```

## 8. Relationship to Amplitude Threshold

The convergence window should also be evaluated against the observed amplitude.

Example:

```yaml id="vle78w"
phase_stability_score: 0.74
observed_amplitude: 0.26
amplitude_threshold: 0.30
```

Interpretation:

```text id="zpyqsi"
The stability score is inside the convergence window.
The observed amplitude is below the threshold.
The reasoning state may continue without rebalance.
```

Counter-example:

```yaml id="gm6xck"
phase_stability_score: 0.74
observed_amplitude: 0.42
amplitude_threshold: 0.30
```

Interpretation:

```text id="x1qz7m"
The stability score is inside the convergence window,
but observed amplitude exceeds the threshold.
The reasoning state may require rebalance or monitoring.
```

## 9. Minimum Duration Requirement

The minimum duration requirement prevents false convergence.

A reasoning state may briefly enter the convergence window and then drift away.

Example:

```yaml id="tolvww"
cycle_1:
  phase_stability_score: 0.66
  status: "inside_window"

cycle_2:
  phase_stability_score: 0.72
  status: "inside_window"
```

If `minimum_duration` is `2`, this may be treated as stable.

Counter-example:

```yaml id="bctzmu"
cycle_1:
  phase_stability_score: 0.66
  status: "inside_window"

cycle_2:
  phase_stability_score: 0.58
  status: "below_window"
```

This should not be treated as stable convergence.

## 10. Stable, Watch, and Rebalance States

The convergence window may support three basic states.

### Stable

```text id="oecbdl"
phase_stability_score is inside the convergence window
oscillation_decay is non-negative
observed_amplitude is within threshold
minimum_duration is satisfied
```

### Watch

```text id="m9s6z4"
phase_stability_score is near the lower bound
oscillation_decay is weak or unchanged
observed_amplitude is near the threshold
minimum_duration is not yet satisfied
```

### Rebalance Required

```text id="sgjzao"
phase_stability_score is below the lower bound
observed_amplitude exceeds the amplitude threshold
oscillation_decay is negative
```

## 11. Example Decision Logic

A simplified decision structure may look like this:

```yaml id="yncvkc"
decision_logic:
  stable:
    conditions:
      - "phase_stability_score >= convergence_window.lower_bound"
      - "phase_stability_score <= convergence_window.upper_bound"
      - "oscillation_decay >= 0.0"
      - "observed_amplitude <= amplitude_threshold"
      - "minimum_duration satisfied"

  watch:
    conditions:
      - "phase_stability_score < convergence_window.lower_bound"
      - "oscillation_decay >= 0.0"

  rebalance_required:
    conditions:
      - "observed_amplitude > amplitude_threshold"
      - "oscillation_decay < 0.0"
```

This logic is illustrative.
Implementations may define more detailed rules depending on context.

## 12. Over-Convergence

Over-convergence occurs when the reasoning process appears too stable too quickly.

This may happen when:

```text id="kcxzuh"
The system locks onto one interpretation prematurely.
Contradictory evidence is ignored.
Phase diversity collapses too early.
The answer becomes rigid before review is complete.
```

In this protocol, the `upper_bound` helps detect possible over-convergence.

Example:

```yaml id="x9rkcf"
phase_stability_score: 0.97

convergence_window:
  lower_bound: 0.65
  upper_bound: 0.90
```

This does not automatically mean failure.
It means the reasoning state may need review before final convergence is accepted.

## 13. Window Adjustment

The convergence window may be adjusted depending on the control mode.

### Conservative Mode

```yaml id="m3w32q"
convergence_window:
  lower_bound: 0.60
  upper_bound: 0.92
  minimum_duration: 3
```

This allows wider fluctuation and requires longer duration.

### Balanced Mode

```yaml id="twcmri"
convergence_window:
  lower_bound: 0.65
  upper_bound: 0.90
  minimum_duration: 2
```

This is suitable for general use.

### Responsive Mode

```yaml id="k3n63n"
convergence_window:
  lower_bound: 0.70
  upper_bound: 0.88
  minimum_duration: 1
```

This reacts more quickly but may increase the risk of premature judgment.

## 14. Relationship to Adaptive Convergence

Adaptive convergence allows the convergence window or related parameters to adjust based on context.

Example:

```yaml id="st0xgp"
adaptive_convergence:
  enabled: true
  adjustment_rate: 0.25
  context_sensitivity: 0.50
```

When enabled, the system may adjust convergence behavior based on:

```text id="oe5tw6"
phase intensity
observed instability
context complexity
oscillation decay
historical stability
```

However, adaptive convergence should remain bounded.
It should not erase claim boundaries or override the parent protocol.

## 15. Practical Use

A convergence window may be useful for:

```text id="rsnqtg"
Detecting stable reasoning states
Avoiding premature closure
Preventing endless fluctuation
Supporting rebalance decisions
Documenting reasoning-control behavior
Testing protocol-level examples
```

It is especially useful when combined with:

```text id="gcx6af"
amplitude_threshold
rebalance_interval
phase_stability_score
oscillation_decay
overcorrection_limit
```

## 16. Claim Boundaries

This document describes a conceptual structure.

It does not claim:

```text id="p6qnsf"
That any specific AI model internally uses convergence windows
That convergence windows guarantee correct reasoning
That this protocol proves internal model behavior
That this protocol replaces empirical evaluation
That convergence is equivalent to truth
```

Allowed claims are more limited:

```text id="j6khvz"
This protocol defines a possible convergence-window structure.
This protocol provides terminology for stability evaluation.
This protocol may support documentation, experimentation, and validation.
```

## 17. Summary

A convergence window defines the acceptable stability range for reasoning behavior.

It helps distinguish:

```text id="bqb5yy"
instability
bounded movement
premature fixation
```

The key fields are:

```text id="gyfn82"
lower_bound
upper_bound
minimum_duration
```

In short:

```text id="b2l89f"
A convergence window does not force stillness.
It defines the range where movement becomes stable enough.
```
