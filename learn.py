import re

# search(pattern, string): return a Match object. Match object has:  span(), string, group(), groups()
#      01234567890123456
txt = "The rain in Spain"      
x = re.search(r"\sS\w+", txt)  # return a Match object
print(x.start())               # => 11
print(x.end())                 # => 17
print(x.span())                # => (11, 17) (starting index, ending index) note: ending index is not included in search string. Just like a[2:5] index 5 is not in included

print(x.string)                # => The rain in Spain  (return the original string passed to search)
print(x.group())               # => " Spain" (there is a space before Spain. It is the pattern \sS\w+: \s-space, then S, then \w+: any word letter)

# group(?): match the parenthesis() string 
txt = "The price of PINEAPPLE ice cream is 20"
x = re.search(r"(\b[A-Z]+\b).+(\b\d+)", txt)       
print(x.group())   # PINEAPPLE ice cream is 20   ( the string matches the pattern)
print(x.groups())  # ('PINEAPPLE', '20')         ( tuple with (\b[A-Z]+\b) and (\b\d+) )
print(x.group(1))  # PINEAPPLE                   (1st parenthesis string match: (\b[A-Z]+\b) )
print(x.group(2))  # 20                          (2nd parenthesis string match: (\b\d+) )

# findall(pattern, string)
txt = "The rain in Spain"
x = re.findall("ai", txt)      # return a list of all occurance
print(x)                       # => ['ai', 'ai']

