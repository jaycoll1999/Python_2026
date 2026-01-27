#list Assignment

list2=[10,20,30,[40,50,[60,80,90],100,110,120],[112,114,116],221,226,336]
print(len(list2))
print(list2)

#what is the output of list2[0] and list2[3]?
print(list2[0])
print(list2[3])

#Extract the list [40,50,[60,80,90],100,110,120]  using indexing.
print(list2[3])

#retrive the 60,80, and 90 from the nested list using indexing
print(list2[3][2])

#What is output of list2[4][1]
print(list2[4][1])

#Write a statement to aceess the element 336
print(list2[-1])

#The lats Elemenet (336)
print(list2[-1])

#The Second to last sub list29[112,114,116])
print(list2[4])

#Acess 110 from the sub -list [40,50,[60,80,90],100,110,120]
print(list2[3][4])

#Retrive the Element 116 from the list [112,114,116]
print(list2[4][2])

#Extract 40 from [40,50[60,80,90],100,110,120]
print(list2[3][0])

#Write a slice to extarct [30,[40,50[60,80,90],100,110,120]]
print(list2[2:4:1])

#Extract [100,110,120] from the nested sub list[40,50,[60,80,90],100,110,120]
print(list2[3][3:6:1])

#Write Slice to reverse the entire list2
print(list2[-1:-9:-1])

#Reverse the list [112,114,116]
print(list2[-4][-1:-4:-1])

#14. Write Slice to get [60,80,90]
print(list2[3][2])

#15. From the main list extract[10,30,[112,114,116]] using slicing
print(list2[0:5:2])

#16. Slice to extact[221,226,336] from the main list
print(list2[5:8:1])

#17.write a slice to extarct [40,50[60,80,90]]

print(list2[3][0:3:1])

#18.Write a slice to get [10,30[112,114,116],226]
print(list2[0:7:2])

#19. How many elements are in list2[3] and list2[4]
print(len(list2[3]))

print(len(list2[4]))

#20. Write the statement to extarct [112,114,116] from list2
print(list2[4])

# 21. print(list2[-5])
print([list2[-5][-1:-7:-1]])