'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# use recursion to iterate thru word
# check if first two index values are = th
# if yes + 1
# slice the first two values and repeat


def count_th(word):
    range = len(word)
    value = 0
    if range < 2:
        return 0
    if word[:2] == 'th':
        return count_th(word[1:]) + 1
    return count_th(word[1:])


test = 'th-th-th-ab'
print(count_th(test))
