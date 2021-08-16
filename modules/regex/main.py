import re

text = '3&22, 222&22, 322&19, 2222&222'
print(re.search(r'\d{3}&\d{2}', text))
print(re.findall(r'\d{3}&\d{2}', text))
for match in re.finditer(r'\d{3}&\d{2}', text):
    print(match)
