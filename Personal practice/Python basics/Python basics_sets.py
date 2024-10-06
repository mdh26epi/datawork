#------------------------------------------------------------------
# Sets
#------------------------------------------------------------------

# To make a set: set([<values])

# Simple null set
s = set()

# Simple numeric set
s1 = set([1, 2, 3])
print(s1) # returns {1, 2, 3}

# Simple string set
s2 = set("Tobacco") # there are two o's and two c's, BUT...
# // set은 중복을 허용하지 않는 특징 때문에 데이터의 중복을 제거하기 위한 필터로 종종 사용된다.
print(s2) # returns {'T', 'a', 'o', 'c', 'b'}, only the UNIQUE elements. 
