## 2024-05-29 - [CRITICAL] Insecure YAML Deserialization
**Vulnerability:** Use of `yaml.load(..., Loader=yaml.Loader)` instead of `yaml.safe_load(...)` or `Loader=yaml.SafeLoader`.
**Learning:** `yaml.Loader` in PyYAML allows for arbitrary code execution during deserialization if malicious YAML input (e.g. `!!python/object/apply:os.system`) is parsed.
**Prevention:** Always use `yaml.safe_load()` or specify `Loader=yaml.SafeLoader` when parsing untrusted YAML data.
