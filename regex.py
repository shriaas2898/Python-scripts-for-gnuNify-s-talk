#Python code to search mobile number in supplied string through regex
import re #importing regex module
phNumRegex = re.compile(r"\d\d-\d{10}") #creating regex for phone number
mo = phNumRegex.search("My Number is 91-8888888888.") #searching regex in string
print("Phone Number found:"+mo.group())#printing all the matching results
