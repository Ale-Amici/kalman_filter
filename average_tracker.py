import numpy as np


def track_average_from_sensors(sensor_history, subset_size=10):
    average_track = None
    for i in range(sensor_history.shape[0]):
        min = max(i - subset_size, 0)
        current_subset = sensor_history[min:i+1]
        if current_subset.size > 0:
            current_average = current_subset.mean(axis=0)
            average_track = store_average(average_track, current_average)
    return average_track


def store_average(average_track, current_average):
    if average_track is None:
        average_track = np.array([current_average])
    else:
        average_track = np.concatenate((average_track, np.array([current_average])), axis=0)
    return average_track