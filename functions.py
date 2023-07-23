# imports
import trajectory
import point
import region
import utils

def douglas_peucker(points, epsilon):
    """Simplify a given trajectory using the Douglas-Peucker algorithm."""
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

def slidingWindow(traj:trajectory,epsilon) -> trajectory:
    return None

def closestPairDistance(traj0:trajectory,traj1:trajectory) -> float:
    return None

def closestPairDistance(trajectory):
    num_points = len(trajectory)
    min_distance = float('inf')
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            distance = pointDistance(trajectory[i], trajectory[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance
def calculate_closest_pair_distances(trajectories):
    closest_distances = {}
    for traj in trajectories:
        closest_distance = closestPairDistance(traj.points)
        closest_distances[traj.number] = closest_distance
    return closest_distances

# Function to calculate the Dynamic Time Warping distance between two trajectories
def dynamic_time_warping(trajectory1, trajectory2):
    len_traj1 = len(trajectory1)
    len_traj2 = len(trajectory2)
    
    # Create a 2D array to store the DTW distances
    dtw_distances = [[0] * len_traj2 for _ in range(len_traj1)]
    
    # Calculate the pairwise Euclidean distances between all points in both trajectories
    for i in range(len_traj1):
        for j in range(len_traj2):
            dtw_distances[i][j] = pointDistance(trajectory1[i], trajectory2[j])
    
    # Initialize the first row and first column of the DTW distances array
    for i in range(1, len_traj1):
        dtw_distances[i][0] += dtw_distances[i - 1][0]
    for j in range(1, len_traj2):
        dtw_distances[0][j] += dtw_distances[0][j - 1]
    
    # Fill the rest of the DTW distances array using dynamic programming
    for i in range(1, len_traj1):
        for j in range(1, len_traj2):
            dtw_distances[i][j] += min(dtw_distances[i - 1][j],
                                      dtw_distances[i][j - 1],
                                      dtw_distances[i - 1][j - 1])
    
    # Return the DTW distance between the two trajectories
    return dtw_distances[-1][-1]

# Function to calculate the DTW distance between all pairs of trajectories
def calculate_dtw_distances(trajectories):
    num_trajectories = len(trajectories)
    dtw_distances = np.zeros((num_trajectories, num_trajectories))

    for i in range(num_trajectories):
        for j in range(i, num_trajectories):
            dtw_dist = dynamicTimeWarping(trajectories[i].points, trajectories[j].points)
            dtw_distances[i, j] = dtw_dist
            dtw_distances[j, i] = dtw_dist

    return dtw_distances

def solveQueryWithRTree(r:region,trajectories:list) -> list:
    return None

def solveQueryWithoutRTree(r:region,trajectories:list) -> list:
    return None