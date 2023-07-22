import matplotlib.pyplot as plt


def plot_trajectories(trajectories):
    plt.figure(figsize=(10, 8))

    for traj in trajectories:
        x = [point.X for point in traj.points]
        y = [point.Y for point in traj.points]
        plt.plot(x, y, label="Trajectory {}".format(traj.number))

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Trajectories")
    plt.legend()
    plt.show()


# Usage:
plot_trajectories(listOfTrajectories)