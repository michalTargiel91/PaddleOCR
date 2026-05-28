## 2024-05-28 - Insecure yaml.load usage
**Vulnerability:** Found multiple usages of `yaml.load` with `yaml.Loader`, which can result in arbitrary code execution if untrusted YAML is parsed.
**Learning:** This occurs across multiple scripts including test configurations and program entry points, suggesting it's an older codebase where SafeLoader wasn't strictly enforced.
**Prevention:** Replace all usages of `yaml.load(..., Loader=yaml.Loader)` with `yaml.safe_load(...)` or `yaml.load(..., Loader=yaml.SafeLoader)` to prevent arbitrary code execution vulnerabilities.
