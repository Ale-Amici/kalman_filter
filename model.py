import math
import numpy as np

class Model:
    '''
    Simple model of a vehicle moving in a circle with constant speed
    '''
    def __init__(self):
        # model parameters
        self.angular_velocity = 4
        self.delta_t = 1  # 1 second
        self.radius = 10
        self.current_angle = 0

        # history
        self.position_history = None
        # model init
        self.time_step = 0
        self.update_state()
        self.time_step = 0



    def update_state(self):
        self.update_current_angle()
        self.x, self.y = self.get_true_position()
        self.x_dot, self.y_dot = self.get_true_velocity()
        self.time_step += 1
        if self.position_history is None:
            self.position_history = np.array([[self.x, self.y]])
        else:
            self.position_history = np.concatenate((self.position_history, np.array([[self.x, self.y]])), axis=0)

    def update_current_angle(self):
        self.current_angle = math.radians(self.time_step * self.angular_velocity)

    def get_true_position(self):
        x = math.cos(self.current_angle) * self.radius
        y = math.sin(self.current_angle) * self.radius
        return np.array([x, y])

    def get_true_velocity(self):
        x_dot = -math.sin(self.current_angle) * self.radius
        y_dot = math.cos(self.current_angle) * self.radius
        return np.array([x_dot, y_dot])

