""""
Non-Constructible Change
Understanding the problem
We are given an array of positive integers, which represent the values of coins that we have in our possession. The array could have duplicates. We are asked to write a function that returns the minimum amount of change that we cannot create with our coins. For instance, if the input array is [1, 2, 5], the minimum amount of change that we cannot create is 4, since we can create 1, 2, 3 (1 + 2) and 5.


"""
def nonConstructibleChange(coins):
    # Write your code here.
  
    # Function to generate all subsets of the given array
    def generate_subsets(arr):
        subsets = [[]]
        for num in arr:
            subsets += [curr + [num] for curr in subsets]
        return subsets
    
    # Generating all possible combinations of coins
    all_combinations = generate_subsets(coins)

    # Calculating the sum of each combination
    possible_sums = set()
    for combination in all_combinations:
        possible_sums.add(sum(combination))

    # Finding the smallest amount of change that cannot be created
    current_change = 1
    while True:
        if current_change not in possible_sums:
            return current_change
        current_change += 1

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()

    def can_make_change(target, coins):
        # Function to check if the target amount can be made with given coins
        if target == 0:
            return True
        if not coins:
            return False
        
        for i in range(len(coins)):
            if coins[i] <= target:
                if can_make_change(target - coins[i], coins[:i] + coins[i+1:]):
                    return True
        return False

    current_change = 1
    while True:
        if not can_make_change(current_change, coins):
            return current_change
        current_change += 1


def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    current=0

    for coin in coins:
        if coin>current+1:
            return current+1
        current+=coin
    return current+1
    

