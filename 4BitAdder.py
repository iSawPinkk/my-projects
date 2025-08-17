# a=int(input('a:'))
# b=int(input('b:'))
# cin=int(input('cin:'))
# sum_=a^b^cin
# cout=(a&b)|(b&cin)|(a&cin)
# print(str(cout)+str(sum_))

# for A in [0,1]:
#     for B in [0,1]:
#         for C in [0,1]:
#           sum_=A^B^C
#           cout=(A&B)|(B&C)|(A&C)
#           print(str(cout)+str(sum_))

cout=0
sum_=0
result=''
def adder(a,b,c):
    sum_ = a ^ b ^ c
    cout=(a&b)|(b&c)|(a&c)
    return sum_, cout
A=format(int(input('number1:')),'04b')
B=format(int(input('number2:')),'04b')
A_=[A[3],A[2],A[1],A[0]]
B_=[B[3],B[2],B[1],B[0]]
for i in range(4):
    sum_,cout=adder(int(A_[i]),int(B_[i]),int(cout))
    result=str(sum_)+str(result)
result=(str(cout)+str(result))
print(str(int(result,2))+'(decimal)='+result+'(binary)')



