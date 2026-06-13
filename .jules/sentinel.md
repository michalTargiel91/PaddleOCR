## 2025-06-13 - Insecure YAML Deserialization
**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` which can lead to arbitrary code execution if an attacker supplies a malicious YAML file.
**Learning:** `yaml.Loader` allows for custom python objects to be instantiated. If an untrusted YAML configuration is parsed, an attacker can leverage PyYAML's `!!python/object/apply` tags to execute arbitrary Python code. This project uses `.yml` for model configurations, which may be supplied by end users.
**Prevention:** Always use `yaml.safe_load()` or `yaml.load(..., Loader=yaml.SafeLoader)` which disables the execution of arbitrary code and only parses basic data types.
