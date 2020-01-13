import math # 'math' needed for 'sqrt'
# Function which returns subset or r length from n
from itertools import combinations

# distance() function to take two (x, y) tuples as parameters
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

# Run through input and reorder in [(x, y), (x,y) ...] format
data_points = ["9.5 7.5", "10.2 19.1", "9.7 10.2"] # Original input list (entered by spacing the two points).
m_input = [] # Manipulated list
final_list = [] # Final list
for o in data_points:
    m_input = o.split()
    x, y = float(m_input[0]), float(m_input[1])
    final_list += [(x, y)] # outputs [(9.5, 7.5), (10.2, 19.1), (9.7, 10.2)]

print("final_list = ", final_list)
print("type final_list = ", type(final_list))

# iterate over all pairs of points from your list final_list
# The function iterools.combinations() is handy for this purpose
min_distance = distance(final_list[0], final_list[1])
for p0, p1 in combinations(final_list, 2):
    min_distance = min(min_distance, distance(p0, p1))

print(" >> min_distance = ", min_distance)

