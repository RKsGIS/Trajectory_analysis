# %%
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

# %%
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

# %%
# imports
import point
import region
import utils
import functions_template as functions

# Import trajectories
listOfTrajectories = utils.importTrajectories("Trajectories")
print(listOfTrajectories)


# %%
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

# %%
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

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
        self.plot_button = ttk.Button(self.root, text="Plot", command=self.plot_trajectory)
        self.plot_button.pack(pady=5)
        
    def plot_trajectory(self):
        selected_trajectory = int(self.trajectory_var.get())
        for traj in self.trajectories:
            if traj.number == selected_trajectory:
                x = [point.X for point in traj.points]
                y = [point.Y for point in traj.points]
                plt.plot(x, y, label="Trajectory {}".format(traj.number))
                break
        
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Trajectory {}".format(selected_trajectory))
        plt.legend()
        plt.grid(True)
        plt.gca().set_aspect("equal")
        plt.tight_layout()
        plt.show()
        
    def run(self):
        self.root.mainloop()

# Usage:
gui = TrajectoryGUI(listOfTrajectories)
gui.run()


# %%
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Assuming you have a list of trajectories named 'listOfTrajectories'

# Define the colormap
cmap = cm.get_cmap('viridis')  # Choose a colormap of your preference

# Iterate over the trajectories and assign a color based on their timestamps
for i, trajectory in enumerate(listOfTrajectories):
    # Calculate the normalized timestamp value (range [0, 1])
    timestamps = [point.timestamp for point in trajectory.points]
    min_timestamp = min(timestamps)
    max_timestamp = max(timestamps)
    norm_timestamps = [(timestamp - min_timestamp) / (max_timestamp - min_timestamp) for timestamp in timestamps]

    # Assign color based on the normalized timestamp
    color = cmap(norm_timestamps[0])  # Use the color of the first point in the trajectory

    # Plot the trajectory with the assigned color
    x = [point.X for point in trajectory.points]
    y = [point.Y for point in trajectory.points]
    plt.plot(x, y, color=color)

# Show the plot
plt.show()


# %%
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from datetime import datetime

# Assuming you have a list of trajectories named 'listOfTrajectories'

# Define the colormap
cmap = cm.get_cmap('viridis')  # Choose a colormap of your preference

# Iterate over the trajectories and assign a color based on their timestamps
for i, trajectory in enumerate(listOfTrajectories):
    # Convert timestamp strings to datetime objects
    timestamps = [datetime.strptime(point.timestamp, '%Y-%m-%d:%H:%M:%S') for point in trajectory.points]

    # Calculate the range of timestamps
    min_timestamp = min(timestamps)
    max_timestamp = max(timestamps)
    timestamp_range = max_timestamp - min_timestamp

    # Assign color based on the normalized timestamp
    for point in trajectory.points:
        norm_timestamp = (datetime.strptime(point.timestamp, '%Y-%m-%d:%H:%M:%S') - min_timestamp) / timestamp_range
        color = cmap(norm_timestamp)  # Assign color based on the normalized timestamp

        # Plot the point with the assigned color
        plt.scatter(point.X, point.Y, color=color)

# Show the plot
plt.show()


# %%
def plot_trajectory(self):
    selected_trajectory = int(self.trajectory_var.get())
    
    # Clear the previous plot
    plt.clf()
    
    for traj in self.trajectories:
        if traj.number == selected_trajectory:
            x = [point.X for point in traj.points]
            y = [point.Y for point in traj.points]
            
            # Update the plot with the selected trajectory
            plt.plot(x, y, label="Trajectory {}".format(traj.number))
            
            # Assign colors based on timestamps
            timestamps = [datetime.strptime(point.timestamp, '%Y-%m-%d:%H:%M:%S') for point in traj.points]
            min_timestamp = min(timestamps)
            max_timestamp = max(timestamps)
            timestamp_range = max_timestamp - min_timestamp
            cmap = cm.get_cmap('viridis')
            
            for point, timestamp in zip(traj.points, timestamps):
                norm_timestamp = (timestamp - min_timestamp) / timestamp_range
                color = cmap(norm_timestamp)
                plt.scatter(point.X, point.Y, color=color)
            
            break
    
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Trajectory {}".format(selected_trajectory))
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect("equal")
    plt.tight_layout()
    plt.show()


# %%
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from datetime import datetime

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
        self.plot_button = ttk.Button(self.root, text="Plot", command=self.plot_trajectory)
        self.plot_button.pack(pady=5)
        
    def plot_trajectory(self):
        selected_trajectory = int(self.trajectory_var.get())
        for traj in self.trajectories:
            if traj.number == selected_trajectory:
                x = [point.X for point in traj.points]
                y = [point.Y for point in traj.points]
                
                # Clear the previous plot
                plt.clf()
                
                # Assign colors based on timestamps
                timestamps = [datetime.strptime(point.timestamp, '%Y-%m-%d:%H:%M:%S') for point in traj.points]
                min_timestamp = min(timestamps)
                max_timestamp = max(timestamps)
                timestamp_range = max_timestamp - min_timestamp
                cmap = cm.get_cmap('viridis')
                
                for point, timestamp in zip(traj.points, timestamps):
                    norm_timestamp = (timestamp - min_timestamp) / timestamp_range
                    color = cmap(norm_timestamp)
                    plt.scatter(point.X, point.Y, color=color)
                
                plt.plot(x, y, label="Trajectory {}".format(traj.number))
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Trajectory {}".format(selected_trajectory))
                plt.legend()
                plt.grid(True)
                plt.gca().set_aspect("equal")
                plt.tight_layout()
                plt.show()
                
                break
        
    def run(self):
        self.root.mainloop()

# Usage:
gui = TrajectoryGUI(listOfTrajectories)
gui.run()


