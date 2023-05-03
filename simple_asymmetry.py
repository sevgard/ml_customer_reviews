import json
import numpy as np
'''
In this file get rid of singletone review sets and create the tables of global and local asymmetries
'''
"Open the file with review sets"
with open('review_sets_full.json', 'r') as json1:#change the name of the file
    review_sets = json.load(json1)

"Open the file with the list of customers"
with open('customers_full.json', 'r') as json2:#change the name of the file
    customers = json.load(json2)

"Open the file with the metadata about the products"
with open('meta_pets.json', 'r') as json3:#change the name of the file
    meta = json.load(json3)

"Count the number of review sets with different length"
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count_else = 0
for i in review_sets:
    if len(i) == 1:
        count1 +=1
    elif len(i) == 2:
        count2 +=1
    elif len(i) == 3:
        count3 +=1
    elif len(i) == 0:
        count0 +=1
    else:
        count_else +=1

print('# of customers left no review: ',count0)
print('# of customers left 1 review: ',count1)
print('# of customers left 2 reviews: ',count2)
print('# of customers left 3 reviews: ',count3)
print('# of customers left more than 3 reviews: ',count_else)

"Refine the list of review sets and the list of customers"#if necessary
review_sets_ns = []
customers_ns = []
for i in review_sets:
    if len(i) != 1:
        review_sets_ns.append(i)
        customers_ns.append(customers[review_sets.index(i)])

with open('review_sets_ns.json', 'w') as json_w1:
    json.dump(review_sets_ns, json_w1)
print("Number of review sets without singletones: ", len(review_sets_ns))

with open('customers_ns.json', 'w') as json_w2:
    json.dump(customers_ns, json_w2)
print("Number of customers: ", len(customers_ns))

"Refine the list of products"
list_products = []
for i in review_sets_ns:
    for j in i:
        if j not in list_products:
            list_products.append(j)
print('len(list_products)', len(list_products))

print(len(set(list_products)))

with open('list_products.json', 'w') as json_w3:
    json.dump(list_products, json_w3)
print("The number of products under consideration: ", len(list_products))


"Create the list of the product titles"
product_title = []
for i in list_products:
    for product in meta:
        if product['asin'] == i:
            product_title.append(product['title'])
print('len(product_title)', len(product_title))

product_titles = dict(zip(list_products, product_title))
print('len(product_titles)', len(product_titles))

for i in list_products:
    if i not in product_titles.keys():
        print(i)

with open('product_titles.json', 'w') as json_w4:
    json.dump(product_titles, json_w4)

print(len(product_titles))
"Create the empty matrix Y_S for all products"
Y_S = np.zeros(len(list_products)**2, dtype=float).reshape(len(list_products),len(list_products))
print(Y_S.shape)
print(Y_S.dtype)

"Change the values in matrix Y for the number of review sets mentioning the products"
for i in range(len(list_products)):
    for j in range(len(list_products)):
        count_i_j = 0
        for k in range(len(review_sets_ns)):
            if list_products[i] in review_sets_ns[k] and list_products[j] in review_sets_ns[k]:
                count_i_j += 1
                Y_S[i][j] = count_i_j

print(Y_S[:7, :7])
np.save('Y_S', Y_S)

"Create the empty matrix Z_S for local asymmetry"
Z_S = np.zeros(len(list_products)**2, dtype=float).reshape(len(list_products),len(list_products))
print(Z_S.shape)
print(Z_S.dtype)
for i in range(len(list_products)):
    for j in range(len(list_products)):
        Z_S[i][j] = Y_S[i][j]/Y_S[i][i]

print(Z_S[:5,:5])
np.save('Z_S', Z_S)
