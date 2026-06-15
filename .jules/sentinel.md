## 2024-05-24 - Insecure Deserialization in YAML Parsing
**Vulnerability:** Found instances of `yaml.load(..., Loader=yaml.Loader)` across the codebase (e.g., in `tools/program.py`, `test_tipc/supplementary/config.py`).
**Learning:** `yaml.Loader` is vulnerable to arbitrary code execution if a malicious YAML payload is parsed. In Python environments, this could allow command injection or system compromise through unsafe Python tags (e.g., `!!python/object/apply:os.system`).
**Prevention:** Always use `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` instead of the default `Loader` or no loader argument. This explicitly disables the execution of custom Python objects during deserialization.
