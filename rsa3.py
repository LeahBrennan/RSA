from Crypto.PublicKey import RSA


f = open('mykey2')
key = RSA.import_key(f.read())
e = key.e
n = key.n
d = key.d

print("ZD" + "{"+ str(n)+ ", "+ str(e)+ "," + str(d)+ "}")

#For date of presentation, importing pycryptodome worked on PyCharm Educational.
