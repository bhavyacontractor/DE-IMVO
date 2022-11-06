D = 33  # Universe Dimension
NP = 20  # Number of universes
G = 500  # Number of iterations
CR = 0.2  # Crossover Probability
F = 0.5  # Difference Coefficient
X_max = 14  # Upper limit of search space
X_min = 0  # Lower limit of search space
V = 50  # Vehicle Speed
M = 58.5  # Freight per unit time
T = 1  # Latest delivery time
H = 11  # Number of hospitals
n_supplies = 3  # Number of emergency supplies
n_veh_types = 3  # Number of vehicle types



N0 = H * n_supplies  # Total number of orders which is aldo equal to universe dimension
Nv = X_max - X_min + 1  # Number of vehicles
# Assume that we have 3 types of vehicles and 5 vehicles of each type.

veh_of_each_type = Nv/n_veh_types  # Vehicles of each type
vehicle_specs = [[ 6, 15],
                 [10, 17],
                 [13, 30]]
# vehicle_specs[i][0] denotes max weight capacity of vehicle of type i in tons
# vehicle_specs[i][1] denotes max volume capacity of vehicle of type i in m^3

supply_specs = [  1.7,
                12.66,
                    3 ]
# supply_specs[i] denotes density of ith emergency supply in tons/m^3

distance_matrix = [[   0, 6.4, 4.6,  7.8, 50, 32,   20, 30,   11, 47,   14, 7.4 ],
                  [ 6.4,   0, 5.2,   10, 44, 37,   19, 28,   14, 46,   19, 6.5 ],
                  [ 4.6, 5.2,   0,   11, 47, 39,   17, 36,   17, 44,   16, 4.5 ],
                  [ 7.8,  10,  11,    0, 49, 32,   27, 18,  8.1, 55,   23, 13.9],
                  [  50,  44,  47,   49,  0, 86,   32, 66,   57, 38,   61, 49  ],
                  [  32,  37,  39,   32, 86,  0,   55, 35,   23, 82,   41, 36  ],
                  [  20,  19,  17,   27, 32, 55,    0, 44,   36, 30,   31, 17.7],
                  [  30,  28,  36,   18, 66, 35,   44,  0,   22, 73,   37, 34  ],
                  [  11,  14,  17,  8.1, 57, 23,   36, 22,    0, 55,   20, 20.8],
                  [  47,  46,  44,   55, 38, 82,   30, 73,   55,  0,   52, 38  ],
                  [  14,  19,  16,   23, 61, 41,   31, 37,   20, 52,    0, 13.2],
                  [ 7.4, 6.5, 4.5, 13.9, 49, 36, 17.7, 34, 20.8, 38, 13.2, 0   ]]

order_matrix = [3, 0.8, 1, 1.5, 1, 2, 1, 0.8, 1.3, 2, 1, 1.5, 0.8, 0.5, 1, 5, 1.8, 1.5, 2.4, 0.8, 0.5, 1.3, 1, 0.8, 1,
                1.2, 1, 0.6, 1.2, 0.6, 1, 1.5, 1]

# distanceMatrix[i][j] is distance between hospital i and hospital j
# index 12 is Distribution Center, rest are hospitals

if D != N0:
    print("Number of orders must equal Universe Dimension. Check initialParams.py")
    exit()

print("Parameters initialized. Step 1 complete !!")