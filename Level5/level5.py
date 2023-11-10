
def factorial(n):
    if n == 0:
        return 1
    result = 1

    for i in range(1, n+1):
        result *= i
    return result

def gcd(a,b):

    if b > a:
        a,b = b,a

    while b:
        a,b = b, a % b
    return a

def cycle_count(c, n):

    result = factorial(n)
    unique_lengths = set(c)

    for length in unique_lengths:
        count = c.count(length)
        result //= (length ** count) * factorial(count)
    return result     

def partition_combinations(n):
    def generate_partitions(n, current_partition):
        if n == 0:
            partitions.append(current_partition)
            return
        if n < 0:
            return

        for i in range(1, n + 1):
            if not current_partition or i >= current_partition[-1]:
                generate_partitions(n - i, current_partition + [i])

    partitions = []
    generate_partitions(n, [])
    return partitions


def solution(w, h, s):
    # Your code here    
    total=0
    width_partition = partition_combinations(w)
    height_partition = partition_combinations(h)

    for widthcom in width_partition:

        for heightcom in height_partition:    

            countAll =cycle_count(widthcom, w) * cycle_count(heightcom, h)

            gcdsum = 0

            for i in widthcom:
                for j in heightcom:
                    gcdsum += gcd(i,j)

            total += (s**gcdsum) * countAll
              
    return str(total //(factorial(w) * factorial(h)))

print(solution(2,2,3))



n = 5
combinations = partition_combinations(n)
print(combinations)
