## 2024-07-10 - Insecure YAML Deserialization
**Vulnerability:** Found uses of `yaml.load(..., Loader=yaml.Loader)` which is vulnerable to arbitrary code execution if an attacker can control the YAML input.
**Learning:** The codebase was widely using `yaml.Loader` instead of `yaml.SafeLoader` for loading configurations.
**Prevention:** Always use `yaml.SafeLoader` or `yaml.safe_load` when parsing YAML, especially from user input or external files.
