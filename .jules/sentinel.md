## 2024-06-21 - Insecure YAML Deserialization in Config Parsing
**Vulnerability:** The codebase was using `yaml.load(..., Loader=yaml.Loader)` directly when parsing YAML configuration files in tools, tests, and benchmarks. This is vulnerable to arbitrary code execution if a malicious payload is supplied via a YAML file, as `yaml.Loader` is insecure.
**Learning:** Config parsing logic often uses unsafe defaults. The YAML loading approach was duplicated across multiple configuration loaders (e.g., in `tools/program.py`, `test_tipc/supplementary/config.py`).
**Prevention:** Always use `yaml.SafeLoader` or `yaml.safe_load()` instead of `yaml.Loader` or `yaml.load()` for deserializing YAML to guarantee safety against arbitrary code execution payloads.
