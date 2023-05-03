import json
import csv
import numpy as np
import matplotlib.pyplot as plt

'''This file is to create the perceived quality of the product measure'''

#Import the rating_sets
with open('ratings.json', 'r') as json1:
    ratings = json.load(json1)

#Import the polarity
with open('polarity.json', 'r') as json2:
    polarity = json.load(json2)


#Import review sets refined
with open('review_sets_ns.json', 'r') as json2:
    review_sets = json.load(json2)

#Import customer sets refiend
with open('customers_ns.json', 'r') as json2:
    customers = json.load(json2)


print(ratings[0:10])

rating_full = []
for i in ratings:
    for j in i:
        rating_full.append(j)

print(rating_full[0:13])
'''
num_bins = 50

# the histogram of the rating
fig, ax = plt.subplots()
n, bins, patches = ax.hist(rating_full, num_bins, density=1)

fig.savefig("rating_distribution.png", dpi=300)

# the histogram of the polarity
fig, ax = plt.subplots()
n, bins, patches = ax.hist(polarity, num_bins, density=1)

fig.savefig("polarity_distribution.png", dpi=300)  # results in 160x120 px image

#measure: rating*polarity
measure = []
for i in range(0,len(rating_full)):
    measure.append(rating_full[i]*polarity[0])

# the histogram of the measure
fig, ax = plt.subplots()
n, bins, patches = ax.hist(measure, num_bins, density=1)

fig.savefig("measure_distribution.png", dpi=300)  # results in 160x120 px image
'''
#long review_set list
review_full = []
for i in review_sets:
    for j in i:
        review_full.append(j)

print(review_sets[0:10])
print(review_full[0:10])

#long customer_set list
customer_full = []
for i in range(0,len(customers)):
    for j in range(0,len(ratings[i])):
        customer_full.append(customers[i])
print(customers[0:10])
print(customer_full[0:10])

polarity_full = []
for i in polarity:
    for j in i:
        polarity_full.append(j)


print(len(polarity_full))
print(len(customer_full))
print(len(review_full))
print(len(rating_full))
print(polarity_full[0:10])
#print(customer_full[0:10])
#print(review_sets[0:10])
#print(review_full[0:10])




with open("out.csv","w", newline='') as f:
    wr = csv.writer(f,delimiter=",")
    for i in range(len(customer_full)):
        wr.writerow([customer_full[i],review_full[i],rating_full[i],polarity_full[i]])
'''

print(polarity[0:10])
#print(ratings[0:10])
#print(helpfulness[0:10])
print(review_sets[0:10])
#print(customers[0:10])


length = []
for j in review_sets:
    length.append(len(j))

print(length[0:10])
print(len(length))

all_polarity_sets = []
for j in range(0,len(length)):
    polarity_set =[]
    for i in range(0,length[j]):
        polarity_set.append(polarity[i+sum(length[:j])])
    all_polarity_sets.append(polarity_set)

print(all_polarity_sets[0:5])
print(ratings[0:15])

#with open('polarity_sets.json', 'w') as json3:
#    json.dump(all_polarity_sets, json3)

#for i in range(0,len(customers)):
#    if

#(all_polarity_sets[0][1]+ratings[0][1])

measures = []
for i in range(len(ratings)):
    measure_set = []
    for j in range(len(ratings[i])):
        measure_set.append(ratings[i][j]+all_polarity_sets[i][j]*0.5)
    measures.append(measure_set)

print(measures[0:10])

#with open('measure_1.json', 'w') as json4:
#    json.dump(measures, json4)

number_full =[]
for i in number_voted_set:
    for j in i:
        number_full.append(j)

for i in number_full:
    if i == 0:
        number_full.remove(i)
print(np.max(number_full))
'''