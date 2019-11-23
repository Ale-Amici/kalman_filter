import numpy as np

def track_average_from_sensors(sensor_history):
    alpha = 0.5
    average_track = None
    current_average = sensor_history[0]
    for sensor_point in sensor_history:
        current_average = current_average + alpha * (current_average - sensor_point)
        average_track = store_average(average_track, current_average)
    return average_track
def store_average(average_track, current_average):
    if average_track is None:
        average_track = np.array([current_average])
    else:
        average_track = np.concatenate((average_track, np.array([current_average])), axis=0)
    return average_track