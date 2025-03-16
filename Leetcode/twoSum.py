def two_sum(nums, target):
    # Dictionary to store numbers we've seen and their indices
    num_to_index = {}
    
    # Loop through the array
    for i, num in enumerate(nums):
        # Calculate the complement (the number we need to find)
        complement = target - num
        
        # If we've seen the complement before, we found our answer
        if complement in num_to_index:
            # Return the indices, with the smaller one first
            j = num_to_index[complement]
            return [min(i, j), max(i, j)]
        
        # Otherwise, store the current number and its index
        num_to_index[num] = i
    
    # This won't be reached since we're guaranteed a solution
    return [-1, -1]