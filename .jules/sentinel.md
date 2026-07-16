## 2024-05-18 - Fix RCE vulnerability via insecure YAML deserialization
**Vulnerability:** Found `yaml.load(..., Loader=yaml.Loader)` in `tools/program.py` which allows Arbitrary Code Execution (RCE) when parsing configuration files or CLI flags.
**Learning:** `yaml.Loader` in PyYAML is unsafe and allows instantiating arbitrary Python objects. This was likely used for convenience without knowing the security implications.
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` when parsing untrusted YAML content.
