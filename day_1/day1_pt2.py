from collections import defaultdict

def get_lines(list1, list2):
    with open('input.txt', 'r') as file:
        for line in file:
            line_split = line.split()
            list1.append(line_split[0])
            list2.append(line_split[1])

def get_similarity(list1, list2):
    repeat_map = defaultdict(int) 
    
    for loc in list2:
        repeat_map[loc] += 1 

    similarity_score = 0
    for loc in list1:
        similarity_score += (int(loc) * repeat_map[loc])

    return similarity_score 

list1, list2 = [], []
get_lines(list1, list2)
score = get_similarity(list1, list2)
print(score)
