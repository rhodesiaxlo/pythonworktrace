"""
展示变量的作用
"""
a  = 2

if a > 1:
    b = 3

d = 2;

def calc(tmp):
    b = 4
    print("d=",d)

def calc2(tmp):
    global b
    b = 5
    d = tmp
    print("d=", d)

#test case 1
calc(10)
print(b)
#output 3


#test case 2 ,use global var inside a funciton
calc2(10)
print(b)