# %%
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from datetime import datetime

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
        self.plot_button = ttk.Button(self.root, text="Plot", command=self.plot_trajectory)
        self.plot_button.pack(pady=5)
        
    def plot_trajectory(self):
        selected_trajectory = int(self.trajectory_var.get())
        for traj in self.trajectories:
            if traj.number == selected_trajectory:
                x = [point.X for point in traj.points]
                y = [point.Y for point in traj.points]
                
                # Clear the previous plot
                plt.clf()
                
                # Assign colors based on timestamps
                timestamps = [datetime.strptime(point.timestamp, '%Y-%m-%d:%H:%M:%S') for point in traj.points]
                min_timestamp = min(timestamps)
                max_timestamp = max(timestamps)
                timestamp_range = max_timestamp - min_timestamp
                cmap = cm.get_cmap('viridis')
                
                norm_timestamps = [(timestamp - min_timestamp) / timestamp_range for timestamp in timestamps]
                color = cmap(norm_timestamps[0])
                plt.plot(x, y, color=color, label="Trajectory {}".format(traj.number))
                
                # Iterate over the points and connect them with lines using the assigned colors
                for i in range(1, len(x)):
                    color = cmap(norm_timestamps[i])
                    plt.plot([x[i-1], x[i]], [y[i-1], y[i]], color=color)
                
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Trajectory {}".format(selected_trajectory))
                plt.legend()
                plt.grid(True)
                plt.gca().set_aspect("equal")
                plt.tight_layout()
                plt.show()
                
                break
        
    def run(self):
        self.root.mainloop()

# Usage:
gui = TrajectoryGUI(listOfTrajectories)
gui.run()


# %%
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from datetime import datetime

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
        self.plot_button = ttk.Button(self.root, text="Plot", command=self.plot_trajectory)
        self.plot_button.pack(pady=5)
        
    def plot_trajectory(self):
        selected_trajectory = int(self.trajectory_var.get())
        for traj in self.trajectories:
            if traj.number == selected_trajectory:
                x = [point.X for point in traj.points]
                y = [point.Y for point in traj.points]
                
                # Clear the previous plot
                plt.clf()
                
                # Assign colors based on timestamps
                timestamps = [datetime.strptime(point.timestamp, '%Y-%m-%d:%H:%M:%S') for point in traj.points]
                min_timestamp = min(timestamps)
                max_timestamp = max(timestamps)
                timestamp_range = max_timestamp - min_timestamp
                cmap = cm.get_cmap('blue')
                
                norm_timestamps = [(timestamp - min_timestamp) / timestamp_range for timestamp in timestamps]
                color = cmap(norm_timestamps[0])
                plt.plot(x, y, color=color, label="Trajectory {}".format(traj.number))
                
                # Iterate over the points and connect them with lines using the assigned colors
                for i in range(1, len(x)):
                    color = cmap(norm_timestamps[i])
                    plt.plot([x[i-1], x[i]], [y[i-1], y[i]], color=color)
                
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Trajectory {}".format(selected_trajectory))
                plt.legend()
                plt.grid(True)
                plt.gca().set_aspect("equal")
                plt.tight_layout()
                plt.show()
                
                break
        
    def run(self):
        self.root.mainloop()

# Usage:
gui = TrajectoryGUI(listOfTrajectories)
gui.run()


# %%
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from datetime import datetime

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
        self.plot_button = ttk.Button(self.root, text="Plot", command=self.plot_trajectory)
        self.plot_button.pack(pady=5)
        
    def plot_trajectory(self):
        selected_trajectory = int(self.trajectory_var.get())
        for traj in self.trajectories:
            if traj.number == selected_trajectory:
                x = [point.X for point in traj.points]
                y = [point.Y for point in traj.points]
                
                # Clear the previous plot
                plt.clf()
                
                # Assign colors based on timestamps
                timestamps = [datetime.strptime(point.timestamp, '%Y-%m-%d:%H:%M:%S') for point in traj.points]
                min_timestamp = min(timestamps)
                max_timestamp = max(timestamps)
                timestamp_range = max_timestamp - min_timestamp
                cmap = cm.get_cmap('blues')
                
                norm_timestamps = [(timestamp - min_timestamp) / timestamp_range for timestamp in timestamps]
                color = cmap(norm_timestamps[0])
                plt.plot(x, y, color=color, label="Trajectory {}".format(traj.number))
                
                # Iterate over the points and connect them with lines using the assigned colors
                for i in range(1, len(x)):
                    color = cmap(norm_timestamps[i])
                    plt.plot([x[i-1], x[i]], [y[i-1], y[i]], color=color)
                
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Trajectory {}".format(selected_trajectory))
                plt.legend()
                plt.grid(True)
                plt.gca().set_aspect("equal")
                plt.tight_layout()
                plt.show()
                
                break
        
    def run(self):
        self.root.mainloop()

# Usage:
gui = TrajectoryGUI(listOfTrajectories)
gui.run()


# %%
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from datetime import datetime

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
        self.plot_button = ttk.Button(self.root, text="Plot", command=self.plot_trajectory)
        self.plot_button.pack(pady=5)
        
    def plot_trajectory(self):
        selected_trajectory = int(self.trajectory_var.get())
        for traj in self.trajectories:
            if traj.number == selected_trajectory:
                x = [point.X for point in traj.points]
                y = [point.Y for point in traj.points]
                
                # Clear the previous plot
                plt.clf()
                
                # Assign colors based on timestamps
                timestamps = [datetime.strptime(point.timestamp, '%Y-%m-%d:%H:%M:%S') for point in traj.points]
                min_timestamp = min(timestamps)
                max_timestamp = max(timestamps)
                timestamp_range = max_timestamp - min_timestamp
                cmap = cm.get_cmap('Blues')
                
                norm_timestamps = [(timestamp - min_timestamp) / timestamp_range for timestamp in timestamps]
                color = cmap(norm_timestamps[0])
                plt.plot(x, y, color=color, label="Trajectory {}".format(traj.number))
                
                # Iterate over the points and connect them with lines using the assigned colors
                for i in range(1, len(x)):
                    color = cmap(norm_timestamps[i])
                    plt.plot([x[i-1], x[i]], [y[i-1], y[i]], color=color)
                
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Trajectory {}".format(selected_trajectory))
                plt.legend()
                plt.grid(True)
                plt.gca().set_aspect("equal")
                plt.tight_layout()
                plt.show()
                
                break
        
    def run(self):
        self.root.mainloop()

