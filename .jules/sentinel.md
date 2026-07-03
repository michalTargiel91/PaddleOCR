## 2024-05-18 - Insecure YAML Deserialization
**Vulnerability:** The application uses `yaml.load(..., Loader=yaml.Loader)` which can execute arbitrary Python code when parsing untrusted YAML files.
**Learning:** Configuration parsing logic must always use safe parsing methods to prevent Remote Code Execution (RCE) via malicious config files.
**Prevention:** Always use `yaml.safe_load()` or `yaml.load(..., Loader=yaml.SafeLoader)` when parsing YAML.
