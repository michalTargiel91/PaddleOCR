## 2025-02-14 - Replace Insecure YAML Loader
**Vulnerability:** Codebase extensively uses `yaml.load(..., Loader=yaml.Loader)` instead of `yaml.SafeLoader` for parsing configuration files.
**Learning:** `yaml.Loader` allows arbitrary code execution during deserialization.
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` when parsing YAML from untrusted or configuration sources.
