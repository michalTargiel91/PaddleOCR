## 2024-05-01 - Insecure Deserialization in YAML
**Vulnerability:** Several places in the codebase were using `yaml.load` with `yaml.Loader`, which allows for arbitrary Python code execution if the YAML file is malicious.
**Learning:** `yaml.load` should always use `yaml.SafeLoader` to prevent insecure deserialization.
**Prevention:** Always use `yaml.safe_load(data)` or `yaml.load(data, Loader=yaml.SafeLoader)`. Avoid `yaml.Loader`.
