import json

with open("product_titles.json", "r") as json1:
    titles = json.load(json1)

"Open the file with review sets"
with open('review_sets_full.json', 'r') as json2:  # change the name of the file
    review_sets = json.load(json2)

"Open the file with the list of customers"
with open('customers_full.json', 'r') as json3:  # change the name of the file
    customers = json.load(json3)

"Open the file with the reviews for products we are interested in"
with open('reviews_refined.json', 'r') as json2:#change the name of the file
    reviews = json.load(json2)
print("Number of reviews: ", len(reviews))

print(len(titles))
print(len(review_sets))
print(len(customers))

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

count = 0
for i in review_sets:
    for j in i:
        if len(i) != 1:
            count +=1

print(count)