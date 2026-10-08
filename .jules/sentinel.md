## 2024-05-24 - [Insecure YAML Deserialization]
**Vulnerability:** Found multiple instances of `yaml.load(..., Loader=yaml.Loader)` across the codebase, which can lead to arbitrary code execution (RCE) via insecure deserialization of untrusted YAML data.
**Learning:** `yaml.load` with `Loader=yaml.Loader` is insecure and should not be used for untrusted input. Configuration files and CLI options in this repository are standard data structures.
**Prevention:** Replace unsafe `yaml.load` calls with `yaml.safe_load` or `yaml.load(..., Loader=yaml.SafeLoader)` to prevent malicious code execution.
