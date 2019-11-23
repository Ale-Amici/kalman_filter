import numpy as np

class LocationSensor:
    def __init__(self):
        self.bias = 0
        self.sigma = 1

    def get_measurement(self, true_value):
        noise = np.random.normal(self.bias, self.sigma, 2)
        return true_value + noise