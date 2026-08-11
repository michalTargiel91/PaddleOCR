## 2025-02-20 - Fix insecure YAML deserialization
**Vulnerability:** Arbitrary code execution (ACE) vulnerability via insecure YAML deserialization. The codebase used `yaml.load(..., Loader=yaml.Loader)` to parse configuration files and command-line arguments in multiple files.
**Learning:** `yaml.Loader` allows constructing arbitrary Python objects (like executing shell commands). In a codebase taking arbitrary config files, this is highly dangerous.
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` when parsing external or user-provided YAML configurations to prevent arbitrary object instantiation.
