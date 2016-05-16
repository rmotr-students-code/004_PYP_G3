user = "sarah@gmail.com"
free_emails = ["john@hotmail.com", "mary@gmail.com", "joe@live.com"]

found = False
for email in free_emails:
    if email == user:
        print("User FREE")
        found = True
        break

if not found:
    print("Whatever we had before in the else statement")
