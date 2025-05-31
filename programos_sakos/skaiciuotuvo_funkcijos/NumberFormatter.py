class NumberFormatter:

    @staticmethod
    def nuliui_ne(value):
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        else:
            return str(value)