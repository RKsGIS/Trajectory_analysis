# test_main_template.py
import point
import pytest
import main_template
import region
listOfTrajectories = main_template.listOfTrajectories

# def test_plot_all_trajectories():
#     # Use the original listOfTrajectories for testing
#     trajectories = main_template.listOfTrajectories

#     # Call the plot_all_trajectories function
#     main_template.plot_trajectories(trajectories)

#     # Add a pause to display the plot (you may need to close the plot manually)
#     plt.pause(1)

# def test_trajectory_gui():
#     # Use the original listOfTrajectories for testing
#     trajectories = main_template.listOfTrajectories

#     # Initialize TrajectoryGUI with the sample trajectories
#     gui = main_template.TrajectoryGUI(trajectories)

#     # Call the run method to start the GUI
#     gui.run()

# def test_trajectory_comparison_gui():
#     # Use the original listOfTrajectories for testing
#     original_trajectories = main_template.listOfTrajectories

#     simplified_trajectories = main_template.simplified_trajectories

#     # Initialize TrajectoryComparisonGUI with the  trajectories
#     gui = main_template.TrajectoryComparisonGUI(original_trajectories, simplified_trajectories)

#     # Set the selected trajectory to the last one and test the plot_trajectory_comparison method
#     gui.run()
#     # Add a pause to display the plot (you may need to close the plot manually)
#     plt.pause(1)
    
def test_solve_query_without_rtree():
    # Test case: Query region contains trajectory 1
    queryRegion = region.region(point.point(0.0012601754558545508, 0.0027251228043638775, 0.0), 0.00003)
    foundTrajectories = main_template.solveQueryWithoutRTree(queryRegion, listOfTrajectories)
    if foundTrajectories:
        print("Trajectories within the query region:")
    for t in foundTrajectories:
        print(t.number)
    else:
        print("No trajectories match the query.")
# Run the tests
if __name__ == "__main__":
    pytest.main()
