from initialParams import *
import random

order_map_vehicle = []

for i in range(N0):
    j = random.randint(Xmin, Xmax)
    order_map_vehicle.append(j)

vehicle_map_order = {}
for i in range(Nv):
    vehicle_map_order[i+1] = []
for i in range(N0):
    vehicle_map_order[order_map_vehicle[i]].append(i)

