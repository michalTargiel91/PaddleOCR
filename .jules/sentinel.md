## 2025-02-12 - Fix insecure yaml.load usage
**Vulnerability:** Found insecure usage of `yaml.load(..., Loader=yaml.Loader)` in config loading files (`tools/program.py`, `benchmark/PaddleOCR_DBNet/utils/util.py`, `configs/rec/multi_language/generate_multi_language_configs.py`, `test_tipc/supplementary/config.py`).
**Learning:** This repo frequently parses user-supplied configuration flags via CLI by splitting key-value pairs and using `yaml.load()` on the value with `Loader=yaml.Loader`. This is an arbitrary code execution risk if a malicious yaml payload is passed via CLI flag or config file.
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` when parsing yaml.
