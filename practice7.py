#Slicing , Concatenation,repetation ,membership On string
string ="Hello,Python! "
print(string[0:5])#slicing (Hello)
print(string  + "World!") # concatenation
print(string *2)#repetation
print("python " *5)#repetation
print("Hello" in string)#membership

#Slicing , Concatenation,repetation ,membership On List
list1=[1,2,3,4,5]
list2=["A","B","C","D","E"]
print(list1[2:5])#slicing
print(list1+list2)#concatenation
print(list2 + [5,6,7,8])#concatenation
print (list1 * 2)#repetation
print (5 in list1)#membership
print (5 in list2)#membership

#Slicing , Concatenation,repetation ,membership On Tuple
my_tuple1=(11,22,33,44,55)
my_tuple2=("Anjali","Ritika","Palak","Vipan")
print(my_tuple2[0:3])#slicing
print(my_tuple1 + my_tuple2)#concatenation
print (my_tuple1 + ("AA","BB","CC"))#concatenation
print (my_tuple1 * 2)#repetation
print ("Vipan" in my_tuple2)#membership
print ("Vipan" in my_tuple1)#membership 




