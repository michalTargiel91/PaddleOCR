## 2024-05-20 - [Unsafe YAML parsing]
**Vulnerability:** Found `yaml.load` being used with `Loader=yaml.Loader` in several files.
**Learning:** `yaml.load` can execute arbitrary python commands if used with the default or full loader.
**Prevention:** Always use `yaml.safe_load` or `yaml.load(..., Loader=yaml.SafeLoader)` instead.
