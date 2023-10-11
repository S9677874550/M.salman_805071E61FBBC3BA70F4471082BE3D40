def linearSearchProduct(productList, targetProduct):
    indices = []

    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)

    return indices

#Example usage:
products = ["Audi", "Bugatti", "Skyline", "Bugatti", "BMW", "Bugatti", "Rolls_Royce", "Supra", "Bugatti"]
target = "Bugatti"
result = linearSearchProduct(products, target)
print(result)
