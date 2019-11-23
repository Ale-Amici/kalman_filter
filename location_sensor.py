import numpy as np


class LocationSensor:
    def __init__(self):
        self.bias = 0
        self.sigma = 0.5
        self.current_position = None
        # history
        self.position_history = None

    def _store_state(self):
        if self.position_history is None:
            self.position_history = np.array([self.current_position])
        else:
            self.position_history = np.concatenate((self.position_history, np.array([self.current_position])), axis=0)

    def get_measurement(self, true_value):
        noise = np.random.normal(self.bias, self.sigma, 2)
        self.current_position =  true_value + noise
        self._store_state()
        return self.current_position
