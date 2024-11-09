'''
for i  in range (10):
    if i==7:
        print("Excecuting at ",i )
        break
    print("Printing the value as ",i )

print("Outside the for loop")
'''


'''
for i in range(10):
     if i==7:
       print(i)
       break
     elif i==5:
         continue
     print(i)
'''

cart=[10,30,40,250,300]
for item in cart:
    if item>260:
      print("item is not allowed")
      break
    print(item)
else:
    print("all items get passed")
