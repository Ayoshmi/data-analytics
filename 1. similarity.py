# Program to find the dissimilarity and similarity between nominal and numeric attributes

def printer(mat, number_of_vals):
    for i in range(number_of_vals):
        for j in range(i + 1):
           print(f"{mat[i][j]:.2f}", end=" ")
        print(" ")

# Open dataset and attribute type files
f = open('./cardata.txt', 'r')
typ = open('./attributetypes.txt', 'r')

# Read dataset
data = {}
features = f.readline()
for i in features.strip().split():
    data[i] = []

keys = list(data.keys())
values = f.readlines()
number_of_vals = len(values)

for i in values:
    k = 0
    for j in i.split():
        data[keys[k]].append(j)
        k = k + 1

print("The data set is : ", data)

# Read attribute types
nom_attr = typ.readline().split()
num_attr = typ.readline().split()

print("The nominal attributes are : ", nom_attr)
print("The numeric attributes are : ", num_attr)
print()

# Initialize dissimilarity matrices
disnom = [[0 for x in range(number_of_vals)] for x in range(number_of_vals)]
disnum = [[0 for x in range(number_of_vals)] for x in range(number_of_vals)]


# Compute dissimilarities
for i in range(number_of_vals):
    for j in range(i + 1):
        m = 0
        e_dist = 0
        for k in nom_attr:
            if data[k][i] == data[k][j]:
                m += 1
        for k in num_attr:
            e_dist = e_dist + ((float(data[k][i]) - float(data[k][j])) ** 2)
        disnom[i][j] = (len(nom_attr) - m) / len(nom_attr)
        disnum[i][j] = e_dist ** 0.5

# Print matrices
print("Dissimilarity matrix for Nominal Attributes")
printer(disnom, number_of_vals)
print()

print("Dissimilarity matrix for Numeric Attributes")
printer(disnum, number_of_vals)
print()

# Find similarity between two data points
i, j = map(int, input("Input the indices of data points to find similarity of: ").split())
print("The similarity of the two data points is:",
      1 - disnom[i][j] if j < i else 1 - disnom[j][i])

# Close files
f.close()
typ.close()
