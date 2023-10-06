def solution(n, b):
    #Your code here
    
    al_list = []

    while True:
        
        result = subtraction(n,b)

        if result == 0:
            return 1
        
        al_list.append(result)
        
        flag = checkDuplicate(al_list)

        if flag != None:
            return flag

        n = result


    return 1

def one_bit_sub(a,b,carry,n):
    #return result and carry
    if a < b + carry :
        return (a-b-carry)%n, 1
    else:
        return (a-b-carry)%n, 0

def subtraction(number, n):
    #perform all bits subtraction 
    y = sorted_str = ''.join(sorted(str(number)))
    x = sorted_str = ''.join(sorted(str(number), reverse=True))

    carry = 0
    result = ''
    for i in range(len(str(number))-1,-1,-1):
        tmp, carry = one_bit_sub(int(x[i]), int(y[i]), carry, n)
        result = str(tmp) + result
    return int(result)

def checkDuplicate(alist):

    for i in range(len(alist)-1):
        for j in range(i+1,len(alist)):
            if alist[i] == alist[j]:
                return j-i

#testcase

a_num = subtraction(202012,3)
print(a_num)

print(checkDuplicate([4789,456]))
print(solution(1211,10))
