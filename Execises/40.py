import math

# Prompt for two sets of coordinates as a single string
coordinates_str = input("Enter two sets of coordinates separated by a space (e.g., 3 5 7 2): ")

# Split the string into two lists of coordinates
l1 = list(map(int, coordinates_str.split()[0:2]))
l2 = list(map(int, coordinates_str.split()[2:4]))

# Calculate the distance using the correct formula and order of operations
dist = math.sqrt((l1[0] - l2[0])**2 + (l1[1] - l2[1])**2)

# Print the distance
print("The distance between the points is:", dist)
