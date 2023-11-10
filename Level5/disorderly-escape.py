from collections import deque 
import copy


def solution(w, h, s):
    # Your code here

    diff = 0
    eqv_list = []

    if w == 1 and h == 1:
        return str(s)

    matrix = [[0 for _ in range(w)] for _ in range(h)]

    total_matrices = s**(w * h)  # Total number of possible matrices

    for count in range(total_matrices):

        # Fill the matrix with values based on the count in base s
        current_count = count

        for i in range(h):

            for j in range(w):

                matrix[i][j] = current_count % s
                current_count //= s

                matrix_copy = copy.deepcopy(matrix)

                if matrix_copy not in eqv_list:

                    diff += 1

                    add_all_eqv(matrix_copy,eqv_list)

    return str(diff)

def add_all_eqv(matrix, eqv_list):

    queue = deque()

    queue.append(matrix)

    eqv_list.append(matrix)

    for r1 in range(len(matrix[0])-1):

        for r2 in range(r1+1,len(matrix[0])):
                
            tmp = switch_columns(matrix,r1,r2)

            if tmp not in eqv_list:

                eqv_list.append(tmp)

                queue.append(tmp)

    for r1 in range(len(matrix)-1):

        for r2 in range(r1+1, len(matrix)):

            tmp = switch_rows(matrix, r1,r2)

            if tmp not in eqv_list:

                eqv_list.append(tmp)

                queue.append(tmp)

    while queue:

        tmp_matrix = queue.popleft()

        for r1 in range(len(tmp_matrix[0])-1):

            for r2 in range(r1+1,len(tmp_matrix[0])):

                tmp = switch_columns(tmp_matrix,r1,r2)

                if tmp not in eqv_list:

                    eqv_list.append(tmp)

                    queue.append(tmp)


        for r1 in range(len(tmp_matrix)-1):

            for r2 in range(r1+1, len(tmp_matrix)):

                tmp = switch_rows(tmp_matrix, r1,r2)

                if tmp not in eqv_list:

                    eqv_list.append(tmp)

                    queue.append(tmp)

    return 0


def switch_rows(matrix,r1,r2):

    tmp = copy.deepcopy(matrix)

    tmp[r1], tmp[r2] = tmp[r2], tmp[r1]

    return tmp


def switch_columns(matrix, c1, c2):

    tmp = copy.deepcopy(matrix)

    for row in tmp:

        row[c1], row[c2] = row[c2], row[c1]

    return tmp


print(solution(2, 2, 2))
print(solution(2, 3, 4))





# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# # m1 = switch_rows(matrix, 0, 2)
# # for row in m1:
# #     print(row)


# # m2 = switch_columns(matrix, 0, 2)
# # for row in m2:
# #     print(row)

# # eqv_list = []
# # add_all_eqv(matrix,eqv_list)
# # print(eqv_list)


# # s = [504,315]
# # def ad(s):
# #     s.append(194)
# # ad(s)

# # print(s)