# Usage:
gui = TrajectoryGUI(listOfTrajectories)
gui.run()


# %%
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from datetime import datetime

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
        self.plot_button = ttk.Button(self.root, text="Plot", command=self.plot_trajectory)
        self.plot_button.pack(pady=5)
        
        # Create a checkbox for showing intersecting trajectories
        self.intersect_var = tk.IntVar()
        self.intersect_checkbox = ttk.Checkbutton(self.root, text="Show Intersecting Trajectories", variable=self.intersect_var)
        self.intersect_checkbox.pack(pady=5)
        
    def plot_trajectory(self):
        selected_trajectory = int(self.trajectory_var.get())
        show_intersecting = self.intersect_var.get()
        
        # Clear the previous plot
        plt.clf()
        
        # Iterate over the trajectories
        for traj in self.trajectories:
            if traj.number == selected_trajectory:
                x = [point.X for point in traj.points]
                y = [point.Y for point in traj.points]
                
                # Assign colors based on timestamps
                timestamps = [datetime.strptime(point.timestamp, '%Y-%m-%d:%H:%M:%S') for point in traj.points]
                min_timestamp = min(timestamps)
                max_timestamp = max(timestamps)
                timestamp_range = max_timestamp - min_timestamp
                cmap = cm.get_cmap('viridis')
                
                norm_timestamps = [(timestamp - min_timestamp) / timestamp_range for timestamp in timestamps]
                color = cmap(norm_timestamps[0])
                plt.plot(x, y, color=color, label="Trajectory {}".format(traj.number))
                
                # Iterate over the points and connect them with lines using the assigned colors
                for i in range(1, len(x)):
                    color = cmap(norm_timestamps[i])
                    plt.plot([x[i-1], x[i]], [y[i-1], y[i]], color=color)
                
            elif show_intersecting and check_trajectory_intersect(traj, selected_trajectory):
                x = [point.X for point in traj.points]
                y = [point.Y for point in traj.points]
                
                # Plot intersecting trajectory with a different color
                plt.plot(x, y, color='red', alpha=0.5, label="Intersecting Trajectory {}".format(traj.number))
        
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Trajectory {}".format(selected_trajectory))
        plt.legend()
        plt.grid(True)
        plt.gca().set_aspect("equal")
        plt.tight_layout()
        plt.show()
        
    def run(self):
        self.root.mainloop()

def check_trajectory_intersect(trajectory, selected_trajectory):
    # Implement the logic to check if a trajectory intersects with the selected_trajectory
    # Return True if they intersect, False otherwise
    return False

# Usage:
gui = TrajectoryGUI(listOfTrajectories)
gui.run()


# %%
def check_trajectory_intersect(trajectory, selected_trajectory):
    selected_points = selected_trajectory.points
    intersect = False

    # Check if any point in the trajectory intersects with the selected_trajectory
    for point in trajectory.points:
        if point in selected_points:
            intersect = True
            break

    return intersect


# %%
    import math

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
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]
    
    return simplified_points

# Example usage:

# List of trajectories (imported or generated)
trajectories = [
    [(0, 0), (1, 1), (2, 2), (3, 2), (4, 4), (5, 5), (6, 4), (7, 5), (8, 6), (9, 5)],
    [(10, 10), (11, 11), (12, 12), (13, 12), (14, 14), (15, 15), (16, 14), (17, 15), (18, 16), (19, 15)]
]

epsilon = 1.0

# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in trajectories:
    simplified_trajectory = douglas_peucker(trajectory, epsilon)
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()

# %%
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
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]
    
    return simplified_points

# Example usage:

# List of trajectories (imported or generated)
trajectories = [
    [(0, 0), (1, 1), (2, 2), (3, 2), (4, 4), (5, 5), (6, 4), (7, 5), (8, 6), (9, 5)],
    [(10, 10), (11, 11), (12, 12), (13, 12), (14, 14), (15, 15), (16, 14), (17, 15), (18, 16), (19, 15)]
]

epsilon = 1.0

# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in trajectories:
    simplified_trajectory = douglas_peucker(trajectory, epsilon)
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()

# %%
import math
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
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]
    
    return simplified_points

# Example usage:

# List of trajectories (imported or generated)
trajectories = [
    [(0, 0), (1, 1), (2, 2), (3, 2), (4, 4), (5, 5), (6, 4), (7, 5), (8, 6), (9, 5)],
    [(10, 10), (11, 11), (12, 12), (13, 12), (14, 14), (15, 15), (16, 14), (17, 15), (18, 16), (19, 15)]
]

epsilon = 1.0

# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in trajectories:
    simplified_trajectory = douglas_peucker(trajectory, epsilon)
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()

# %%
# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in trajectories:
    simplified_trajectory = douglas_peucker(trajectory, epsilon)
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()for trajectory in listOfTrajectories:
    # Convert trajectory points to a list of (x, y) tuples
    points = [(point.X, point.Y) for point in trajectory.points]
    
    # Apply the Douglas-Peucker algorithm
    simplified_points = douglas_peucker(points, epsilon)
    
    # Convert back to the original point format
    simplified_trajectory = [point.point(x, y, "") for x, y in simplified_points]
    
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()

