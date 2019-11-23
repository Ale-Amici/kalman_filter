from vehicle import Vehicle
from matplotlib import pyplot as plt
from average_tracker import track_average_from_sensors

def plot_true_positions(vehicle):
    model = vehicle.model
    plt.clf()
    plt.scatter(model.position_history[:, 0], model.position_history[:, 1])
    plt.show()

def plot_sensed_positions(vehicle):
    loc_sensor = vehicle.location_sensor
    plt.clf()
    plt.scatter(loc_sensor.position_history[:, 0], loc_sensor.position_history[:, 1])
    plt.show()

def plot_tracked_average(tracked_average):
    plt.clf()
    plt.scatter(tracked_average[:, 0], tracked_average[:, 1])
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




if __name__ == "__main__":
        main()
