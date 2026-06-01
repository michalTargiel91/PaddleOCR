## 2025-02-14 - Fix Insecure YAML Deserialization
**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` across the codebase (e.g., config parsers, benchmarks).
**Learning:** PyYAML's default `Loader` allows executing arbitrary Python commands embedded in YAML files (e.g., via `!!python/object/apply`). This can lead to Remote Code Execution (RCE) if an attacker can manipulate config files.
**Prevention:** Always use `yaml.safe_load()` or explicitly pass `Loader=yaml.SafeLoader` when parsing untrusted YAML content.
