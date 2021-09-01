import math

def primeproduct(num):
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num /= i
            cnt += 1
            
        if cnt >= 2:
            break
    if(num > 1):
        cnt += 1
        return cnt == 2
    if cnt==2:
        return True
    return False
        
    # if primeproduct() == True:
    #     return True
    # else:
    #     return False

# def primeproduct(m):
#     l = []
#     # if m>0:
#     for i in range(2, m):
#             if m % i == 0:
#                 l += [i]
#     if len(l) == 2:
#         if l[0]*l[1] == m:
#             if l[1]%l[0] == 0:
#                 return False
#             else:
#                 return True
#         elif len(l) == 1:
#             if l[0]*l[0] == m:
#                 return True
#             return False
#         else:
#             return False
#     # else:
#     #     return False



print(primeproduct(188))
