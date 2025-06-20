import warnings


class PromptLoader:
    def __init__(self, filename):
        self._filename = filename

    def filename(self):
        return self._filename

    def load_prompt(self) -> str:
        try:
            with open(self._filename, "r", encoding="utf-8") as f:
                return f.read()
        except OSError:
            warnings.warn(
                message="File not found, check the provided filname. Empty prompt loaded.",
                category=RuntimeWarning,
                stacklevel=3,
            )
            return ""
