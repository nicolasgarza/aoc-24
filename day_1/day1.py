def get_lines(list1, list2):
    with open('input.txt', 'r') as file:
        for line in file:
            line_split = line.split()
            list1.append(line_split[0])
            list2.append(line_split[1])

def get_diff(list1, list2):
    list1.sort()
    list2.sort()
    
    diff = 0
    for l1, l2 in zip(list1, list2):
        diff += abs(int(l1) - int(l2))

    return diff

list1, list2 = [], []
get_lines(list1, list2)
diff = get_diff(list1, list2)
print(diff)
