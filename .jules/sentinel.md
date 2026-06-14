## 2024-05-24 - Insecure YAML Deserialization in Config Parsing
 **Vulnerability:** Multiple configuration parsing scripts (e.g., `tools/program.py`, `test_tipc/supplementary/config.py`) use `yaml.load(..., Loader=yaml.Loader)`. This allows arbitrary Python code execution if a maliciously crafted YAML file is loaded.
 **Learning:** The codebase relies heavily on custom config parsing scripts for running training/evaluation and uses `yaml.load` natively instead of `yaml.safe_load` for convenience without realizing the deserialization risk.
 **Prevention:** Always enforce the use of `yaml.safe_load()` or `yaml.load(..., Loader=yaml.SafeLoader)` across all config loading utilities in the project to eliminate insecure deserialization.
