# imports
import numpy as np
import point
import region
import utils
import functions
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.cm import get_cmap

import math
from typing import List

import trajectory 
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

# Simplify at least one of the trajectories with Douglas Peucker and/or Sliding Window Algorithm
def perpendicular_distance(point, line_start, line_end):
    """
    Calculate the perpendicular distance between a point and a line segment.
    """
    x, y = point
    start_x, start_y = line_start
    end_x, end_y = line_end
    # Calculate the slope of the line
    line_slope = (end_y - start_y) / (end_x - start_x)
    # Calculate the y-intercept of the line
    line_intercept = start_y - line_slope * start_x
    # Calculate the perpendicular distance
    distance = abs(line_slope * x - y + line_intercept) / np.sqrt(line_slope ** 2 + 1)
    return distance


def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    if len(points) < 3:
        return points

    # Get the start and end points (numeric X and Y coordinates only)
    start = np.array(points[0][:2])
    end = np.array(points[-1][:2])

    # Find distance from other points to the line formed by start and end
    dist_point_to_line = [perpendicular_distance(point[:2], start, end) for point in points]
    # Get the index of the points with the largest distance
    max_idx = np.argmax(dist_point_to_line)
    max_value = dist_point_to_line[max_idx]

    result = []
    if max_value > epsilon:
        partial_results_left = douglas_peucker(points[:max_idx + 1], epsilon)
        result += partial_results_left
        partial_results_right = douglas_peucker(points[max_idx:], epsilon)
        result += partial_results_right[1:]  # Exclude the duplicate point
    else:
        result += [points[0], points[-1]]

    return result


epsilon = 0.0001
simplified_trajectories = []
for trajectory in listOfTrajectories:
    points = [(point.X, point.Y) for point in trajectory.points]  # Extract (X, Y) coordinates from each point
    simplified_traj = douglas_peucker(points, epsilon)
    simplified_trajectories.append(simplified_traj)

# Visualize original trajectory and its two simplifications

class TrajectoryComparisonGUI:
    def __init__(self, original_trajectories, simplified_trajectories):
        self.original_trajectories = original_trajectories
        self.simplified_trajectories = simplified_trajectories
        self.num_trajectories = len(original_trajectories)

        self.root = tk.Tk()
        self.root.title("Trajectory Comparison")

        self.trajectory_var = tk.StringVar()
        self.trajectory_var.set("1")

        self.trajectory_dropdown = ttk.Combobox(self.root, textvariable=self.trajectory_var, state="readonly")
        self.trajectory_dropdown["values"] = [str(i) for i in range(1, self.num_trajectories + 1)]
        self.trajectory_dropdown.pack(pady=10)

        self.plot_button = ttk.Button(self.root, text="Plot", command=self.plot_trajectory_comparison)
        self.plot_button.pack(pady=5)

        self.figure, self.ax = plt.subplots(figsize=(10, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()

    def plot_trajectory_comparison(self):
        selected_trajectory = int(self.trajectory_var.get()) - 1

        self.ax.clear()
        original_traj = self.original_trajectories[selected_trajectory]
        simplified_traj = self.simplified_trajectories[selected_trajectory]

        original_points = [(point.X, point.Y) for point in original_traj.points]
        simplified_points = simplified_traj
        original_x, original_y = zip(*original_points)
        simplified_x, simplified_y = zip(*simplified_points)

        self.ax.plot(original_x, original_y, label=f"Original Trajectory {selected_trajectory + 1}", color='blue')
        self.ax.plot(simplified_x, simplified_y, label=f"Simplified Trajectory DP {selected_trajectory + 1}", color='red', linestyle='dashed')
        self.ax.legend()
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title(f"Trajectory Comparison: Original vs. Simplified (Trajectory DP {selected_trajectory + 1})")

        self.canvas.draw()

    def run(self):
        self.root.mainloop()

# Calculate the distance between at least two trajectories with Closest-Pair-Distance and/or Dynamic Time Warping

# Build R-tree with all given 62 trajectories



# Query the trajectories using the built R-tree and the region. Which trajectories lie in the given region?
# This query should return the trajectories with ids 43, 45, 50, 71, 83



from trajectory import Trajectory  # Update the import statement to use the class from trajectory.py


def euclidean_distance(p1: point.point, p2: point.point) -> float:
    return math.sqrt((p1.X - p2.X) ** 2 + (p1.Y - p2.Y) ** 2)

def point_in_region(query_point: point.point, query_region: region.region) -> bool:
    distance = euclidean_distance(query_point, query_region.center)
    return distance <= query_region.radius

def solveQueryWithoutRTree(r: region.region, trajectories: List[Trajectory]) -> List[Trajectory]:
    found_trajectories = []
    
    for traj in trajectories:
        for p in traj.points:
            if point_in_region(p, r):
                found_trajectories.append(traj)
                break  # Add the trajectory once and move to the next one

    return found_trajectories

## to verify 


queryRegion = region.region(point.point(0.0012601754558545508, 0.0027251228043638775, 0.0), 0.00003)
foundTrajectories = solveQueryWithoutRTree(queryRegion, listOfTrajectories)

if foundTrajectories:
    print("Trajectories within the query region:")
    for t in foundTrajectories:
        print(t.number)
else:
    print("No trajectories match the query.")

    