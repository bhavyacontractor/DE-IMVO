from constraints import *
import random


X = []  # Initial Multiverse consisting of NP universes
count = 0
while count < NP:
    order_map_vehicle = []

    for i in range(N0):
        j = random.randint(X_min, X_max)
        order_map_vehicle.append(j)

    vehicle_map_order = {}
    for i in range(Nv):
        vehicle_map_order[i] = []
    for i in range(N0):
        vehicle_map_order[order_map_vehicle[i]].append(i)

    if check_constraints(vehicle_map_order):
        X.append(order_map_vehicle)
        count += 1

print(X)