## 2026-06-10 - Insecure YAML Deserialization in Config Parsers
**Vulnerability:** Several config parsing scripts in the repository used `yaml.load(..., Loader=yaml.Loader)` rather than the secure `yaml.SafeLoader` or `yaml.safe_load()`.
**Learning:** This repo frequently parses YAML configuration files and command line config arguments through custom argument parsers. The pattern of `yaml.load(v, Loader=yaml.Loader)` allows for arbitrary code execution if a user provides a malicious YAML file or argument, which is a critical risk for machine learning applications that often run with high privileges.
**Prevention:** Always use `yaml.safe_load()` or `yaml.load(..., Loader=yaml.SafeLoader)` for all YAML deserialization, and enforce this pattern through linting or code review policies.
