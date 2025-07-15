def add(a,b):
    print(a+b)

def add_v2(a,b,c):
    print(a+b+c)

print(__name__)
#  when ruuning a.py the value of __name__ will be __main__
#  when we inport a in other file and run that file then __name__ will be a 

class A:
    def add(self):
        pass



# When we import this file completely in b 
#  like from a import *
#  and run b 
#  it will run all the functions of b without calling them 
#  for this we use if __name__ == "__main__":


if __name__ == "__main__":
    # __name__ == "a": --> when i import  file a in b 
    # __name__ == "__main__": --> when i run python a.py
    # Multiprocessing works inside this block only 
    #  When another file is using a.py "from a import *" it cannot run this code block because there __name__ is equal to "a"
    A()
    add(1,2)
    add_v2(1,2,3)