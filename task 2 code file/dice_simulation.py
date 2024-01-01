import random
import sys

## Task 2 part 1 calculations ##
def count_ways_to_get_sum(target_sum, num_dice, memo={}):
    if num_dice == 1:
        # Base case: one die, the sum must be between 1 and 6
        return 1 if 1 <= target_sum <= 6 else 0

    if (target_sum, num_dice) in memo:
        return memo[(target_sum, num_dice)]

    ways = 0
    for i in range(1, 7):
        if target_sum - i >= 0:
            ways += count_ways_to_get_sum(target_sum - i, num_dice - 1, memo)

    memo[(target_sum, num_dice)] = ways
    return ways

def probability_of_sum(target_sum, num_dice):
    total_ways = count_ways_to_get_sum(target_sum, num_dice)
    total_outcomes = 6 ** num_dice
    probability = total_ways / total_outcomes
    return probability  ## part 1 end ##

## Task 2 part 2 calculations ##
def simulate_dice_throws(num_simulations, num_dice, target_sum):
    count_success = 0

    for _ in range(num_simulations):
        # Simulate throwing num_dice and summing the results
        dice_results = [random.randint(1, 6) for _ in range(num_dice)]
        total_sum = sum(dice_results)

        # Check if sum matches the target_sum
        if total_sum == target_sum:
            count_success += 1

    probability = count_success / num_simulations
    return probability  ## part 2 end ##


# Check if the number of CL arguments is correct
if len(sys.argv) != 2:
    print("Usage: python dice_simulation.py <num_simulations>")
    sys.exit(1)

# Parse CL argument
num_dice = 10
target_sum = 32
num_simulations = int(sys.argv[1])

#Calculate the exact probability
result = probability_of_sum(target_sum, num_dice)
print(f"probability of getting a sum of {target_sum} from {num_dice} dice throws is: {result:.10f}")

# Perform the simulation
result = simulate_dice_throws(num_simulations, num_dice, target_sum)
print(f"Simulated probability of getting a sum of {target_sum} from "f"{num_dice} dice throws in {num_simulations} simulations: {result:.4f}")

#python dice_simulation.py 500


