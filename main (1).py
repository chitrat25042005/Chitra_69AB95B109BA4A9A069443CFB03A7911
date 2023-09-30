def linear_search_product(products, target):

    indices = []

    for i, product in enumerate(products):

        if product == target:

            indices.append(i)

    return indices

products = ["apple", "banana", "apple", "orange", "apple"]

target_product = "apple"

result = linear_search_product(products, target_product)

print(result)