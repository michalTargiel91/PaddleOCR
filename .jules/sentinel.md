## 2025-05-15 - Insecure YAML Deserialization

**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` which is vulnerable to arbitrary code execution if malicious YAML is parsed.
**Learning:** The codebase used `yaml.Loader` in config loading modules, which can deserialize arbitrary Python objects.
**Prevention:** Always use `yaml.SafeLoader` or `yaml.safe_load()` when parsing untrusted YAML data.
