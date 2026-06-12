## 2024-05-24 - Unsafe YAML loading in tools/program.py
**Vulnerability:** The code uses `yaml.load(v, Loader=yaml.Loader)` which can lead to arbitrary code execution if an attacker provides a malicious YAML payload.
**Learning:** This repo was relying on the default `yaml.load()` and `yaml.Loader` which is unsafe because it allows instantiating arbitrary python objects.
**Prevention:** Always use `yaml.safe_load(v)` or `yaml.load(v, Loader=yaml.SafeLoader)`.
