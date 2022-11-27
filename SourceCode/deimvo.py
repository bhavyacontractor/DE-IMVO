from functionValue import *


def roulette_wheel(fit, x):
    return random.choices(x, weights=fit)


for iteration in range(G):
    fitness = []
    min_fit = 1e9
    max_fit = -1e9
    X_best = []
    for universe in X:
        cur_fit = f(universe)
        fitness.append(cur_fit)
        if cur_fit < min_fit:
            min_fit = cur_fit
        if cur_fit > max_fit:
            max_fit = cur_fit
            X_best = universe

    normalized_fitness = []
    for universe in fitness:
        numerator = universe - min_fit
        denominator = max_fit - min_fit
        normalized_fitness.append(numerator / denominator)

    l = -1
    for i in range(NP):

        r1 = random.uniform(0, 1)
        white_hole = roulette_wheel(fitness, X)
        white_hole = white_hole[0]

        if r1 < normalized_fitness[i]:

            X[i] = white_hole

        elif r1 > normalized_fitness[i]:

            r2 = random.uniform(0, 1)

            if r2 < CR:

                r3 = random.uniform(0, 1)

                if r3 < 0.5:

                    for j in range(D):
                        X[i][j] = X_best[j] + int(F*(white_hole[j] - X[iteration][j]))
                        if X[i][j] < X_min:
                            X[i][j] = 0
                        if X[i][j] > X_max:
                            X[i][j] = 15

                else:

                    for j in range(D):
                        X[i][j] = X_best[j] - int(F * (white_hole[j] - X[iteration][j]))
                        if X[i][j] < X_min:
                            X[i][j] = 0
                        if X[i][j] > X_max:
                            X[i][j] = 15

            elif r2 > CR:

                r4 = random.uniform(X_max - X_min, 2*(X_max - X_min))
                if l == -1:
                    l = (X_max - X_min) / r4

                r5 = random.uniform(-0.5, 0.5)
                X_new = []
                for j in range(D):
                    x_dash = int(X[i][j] + 0.5 * r5 * l * (X_max - X_min) + X_min)

                    if x_dash < X_min:
                        x_dash = X_min
                        # X_new.append(0)
                    if x_dash > X_max:
                        x_dash = X_max
                        # X_new.append(X_max)
                    X_new.append(x_dash)


                if f(X_new) > fitness[i]:
                    X[i] = X_new

                if (l < (X_max - X_min) / 2) and (l > X_min):
                    l = 2*l
                elif ((X_max - X_min)/2 <= l) and (l < X_max):
                    l = 2*l - 1

fitness = []
min_fit = 1e9
max_fit = -1e9
X_best = []
for universe in X:
    cur_fit = f(universe)
    fitness.append(cur_fit)
    if cur_fit < min_fit:
        min_fit = cur_fit
    if cur_fit > max_fit:
        max_fit = cur_fit
        X_best = universe

print(X_best)
print(min_fit, max_fit)





