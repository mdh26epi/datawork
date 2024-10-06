#---------------------------------------------------------
# A simple IF loop
#---------------------------------------------------------

# Simple numeric set
s1 = set([1, 2, 3])
print(s1) # returns {1, 2, 3}
# Simple string set
s2 = set("Tobacco") # there are two o's and two c's, BUT...
# // set은 중복을 허용하지 않는 특징 때문에 데이터의 중복을 제거하기 위한 필터로 종종 사용된다.
print(s2) # returns {'T', 'a', 'o', 'c', 'b'}, only the UNIQUE elements. 

if (1 in s1):
    print(s1)
else: 
    print(s2)


#---------------------------------------------------------
# WHILE loop: enter a particular value to terminate
#---------------------------------------------------------
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """

print(prompt)

number = 0
while number != 4:   
    print(prompt)
    number = int(input())   # this WHILE loop stops only when the user enters an integer of '4' in the command window.

#---------------------------------------------------------
# WHILE loop: a more realistic example, a coffee machine
#---------------------------------------------------------

# coffee.py
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

# CONTINUE: How to return to the beginning of a WHILE loop
# The loop below starts at a=0, and it prints increasing odd numbers (1,3,5,7,9) until a=10 (loop breaks)
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

