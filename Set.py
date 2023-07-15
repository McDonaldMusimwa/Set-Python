myArray= []
for i in range(0,10):
    myArray.append(i)

myArray.append(9)
myArray.append(0)
set1 = set(myArray)
print(set1)


numbers1 = [1,2,3,4]
numbers2 = [3,5,6,7]
numbers1 = set(numbers1) 
numbers2 = set(numbers2) 


combinedsets = numbers1.union(numbers2)
print(combinedsets) 
intersection = numbers1.intersection(numbers2)
print(intersection)
newsetnumbers = numbers1.update(numbers2) 

numbers1.intersection_update(numbers2) 
    