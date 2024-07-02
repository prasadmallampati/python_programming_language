#local variable
def local_example():
    a=10  # local variable
    print(f'calling inside function={a}')
#calling function
local_example()
# the below statement get error
# print(f'outside function {a}')