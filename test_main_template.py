# test_main_template.py
import pytest
import main_template

def test_plot_all_trajectories():
    # Use the original listOfTrajectories for testing
    trajectories = main_template.listOfTrajectories

    # Call the plot_all_trajectories function
    main_template.plot_trajectories(trajectories)

    # Add a pause to display the plot (you may need to close the plot manually)
    plt.pause(1)

def test_trajectory_gui():
    # Use the original listOfTrajectories for testing
    trajectories = main_template.listOfTrajectories

    # Initialize TrajectoryGUI with the sample trajectories
    gui = main_template.TrajectoryGUI(trajectories)

    # Call the run method to start the GUI
    gui.run()

def test_trajectory_comparison_gui():
    # Use the original listOfTrajectories for testing
    original_trajectories = main_template.listOfTrajectories

    simplified_trajectories = main_template.simplified_trajectories

    # Initialize TrajectoryComparisonGUI with the  trajectories
    gui = main_template.TrajectoryComparisonGUI(original_trajectories, simplified_trajectories)

    # Set the selected trajectory to the last one and test the plot_trajectory_comparison method
    gui.run()
    # Add a pause to display the plot (you may need to close the plot manually)
    plt.pause(1)

# Run the tests
if __name__ == "__main__":
    pytest.main()
