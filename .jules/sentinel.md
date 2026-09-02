## 2024-05-16 - Prevent Arbitrary Code Execution in YAML parsing
**Vulnerability:** Insecure deserialization via `yaml.load` using `yaml.Loader` in configuration loading scripts.
**Learning:** Configurations loaded directly from user input or external files were passing `Loader=yaml.Loader`, which permits instantiation of arbitrary Python objects and leads to remote code execution (RCE).
**Prevention:** Always enforce `Loader=yaml.SafeLoader` or use `yaml.safe_load` when parsing YAML files or configuration strings to restrict parsing to standard data types.
