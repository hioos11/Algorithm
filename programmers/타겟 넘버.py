def solution(numbers, target):
    tree = [0]
    for n in numbers:
        sub_tree = []
        for t in tree:
            sub_tree.append(t + n)
            sub_tree.append(t - n)
        tree = sub_tree
    return tree.count(target)