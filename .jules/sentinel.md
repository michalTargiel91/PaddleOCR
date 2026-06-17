## 2024-05-24 - Fix Insecure YAML Deserialization
**Vulnerability:** Found multiple instances using `yaml.load(..., Loader=yaml.Loader)` to deserialize YAML configurations. This is vulnerable to Arbitrary Code Execution if untrusted YAML is parsed.
**Learning:** Python's `yaml.load` with `yaml.Loader` allows instantiating arbitrary Python objects, making it unsafe. It was likely used because it's the default or out of habit, without realizing the security implications for configuration files.
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` when parsing YAML from untrusted sources or as a general best practice for configuration files to prevent insecure deserialization.
