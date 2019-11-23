
class OdometrySensor:
    def __init__(self):
        self.bias = 0
        self.sigma = 0.5

        # history
        self.position_history = None

    def get_