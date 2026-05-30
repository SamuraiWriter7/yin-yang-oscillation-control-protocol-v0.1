#!/usr/bin/env python3
"""
Validation script for the Yin-Yang Oscillation Control Protocol.

This script validates:

1. Core protocol specification:

   * spec/oscillation-control-protocol-v0.1.yaml
   * against schemas/oscillation-control.schema.json

2. Example YAML files:

   * examples/convergence-window.example.yaml
   * examples/amplitude-threshold.example.yaml
   * examples/rebalance-interval.example.yaml

The examples are checked for YAML validity and basic structural integrity.
"""

from **future** import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT_DIR = Path(**file**).resolve().parents[1]

SPEC_PATH = ROOT_DIR / "spec" / "oscillation-control-protocol-v0.1.yaml"
SCHEMA_PATH = ROOT_DIR / "schemas" / "oscillation-control.schema.json"

EXAMPLE_PATHS = [
ROOT_DIR / "examples" / "convergence-window.example.yaml",
ROOT_DIR / "examples" / "amplitude-threshold.example.yaml",
ROOT_DIR / "examples" / "rebalance-interval.example.yaml",
]

def load_yaml(path: Path) -> Any:
"""Load a YAML file."""
with path.open("r", encoding="utf-8") as file:
return yaml.safe_load(file)

def load_json(path: Path) -> Any:
"""Load a JSON file."""
with path.open("r", encoding="utf-8") as file:
return json.load(file)

def validate_file_exists(path: Path) -> None:
"""Ensure that a required file exists."""
if not path.exists():
raise FileNotFoundError(f"Required file not found: {path}")

def validate_spec() -> None:
"""Validate the main protocol YAML against the JSON Schema."""
print(f"Validating spec: {SPEC_PATH.relative_to(ROOT_DIR)}")

```
validate_file_exists(SPEC_PATH)
validate_file_exists(SCHEMA_PATH)

spec_data = load_yaml(SPEC_PATH)
schema_data = load_json(SCHEMA_PATH)

validator = Draft202012Validator(schema_data)
errors = sorted(
    validator.iter_errors(spec_data),
    key=lambda error: list(error.path),
)

if errors:
    print("Spec validation failed:")
    for error in errors:
        location = "/".join(str(part) for part in error.path)
        location = location if location else "<root>"
        print(f"  - {location}: {error.message}")
    raise ValueError("Spec validation failed.")

print("Spec validation passed.")
```

def validate_example_basic_structure(path: Path, data: Any) -> None:
"""Validate basic structure for example YAML files."""
if not isinstance(data, dict):
raise ValueError(f"{path.name}: example file must contain a YAML object.")

```
required_top_level_keys = [
    "example",
    "description",
    "parent_protocol",
    "evaluation_context",
    "decision_logic",
    "example_result",
    "recommended_response",
    "claim_boundary",
]

missing_keys = [
    key for key in required_top_level_keys
    if key not in data
]

if missing_keys:
    raise ValueError(
        f"{path.name}: missing required top-level keys: {', '.join(missing_keys)}"
    )

example = data.get("example")
if not isinstance(example, dict):
    raise ValueError(f"{path.name}: 'example' must be an object.")

for key in ["id", "name", "version", "type"]:
    if key not in example:
        raise ValueError(f"{path.name}: example.{key} is required.")

parent_protocol = data.get("parent_protocol")
if not isinstance(parent_protocol, dict):
    raise ValueError(f"{path.name}: 'parent_protocol' must be an object.")

for key in ["id", "version"]:
    if key not in parent_protocol:
        raise ValueError(f"{path.name}: parent_protocol.{key} is required.")
```

def validate_examples() -> None:
"""Validate example YAML files for parseability and basic structure."""
for path in EXAMPLE_PATHS:
print(f"Validating example: {path.relative_to(ROOT_DIR)}")

```
    validate_file_exists(path)
    data = load_yaml(path)
    validate_example_basic_structure(path, data)

    print(f"Example validation passed: {path.name}")
```

def main() -> int:
"""Run all validations."""
try:
validate_spec()
validate_examples()
except Exception as error:
print("")
print("Validation failed.")
print(f"Error: {error}")
return 1

```
print("")
print("All validations passed.")
return 0
```

if **name** == "**main**":
sys.exit(main())
