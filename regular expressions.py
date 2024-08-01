######Regular Expressions################


import re

##Search()
# import re
message = "i like football"
x = re.search("f", message)
print(x.start())


##findall()
# import re
message = "hagi is the perfect footballer. hagi is from romania"
a = re.findall("hagi", message)
print(a)


##split()
# import re
message = "i like football"
x = re.split("\\s", message)
print(x)

# import re
message = "i like football volleyball basketball"
x = re.split("\\s", message)
print(x)


##sub()
# import re
message = "i like football"
x = re.sub("\\s","-", message)
print(x)


# import re
message = "i like football"
x = re.sub("\\s","-", message,1)
print(x)


pattern = "Python"
text = "i write code in python"
match = re.search(pattern, text)
print("match found::", bool(match))


pattern = "a"
text = "i love to code in python and its amazing"
matches = re.findall(pattern, text)
print("matches found::", len(matches))

pattern = "\s"
text = "i like python and it is amazing"
split_text = re.split(pattern, text)
print("split_text", split_text)

##string replacement
pattern = "python"
replacement = "java"
text = "python is fun"
substituted_text = re.sub(pattern, replacement, text)
print("replacement is::", substituted_text)


##using * to match zero or more occurances of a character
pattern = "py.*n"
count = 0
text = ["python coding", "pyt3on", "java", "py45n", "py@#n", "pyn"]
for i in text:
    if(re.findall(pattern, i)):
        count+=1
print("matches found::", count)

##using + to match one or more occurances of a character
pattern = "py.+n"
count = 0
text = ["python coding", "pyt3on", "java", "py45n", "py@#n", "pyn"]
for i in text:
    if(re.findall(pattern, i)):
        count+=1
print("matches found::", count)



##using ? to match zero or one occurances of a character
pattern = "py.?n"
count = 0
text = ["python coding", "pyt3on", "java", "py45n", "py@h#n", "pynn", "pyhn", "pyn"]
for i in text:
    if(re.findall(pattern, i)):
        count+=1
print("matches found::", count)


##Using [] to create a character set

pattern = "[Pp]ython"
text = "I write code in python and Python!"
matches = re.findall (pattern, text)
print("Matches found",len(matches))

##using {} to specify the number of occurances of a character
pattern = "py{1,2}n"
text = "i love pyn, pyyn and pyyyn"
matches = re.findall(pattern, text)
print("matches found::", len(matches))


##using \d to match dugits
pattern = "\d+"
text = "my phone number is 123-456-7890"
matches = re.findall(pattern, text)
print(matches)
print("matches found::", len(matches))


##using \w to find alphanumeric characters
pattern = "\w+"
text = "i_love_python !"
matches = re.findall(pattern, text)
print(matches)
print("matches found::", len(matches))


##using \s to mmatch whitespace character
pattern = "\s+"
text = "i love python"
matches = re.findall(pattern, text)
print("matches found::", len(matches))

##using | as an OR operator
pattern = "python|java"
text = "i write code python and java"
matches = re.findall(pattern, text)
print("matches found::", matches)
print(len(matches))

##using() to group operators
pattern = "(\d{3})-(\d{3})-(\d{4})"
text = "my phone number is 123-456-7890"
match = re.search(pattern,text)
if match:
    print("area code::", match.group(1))
    print("local exchange::", match.group(2))
    print("line number::", match.group(3))





