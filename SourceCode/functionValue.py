from initialMultiverse import *
import itertools


def find_min_path(vehicle_map_order):
    min_path = []
    min_dis = []
    for i in range(Nv):
        per = list(itertools.permutations(vehicle_map_order[i]))
        cur_min = 1e9
        cur_path = []
        # print(per)
        for j in per:
            if len(j) != 0:
                dis = distance_matrix[len(distance_matrix)-1][int(j[0]/n_supplies)]

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
        vehicle_type = int(vehicle_number/veh_of_each_type)
        cur_weight = 0
        cur_vol = 0
        max_weight = vehicle_specs[vehicle_type][0]
        max_vol = vehicle_specs[vehicle_type][1]
        
        for j in vehicle_map_order[vehicle_number]:
            order_type = j % n_supplies
            cur_weight += order_matrix[j]
            cur_vol += (order_matrix[j]) / supply_specs[order_type]
        
        temp += max((cur_weight / max_weight), (cur_vol / max_vol))

    return temp

def demand_urgency(min_path):
    urgency_value = 0

    for vehicle_number in range(Nv):
        cur_time = 0    
        prev = len(distance_matrix)-1
        for order in min_path[vehicle_number]:
            hospital = int(order / n_supplies)
            cur_time += distance_matrix[prev][hospital] / V
            prev = hospital

            if cur_time <= T:
                urgency_value += demand_urgency_values[hospital][order % n_supplies]
            else: 
                break

    return urgency_value




def f(X):
    vehicle_map_order = create_vehicle_map(X)
    min_path, min_dis = find_min_path(vehicle_map_order)

    cost = transportation_cost(min_dis)
    tau = vehicle_utilization(vehicle_map_order)
    gamma = demand_urgency(min_path)

    # print(min_path, min_dis)
    # print(cost)
    # print(tau)
    # print(gamma)
    return tau * gamma / cost

# print(f([1, 12, 1, 0, 13, 14, 4, 14, 8, 2, 12, 0, 5, 5, 5, 6, 2, 9, 3, 11, 5, 0, 13, 0, 6, 6, 10, 8, 7, 11, 14, 10, 8]))