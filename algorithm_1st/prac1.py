import sys
from collections import defaultdict
arr = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

def group_anagram(arr):
    ans = defaultdict(list)
    for w in arr:
        ans[''.join(sorted(w))].append(w)
    return list(ans.values())



print(group_anagram(arr))

