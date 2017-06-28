class InlineStyle:
    def __init__(self, **params):
        for key, value in params.items():
            setattr(self, key.replace("_","-"), value)

    def __str__(self):
        return " ".join([f"{key}:{value};" for key, value in self.__dict__.items()])


class Class:
    def __init__(self, *params):
        self.selectors = params

    def __str__(self):
        return " ".join(self.selectors)
