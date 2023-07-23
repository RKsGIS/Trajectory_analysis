# imports
import point
import region
import utils
import functions_template as functions
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
# Import trajectories
listOfTrajectories = utils.importTrajectories("Trajectories")
# # print(listOfTrajectories)

# Visualize trajectories

###visulize all trejactories function
def plot_trajectories(trajectories):
    plt.figure(figsize=(10, 8))

    for traj in trajectories:
        x = [point.X for point in traj.points]
        y = [point.Y for point in traj.points]
        plt.plot(x, y, label="Trajectory {}".format(traj.number))

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Trajectories")
    # plt.legend()
    plt.show()


###visulize trejactories GUI


# Define the GUI class
class TrajectoryGUI:
    def __init__(self, trajectories):
        self.trajectories = trajectories
        
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Trajectory Visualization")
        
        # Create a dropdown for trajectory selection
        self.trajectory_var = tk.StringVar()
        self.trajectory_dropdown = ttk.Combobox(self.root, textvariable=self.trajectory_var, state="readonly")
        self.trajectory_dropdown["values"] = [str(traj.number) for traj in self.trajectories]
        self.trajectory_dropdown.set("Select Trajectory")
        self.trajectory_dropdown.pack(pady=10)
        
        # Create a button to plot the selected trajectory
        self.plot_button = ttk.Button(self.root, text="Plot Selected Trajectory", command=self.plot_selected_trajectory)
        self.plot_button.pack(pady=5)
        
        # Create a button to plot all trajectories
        self.plot_all_button = ttk.Button(self.root, text="Plot All Trajectories", command=self.plot_all_trajectories)
        self.plot_all_button.pack(pady=5)
        
        # Define a colormap for trajectories
        self.cmap = get_cmap('tab20')
        
    def plot_trajectory(self, traj):
        x = [point.X for point in traj.points]
        y = [point.Y for point in traj.points]
        color = self.cmap(traj.number % 20)  # Assign a unique color based on trajectory number
        plt.plot(x, y, label="Trajectory {}".format(traj.number), color=color)
        
    def plot_selected_trajectory(self):
        selected_trajectory = int(self.trajectory_var.get())
        for traj in self.trajectories:
            if traj.number == selected_trajectory:
                plt.figure()
                self.plot_trajectory(traj)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Trajectory {}".format(selected_trajectory))
                plt.legend()
                plt.grid(True)
                plt.gca().set_aspect("equal")
                plt.tight_layout()
                plt.show()
                break
        
    def plot_all_trajectories(self):
        plt.figure()
        for traj in self.trajectories:
            self.plot_trajectory(traj)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("All Trajectories")
        # plt.legend()
        plt.grid(True)
        plt.gca().set_aspect("equal")
        plt.tight_layout()
        plt.show()
        
    def run(self):
        self.root.mainloop()




# Simplify at least one of the trajectories with Douglas Peucker and/or Sliding Window Algorithm

# Visualize original trajectory and its two simplifications

# Calculate the distance between at least two trajectories with Closest-Pair-Distance and/or Dynamic Time Warping

# Build R-tree with all given 62 trajectories

# Query the trajectories using the built R-tree and the region. Which trajectories lie in the given region?
# This query should return the trajectories with ids 43, 45, 50, 71, 83


# queryRegion = region.region(point.point(0.0012601754558545508,0.0027251228043638775,0.0),0.00003)
# foundTrajectories = functions.solveQueryWithRTree(queryRegion,listOfTrajectories)
# if foundTrajectories != None:
#     if len(foundTrajectories)==0:
#         print("No trajectories match the query.")
#     for t in foundTrajectories:
#         print(t)