# %%
for trajectory in listOfTrajectories:
    # Convert trajectory points to a list of (x, y) tuples
    points = [(point.X, point.Y) for point in trajectory.points]
    
    # Apply the Douglas-Peucker algorithm
    simplified_points = douglas_peucker(points, epsilon)
    
    # Convert back to the original point format
    simplified_trajectory = [point.point(x, y, "") for x, y in simplified_points]
    
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()

# %%
import math

# Define the perpendicular_distance and douglas_peucker functions as shown in the previous code.

# Assuming you have a list of trajectories named 'listOfTrajectories'

def convert_trajectory_to_points(trajectory):
    # Convert the trajectory points to a list of tuples (X, Y)
    return [(point.X, point.Y) for point in trajectory.points]

def convert_points_to_trajectory(points, trajectory_number):
    # Convert a list of points (tuples) to a trajectory object
    trajectory = trajectory(trajectory_number)
    for point in points:
        x, y = point
        timestamp = ""  # You can set the timestamp here based on your needs
        trajectory.addPoint(point(x, y, timestamp))
    return trajectory

def simplify_trajectories(trajectories, epsilon):
    # Apply the Douglas-Peucker algorithm to each trajectory and convert back to trajectory objects
    simplified_trajectories = []
    for traj in trajectories:
        points = convert_trajectory_to_points(traj)
        simplified_points = douglas_peucker(points, epsilon)
        simplified_traj = convert_points_to_trajectory(simplified_points, traj.number)
        simplified_trajectories.append(simplified_traj)
    return simplified_trajectories

# Example usage:

# Your list of trajectories named 'listOfTrajectories'
trajectories = listOfTrajectories

epsilon = 0.0001  # You can adjust the value of epsilon based on your desired level of simplification

# Simplify the trajectories
simplified_trajectories = simplify_trajectories(trajectories, epsilon)

# Now, you can plot the simplified trajectories using the same GUI code provided earlier.
# You can also use the `simplified_trajectories` list for other purposes.


# %%
for trajectory in trajectories:
    simplified_trajectory = douglas_peucker(trajectory, epsilon)
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()

# %%
import math
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
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]
    
    return simplified_points

# Example usage:

# List of trajectories (imported or generated)
trajectories = [
    [(0, 0), (1, 1), (2, 2), (3, 2), (4, 4), (5, 5), (6, 4), (7, 5), (8, 6), (9, 5)],
    [(10, 10), (11, 11), (12, 12), (13, 12), (14, 14), (15, 15), (16, 14), (17, 15), (18, 16), (19, 15)]
]

epsilon = 1.0

# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in trajectories:
    simplified_trajectory = douglas_peucker(trajectory, epsilon)
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()

# %%
# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in trajectories:
    simplified_trajectory = douglas_peucker(trajectory, epsilon)
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()

# %%
# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in trajectories:
    simplified_trajectory = douglas_peucker(trajectory, epsilon)
    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()

# %%
import math

# Define the perpendicular_distance and douglas_peucker functions as shown in the previous code.

# Assuming you have a list of trajectories named 'listOfTrajectories'

def convert_trajectory_to_points(trajectory):
    # Convert the trajectory points to a list of tuples (X, Y)
    return [(point.X, point.Y) for point in trajectory.points]

def convert_points_to_trajectory(points, trajectory_number):
    # Convert a list of points (tuples) to a trajectory object
    traj = trajectory(trajectory_number)
    for point in points:
        x, y = point
        timestamp = ""  # You can set the timestamp here based on your needs
        traj.addPoint(point(x, y, timestamp))
    return traj

def simplify_trajectories(trajectories, epsilon):
    # Apply the Douglas-Peucker algorithm to each trajectory and convert back to trajectory objects
    simplified_trajectories = []
    for traj in trajectories:
        points = convert_trajectory_to_points(traj)
        simplified_points = douglas_peucker(points, epsilon)
        simplified_traj = convert_points_to_trajectory(simplified_points, traj.number)
        simplified_trajectories.append(simplified_traj)
    return simplified_trajectories

# Example usage:

# Your list of trajectories named 'listOfTrajectories'
trajectories = listOfTrajectories

epsilon = 0.0001  # You can adjust the value of epsilon based on your desired level of simplification

# Simplify the trajectories
simplified_trajectories = simplify_trajectories(trajectories, epsilon)

# Now, you can plot the simplified trajectories using the same GUI code provided earlier.
# You can also use the 'simplified_trajectories' list for other purposes.


# %%
import math

# Define the perpendicular_distance and douglas_peucker functions as shown in the previous code.

# Assuming you have a list of trajectories named 'listOfTrajectories'

def convert_trajectory_to_points(trajectory):
    # Convert the trajectory points to a list of tuples (X, Y)
    return [(point.X, point.Y) for point in trajectory.points]

def convert_points_to_trajectory(points, trajectory_number):
    # Convert a list of points (tuples) to a trajectory object
    traj = trajectory(trajectory_number)
    for pt in points:  # Use a different variable name to avoid conflicts
        x, y = pt
        timestamp = ""  # You can set the timestamp here based on your needs
        traj.addPoint(point(x, y, timestamp))
    return traj

def simplify_trajectories(trajectories, epsilon):
    # Apply the Douglas-Peucker algorithm to each trajectory and convert back to trajectory objects
    simplified_trajectories = []
    for traj in trajectories:
        points = convert_trajectory_to_points(traj)
        simplified_points = douglas_peucker(points, epsilon)
        simplified_traj = convert_points_to_trajectory(simplified_points, traj.number)
        simplified_trajectories.append(simplified_traj)
    return simplified_trajectories

# Example usage:

# Your list of trajectories named 'listOfTrajectories'
trajectories = listOfTrajectories

epsilon = 0.0001  # You can adjust the value of epsilon based on your desired level of simplification

