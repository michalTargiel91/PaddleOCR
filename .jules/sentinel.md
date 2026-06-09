## 2024-05-15 - Insecure YAML Deserialization via yaml.load
**Vulnerability:** Found multiple instances using `yaml.load(..., Loader=yaml.Loader)` instead of `yaml.safe_load(...)` for parsing configuration files.
**Learning:** `yaml.load` with `Loader=yaml.Loader` allows arbitrary code execution if a maliciously crafted YAML payload is supplied, because it can instantiate arbitrary Python objects. This was likely done out of convenience for parsing arbitrary configurations without realizing the security implications.
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` when processing YAML files, especially when loading user-provided or external configurations.
