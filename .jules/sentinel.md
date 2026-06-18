## 2025-06-05 - Insecure YAML Deserialization
**Vulnerability:** Found `yaml.load` configured with `Loader=yaml.Loader` in configuration parsing files, which permits insecure deserialization and remote code execution if parsed YAML originates from an untrusted source.
**Learning:** Legacy configuration systems in the repo parsed user-provided or external configurations using `yaml.load` natively instead of `yaml.safe_load`, exposing a potentially critical security flaw.
**Prevention:** Always use `yaml.safe_load(...)` for any and all YAML parsing across the codebase to ensure objects are fully stripped of potentially arbitrary executable capabilities during parsing.
