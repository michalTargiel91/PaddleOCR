## 2024-05-18 - Insecure Deserialization via yaml.load
**Vulnerability:** Found multiple usages of `yaml.load(..., Loader=yaml.Loader)` and `yaml.load(...)` across the codebase, which allow for insecure deserialization of YAML files.
**Learning:** This existed because `Loader=yaml.Loader` was explicitly specified in many places for reading configuration files, likely due to legacy code or lack of awareness of the dangers of `yaml.Loader` in PyYAML, which allows arbitrary Python code execution.
**Prevention:** Always use `yaml.safe_load()` or `yaml.load(..., Loader=yaml.SafeLoader)` for parsing YAML to prevent this class of vulnerabilities.
