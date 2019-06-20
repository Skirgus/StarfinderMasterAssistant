class RaceListDto:
    """
    Dto для списка рас

        id - идентификатор
        displayName - отображаемое название

    """
    def __init__(self, id, displayName):
        self.id = id
        self.displayName = displayName