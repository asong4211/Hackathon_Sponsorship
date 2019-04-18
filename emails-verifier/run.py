from validate_email import validate_email
import sys



def email_verifier(email):
    mx_valid = validate_email(email,check_mx = True)
    email_exist = validate_email(email, verify= True)
    if mx_valid and email_exist:
        print("Email:", email, "exists!")
    else:
        print("Email:", email, "does not exist!")


if(len(sys.argv) >= 2):
    # reading input
    input = sys.argv[1]
    email_verifier(input)
