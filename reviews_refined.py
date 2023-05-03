import json
'''
This is the python file to create the new json file with only reviews for products of interst.
'''

"Open the file with all the reviews in the category"
with open('reviews_pets.json', 'r') as json1: #change the name of the file
    reviews = json.load(json1)

"Open the file with the list of products we are interested in (created by the commands in meta_products.py file"
with open('substitutes_products.json', 'r') as json2:#change the name of the file
    products = json.load(json2)
print(len(products))

"Open the file with all the products in the category"
with open('meta_pets.json', 'r') as json3:#change the name of the file
    meta = json.load(json3)

'''Pick all the reviews for the products we are interested in'''
product_reviews = []
for review in reviews:
    if review['asin'] in products:
        product_reviews.append(review)
print(len(product_reviews))

'''Check whether there are any duplicates in the reviews'''#does not work properly
'''
for i in product_reviews[0:100]:
    for j in reviews[product_reviews.index(i)+1:len(product_reviews)]:
        if i['reviewerID'] == j['reviewerID'] and i['asin'] == j['asin']:
            product_reviews.remove(j)
'''


print(len(product_reviews))

'''Save the new data file with refined reviews'''
json = json.dumps(product_reviews)
f = open("reviews_refined.json","w")#change the name of the file
f.write(json)
f.close()
