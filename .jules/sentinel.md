## 2024-06-20 - Fix Insecure YAML Deserialization
**Vulnerability:** The codebase uses `yaml.load(..., Loader=yaml.Loader)` to parse configuration files (e.g., in `tools/program.py`, `test_tipc/supplementary/config.py`, etc.), exposing the application to arbitrary code execution via crafted YAML files.
**Learning:** Because the project relies heavily on dynamic configuration loading, the use of the default/unsafe loader was widespread. This is a common pattern in machine learning projects where configs dictate execution logic.
**Prevention:** Enforce the use of `yaml.safe_load()` or `yaml.load(..., Loader=yaml.SafeLoader)` for all YAML parsing to prevent insecure deserialization.
