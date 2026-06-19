a='abc'
b='ACB'
a=a.lower()
b=b.lower()
if sorted(a)==sorted(b):
    print('anagram')
else:
    print('not anagram')
