import json
import numpy as np

"This file is to create the measure and the tables of global and local asymmetry"

with open('list_products.json','r') as json1:
    list_products= json.load(json1)

with open('review_sets_ns.json','r') as json2:
    review_sets= json.load(json2)

with open('ratings.json','r') as json3:
    all_rating_set= json.load(json3)

with open('polarity.json', 'r') as json4:
    polarity= json.load(json4)

"Create the measure"
measure = []
for i in range(len(polarity)):
    measure_list = []
    for j in range(len(polarity[i])):
        measure_list.append(all_rating_set[i][j]+0.5*polarity[i][j])
    measure.append(measure_list)
print(measure[:10])


"Create the empty matrix Y_M for global asymmetry"
Y_M = np.zeros(len(list_products)**2, dtype=float).reshape(len(list_products),len(list_products))
print(Y_M.shape)
print(Y_M.dtype)

"Change the matrix"
for i in range(len(list_products)):
    for j in range(len(list_products)):
        count_i_j = 0
        for k in range(len(review_sets)):
            if list_products[i] in review_sets[k] and list_products[j] in review_sets[k]:
                count_i_j += measure[k][review_sets[k].index(list_products[i])]
        Y_M[i][j] = count_i_j

print(Y_M[:5, :5])
np.save('Y_M', Y_M)

'''Create the empty matrix Z_M for local asymmetry"'''
Z_M = np.zeros(len(list_products)**2, dtype=float).reshape(len(list_products),len(list_products))
print(Z_M.shape)
print(Z_M.dtype)

for i in range(len(list_products)):
    for j in range(len(list_products)):
        Z_M[i][j] = Y_M[i][j]/Y_M[i][i]

print(Z_M[:5,:5])
np.save('Z_M', Z_M)
