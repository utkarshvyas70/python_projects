#Get a email id as a input from user.

emailId=input("Enter your eamil id: ")

#Now commanding to sort the email id till @.

username=emailId[:emailId.index("@")]

#Now commanding to sort the eamil id after @.
domain=emailId[emailId.index("@")+1:]

#print the statement using format method.

print(f"Your desired username is {username} and your desired domain is {domain}")
