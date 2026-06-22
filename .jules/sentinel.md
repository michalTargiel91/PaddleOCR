## 2024-05-24 - Insecure YAML Deserialization
**Vulnerability:** Use of `yaml.load(..., Loader=yaml.Loader)` which is vulnerable to insecure deserialization (arbitrary code execution).
**Learning:** Config parsers in python frequently default to full yaml loaders instead of safe loaders out of convenience or outdated habits, exposing tools to RCE if maliciously crafted config files are parsed.
**Prevention:** Always use `yaml.safe_load()` or `yaml.load(..., Loader=yaml.SafeLoader)` when parsing YAML files unless custom object deserialization is strictly required and trusted.
