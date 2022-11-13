from initialMultiverse import *
import itertools


def find_min_path(vehicle_map_order):
    print(vehicle_map_order)
    min_path = []
    min_dis = []
    for i in range(Nv):
        per = list(itertools.permutations(vehicle_map_order[i]))
        cur_min = 1e9
        cur_path = []
        # print(per)
        for j in per:
            if len(j) != 0:
                dis = distance_matrix[11][int(j[0]/n_supplies)]

                for k in range(1, len(j)):
                    dis += distance_matrix[int(j[k-1]/n_supplies)][int(j[k]/n_supplies)]

                if cur_min > dis:
                    cur_min = dis
                    cur_path = j

        min_path.append(cur_path)
        min_dis.append(cur_min)
    return min_path, min_dis

def transportation_cost(min_dis):
    temp = 0

    for i in min_dis:
        temp += i

    return M*temp/V

def vehicle_utilization(vehicle_map_order):
    temp = 0

    for vehicle_number in range(Nv):
        vehicle_type = int(i/veh_of_each_type)
        cur_weight = 0
        cur_vol = 0
        max_weight = vehicle_specs[vehicle_type][0]
        max_vol = vehicle_specs[vehicle_type][1]
        
        for j in vehicle_map_order[vehicle_number]:
            order_type = j % n_supplies
            cur_weight += order_matrix[j]
            cur_vol += (order_matrix[j]) / supply_specs[order_type]
        
        temp += max(cur_weight / max_weight, cur_vol / max_vol)

    return temp


def f(X):
    vehicle_map_order = create_vehicle_map(X)
    min_path, min_dis = find_min_path(vehicle_map_order)

    cost = transportation_cost(min_dis)
    tau = vehicle_utilization(vehicle_map_order)

    print(min_path, min_dis)
    print(cost)

f([7, 1, 4, 10, 8, 10, 9, 12, 5, 3, 12, 6, 1, 11, 2, 8, 12, 13, 8, 5, 2, 14, 2, 4, 9, 6, 0, 10, 8, 11, 10, 14, 6]) 