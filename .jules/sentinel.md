## YYYY-MM-DD - Insecure YAML Deserialization
**Vulnerability:** Found multiple usages of `yaml.load(..., Loader=yaml.Loader)` when parsing user-provided configuration files and strings, enabling arbitrary code execution.
**Learning:** PyYAML's `Loader` permits instantiation of Python objects, making it unsafe for untrusted input. The safe alternative is `yaml.SafeLoader` or `yaml.safe_load()`.
**Prevention:** Use `yaml.safe_load(...)` or explicitly pass `Loader=yaml.SafeLoader` in all `yaml.load` calls to prevent unsafe deserialization.
