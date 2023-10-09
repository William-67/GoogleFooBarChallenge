def solution(n):
    # Your code here

    num = int(n)
    count = 0

    while num > 1:

        if num %2 == 0:

            num//=2

        else:

            if num == 3 or (num-1) % 4 == 0:
                num-=1
            else:
                num+=1

        count+=1

    return count

#recursive reach max so the solution has to be using iterator    
#     return division(int(n),0)
    
# def division(n,count):
    
#     #two possible path exist
#     #choose the path which is still even after divided

#     if n==1:
#         return count

#     if n%2==0:
#         return division(n//2,count+1)
#     else:
#         if n==3 or (n-1) % 4 ==0:
#             return division(n-1,count+1)
#         else:
#             return division(n+1,count+1)

print(solution(str(10**309-1)))