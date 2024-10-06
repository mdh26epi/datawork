#-----------------------------------------------------------------------------------------------------
# Dictionary Data Format (R equivalent is NOT a data frame, as R also has a ditionary data format)
#-----------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------
# Basic structure   {Key1: Value1, Key2: Value2, Key3: Value3, ...}
# Note: keys are supposed to be unique values. Therefore, if there is a duplicate key, Python will pick up only the first detected key and its values.
# Note: Lists [mutable] cannot be keys, but tuples (immutable) can be keys.
#--------------------------------------------------------------------------------------------------------------------------------------------------

# EXAMPLE 1
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])      # returns 10 for the dictionary value 'pey'
print(grade['julliet'])  # returns 99 for the dictionary value 'julliet'

# EXAMPLE 2 - to emphasizse that indexing does NOT work for a dictionary object, unlike for a list or tuple.
# For a dictionary, <object>[key] does NOT numerically index a value, even if the key looks like a number.
a = {3:('a', 'b'), 5:('x', 'y')}
print(a[3])     # returns ('a', 'b'), because here [1] is not indexing, but rather calling the first key, '3'
print(a[5])     # returns ('x', 'y'), because here [1] is not indexing, but rather calling the second key, '5'

print(a[5][0])  # returns x, the first element[0] of the values for the key '5'

# How to add/replace/delete keys and values into a dictionary object
a = {3: ['a', 'p']}
a['x'] = ('b', 'c') # 
print(a)     # returns {3: 'a', 'x': 'b'}
a[3] = [a[3], [1, 2, 3]]
print(a)     # returns {3: [['a', 'p'], [1, 2, 3]], 'x': ('b', 'c')}

del a[3][0]  # Delete the first value under the key '3'; returns {3: [[1, 2, 3]], 'x': ('b', 'c')}
print(a)


#--------------------------------------------------------------------------------------------------------------------------------------------------
# 파이썬 3.0 이후 버전의 keys 함수, 어떻게 달라졌나?
# 파이썬 2.7 버전까지는 a.keys() 함수를 호출하면 dict_keys가 아닌 리스트를 리턴한다. 
# 리스트를 리턴하기 위해서는 메모리 낭비가 발생하는데, 파이썬 3.0 이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_keys 객체를 리턴하도록 변경되었다. 
# 다음에 소개할 dict_values, dict_items 역시 파이썬 3.0 이후 버전에서 추가된 것들이다. 
# 만약 3.0 이후 버전에서 리턴값으로 리스트가 필요한 경우에는 list(a.keys())를 사용하면 된다. 
# dict_keys, dict_values, dict_items 객체는 리스트로 변환하지 않더라도 기본적인 반복 구문(예: for 문)에서 사용할 수 있다.
#--------------------------------------------------------------------------------------------------------------------------------------------------

# Basic dictionary functions

# Creating a key list: <dict>.keys()
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a.keys()           
print(a.keys())    # returns an OBJECT to save memory, dict_keys(['name', 'phone', 'birth'])

list(a.keys())
print(list(a.keys()))   # returns a list, ['name', 'phone', 'birth']. However this operation uses more memory than a.keys()


# Extracting values from a dictionary

# 1. CRUDE - Making a list of values: <dict>.values()
a.values()
print(a.values()) # returns only the object of list of values from line 47, dict_values(['pey', '010-9999-1234', '1118'])

# 2. CRUDE - Empty all elements of a dictionary object: a.clear()

# 3. CRUDE - Extracting key-value pairs: <dict>.items()
a.items()
print(a.items()) # returns the key-value pairs from line 47, dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

# 4. ESSENTIAL - Extravt values corresponding to a key
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.get('name')   # returns 'pey' from the key 'name'
a.get('phone')  # returns'010-9999-1234' from the key 'phone'

# 딕셔너리 안에 찾으려는 Key가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는 get(x, '디폴트 값')을 사용하면 편리하다.
a.get('nokey', 'foo') # returns 'foo'

# 5. ESSENTIAL - Searching for a key within a dictionary
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
'name' in a    # returns 'True'
'email' in a   # returns 'False'
'pey' in a # returns 'False', because 'pey' is a value, not a key.