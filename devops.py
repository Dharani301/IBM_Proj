import time
import random
import matplotlib.pyplot as plt

class DevOpsAutomationTracker:
    def __init__(self):
        self.deployment_times = []
        self.failure_rates = []
        self.recovery_times = []
    
    def simulate_deployment(self):
        deployment_time = random.uniform(5, 15)  # Simulated time in minutes
        self.deployment_times.append(deployment_time)
        
        failure_occurred = random.choice([True, False])
        if failure_occurred:
            failure_rate = random.uniform(0.1, 0.5)  # 10% to 50% chance of failure
            recovery_time = random.uniform(5, 20)  # Simulated recovery time in minutes
        else:
            failure_rate = 0
            recovery_time = 0
        
        self.failure_rates.append(failure_rate)
        self.recovery_times.append(recovery_time)
    
    def run_simulation(self, deployments=10):
        for _ in range(deployments):
            self.simulate_deployment()
            time.sleep(1)  # Simulating time delay between deployments
    
    def visualize_metrics(self):
        fig, axs = plt.subplots(3, 1, figsize=(10, 8))
        
        axs[0].plot(self.deployment_times, marker='o', linestyle='-')
        axs[0].set_title('Deployment Times (minutes)')
        axs[0].set_ylabel('Time')
        
        axs[1].plot(self.failure_rates, marker='o', linestyle='-', color='r')
        axs[1].set_title('Failure Rates')
        axs[1].set_ylabel('Rate')
        
        axs[2].plot(self.recovery_times, marker='o', linestyle='-', color='g')
        axs[2].set_title('Recovery Times (minutes)')
        axs[2].set_ylabel('Time')
        
        plt.tight_layout()
        plt.show()

# Running the simulation
tracker = DevOpsAutomationTracker()
tracker.run_simulation(deployments=10)
tracker.visualize_metrics()
