def solution(h, q):
    # Your code here
    result = []
    
    for node in q:
        
        tmp = traverse(h,node)
        result.append(tmp)
        
    return result


def traverse(h,node):
    
    #if the node less than 2^(h-1), it's on left
    #on the right otherwise
    
    root = 2**h - 1
    level = h-1
    if root == node:
        return -1

    while(level>=1):

        right = root -1
        left = right - (2**level-1)
        if node == right or node == left:
            return root
        
        if node < left:
            root = left
        elif node >left:
            root = right
        level -= 1
        
    return 0
