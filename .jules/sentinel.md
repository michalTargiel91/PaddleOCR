## 2026-06-27 - [Insecure YAML Deserialization]
**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` which is vulnerable to insecure deserialization (RCE).
**Learning:** The codebase was still using the unsafe `yaml.Loader` for parsing configurations, potentially allowing attackers to execute arbitrary code if they can provide malicious YAML files.
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` when parsing YAML.
