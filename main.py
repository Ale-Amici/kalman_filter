from vehicle import Vehicle
from matplotlib import pyplot as plt


def plot_true_positions(vehicle):
    model = vehicle.model
    plt.clf()
    plt.scatter(model.position_history[:, 0], model.position_history[:, 1])
    plt.show()

def main():
    print("Start")
    v = Vehicle()
    v.run()

    # plots
    plot_true_positions(v)




if __name__ == "__main__":
        main()
