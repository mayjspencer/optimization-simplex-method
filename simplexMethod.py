def simplexMethod(tableauArg, iteration):
    # Initial tableau
    tableau = tableauArg

    pivot_column_index = 0
    pivot_column_candidate = []
    # Find pivot column candidate (negative reduced costs)
    for i in range(1, len(tableau[0])):
        if tableau[0][i] < 0:
            pivot_column_candidate.append(i)

    # If there are no negative reduced costs, terminate algorithm
    if len(pivot_column_candidate) == 0:
        print("Optimal solution found: current Basic Feasible Solution")
        # End algorithm current basic feasible solution is optimal
        exit()

    # choose the closest to 0 (as the text book does)
    max = tableau[0][pivot_column_candidate[0]]
    for i in range(0, len(pivot_column_candidate)):
        if tableau[0][pivot_column_candidate[i]] >= max:
            max = tableau[0][pivot_column_candidate[i]]
            pivot_column_index = pivot_column_candidate[i]

    # look for a non-negative in the pivot column - put all in pivot_row_candidate array
    pivot_row_candidate = []
    for i in range(1, len(tableau)):
        if tableau[i][pivot_column_index] >= 0:
            pivot_row_candidate.append(i)

    # if no non-negatives found, end
    if len(pivot_row_candidate) == 0:
        print("Optimal cost is (-) infinity")
        # End algorithm optimal cost is (-) infinity
        exit()
    else:
        # if array of positive column components is just 1 component - it must be the pivot row
        if len(pivot_row_candidate) == 1:
            pivot_row_index = pivot_row_candidate[0]
        else:
            min_ratio = tableau[pivot_row_candidate[0]][0] / tableau[pivot_row_candidate[0]][pivot_column_index]
            pivot_row_index = pivot_row_candidate[0]
            for i in range(1, len(pivot_row_candidate)):
                ratio = tableau[pivot_row_candidate[i]][0] / tableau[pivot_row_candidate[i]][pivot_column_index]
                if ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row_index = pivot_row_candidate[i]

    # Elementary ops on Pivot Element
    pivot_element_value = tableau[pivot_row_index][pivot_column_index]
    # set pivot element to one
    for i in range(0, len(tableau[pivot_row_index])):
        tableau[pivot_row_index][i] = round(tableau[pivot_row_index][i] / pivot_element_value, 2)
    # set all else in column to 0
    for i in range(0, len(tableau)):
        if i != pivot_row_index:
            multiplier = tableau[i][pivot_column_index]
            for j in range(0, len(tableau[i])):
                tableau[i][j] = round(tableau[i][j] - multiplier * tableau[pivot_row_index][j], 2)

    # Display the updated tableau
    print("Iteration", iteration)
    print()
    for row in tableau:
        print(row)
    print()

    for i in range(1, len(tableau[0])):
        if tableau[0][i] < 0:
            simplexMethod(tableau, iteration + 1)


tableau = [[0, -10, -12, -12, 0, 0, 0],
            [20, 1, 2, 2, 1, 0, 0],
            [20, 2, 1, 2, 0, 1, 0],
            [20, 2, 2, 1, 0, 0, 1]]

print("Before Simplex Method:")
print()
for row in tableau:
    print(row)
print()

simplexMethod(tableau, 1)
