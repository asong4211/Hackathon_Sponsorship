from run import email_verifier
import sys



first = input("What's his/her first name? ").strip().lower()
middle = input("What's his/her middle name? Skip if you don't know ").strip().lower()
last = input("What's his/her last name? ").strip().lower()
domain = input("What's his/her company domain name? ").strip().lower()
if(not domain):
    print("You need his/her domain to run this program ")
    sys.exit()
if(not first and not last):
    print("You need at least the person's first or last name to run this program")
    sys.exit()

guess_emails = [];
def email_check(email):
    email = email.strip()
    temp = "{}@{}".format(email, domain)
    email_verifier(temp)

if(first and last and domain):
    email_check("{}.{}".format(first,last))
    email_check("{}_{}".format(first,last))
    email_check("{}{}".format(first[0],last))
    email_check("{}{}".format(first,last[0]))
    email_check("{}-{}".format(first,last))
    email_check("{}".format(last))
    email_check("{}".format(first))
if(first and last and domain and middle):
    email_check("{}.{}.{}".format(first,middle[0], last))
    email_check("{}_{}_{}".format(first,middle[0], last))
    email_check("{}.{}.{}".format(first, middle,last))
    email_check("{}_{}_{}".format(first, middle, last))
