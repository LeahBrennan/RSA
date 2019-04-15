from Crypto.PublicKey import RSA


f = open('mykey3')
key = RSA.import_key(f.read())
e = key.e
n = key.n
d = key.d
p = key.p
q = key.q
print("ZD" + "{"+ str(n)+ ", "+ str(e)+ "," + str(d)+ ", " + str(p) + "," + str(q)  + "}")

#For date of code presentation: adding the pycryptodome module worked in PyCharmEdu.
