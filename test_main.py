# test_main.py
import point
import pytest
import main
import region
listOfTrajectories = main.listOfTrajectories

def test_plot_all_trajectories():
    # Use the original listOfTrajectories for testing
    trajectories = main.listOfTrajectories

    # Call the plot_all_trajectories function
    main.plot_trajectories(trajectories)

    # Add a pause to display the plot (you may need to close the plot manually)
    plt.pause(1)

def test_trajectory_gui():
    # Use the original listOfTrajectories for testing
    trajectories = main.listOfTrajectories

    # Initialize TrajectoryGUI with the sample trajectories
    gui = main.TrajectoryGUI(trajectories)

    # Call the run method to start the GUI
    gui.run()

def test_trajectory_comparison_gui():
    # Use the original listOfTrajectories for testing
    original_trajectories = main.listOfTrajectories

    simplified_trajectories = main.simplified_trajectories

    # Initialize TrajectoryComparisonGUI with the  trajectories
    gui = main.TrajectoryComparisonGUI(original_trajectories, simplified_trajectories)

    # Set the selected trajectory to the last one and test the plot_trajectory_comparison method
    gui.run()
    # Add a pause to display the plot (you may need to close the plot manually)
    plt.pause(1)
    
# def test_solve_query_without_rtree():
#     # Test case: Query region contains trajectory 1
#     queryRegion = region.region(point.point(0.0012601754558545508, 0.0027251228043638775, 0.0), 0.00003)
#     foundTrajectories = main.solveQueryWithoutRTree(queryRegion, listOfTrajectories)
#     if foundTrajectories:
#         print("Trajectories within the query region:")
#     for t in foundTrajectories:
#         print(t.number)
#     else:
#         print("No trajectories match the query.")
# # Run the tests
if __name__ == "__main__":
    pytest.main()
