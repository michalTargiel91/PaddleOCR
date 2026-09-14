## 2024-06-12 - [Critical] Insecure YAML Deserialization
**Vulnerability:** Found `yaml.load()` which allows arbitrary code execution (RCE) in `tools/program.py`, `test_tipc/supplementary/config.py`, `benchmark/PaddleOCR_DBNet/utils/util.py` and `configs/rec/multi_language/generate_multi_language_configs.py`. Also found insecure `pickle.load()` in multiple places.
**Learning:** Python's `yaml.load` (when used with `Loader=yaml.Loader` or without a safe loader) and `pickle.load` can deserialize arbitrary Python objects, allowing for arbitrary code execution.
**Prevention:** Use `yaml.safe_load()` for YAML files, and be cautious with `pickle`. If `pickle` is necessary, ensure it is only used on trusted data.