# Simplify the trajectories
simplified_trajectories = simplify_trajectories(trajectories, epsilon)

# Now, you can plot the simplified trajectories using the same GUI code provided earlier.
# You can also use the 'simplified_trajectories' list for other purposes.


# %%
plot_trajectories(listOfTrajectories)

# %%
import math

class Point:
    def __init__(self, x, y, timestamp):
        self.X = x
        self.Y = y 
        self.timestamp = timestamp

class Trajectory:
    def __init__(self, number):
        self.number = number
        self.points = []

def perpendicular_distance(point, line_start, line_end):
    """
    Calculate the perpendicular distance between a point and a line segment.
    """
    x, y = point.X, point.Y
    start_x, start_y = line_start.X, line_start.Y
    end_x, end_y = line_end.X, line_end.Y
    # Calculate the slope of the line
    line_slope = (end_y - start_y) / (end_x - start_x)
    # Calculate the y-intercept of the line
    line_intercept = start_y - line_slope * start_x
    # Calculate the perpendicular distance
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]
    
    return simplified_points

# Example usage:

# Assuming you have a list of trajectories named 'listOfTrajectories'
trajectories = listOfTrajectories

epsilon = 1.0

# Apply the Douglas-Peucker algorithm to each trajectory
for traj in trajectories:
    simplified_trajectory_points = douglas_peucker(traj.points, epsilon)
    simplified_trajectory = Trajectory(traj.number)
    simplified_trajectory.points = simplified_trajectory_points
    print("Original Trajectory:", traj.points)
    print("Simplified Trajectory:", simplified_trajectory.points)
    print()


# %%
import math

class Point:
    def __init__(self, x, y, timestamp):
        self.X = x
        self.Y = y 
        self.timestamp = timestamp

class Trajectory:
    def __init__(self, number):
        self.number = number
        self.points = []

def perpendicular_distance(point, line_start, line_end):
    """
    Calculate the perpendicular distance between a point and a line segment.
    """
    x, y = point.X, point.Y
    start_x, start_y = line_start.X, line_start.Y
    end_x, end_y = line_end.X, line_end.Y
    # Calculate the slope of the line
    line_slope = (end_y - start_y) / (end_x - start_x)
    # Calculate the y-intercept of the line
    line_intercept = start_y - line_slope * start_x
    # Calculate the perpendicular distance
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]
    
    return simplified_points

# Example usage:

# Assuming you have a list of trajectories named 'listOfTrajectories'
trajectories = listOfTrajectories

epsilon = 1.0

# Apply the Douglas-Peucker algorithm to each trajectory
for traj in trajectories:
    simplified_points = douglas_peucker(traj.points, epsilon)
    simplified_trajectory = Trajectory(traj.number)
    simplified_trajectory.points = [Point(point.X, point.Y, point.timestamp) for point in simplified_points]
    print("Original Trajectory:", [point.timestamp for point in traj.points])
    print("Simplified Trajectory:", [point.timestamp for point in simplified_trajectory.points])
    print()


# %%
import math

class Point:
    def __init__(self, x, y, timestamp):
        self.X = x
        self.Y = y 
        self.timestamp = timestamp

class Trajectory:
    def __init__(self, number):
        self.number = number
        self.points = []

def perpendicular_distance(point, line_start, line_end):
    """
    Calculate the perpendicular distance between a point and a line segment.
    """
    x, y = point.X, point.Y
    start_x, start_y = line_start.X, line_start.Y
    end_x, end_y = line_end.X, line_end.Y
    # Calculate the slope of the line
    line_slope = (end_y - start_y) / (end_x - start_x)
    # Calculate the y-intercept of the line
    line_intercept = start_y - line_slope * start_x
    # Calculate the perpendicular distance
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]
    
    return simplified_points

# Example usage:

# Assuming you have a list of trajectories named 'listOfTrajectories'
trajectories = listOfTrajectories

epsilon = 0.01

# Apply the Douglas-Peucker algorithm to each trajectory
for traj in trajectories:
    simplified_points = douglas_peucker(traj.points, epsilon)
    simplified_trajectory = Trajectory(traj.number)
    simplified_trajectory.points = [Point(point.X, point.Y, point.timestamp) for point in simplified_points]
    print("Original Trajectory:", [point.timestamp for point in traj.points])
    print("Simplified Trajectory:", [point.timestamp for point in simplified_trajectory.points])
    print()


# %%
import math

class Point:
    def __init__(self, x, y, timestamp):
        self.X = x
        self.Y = y 
        self.timestamp = timestamp

class Trajectory:
    def __init__(self, number):
        self.number = number
        self.points = []

def perpendicular_distance(point, line_start, line_end):
    """
    Calculate the perpendicular distance between a point and a line segment.
    """
    x, y = point.X, point.Y
    start_x, start_y = line_start.X, line_start.Y
    end_x, end_y = line_end.X, line_end.Y
    # Calculate the slope of the line
    line_slope = (end_y - start_y) / (end_x - start_x)
    # Calculate the y-intercept of the line
    line_intercept = start_y - line_slope * start_x
    # Calculate the perpendicular distance
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]
    
    return simplified_points

# Example usage:

# Assuming you have a list of trajectories named 'listOfTrajectories'
trajectories = listOfTrajectories

epsilon = 0.001

# Apply the Douglas-Peucker algorithm to each trajectory
for traj in trajectories:
    simplified_points = douglas_peucker(traj.points, epsilon)
    simplified_trajectory = Trajectory(traj.number)
    simplified_trajectory.points = [Point(point.X, point.Y, point.timestamp) for point in simplified_points]
    print("Original Trajectory:", [point.timestamp for point in traj.points])
    print("Simplified Trajectory:", [point.timestamp for point in simplified_trajectory.points])
    print()


# %%
import math
from datetime import datetime

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
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    if len(points) < 3:
        return points

    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]

    return simplified_points

