from initialParams import *


def check_constraints(order_map_vehicle):
    vehicle_map_order = {}
    for i in range(Nv):
        vehicle_map_order[i] = []
    for i in range(N0):
        vehicle_map_order[order_map_vehicle[i]].append(i)

    for i in range(Nv):
        vehicle_type = int(i/veh_of_each_type)
        if len(vehicle_map_order[i]) > 5:
            return False

        cur_weight = 0
        cur_vol = 0
        max_weight = vehicle_specs[vehicle_type][0]
        max_vol = vehicle_specs[vehicle_type][1]
        for j in vehicle_map_order[i]:
            order_type = j % n_supplies
            cur_weight += order_matrix[j]
            cur_vol += (order_matrix[j]) / supply_specs[order_type]

            if (cur_vol > max_vol) or (cur_weight > max_weight):
                return False
    return True

# import itertools
#
# values = [1, 2, 3]
#
# per = list(itertools.permutations(values))
#
# for val in per:
#     print(val[0])
