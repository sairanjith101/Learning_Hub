def productsum(arr1,arr2):
    product_sum = 0
    for i in range(len(arr1)):
        if i % 2 == 0:
            product_sum += arr1[i]
        else:
            product_sum += arr2[i]
    return product_sum

arr1 = [10,20,30,40,60]
arr2 = [70,80,90,100,200]

print(productsum(arr1,arr2))