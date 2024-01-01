import argparse
import random
import math
import pandas as pd
import matplotlib.pyplot as plt
import sys

def throwing_dart():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = math.sqrt(x**2 + y**2)
    return distance <= 1

def simulates_dart_game(num_of_darts):
    hits = 0
    for _ in range(num_of_darts):
        if throwing_dart():
            hits += 1
    return hits / num_of_darts

def estimate_pi(num_experiments, num_darts_per_experiment):
    pi_values = []
    for _ in range(num_experiments):
        probability = simulates_dart_game(num_darts_per_experiment)
        pi_estimate = 4 * probability
        pi_values.append(pi_estimate)
    return pi_values

def log_experiment_results(experiment_results, filename):
    df = pd.DataFrame(experiment_results, columns=['Number of Darts', 'Mean Pi', 'Mode Pi'])
    df.to_excel(filename, index=False)
    print(f"Experiment results logged in {filename}")

def plot_pi_estimates(pi_values, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(pi_values)
    plt.axhline(y=math.pi, color='r', linestyle='--', label='True Pi')
    plt.xlabel('Number of Experiments')
    plt.ylabel('Pi Estimate')
    plt.title('Convergence of Estimated Pi with Increasing Number of Experiments')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

def main():
    # command line argument to change the number of experiments need to be run the simulation
    parser = argparse.ArgumentParser(description='Monte Carlo Simulation for Dart Game')
    parser.add_argument('num_experiments', type=int, help='Number of experiments to run')
    args = parser.parse_args()

    num_darts_per_experiment = [1000, 10000, 100000, 1000000, 10000000]
    experiment_results = []

    for num_darts in num_darts_per_experiment:
        # calculate the probability of hitting in each number of darts per experiment
        probability = simulates_dart_game(num_darts)
        print(f"Probability of hitting with {num_darts} darts: {probability}")

        # get the pi values and calculate mean and mode of estimated pi values
        pi_values = estimate_pi(args.num_experiments, num_darts)
        mean_pi = sum(pi_values) / len(pi_values)
        mode_pi = max(set(pi_values), key=pi_values.count)
        experiment_results.append((num_darts, mean_pi, mode_pi))

        # print the calculated pi, mean, and mode values
        print(f"Estimated Pi values for {args.num_experiments} experiments with {num_darts} darts: {pi_values}")
        print(f"Mean Pi: {mean_pi}")
        print(f"Mode Pi: {mode_pi}")

    # log the results in an Excel sheet
    log_experiment_results(experiment_results, 'dart_game_results.xlsx')

    # create a plot of estimated pi values
    all_pi_values = estimate_pi(args.num_experiments, max(num_darts_per_experiment))
    plot_pi_estimates(all_pi_values, 'pi_estimates_plot.png')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dart_simulation.py <num_experiments>")
        sys.exit(1)
    main()


#python dart_simulation.py 1
#python dart_simulation.py 10

