# Playing with Python variables

## variable pointing vs copying
a = [1,2,3]
print (a)

# b "points" to a 
b=a
print(b)

# c "copes" a
c = a.copy()
print(c)

a[2] = 5

print(a)
print(b) # b now prints as [1,2,5], because b "points" to a
print(c) # c is a "copy" item of a, thus it remains unaffected by the index change of a.

#-----------------------------------------------------------------------------------------------------
# Creating variables in same-different ways
a, b = ('python', 'life')
print (a,b) # gives "python life"

(a, b) = 'python', 'life'
print (a,b) # gives "python life"

[a, b] = ['python', 'life'] # Creating variables a and b as a list
print (a,b) # gives "python life"

a = b = 'python' # inserting the same value across multiple variables
print (a,b) # gives "python python"

# application of the above 
a=5
b=3
a,b=b,a # variable switch, not indexing switch
print(a,b) # prints 3 5

## Creating lists in Python
a = [] # empty list
b = list() # ALSO, empty list
c = [1, 2, 3] 
d = ['Life', 'is', 'too', 'short']
e = [1, 2, 'Life', 'is']
f = [1, 2, ['Life', 'is']]
print (a,b,c,d,e,f)
print(f[2]) # prints ['Life', 'is'] of f = [1, 2, ['Life', 'is']]. Note that Python counts from 0.

#-----------------------------------------------------------------------------------------------------
# Indexing a list
a = [1, 2, 3, 4]
print(a[-1])  # prints 4, the first last element
print(a[-2])  # prints 3, the second last element

# Indexing a list within a list
x = [1, 2, 3, ['a', 'b', 'c']] # First: 1, Second: 2, Third: 3, Fourth: ['a', 'b', 'c']
print(x[3])  # prints ['a', 'b', 'c']
print(x[3][1]) # prints 'b', the second (index=1) element of the third element of the list 'x'

# Adding lists (not a numerical operation)
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)  # prints [1, 2, 3, 4, 5, 6]

# Repeating lists
a = [1, 2, 3]
print(a*3) # prints [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Length of a list
len(a) # returns 3

# changing an element of a list
a = [1, 2, 3]
a[2] = 5
print(a)  # returns [1,2,5]

# Deleting an element of a list
a = [1, 2, 3]
del a[1]  # delete the second element of the list 'a'
print(a)  # returns [1, 3]

# Deleting multiple elements of a list
a = [1, 2, 3, 4, 5]
del a[2:]  # returns [1,2] because it deletes all elements from position 2 until the end
# The R grammar such as -a[2:] doesn't work in Python. Must use "del" or "remove" instead.

#//////////////////////////////////////////////////
# Adding a list of elements to a list: append()
a = [1, 2, 3]
a.append(4)  # returns [1,2,3,4]
a.append([5, 6]) # returns [1, 2, 3, 4, [5, 6]]
# Note that a code line such as a.append(7,8,9) wouldn't work, because list.append() takes exactly one argument (3 given).
#//////////////////////////////////////////////////
# Adding elements into a list: extend()
a = [1, 2, 3]
a.extend([4, 5]) # returns [1,2,3,4,5] instead of [1,2,3, [4,5] ], which you'd get from using append()
b = [6, 7]
a.extend(b) # returns [1, 2, 3, 4, 5, 6, 7]
#//////////////////////////////////////////////////


# Sorting the elements within a list
a = [1, 4, 3, 2]
a.sort()
print(a) # returns [1, 2, 3, 4]. Works the same for alphabetical string values.

a.reverse() # returns [4,3,2,1]
a.index(3) #returns 1

# Inserting an element into a list
a = [1, 2, 3]
a.insert(0, 4) # At position 0, insert '4'
print(a) # returns [4, 1, 2, 3]
a.insert(2, 5) # At position 2 of list a, insert '5'. Recall position 0: 4, position 1: 1, position 2: 2, position 3: 3
print(a) # returns [4,1, 5, 2,3]

# Removing an element of a list. 
a = [1, 2, 3, 1, 2, 3]
a.remove(3)  # removes the FIRST '3' within the list 3, returning [1,2,1,2,3]

# Very Python: pop() function
# Takes out the very last element of a list and deletes it off from the original list
a=[1,2,3]
a.pop() # returns 3, and now a=[1,2]
print(a) # returns [1,2]