class NotFoundError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class DuplicateError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Conflit(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
