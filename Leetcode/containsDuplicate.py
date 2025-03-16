def contains_duplicate(nums):
    # Create a set to track seen numbers
    seen = set()
    
    # Iterate through the array
    for num in nums:
        # If the number is already in the set, we found a duplicate
        if num in seen:
            return True
        
        # Otherwise, add it to the set
        seen.add(num)
    
    # If we've gone through the entire array without finding duplicates
    return False