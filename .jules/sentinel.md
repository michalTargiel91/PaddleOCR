## 2024-05-18 - Fix insecure YAML deserialization
**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` across the codebase.
**Learning:** `yaml.load()` with `yaml.Loader` is insecure and can execute arbitrary code during deserialization.
**Prevention:** Always use `yaml.safe_load()` for parsing YAML files.
