import re
phNumRegex = re.compile(r"\d\d-\d{10}")
mo = phNumRegex.search("My Number is 91-8888888888.")
print("Phone Number found:"+mo.group())
