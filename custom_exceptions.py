
class CellOcupiedError(Exception):
    """Класс исключения, отображающего, что выбранная клетка занята"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка: {self.message}'
