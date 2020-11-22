from collections import defaultdict

def earliest_ancestor(ancestors, starting_node):
    parent_dictionary = defaultdict(list)
    
    for pair in ancestors:
        parent_dictionary[pair[1]].append(pair[0])


    if starting_node not in parent_dictionary:
        return -1

    def recursive_ancestor(child, level=0):

        if child not in parent_dictionary:

            return (child, level)
        else:
            candidates = []
            for parent in parent_dictionary[child]:
                candidates.append(recursive_ancestor(parent, level + 1))
            return sorted(candidates, key=lambda x: (x[1]), reverse=True)[0]
    return recursive_ancestor(starting_node)[0]

if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 9))