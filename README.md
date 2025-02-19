# DevOps Automation Tracker

## Overview
The **DevOps Automation Tracker** is a Python-based tool designed to measure and analyze key DevOps metrics such as deployment times, failure rates, and recovery times. It helps evaluate the effectiveness of automation in DevOps processes using simulated data and visualization.

## Features
- **Simulates Deployment Metrics:** Tracks deployment time, failure rate, and recovery time.
- **Randomized Test Scenarios:** Uses simulated data to model real-world automation effectiveness.
- **Visualization:** Generates graphs for clear insights using Matplotlib.
- **Customizable Deployment Cycles:** Run multiple deployment simulations for deeper analysis.

## Installation
Ensure you have **Python 3.x** installed. Then, install dependencies using:
```sh
pip install matplotlib
```

## Usage
1. Clone or download the script `devops_tracker.py`.
2. Open a terminal in the script directory and run:
```sh
python devops_tracker.py
```
3. The script will:
   - Simulate 10 deployments (modifiable in code).
   - Generate performance graphs for visualization.

## Expected Output
- **Graph 1:** Deployment Times (minutes)
- **Graph 2:** Failure Rates
- **Graph 3:** Recovery Times (minutes)

## Customization
- Modify the `deployments=10` parameter in `tracker.run_simulation(deployments=10)` to change the number of simulations.
- Adjust failure probability in `simulate_deployment()` for more realistic modeling.

## Future Enhancements
- Store results in a CSV or database.
- Integrate real CI/CD logs from Jenkins, GitHub Actions, or GitLab CI/CD.
- Implement automated alerts for failure rate thresholds.



