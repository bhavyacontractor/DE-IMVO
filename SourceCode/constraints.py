from initialParams import *

def create_vehicle_map(order_map_vehicle):
    vehicle_map_order = {}
    for i in range(Nv):
        vehicle_map_order[i] = []
    for i in range(N0):
        vehicle_map_order[order_map_vehicle[i]].append(i)

    return vehicle_map_order


def check_constraints(order_map_vehicle):
    vehicle_map_order = create_vehicle_map(order_map_vehicle)

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

# print(check_constraints([6, 9, 9, 4, 8, 12, 12, 4, 10, 5, 13, 14, 1, 4, 12, 2, 12, 3, 6, 12, 1, 10, 2, 9, 0, 0, 6, 1, 0, 13, 6, 11, 1]))