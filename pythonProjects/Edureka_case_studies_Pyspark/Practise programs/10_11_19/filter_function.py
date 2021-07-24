# filter function to filter only odd numbers of a list.

list1 = [1,2,3,4,5,6,7,8,9,0,11,12]
print(list(filter(lambda x: x%2!=0, list1)))