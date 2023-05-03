import json

'''
This file is for creating the review lists
'''

"Open the file with the list of products we are interested in"
with open('substitutes_products.json', 'r') as json2:#change the name of the file
    products = json.load(json2)
print("Number of products and substitutes: ", len(products))

"Open the file with the reviews for products we are interested in"
with open('reviews_refined.json', 'r') as json2:#change the name of the file
    reviews = json.load(json2)
print("Number of reviews: ", len(reviews))

"Find the number of unique customers who left the reviews"
customers= []
for review in reviews:
    if review['asin'] in products:
        customers.append(review['reviewerID'])

customers_full = list(set(customers))
print(len(customers))
print("Number of reviewers: ", len(customers_full))

"Save the full list of the customers"
with open("customers_full.json", 'w') as json_w1:#change the name of the file
    json.dump(customers_full, json_w1)


"For every customer create his/her review set"
all_review_sets = []
for customer in customers_full:
    review_set = []
    for review in reviews:
        if customer == review['reviewerID']:
            review_set.append(review['asin'])
    all_review_sets.append(review_set)

"Save the review sets of the customers in the separate json file"
with open("review_sets_full.json", 'w') as json_w2:
    json.dump(all_review_sets, json_w2)

'''Count the number of review sets with different length'''
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count_else = 0
for i in all_review_sets:
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

