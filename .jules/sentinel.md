## 2024-06-16 - Prevent Insecure Deserialization in YAML Parsing
**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` across the codebase (e.g., `tools/program.py`, `test_tipc/supplementary/config.py`, `benchmark/PaddleOCR_DBNet/utils/util.py`, `configs/rec/multi_language/generate_multi_language_configs.py`). `yaml.Loader` is insecure and allows arbitrary code execution during deserialization.
**Learning:** Developers likely copy-pasted configuration loading code without realizing `yaml.Loader` defaults to unsafe parsing, whereas `yaml.SafeLoader` should always be used.
**Prevention:** Always enforce the use of `yaml.SafeLoader` or `yaml.safe_load()` for YAML parsing in Python to prevent arbitrary code execution, especially for user-provided configurations.
