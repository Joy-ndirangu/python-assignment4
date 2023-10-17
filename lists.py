# total number of items is called length
# negative indexing starts referencing from the last item wih an index of -1
cars = ["Audi", "Mercedes", "Vox", "Toyota", "G-wagon"]
print(cars)
print(cars[-5])

#using a full colon to filter list items
#using a full colon to print a certain number of items once
# prints the first three values
print(cars[:3])

#skips the first two and gives us 3 and 4

print(cars[2:4])
#using len() function to count the number of items

print("The length of the list is:", len(cars))

#lists allows duplicate values
cars = ["Audi", "G-wagon", "Mercedes", "Vox", "Toyota", "G-wagon", "Mercedes"]
for x in cars:
    print(x)
