# Python Identification

if 5>10 :
    print("5 is greater than 10")
else :
  print('5 is less than 10')
   
#Python VAriables
 
  x=5 
  x='alif'
  print(type(x))
  
#Python List
  fruits=['apple','bannana','orange']  
  print(fruits)
  print(len(fruits))
  
#Access List Items
fruits=['apple','bannana','orange'] 
print(fruits[0])#first Item
print(fruits[1])#Second Item
print(fruits[2])#Third Item
print(fruits[-1])#last item
print(fruits[-2])#second last item
print(fruits[-3])#Third last items
x=[ "cherry", "kiwi", "melon", "mango"]
print(x[2:5])#Return the third, fourth, and fifth item:
print(x[:5])#Return the first five items
x[1:3]='watermilon','guavera' #Change a Range of Item Values
print(x)
fruits.insert(1,'cherry')#Insert Items
print(fruits)
fruits.extend(x)#Extend List
print(fruits)
fruits.remove('apple')#remove item
print (fruits)
for y in fruits:#Loop Through a List
      print(y)
colour=['yellow','black','green','blue']
for i in range(len(colour)):#Loop Through a List
      print(colour[i])
      
house=['bedroom','washroom','kitchen','drawingroom']
print()
i=0
while(i<len(house)):#While Loop Through a List
      print(house[i])
      i=i+1

