str = "Hello"

list = []
for letter in str:
	list.append(letter)

print(list)

###########################

print([i for i in str])

##############
print([x for x in "word"])

#################################
print([num for num in range(1,11)])
################################
print([num**2 for num in range(1,11)])
##################################
print([num for num in range(1,11) if num%2==0])
################################
cel = [0,10,34.5]
fer = [(9/5*temp)+32 for temp in cel]
print(fer)
###################################
faren = []
for temp in cel:
	faren.append((9/5*temp)+32 )

print(faren)

#########################################
print([x if x%2==0 else "ODD" for x  in range(0,11)  ])
######################################
li = []
for x in [2,4,6]:
	for y in [100,200,300]:
		li.append(x*y)

print(li)

##########################

print([x*y for x in [2,4,6] for y in [100,200,300]])