## 2024-05-24 - [Insecure YAML Deserialization]
 **Vulnerability:** Found uses of `yaml.load` and `Loader=yaml.Loader` which allow arbitrary code execution when parsing malicious YAML configs.
 **Learning:** Legacy code used the standard loader which parses `!!python/object/apply` tags. This project loads configurations from external files heavily, making this a critical Remote Code Execution (RCE) vector.
 **Prevention:** Always use `yaml.safe_load(file)` or `yaml.load(file, Loader=yaml.SafeLoader)`. Ensure all `yaml.load` calls explicitly specify the safe loader.
