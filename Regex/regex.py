import re
file = open('C:/Users/aasmi/Desktop/SEM 5/PYTHON/Regex/sample.txt')
text = file.read() 
pattern_name = r'M\w*.\s*\w*\s*\w*[\n]'
pattern_email = r'[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+'
patterm_phone = r'[0-9]+[#\-*]+[0-9]+[#\-*+]'
pattern_username = r'\S+.@'
pattern_domain =r'@\S+.'

names_in_text = re.findall(pattern_name,text)
names = []
for i in names_in_text:
    names.append(i)

for name in names:
    print(name)

emails_in_text = re.findall(pattern_email,text)
emails = []
for i in emails_in_text:
    emails.append(i)

for email in emails:
    print(email)

usernames = re.findall(pattern_username, ' '.join(emails))
domains = re.findall(pattern_domain, ' '.join(emails))
print("Usernames and domains of each of the email addresses are:")
for i, j in zip(usernames, domains):
    print("User Id.: ", i[:-1], "; Domain: ", j[1:], sep="")
print()

phone_numbers = re.findall(patterm_phone,text)
for i in phone_numbers:
    print(i)

