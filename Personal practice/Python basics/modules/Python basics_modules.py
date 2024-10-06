#---------------------------------------------------------------#
# Modules: Python files of methods, variables, and/or classes
#---------------------------------------------------------------#

# Create a module
# Created a "mod1.py" under a subdirectory, "C:\Users\handa\OneDrive\Desktop\PhD progress\datawork\doit"


#-------------------------------------------------------------------------------------------
# Call a module (within the same folder)

# First, change working directory to "modules" folder under "Python basics"
# Put both this script and "mod1.py" script within the "modules" folder
# Run in the terminal: cd "C:\Users\handa\OneDrive\Desktop\PhD progress\datawork\Personal practice\Python basics\modules"
# Run in the terminal: See what's in the directory, run "dir" to ensure I'm in the correct working directory
# then run the following 

import mod1          # import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
print(mod1.add(3,4)) # returns 7
print(mod1.sub(5,3)) # returns 2






#-------------------------------------------------------------------------------------------
# The meaning of [ if __name__ == "__main__" ]



#-------------------------------------------------------------------------------------------
# A module with a class or variables




#-------------------------------------------------------------------------------------------
# Call a module from another file (within the same directory)




#-------------------------------------------------------------------------------------------
# Call a module from another file (from another directory)
# - use: sys.path.append
# - use: PYTHONPATH

