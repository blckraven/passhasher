import hashlib

password = input("Input the text to hash:\n>")
print("Which hash function do You want to use: \n1. SHA1\n2. MD5\n3. SHA256\n4. SHA512\n")
choose = int(input("I choose (1/2/3/4): " ))
if choose == 1:
    print("\nSHA1:\n")
    for i in range(3):
        setpass = bytes(password, 'utf-8')
        hash_object = hashlib.sha1(setpass)
        guess_pw = hash_object.hexdigest()
        print(guess_pw)
if choose == 2:
    print("\nMD5:\n")
    for i in range(3):
        setpass = bytes(password, 'utf-8')
        hash_object = hashlib.md5(setpass)      
        guess_pw = hash_object.hexdigest()
        print(guess_pw)
if choose == 3:
    print("\nSHA256:\n")
    for i in range(3):
        setpass = bytes()(password, 'utf-8')
        hash_object = hashlib.sha256(setpass)
        guess_pw = hash_object.hexdigest()
        print(guess_pw)
if choose == 4:
    print("\nSHA512:\n")
    for i in range(3):
        setpass = bytes(password, 'utf-8')
        hash_object = hashlib.sha512(setpass)
        guess_pw = hash_object.hexdigest()
        print(guess_pw)
