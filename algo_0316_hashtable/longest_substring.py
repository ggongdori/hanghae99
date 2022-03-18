# from collections import defaultdict

s = 'pwwkew'

rep = {}
ans = start = 0
for i, c in enumerate(s):


    if c in rep and start <= rep[c]:
        start = rep[c] + 1
    else:
        ans = max(ans, i - start + 1)
    rep[c] = i
print(ans)

#2

i, longest, seen = 0, 0, set()
for c in s:
    while c in seen:
        #If c is in seen, continue to remove letters from the beginning until we remove c
        seen.remove(s[i])
        i += 1
    #Add c to set of seen numbers
    seen.add(c)
    ans = max(longest,len(seen))
print(ans)

#3

# dic will store our current unique values
dic = {}

# Our left pointer
left = 0

# Longest will store the current longest substring of unqiue values
longest = 0

# The index will be our right pointer
for right in range(len(s)):

    # While a repeated value is in dictionary we're going to iterate until we have unqiue values again
    while s[right] in dic:
        leftVal = s[left]
        del dic[leftVal]

        left += 1
    # We add our unique value to our dictionary
    dic[s[right]] = True

    # The longest global substring is compared to the newly formed dictionary
    longest = max(longest, len(dic))

# Return the length of the longest substring
print(longest)