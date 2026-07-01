## 2026-07-01 - Use Safe YAML Deserialization
**Vulnerability:** Insecure deserialization via `yaml.load(..., Loader=yaml.Loader)`.
**Learning:** `yaml.Loader` allows arbitrary code execution in PyYAML if maliciously crafted YAML is loaded. In a machine learning codebase, configuration files may be loaded from untrusted sources.
**Prevention:** Always use `yaml.load(..., Loader=yaml.SafeLoader)` or `yaml.safe_load(...)` instead of `yaml.Loader` or `yaml.UnsafeLoader`.
