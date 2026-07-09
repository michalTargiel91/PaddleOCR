## 2026-07-09 - Fix Insecure YAML Deserialization
**Vulnerability:** Arbitrary Code Execution (ACE) via `yaml.load(..., Loader=yaml.Loader)`
**Learning:** Found in multiple locations (`test_tipc/supplementary/config.py`, `configs/rec/multi_language/generate_multi_language_configs.py`, `benchmark/PaddleOCR_DBNet/utils/util.py`, `tools/program.py`), particularly in configuration loading mechanisms. Usage of `yaml.Loader` allows for arbitrary Python objects to be constructed, potentially leading to arbitrary code execution if a malicious configuration file is loaded.
**Prevention:** Replaced `yaml.Loader` with `yaml.SafeLoader`. This ensures only standard YAML types are constructed, avoiding arbitrary code execution while preserving all necessary functionality for configuration parsing.
