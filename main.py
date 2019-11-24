from vehicle import Vehicle
from matplotlib import pyplot as plt
from average_tracker import track_average_from_sensors

def plot_true_positions(vehicle, clear=True, show=True, icon='o'):
    model = vehicle.model
    if clear:
        plt.clf()
    plt.scatter(model.position_history[:, 0],
                model.position_history[:, 1],
                marker=icon,
                c=range(model.position_history.shape[0]),
                cmap='viridis')
    if show:
        plt.show()

def plot_sensed_positions(vehicle, clear=True, show=True, icon='o'):
    loc_sensor = vehicle.location_sensor
    if clear:
        plt.clf()
    plt.scatter(loc_sensor.position_history[:, 0],
                loc_sensor.position_history[:, 1],
                marker=icon,
                c=range(loc_sensor.position_history.shape[0]),
                cmap='viridis')
    if show:
        plt.show()

def plot_tracked_average(tracked_average, clear=True, show=True, icon='o'):
    if clear:
        plt.clf()
    plt.scatter(tracked_average[:, 0],
                tracked_average[:, 1],
                marker=icon,
                c=range(tracked_average.shape[0]),
                cmap='viridis')
    if show:
        plt.show()

def main():
    print("Start")
    v = Vehicle()
    v.run()
    tracked_average = track_average_from_sensors(v.location_sensor.position_history)

    # plots
    plot_true_positions(v)
    plot_sensed_positions(v)
    plot_tracked_average(tracked_average)

    plot_true_positions(v, show=False, icon='^')
    plot_sensed_positions(v, show=False, clear=False, icon='+')
    plot_tracked_average(tracked_average, clear=False)




if __name__ == "__main__":
        main()
