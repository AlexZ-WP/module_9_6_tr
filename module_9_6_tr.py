
# def all_variants(text):
#     for i in text:
#         yield i

# def all_variants(text):
#     for r in range(len(text)):
#         for j in range(r, len(text)):
#             yield text[r:j + 1]

def all_variants(text):
    for r in range(len(text)):
        for j in range(len(text)-r):
            yield text[j:j+r+1]


a = all_variants("abc")
for i in a:
    print(i)

text = 'abc'
print(len(text))


def subseq_rec(idx, curr, s, res):# Base case: If we've processed all characters,add current subsequence
    if idx == len(s):
        res.append(curr)
        return
    subseq_rec(idx + 1, curr + s[idx], s, res) # Include current character in subsequence
    subseq_rec(idx + 1, curr, s, res)# Exclude current character from subsequence
def all_subseq_rec(s):
    res = []
    subseq_rec(0, "", s, res)
    return res
s = "abc"
print(all_subseq_rec(s))