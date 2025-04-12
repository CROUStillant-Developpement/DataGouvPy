class DataGouvAPIError(Exception):
    def __init__(self, error: str = "Une erreur est survenue lors de la requête."):
        self.error = error
