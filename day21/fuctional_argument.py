# # def average(a,b):
# #     print("The average of two number ",(a+b)/2)
# #average(4,8)
# def average(a=9,b=8):
#     print("The average of two number ",(a+b)/2)
# #average(4,8)
def average(*number):
    sum=0
    for i in number:
        sum=sum+i
    print("Avrage is ",sum/len(number))
average(5,6,7,8,9)