# Example usage:

# Assuming you have a list of trajectories named 'listOfTrajectories'

epsilon = 0.1

# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in listOfTrajectories:
    # Convert timestamp strings to datetime objects
    timestamps = [datetime.strptime(ts, '%Y-%m-%d:%H:%M:%S') for ts in trajectory]

    # Pair each timestamp with its corresponding X, Y coordinate
    points = list(zip(timestamps, trajectory))

    # Sort points based on the timestamp
    points.sort(key=lambda p: p[0])

    # Simplify the trajectory
    simplified_points = douglas_peucker(points, epsilon)

    # Convert simplified points back to the list of timestamps
    simplified_trajectory = [ts.strftime('%Y-%m-%d:%H:%M:%S') for ts, _ in simplified_points]

    print("Original Trajectory:", trajectory)
    print("Simplified Trajectory:", simplified_trajectory)
    print()


# %%
import math
from datetime import datetime

def perpendicular_distance(point, line_start, line_end):
    """
    Calculate the perpendicular distance between a point and a line segment.
    """
    x, y = point.X, point.Y
    start_x, start_y = line_start.X, line_start.Y
    end_x, end_y = line_end.X, line_end.Y
    # Calculate the slope of the line
    line_slope = (end_y - start_y) / (end_x - start_x)
    # Calculate the y-intercept of the line
    line_intercept = start_y - line_slope * start_x
    # Calculate the perpendicular distance
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    if len(points) < 3:
        return points

    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]

    return simplified_points

# Example usage:

# Assuming you have a list of trajectories named 'listOfTrajectories'

epsilon = 0.1

# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in listOfTrajectories:
    # Simplify the trajectory
    simplified_trajectory = douglas_peucker(trajectory, epsilon)

    print("Original Trajectory:", [point.X for point in trajectory], [point.Y for point in trajectory])
    print("Simplified Trajectory:", [point.X for point in simplified_trajectory], [point.Y for point in simplified_trajectory])
    print()



# %%
import math
from datetime import datetime

def perpendicular_distance(point, line_start, line_end):
    """
    Calculate the perpendicular distance between a point and a line segment.
    """
    x, y = point.X, point.Y
    start_x, start_y = line_start.X, line_start.Y
    end_x, end_y = line_end.X, line_end.Y
    # Calculate the slope of the line
    line_slope = (end_y - start_y) / (end_x - start_x)
    # Calculate the y-intercept of the line
    line_intercept = start_y - line_slope * start_x
    # Calculate the perpendicular distance
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    if len(points) < 3:
        return points

    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]

    return simplified_points

# Example usage:

# Assuming you have a list of trajectories named 'listOfTrajectories'

epsilon = 0.1

# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in listOfTrajectories:
    # Simplify the trajectory
    simplified_trajectory = douglas_peucker(trajectory, epsilon)

    print("Original Trajectory:", [point.X for point in trajectory], [point.Y for point in trajectory])
    print("Simplified Trajectory:", [point.X for point in simplified_trajectory], [point.Y for point in simplified_trajectory])
    print()


# %%
import math
from datetime import datetime

def perpendicular_distance(point, line_start, line_end):
    """
    Calculate the perpendicular distance between a point and a line segment.
    """
    x, y = point.X, point.Y
    start_x, start_y = line_start.X, line_start.Y
    end_x, end_y = line_end.X, line_end.Y
    # Calculate the slope of the line
    line_slope = (end_y - start_y) / (end_x - start_x)
    # Calculate the y-intercept of the line
    line_intercept = start_y - line_slope * start_x
    # Calculate the perpendicular distance
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    if len(points) < 3:
        return points

    # Find the point with the maximum perpendicular distance
    max_distance = 0
    index = 0
    end = len(points) - 1
    for i in range(1, end):
        distance = perpendicular_distance(points[i], points[0], points[end])
        if distance > max_distance:
            max_distance = distance
            index = i

    # If the maximum distance is greater than epsilon, recursively simplify the sub-trajectories
    simplified_points = []
    if max_distance > epsilon:
        recursive_simplified1 = douglas_peucker(points[:index+1], epsilon)
        recursive_simplified2 = douglas_peucker(points[index:], epsilon)
        simplified_points = recursive_simplified1[:-1] + recursive_simplified2
    else:
        # If the maximum distance is smaller than epsilon, return the start and end points
        simplified_points = [points[0], points[end]]

    return simplified_points

# Example usage:

# Assuming you have a list of trajectories named 'listOfTrajectories'

epsilon = 0.1

# Apply the Douglas-Peucker algorithm to each trajectory
for trajectory in listOfTrajectories:
    # Convert the trajectory object to a list of points
    points = [(point.X, point.Y) for point in trajectory]

    # Simplify the trajectory
    simplified_trajectory = douglas_peucker(points, epsilon)

    print("Original Trajectory:", points)
    print("Simplified Trajectory:", simplified_trajectory)
    print()


# %%
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def rdp(points, epsilon):
    # get the start and end points
    start = np.tile(np.expand_dims(points[0], axis=0), (points.shape[0], 1))
    end = np.tile(np.expand_dims(points[-1], axis=0), (points.shape[0], 1))

    # find distance from other_points to line formed by start and end
    dist_point_to_line = np.abs(np.cross(end - start, points - start, axis=-1)) / np.linalg.norm(end - start, axis=-1)
    # get the index of the points with the largest distance
    max_idx = np.argmax(dist_point_to_line)
    max_value = dist_point_to_line[max_idx]

    result = []
    if max_value > epsilon:
        partial_results_left = rdp(points[:max_idx+1], epsilon)
        result += [list(i) for i in partial_results_left if list(i) not in result]
        partial_results_right = rdp(points[max_idx:], epsilon)
        result += [list(i) for i in partial_results_right if list(i) not in result]
    else:
        result += [points[0], points[-1]]

    return result


