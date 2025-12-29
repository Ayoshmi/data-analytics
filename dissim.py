def printer(mat, number_of_vals):
    """Prints the lower-triangular matrix with 2 decimal precision."""
    for i in range(number_of_vals):
        for j in range(i + 1):
            print("{0:.2f}".format(mat[i][j]), end=' ')
        print("")  # Move to next line


# ---- Read data from cardata.txt ----
with open('./cardata.txt', 'r') as f:
    # First line = feature names
    features = f.readline().strip().split()

    # Create dictionary with feature names as keys
    data = {feature: [] for feature in features}

    keys = list(data.keys())
    values = f.readlines()
    number_of_vals = len(values)

    # Fill dictionary with data
    for line in values:
        for k, val in enumerate(line.split()):
            data[keys[k]].append(val)


# ---- Read attribute types (nominal / numeric) ----
with open('./attributetypes.txt', 'r') as typ:
    nom_attr = typ.readline().split()   # nominal attributes
    num_attr = typ.readline().split()   # numeric attributes


# ---- Display the data ----
print("The data set is:\n", data)
print("The nominal attributes are:", nom_attr)
print("The numeric attributes are:", num_attr, "\n")


# ---- Initialize dissimilarity matrices ----
disnom = [[0 for _ in range(number_of_vals)] for _ in range(number_of_vals)]
disnum = [[0 for _ in range(number_of_vals)] for _ in range(number_of_vals)]


# ---- Calculate dissimilarities ----
for i in range(number_of_vals):
    for j in range(i + 1, number_of_vals):

        # --- Nominal attributes ---
        matches = sum(1 for k in nom_attr if data[k][i] == data[k][j])
        disnom[i][j] = (len(nom_attr) - matches) / len(nom_attr)

        # --- Numeric attributes (Euclidean distance) ---
        e_dist = sum((float(data[k][i]) - float(data[k][j])) ** 2 for k in num_attr)
        disnum[i][j] = e_dist ** 0.5


# ---- Print the results ----
print("Dissimilarity matrix for Nominal Attributes:")
printer(disnom, number_of_vals)
print()

print("Dissimilarity matrix for Numeric Attributes:")
printer(disnum, number_of_vals)
print()


# ---- Find similarity between two data points ----
i, j = map(int, input("Input the indices of data points to find similarity of: ").split())

# similarity = 1 - dissimilarity
similarity = 1 - disnom[i][j] if j < i else 1 - disnom[j][i]

print(f"The similarity of the two data points is: {similarity:.2f}")
