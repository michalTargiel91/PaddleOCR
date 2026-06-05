## 2024-06-05 - Insecure YAML Deserialization
**Vulnerability:** Use of yaml.load with yaml.Loader instead of yaml.SafeLoader.
**Learning:** Found yaml.load(..., Loader=yaml.Loader) which can execute arbitrary code during YAML parsing. The codebase utilizes yaml to load configuration files. Modifying this config deserialization from `yaml.Loader` to `yaml.SafeLoader` is critical to prevent code execution via untrusted YAML files.
**Prevention:** Always use yaml.safe_load() or yaml.load(..., Loader=yaml.SafeLoader).
