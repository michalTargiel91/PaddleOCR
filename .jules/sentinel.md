## 2024-05-23 - Insecure YAML Deserialization in Config Loaders
**Vulnerability:** Found `yaml.load(..., Loader=yaml.Loader)` used extensively in configuration loading scripts (e.g., `tools/program.py`).
**Learning:** This existed because Python's default PyYAML `Loader` can deserialize arbitrary Python objects, allowing for arbitrary code execution if a user provides a malicious YAML file or command-line option.
**Prevention:** Always use `yaml.safe_load(...)` or explicitly pass `Loader=yaml.SafeLoader` when processing YAML input from untrusted sources.