if __name__ == "__main__":
    min_x = 0
    max_x = 5

    xs = np.linspace(min_x, max_x, num=200)
    ys = np.exp(-xs) * np.cos(2 * np.pi * xs)
    sample_points = np.concatenate([
        np.expand_dims(xs, axis=-1),
        np.expand_dims(ys, axis=-1)
    ], axis=-1)

    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(min_x, max_x), ylim=(-1, 1))
    plt.xlabel("x")
    plt.ylabel("y")
    text_values = ax.text(
        0.70,
        0.15,
        "",
        transform=ax.transAxes,
        fontsize=12,
        verticalalignment='top',
        bbox=dict(boxstyle='round',
                  facecolor='wheat',
                  alpha=0.2)
    )
    original_line, = ax.plot(xs, ys, lw=2, label=r"$y = e^{-x}cos(2 \pi x)$")
    simplified_line, = ax.plot([], [], lw=2, label="simplified", marker='o', color='r')

    # initialization function: plot the background of each frame
    def init():
        simplified_line.set_data(xs, ys)
        return original_line, simplified_line, text_values

    # animation function.  This is called sequentially
    def animate(i):
        epsilon = 0 + (i * 0.1)
        simplified = np.array(rdp(sample_points, epsilon))
        print(f"i: {i}, episilon: {'%.1f' % epsilon}, n: {simplified.shape[0]}")
        simplified_line.set_data(simplified[:, 0], simplified[:, 1])
        text_values.set_text(fr"$\epsilon$: {'%.1f' % epsilon}, $n$: {simplified.shape[0]}")
        return original_line, simplified_line, text_values

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(
        fig,
        animate,
        init_func=init,
        frames=21,
        interval=1000,
        repeat=True
    )
    plt.legend()
    plt.show()

# %%
import math
import numpy as np

def perpendicular_distance(point, line_start, line_end):
    """
    Calculate the perpendicular distance between a point and a line segment.
    """
    x, y, _ = point
    start_x, start_y, _ = line_start
    end_x, end_y, _ = line_end
    # Calculate the slope of the line
    line_slope = (end_y - start_y) / (end_x - start_x)
    # Calculate the y-intercept of the line
    line_intercept = start_y - line_slope * start_x
    # Calculate the perpendicular distance
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
    return distance

def douglas_peucker(points, epsilon):
    """
    Simplify a given trajectory using the Douglas-Peucker algorithm.
    """
    # Get the start and end points
    start = np.tile(np.expand_dims(points[0], axis=0), (len(points), 1))
    end = np.tile(np.expand_dims(points[-1], axis=0), (len(points), 1))

    # Find distance from other points to the line formed by start and end
    dist_point_to_line = np.abs(np.cross(end - start, points - start, axis=-1)) / np.linalg.norm(end - start, axis=-1)
    # Get the index of the points with the largest distance
    max_idx = np.argmax(dist_point_to_line)
    max_value = dist_point_to_line[max_idx]

    result = []
    if max_value > epsilon:
        partial_results_left = douglas_peucker(points[:max_idx+1], epsilon)
        result += [i for i in partial_results_left if i not in result]
        partial_results_right = douglas_peucker(points[max_idx:], epsilon)
        result += [i for i in partial_results_right if i not in result]
    else:
        result += [points[0], points[-1]]

    return result

# Example usage for your trajectories

# Represent each trajectory as a list of tuples (X, Y, Timestamp)
trajectory1 = [
    (0.0014788576577, 0.0037183030576, '2000-01-01:01:09:13'),
    (0.0014788576577, 0.0037183030576, '2000-01-01:01:09:14'),
    (0.0014788576577, 0.0037183030576, '2000-01-01:01:09:15')
]

trajectory4 = [
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:38'),
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:39'),
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:40'),
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:41'),
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:42')
]

# Apply the Douglas-Peucker algorithm to each trajectory
epsilon = 0.0001  # Set your desired epsilon value
simplified_trajectory1 = douglas_peucker(trajectory1, epsilon)
simplified_trajectory4 = douglas_peucker(trajectory4, epsilon)

# Print the simplified trajectories
print("Original Trajectory 1:", trajectory1)
print("Simplified Trajectory 1:", simplified_trajectory1)

print("Original Trajectory 4:", trajectory4)
print("Simplified Trajectory 4:", simplified_trajectory4)


# %%
import math
import numpy as np

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
    distance = abs(line_slope * x - y + line_intercept) / math.sqrt(line_slope**2 + 1)
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
        partial_results_left = douglas_peucker(points[:max_idx+1], epsilon)
        result += partial_results_left
        partial_results_right = douglas_peucker(points[max_idx:], epsilon)
        result += partial_results_right[1:]  # Exclude the duplicate point
    else:
        result += [points[0], points[-1]]

    return result

# Example usage for your trajectories

# Represent each trajectory as a list of tuples (X, Y, Timestamp)
trajectory1 = [
    (0.0014788576577, 0.0037183030576, '2000-01-01:01:09:13'),
    (0.0014788576577, 0.0037183030576, '2000-01-01:01:09:14'),
    (0.0014788576577, 0.0037183030576, '2000-01-01:01:09:15')
]

trajectory4 = [
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:38'),
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:39'),
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:40'),
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:41'),
    (0.0014316036036, 0.0036914073741, '2000-01-01:01:11:42')
]

# Apply the Douglas-Peucker algorithm to each trajectory
epsilon = 0.0001  # Set your desired epsilon value
simplified_trajectory1 = douglas_peucker(trajectory1, epsilon)
simplified_trajectory4 = douglas_peucker(trajectory4, epsilon)

# Print the simplified trajectories
print("Original Trajectory 1:", trajectory1)
print("Simplified Trajectory 1:", simplified_trajectory1)

