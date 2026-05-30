# Relationship to Yin-Yang Five-Phase Reasoning Protocol

## 1. Purpose of This Document

This document explains the relationship between the Yin-Yang Oscillation Control Protocol and the Yin-Yang Five-Phase Reasoning Protocol.

The Yin-Yang Oscillation Control Protocol is not a replacement for the parent protocol. It is a control-layer extension that builds on the core reasoning structure already defined by the parent repository.

In simple terms:

```text
Yin-Yang Five-Phase Reasoning Protocol
= Core reasoning structure

Yin-Yang Oscillation Control Protocol
= Dynamic control and stabilization layer
```

## 2. Parent Protocol Role

The parent protocol defines the foundation of the reasoning system.

Its main role is to describe:

```text
Five-phase reasoning structure
Yin-Yang balancing logic
Dynamic reasoning metrics
Validation foundation
Claim boundaries
Core protocol positioning
```

The parent protocol answers the question:

```text
How is the reasoning structure organized?
```

It defines the body of the reasoning system.

## 3. Extension Protocol Role

The Oscillation Control Protocol focuses on dynamic behavior after the core structure has already been defined.

It describes:

```text
Oscillation period
Amplitude threshold
Convergence window
Rebalance interval
Overcorrection limit
Phase stability score
Oscillation decay
Adaptive convergence
```

This protocol answers the question:

```text
How should the reasoning structure be dynamically tuned over time?
```

It does not define the body.
It defines posture, rhythm, and stabilization behavior.

## 4. Why the Extension Was Separated

The parent protocol reached a stable core form through the following progression:

```text
v0.1.0 = Five-Phase reasoning skeleton
v0.1.1 = Validation foundation
v0.2.0 = Dynamic control metrics
v0.3.0 = Yin-Yang Balancer
v0.3.1 = Documentation and claim-boundary polish
```

At v0.3.1, the parent protocol became sufficiently complete as a core specification.

Further additions such as convergence windows, amplitude thresholds, oscillation decay, and adaptive rebalance behavior would make the parent repository too broad.

Therefore, those concerns are separated into this extension repository.

```text
Parent protocol:
Keeps the core reasoning structure stable.

Extension protocol:
Explores control optimization without overloading the parent.
```

This separation preserves clarity.

## 5. Layer Relationship

The relationship can be understood as a layered architecture.

```text
Layer 1: Yin-Yang Five-Phase Reasoning Protocol
         - phases
         - metrics
         - balance
         - validation
         - claim boundaries

Layer 2: Yin-Yang Oscillation Control Protocol
         - oscillation tuning
         - convergence windows
         - amplitude thresholds
         - rebalance timing
         - overcorrection limits
```

The parent protocol provides the structural base.
The extension protocol provides dynamic control over that structure.

## 6. Dependency Type

This repository has a conceptual dependency on the parent protocol.

That means:

```text
The parent protocol can exist independently.
This protocol assumes the parent protocol's structure.
This protocol does not rewrite or override the parent protocol.
```

The dependency is not a runtime dependency unless an implementation chooses to make it one.

## 7. What This Protocol Adds

The parent protocol may define that reasoning should remain balanced.

This protocol adds a language for discussing how that balance may be monitored and adjusted over time.

For example:

```text
Parent protocol:
Reasoning should maintain Yin-Yang and Five-Phase balance.

Oscillation Control Protocol:
How often should balance be checked?
How much deviation is acceptable?
When is rebalance required?
How strong should correction be?
How can overcorrection be avoided?
```

This makes the extension more specific without changing the parent structure.

## 8. What This Protocol Does Not Add

This protocol does not add a new phase system.

It does not redefine:

```text
wood
fire
earth
metal
water
yin
yang
```

It also does not redefine the philosophical or structural assumptions of the parent protocol.

The extension is limited to control behavior.

It does not claim to provide:

```text
A complete AI safety system
A consciousness model
A production-ready runtime
A replacement for empirical testing
A proof of internal AI model behavior
```

## 9. Complementary Use

The two repositories should be read together.

Recommended reading order:

```text
1. Yin-Yang Five-Phase Reasoning Protocol
2. Yin-Yang Oscillation Control Protocol
```

The first gives the structural foundation.
The second gives the dynamic control layer.

A simple relationship model:

```text
Core structure
     ↓
Dynamic observation
     ↓
Stability evaluation
     ↓
Rebalance decision
     ↓
Bounded adjustment
```

## 10. Example

A parent-protocol statement may look like this:

```text
The reasoning system should maintain balance across Five-Phase and Yin-Yang dimensions.
```

An oscillation-control statement may look like this:

```text
If phase stability falls below the convergence window and observed amplitude exceeds the configured threshold, rebalance behavior may be required.
```

The first statement defines a structural principle.
The second statement defines a control-layer condition.

## 11. Why This Matters

Without separation, the parent protocol may become too large and difficult to understand.

With separation, each repository has a clear role.

```text
Parent repository:
Defines the reasoning OS.

Extension repository:
Defines the tuning engine.
```

This allows the parent protocol to remain stable while the control layer can evolve more freely.

## 12. Claim Boundary Inheritance

This protocol inherits the claim-boundary discipline of the parent protocol.

That means it should avoid unsupported claims such as:

```text
This protocol proves how AI models internally think.
This protocol guarantees correct reasoning.
This protocol creates consciousness.
This protocol replaces safety evaluation.
```

Allowed claims are more modest:

```text
This protocol defines a possible control-layer structure.
This protocol describes oscillation and convergence behavior.
This protocol may support documentation, experimentation, or validation.
```

The extension should remain structurally useful while staying technically modest.

## 13. Summary

The Yin-Yang Five-Phase Reasoning Protocol defines the structure.

The Yin-Yang Oscillation Control Protocol defines how that structure may be dynamically monitored, tuned, and stabilized.

In short:

```text
Parent = structure
Extension = control
```

Or more simply:

```text
Parent = the body
Extension = the balance mechanism
```

The purpose of this repository is to keep the core protocol clean while giving oscillation tuning and convergence optimization their own dedicated space.
