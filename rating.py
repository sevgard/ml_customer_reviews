import json
from textblob import TextBlob

"Open the file with the reviews for products we are interested in"
with open('reviews_refined.json', 'r') as json2:#change the name of the file
    reviews = json.load(json2)

"Open the file with customers"
with open('customers_ns.json', 'r') as json3:
    customers_ns = json.load(json3)

"Open nonsingular review set list"
with open('review_sets_ns.json', 'r') as json4:
    review_sets_ns = json.load(json4)

"Create the rating set for all review sets"
all_rating_set = []
for i in range(len(customers_ns)):
    rating_set =[]
    for j in range(len(review_sets_ns[i])):
        for review in reviews:
            if customers_ns[i]==review['reviewerID'] and review_sets_ns[i][j] ==review['asin']:
                rating_set.append(review['overall'])
    all_rating_set.append(rating_set)

print(all_rating_set[0:10])
print(len(all_rating_set))
"Save the rating list"
with open('ratings.json','w') as json_w1:
    json.dump(all_rating_set, json_w1)

"Create the list with polarity measures"
polarity = []
for i in range(len(customers_ns)):
    polarity_set =[]
    for j in range(len(review_sets_ns[i])):
        for review in reviews:
            if customers_ns[i]==review['reviewerID'] and review_sets_ns[i][j] ==review['asin']:
                polarity_set.append(TextBlob(review['reviewText']).sentiment.polarity)
    polarity.append(polarity_set)

with open('polarity.json', 'w') as json_w2:
    json.dump(polarity, json_w2)
print(polarity[0:10])
print(len(polarity))