print("Original Trajectory 4:", trajectory4)
print("Simplified Trajectory 4:", simplified_trajectory4)



# %%
simplified_trajectories = []
for traj in trajectories:
    simplified_traj = douglas_peucker(traj.points, epsilon)
    simplified_trajectories.append(simplified_traj)

# Print the simplified trajectories
for i, simplified_traj in enumerate(simplified_trajectories, start=1):
    print(f"Simplified Trajectory {i}:", simplified_traj)

# %%
simplified_trajectories = []
for traj in trajectories:
    simplified_traj = douglas_peucker(traj, epsilon)
    simplified_trajectories.append(simplified_traj)

# Print the simplified trajectories
for i, simplified_traj in enumerate(simplified_trajectories, start=1):
    print(f"Original Trajectory {i}:", trajectories[i - 1])
    print(f"Simplified Trajectory {i}:", simplified_traj)

# %%
simplified_trajectories = []
for traj in listOfTrajectories:
    simplified_traj = douglas_peucker(traj, epsilon)
    simplified_trajectories.append(simplified_traj)

# Print the simplified trajectories
for i, simplified_traj in enumerate(simplified_trajectories, start=1):
    print(f"Original Trajectory {i}:", listOfTrajectories[i - 1])
    print(f"Simplified Trajectory {i}:", simplified_traj)

# %%
listOfTrajectories.shape()

# %%
shape(listOfTrajectories)

# %%
type(listOfTrajectories)

# %%
dim(list)

# %%
dim(listOfTrajectories)

# %%
shape(listOfTrajectories)

# %%
print(len(listOfTrajectories)) 

# %%
first_trajectory = listOfTrajectories[0]
print(first_trajectory)

# %%
for i, trajectory in enumerate(listOfTrajectories, start=1):
    print(f"Trajectory {i}:")
    for point in trajectory:
        print(point)


# %%
for i, trajectory in enumerate(listOfTrajectories, start=1):
    print(f"Trajectory {i}:")
    for point in trajectory.points:
        print(point)


# %%
simplified_trajectories = []
for trajectory in listOfTrajectories:
    simplified_traj = douglas_peucker(trajectory.points, epsilon)
    simplified_trajectories.append(simplified_traj)

# Print the simplified trajectories
for i, simplified_traj in enumerate(simplified_trajectories, start=1):
    print(f"Simplified Trajectory {i}:")
    for point in simplified_traj:
        print(point)

# %%
simplified_trajectories = []
for trajectory in listOfTrajectories:
    points = [(point.X, point.Y) for point in trajectory.points]  # Extract (X, Y) coordinates from each point
    simplified_traj = douglas_peucker(points, epsilon)
    simplified_trajectories.append(simplified_traj)

# Print the simplified trajectories
for i, simplified_traj in enumerate(simplified_trajectories, start=1):
    print(f"Simplified Trajectory {i}:")
    for x, y in simplified_traj:
        print(f"({x},{y})")

# %%
for i, (original_traj, simplified_traj) in enumerate(zip(listOfTrajectories, simplified_trajectories), start=1):
    original_points = [(point.X, point.Y) for point in original_traj.points]
    simplified_points = simplified_traj
    original_x, original_y = zip(*original_points)
    simplified_x, simplified_y = zip(*simplified_points)

    plt.figure(figsize=(10, 5))
    plt.plot(original_x, original_y, label=f"Original Trajectory {i}", color='blue')
    plt.plot(simplified_x, simplified_y, label=f"Simplified Trajectory {i}", color='red', linestyle='dashed')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f"Trajectory Comparison: Original vs. Simplified (Trajectory {i})")
    plt.show()

# %%
def sliding_window(points, window_size, threshold):
    """
    Simplify a given trajectory using the Sliding-Window Algorithm.
    """
    if len(points) < window_size:
        return points

    simplified_points = [points[0]]
    i = 0
    while i < len(points) - 1:
        j = i + window_size
        if j >= len(points):
            j = len(points) - 1

        x1, y1 = points[i]
        x2, y2 = points[j]

        # Calculate the distance of points from the line formed by (x1, y1) and (x2, y2)
        distances = [perpendicular_distance(point, (x1, y1), (x2, y2)) for point in points[i+1:j]]
        max_distance = max(distances)

        # Add the point to the simplified trajectory if it is far enough from the line
        if max_distance > threshold:
            simplified_points.append(points[j])

        i += 1

    return simplified_points

# %%
window_size = 5  # Adjust the window size based on your preference
threshold = 0.0001  # Adjust the threshold distance based on your preference
simplified_trajectories_sw = []
for trajectory in listOfTrajectories:
    points = [(point.X, point.Y) for point in trajectory.points]
    simplified_traj = sliding_window(points, window_size, threshold)
    simplified_trajectories_sw.append(simplified_traj)

# Plot the original, Douglas-Peucker, and Sliding-Window trajectories
for i, (original_traj, dp_traj, sw_traj) in enumerate(zip(listOfTrajectories, simplified_trajectories_dp, simplified_trajectories_sw), start=1):
    original_points = [(point.X, point.Y) for point in original_traj.points]
    dp_points = dp_traj
    sw_points = sw_traj
    original_x, original_y = zip(*original_points)
    dp_x, dp_y = zip(*dp_points)
    sw_x, sw_y = zip(*sw_points)

    plt.figure(figsize=(12, 6))
    plt.plot(original_x, original_y, label=f"Original Trajectory {i}", color='blue', alpha=0.7)
    plt.plot(dp_x, dp_y, label=f"Douglas-Peucker Trajectory {i}", color='red', linestyle='dashed')
    plt.plot(sw_x, sw_y, label=f"Sliding-Window Trajectory {i}", color='green', linestyle='dotted')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f"Trajectory Comparison: Original vs. Douglas-Peucker vs. Sliding-Window (Trajectory {i})")
    plt.show()


