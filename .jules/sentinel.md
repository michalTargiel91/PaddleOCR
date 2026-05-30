## 2024-05-24 - [Fix Insecure YAML Deserialization]
**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` across the codebase, allowing for arbitrary code execution during YAML parsing.
**Learning:** `yaml.Loader` in PyYAML is unsafe and can deserialize arbitrary Python objects, posing a severe security risk when parsing user-provided or external configuration files.
**Prevention:** Always use `yaml.SafeLoader` or `yaml.safe_load()` for parsing YAML files to ensure only basic YAML entities are evaluated.
