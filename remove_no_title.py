import json
'''Open the file with all the products in the category'''
with open('meta_pets.json', 'r') as json1:#change the name of the file
    meta = json.load(json1)

with open('reviews_pets.json', 'r') as json2:
    reviews = json.load(json2)

print(len(meta))

"Check and refine the list to remove the products with no title"
list_no_titles = []
for product in meta:
    if 'title' not in product.keys():
        list_no_titles.append(product['asin'])
        meta.remove(product)
print(len(list_no_titles))
print(len(meta))

print(len(list_no_titles))

count=0
for i in list_no_titles:
    for review in reviews:
        if i == review['asin']:
            count+=1
            reviews.remove(review)

print(count)
"Save the list of the product"
with open("meta_pets.json","w") as json_w1:#change the name of the file
    json.dump(meta, json_w1)


"Save the list of the reviews"
with open("reviews_pets.json","w") as json_w2:#change the name of the file
    json.dump(reviews, json_w2)

