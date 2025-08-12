# Week Two Assignment - Ronaldo's jersey list

# Step 1: Empty list
my_list = []

# Step 2: Add some Ronaldo-related numbers
my_list.append(7)   # Ronaldo's famous jersey
my_list.append(20)  # Year he returned to Man United (2021)
my_list.append(30)  # Just a random match stat
my_list.append(40)  # Another random stat

# Step 3: Insert 15 (young Bellingham's Dortmund jersey when he joined)
my_list.insert(1, 15)

# Step 4: Add more numbers to the list
my_list.extend([50, 60, 70])

# Step 5: Remove the last number
my_list.pop()

# Step 6: Sort the list
my_list.sort()

# Step 7: Find where "30" is in the list
index_of_30 = my_list.index(30)

# Step 8: Show final result
print("Final list:", my_list)
print("Number 30 is at position:", index_of_30)
