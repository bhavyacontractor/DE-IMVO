from constraints import *
import random


X = []  # Initial Multiverse consisting of NP universes
count = 0
while count < NP:
    order_map_vehicle = []

    for i in range(N0):
        j = random.randint(X_min, X_max)
        order_map_vehicle.append(j)

    if check_constraints(order_map_vehicle):
        X.append(order_map_vehicle)
        count += 1

# print(X)
for i in X:
    print(i)
print("\n")
print("Multiverse initialized. Step 2 complete !!")