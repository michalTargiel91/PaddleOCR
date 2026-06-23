## 2024-05-24 - Fix insecure YAML deserialization
**Vulnerability:** Arbitrary code execution vulnerability via insecure YAML deserialization using `yaml.Loader`.
**Learning:** `yaml.load(..., Loader=yaml.Loader)` allows the instantiation of arbitrary Python objects, which is a known vector for remote code execution if the YAML input is not entirely trusted.
**Prevention:** Always use `yaml.SafeLoader` or `yaml.safe_load()` for parsing YAML files.
