class _GetitemToCall:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def __getitem__(self, args):
        if isinstance(args, tuple):
            return self.func(self.name, *args)
        else:
            return self.func(self.name, args)

    def __str__(self):
        return f"{_GetitemToCall.__module__}.{self.name}"

    def __repr__(self):
        return str(self)


def resolve_name_mapping(mapping):
    if mapping is None:
        return lambda x: x
    elif mapping == "lower":
        mapping = str.lower
    elif mapping == "upper":
        mapping = str.upper
    elif mapping == "capitalize":
        mapping = str.capitalize
    return mapping