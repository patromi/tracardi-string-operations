from tracardi_string_operations.model.configuration import Configuration


class Operator:
    def __init__(self, config: Configuration):
        self.config = config

    def _get_operation(self):
        dict = {"capitalize": self.config.string.capitalize(),
                "casefold": self.config.string.casefold(),
                "encode": self.config.string.encode(),
                "isalnum": self.config.string.isalnum(),
                "isalpha": self.config.string.isalpha(),
                "isascii": self.config.string.isascii(),
                "isdecimal": self.config.string.isdecimal(),
                "isdigit": self.config.string.isdigit(),
                "isidentifier": self.config.string.isidentifier(),
                "islower": self.config.string.islower(),
                "isnumeric": self.config.string.isnumeric(),
                "isprintable": self.config.string.isprintable(),
                "isspace": self.config.string.isspace(),
                "istitle": self.config.string.istitle(),
                "isupper": self.config.string.isupper(),
                "lower": self.config.string.lower(),
                "lstrip": self.config.string.lstrip(),
                "swapcase": self.config.string.swapcase(),
                "title": self.config.string.title(),
                "upper": self.config.string.upper()}
        return dict[self.config.operation]

    def execution(self):
        return self._get_operation()
