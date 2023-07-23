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

# Run the tests
if __name__ == "__main__":
    pytest.main()
