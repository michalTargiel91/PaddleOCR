## 2025-02-27 - Fix command injection vulnerabilities
**Vulnerability:** Found `os.system` and `subprocess.call(..., shell=True)` used to execute external commands with dynamic arguments, exposing the app to command injection if paths contain shell metacharacters.
**Learning:** These vulnerabilities exist when string formatting or concatenation is used directly in external process execution, especially when `shell=True` is explicitly enabled or implicit like with `os.system`.
**Prevention:** Always use `subprocess.Popen` or `subprocess.call` with argument lists (e.g., `["command", "arg"]`) and avoid `shell=True` for external execution.
