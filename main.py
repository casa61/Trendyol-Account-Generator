import settings

mails = open("mails.txt", "r", encoding="utf8").read().split("\n")
PASSWORD = "107861ca"

for x in mails:
    settings.new_account(x,PASSWORD)
