## 2024-10-24 - Insecure YAML Deserialization
**Vulnerability:** Arbitrary code execution via `yaml.load(..., Loader=yaml.Loader)` in configuration parsing scripts (e.g., `tools/program.py`).
**Learning:** The codebase relies heavily on YAML for model configurations, and developers used the default `yaml.Loader` which allows arbitrary Python code execution when parsing untrusted YAML files.
**Prevention:** Always use `yaml.SafeLoader` or `yaml.safe_load()` when parsing YAML files to prevent insecure deserialization vulnerabilities.
