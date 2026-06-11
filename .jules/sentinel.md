## 2025-02-14 - Fix Insecure YAML Load
**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` across the codebase.
**Learning:** `yaml.Loader` allows for arbitrary code execution upon deserialization of YAML files.
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` when loading untrusted YAML files.
