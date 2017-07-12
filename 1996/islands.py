# В двумерном массиве посчитать число
# Изолированных 0- областей

def in_one_part(array, all_find_in_one_part, i, j):
    """возвращает список [(k,l),..]
    таких, что  (k,l) и (i,j) лежат в одной
    области"""
    # all_find_in_one_part = []
    all_find_in_one_part.add((i,j))
    all_neighbors = [place for place in neighbors(i,j, len(array), len(array[0]))
                     if array[place[0]][place[1]] == 0
                     and not place in all_find_in_one_part]

    if len(all_neighbors) == 0:
        return all_find_in_one_part

    for place in all_neighbors:
        new_neighbors = in_one_part(array, all_find_in_one_part, place[0], place[1])
        all_find_in_one_part.union(set(new_neighbors))

    return all_find_in_one_part


def num_of_islands(array):
    num_of_part = 0
    for i, line in enumerate(array):
        for j, element in enumerate(line):
            if element == 0:
                num_of_part += 1
                places_in_part = in_one_part(array, {(i,j)}, i, j)
                for place in places_in_part:
                    array[place[0]][place[1]] = 1

    return num_of_part


def neighbors(i, j, n, m):
    b = []
    if i + 1 < n:
        b.append((i + 1, j))
    if i - 1 > 0:
        b.append((i - 1, j))
    if j + 1 < m:
        b.append((i, j + 1))
    if j - 1 > 0:
        b.append((i, j - 1))
    return b

array = [[1, 0, 1, 1],
         [1, 0, 0, 1],
         [1, 0, 1, 0],
         [0, 1 ,1 ,0]
         ]
print(in_one_part(array, set(), 0, 1))
print(num_of_islands(array))