print("Password Guesser 8009")
print("Type a 4 digit password and the computer will guess it :" )

userpass = input()
if userpass == int :
    print("try again")
correct_password = str(userpass)
for guess in range(10000) :
    attempt = str(guess).zfill(4)
    
    if attempt == correct_password :
        print("The password is",attempt)     
        print("Tries taken:", guess+ 1 )
