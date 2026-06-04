## 2024-05-24 - Insecure YAML Deserialization
**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` across the codebase, which can lead to arbitrary code execution if an attacker provides a malicious YAML file.
**Learning:** The codebase relies heavily on YAML for configuration parsing but defaults to the insecure `yaml.Loader`. This is a common pattern for loading configurations but poses a critical risk if configuration files are ever user-supplied or fetched from untrusted sources.
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` for all YAML parsing. Tools or linters should enforce the prohibition of `Loader=yaml.Loader` or vanilla `yaml.load()` without explicit loaders.
