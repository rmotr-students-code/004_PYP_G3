l = ["hello", "world", "banana"]


def has_5_chars(x):
    if len(x) == 5:
        return True
    else:
        return False

# filter: function, list(str) > list(str) (shorten) (just the ones with 5 chars)
# function: (str) > (Boolean) True or False

# words_with_5_chars = filter(has_5_chars, l)


# [elem for elem in list CONDITION]
res = map(len, filter(lambda x: len(x) == 5, l))

res = [len(x) for x in l if len(x) == 5]