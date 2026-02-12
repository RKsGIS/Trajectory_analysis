# Trajectory Analysis Project

A Python toolkit for analyzing, simplifying, and indexing spatial trajectory data from the  [GeoGami geogame](https://github.com/geogami-team/geogami)


---

## Overview

This project processes 62 real-world movement trajectories and implements core spatial algorithms for:

- Visualization of movement patterns
- Trajectory simplification
- Spatial indexing
- Efficient range querying
- Performance benchmarking

---

## Features

- Interactive GUI built with Tkinter
- Trajectory simplification:
  - Douglas-Peucker algorithm
  - Sliding Window algorithm
- Distance metrics:
  - Closest-Pair Distance
  - Dynamic Time Warping (DTW)
- R-tree spatial indexing
- Range queries (R-queries)
- Performance comparison:
  - R-tree search vs. Naive linear search

---

## Installation

### Prerequisites

- Python 3.8+
- Matplotlib
- NumPy
- Pytest

### Setup

    git clone https://github.com/RKsGIS/Trajectory_analysis.git
    cd Trajectory_analysis
    pip install -r requirements.txt

---

## Run the Application

    python main.py

---

## Tech Stack

- Matplotlib – Visualization and plotting
- Tkinter – Graphical User Interface
- NumPy – Numerical computations
- Pytest – Unit testing

---

## Project Structure

Trajectory_analysis/
- main.py          # GUI and entry point
- functions.py     # Core algorithms
- trajectory.py    # Data models (Point, Trajectory, Region)
- utils.py         # Data import and helper functions
- test_main.py     # Unit tests
- Trajectories/    # Raw trajectory data (.txt files)



## Project Authors
- [Ram Kumar Muthusamy](mailto:ramkumar.m@uni-muenster.de)
- [Mohamed Shamsudeen](mailto:shamsudeen.m@uni-muenster.de)

---

This project was developed for the Trajectory Analysis course at the University of Münster.
