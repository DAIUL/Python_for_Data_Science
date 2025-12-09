def count_in_list(lst, word):
    return sum(1 for w in lst if w == word)
