#---------------------------------------------------------------#
# Modules: Python files of methods, variables, and/or classes
#---------------------------------------------------------------#

# Create a module
# Created a "mod1.py" under a subdirectory, "C:\Users\handa\OneDrive\Desktop\PhD progress\datawork\doit"


#-------------------------------------------------------------------------------------------
# Call a module frmo another file (within the same folder)

# First, change working directory to "modules" folder under "Python basics"
# Put both this script and "mod1.py" script within the "modules" folder
# Run in the terminal: cd "C:\Users\handa\OneDrive\Desktop\PhD progress\datawork\Personal practice\Python basics\modules"
# Run in the terminal: See what's in the directory, run "dir" to ensure I'm in the correct working directory

# Then, run the following by running import <module_name>:
import mod1          # import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
a = mod1.add(3,4)
b = mod1.sub(5,3)
print(a) # calls add() from mod1.py, returns 7
print(b) # calls sub() from mod1.py, returns 2

# A cleaner way that allows PARTIAL IMPORT of methods:
from mod1 import add, sub    # imports add() and sub() from mod1.py
c = add(3,4)
d = sub(5,3)
print(c)  # returns 7
print(d)  # returns 2

# Alternative way that imports ALL methods from a module:
from mod1 import *
e = add(3,4)
f = sub(5,3)
print(e)  # returns 7
print(f)  # returns 2


#-------------------------------------------------------------------------------------------
# The meaning of [ if __name__ == "__main__" ]

# 모듈 안에 if __name__ == "__main__"을 사용하면 C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는
# __name__ == "__main__"이 참이 되어 if 문 다음 문장이 수행된다. 

# 이와 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러 사용할 때는
# __name__ == "__main__"이 거짓이 되어 if 문 다음 문장이 수행되지 않는다.





#-------------------------------------------------------------------------------------------
# A module with a class or variables








#-------------------------------------------------------------------------------------------
# Call a module from another file (from another directory)
# - use: sys.path.append
# - use: PYTHONPATH

