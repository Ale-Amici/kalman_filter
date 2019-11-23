from model import Model
from location_sensor import LocationSensor
#from odometry_sensor import OdometrySensor

class Vehicle:
    def __init__(self):
        self.model = Model()
        self.location_sensor = LocationSensor()
        #self.odometry_sensor = OdometrySensor()

        self.n_timestep = 90

    def run(self):
        for time_step in range(self.n_timestep):
            self.model.update_state()