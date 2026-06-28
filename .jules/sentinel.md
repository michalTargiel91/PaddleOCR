
## 2025-03-01 - Insecure YAML Deserialization
**Vulnerability:** Found `yaml.load(..., Loader=yaml.Loader)` being used across the project to parse config files (e.g. `test_tipc/supplementary/config.py`, `configs/rec/multi_language/generate_multi_language_configs.py`, `benchmark/PaddleOCR_DBNet/utils/util.py`, `tools/program.py`).
**Learning:** `yaml.Loader` allows execution of arbitrary Python code when loading untrusted YAML files, posing a Remote Code Execution (RCE) risk. This happens because the default `yaml.Loader` in PyYAML deserializes arbitrary Python objects.
**Prevention:** Always use `yaml.load(..., Loader=yaml.SafeLoader)` or `yaml.safe_load(...)` which limits deserialization to standard YAML types, mitigating code execution risks.
