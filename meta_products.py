import json

'''
This is the file for finding out the products we are interested in
'''

"Open the file with all the products in the category"
with open('meta_pets.json', 'r') as m:#change the name of the file
    meta = json.load(m)
print(len(meta))

"Check and refine the list to remove the products with no title"
count_title = 0
for product in meta:
    if 'title' not in product.keys():
        count_title +=1
        meta.remove(product)
print(count_title)
print(len(meta))

'''Input the algorithm to define the products of interest. Here we just use the key word search in the title and subcategory.'''
name = "dog food"#change the name of the product
list_products = []
for product in meta:
    if name in product['title'].lower():
        list_products.append(product['asin'])
    else:
        for i in product['categories']:
            for j in i:
                if name in j.lower():
                    list_products.append(product['asin'])

print('Number of products of interest: ', len(list_products))


"Add to the list of 'pure' products of interest their substitutes. We use 'buy_after_viewing' set"
count = 0
count1 = 0
lists = list(list_products)
for product in meta:
    if product['asin'] in list_products:
        if 'related' in product.keys():
            count += 1
            if 'buy_after_viewing' in product['related']:
                count1 +=1
                lists += product['related']['buy_after_viewing']


list_pure = list(set(lists))

print("# of products and substitutes: ",len(list_pure))

"Kick out some categories from the list"#remove if necessary
wrong_products = ["cat", "fish", "bird", "toy", "container", "bowl", "horses", "horse", "backpack", "ball", "scoop", "storage", "oil", "kit", "single-door", "feeder" ]

for item in list_pure:
    for product in meta:
        if item == product['asin']:
            for word in wrong_products:
                if word in product['title'].lower():
                    if item in list_pure:
                        list_pure.remove(item)

print("# of products and substitutes: ",len(list_pure))

print("# of product with 'related' category", count)
print("# of product with 'also_viewed' category", count1)
print("# of products of interest: ",len(list_products))
print("# of products and substitutes including duplicates: ", len(lists))
print("# of products and substitutes: ",len(list_pure))

"Save the list of the product of interest and their substitutes in the separate json file"
json = json.dumps(list_pure)
f = open("substitutes_products.json","w")#change the name of the file
f.write(json)
f.close()

"Check the titles of the products"#remove if necessary
for item in list_pure[0:100]: #list_products[0:100]:
    for product in meta:
        if item == product['asin']:
            print(product['title'])
