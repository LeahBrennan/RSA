#Sourced from: https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49
#egcd has changed to egcd2 as similar code was used to solve level 5,both scripts were originally named egcd and egcd 2

p = 163598797232837275790583032413921422452851861145478369331976309880028992955089558380171554447759405365296693377570783300198791468861355639873166150884714034914366548252757855530548966926710596087588892893653952147784119788340592861717511574050564549916735627066568966135368285851889401719649796310308064172229

q =  151928351783926490385254692544226090032004315756120674902384041799040568083955129227360764179393042678005292005933989750269377019057534023167675372696224003953154715102625798599561576746593076228704448522848509650863715575134525964992439285085243915010868628145127710442853766119688772555932018349278733467937



n = p*q
phi = (p-1)*(q-1)

# Took from SO-ofaurax
def egcd2(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd2(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd2(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

e = 65537

d = modinv(e, phi)

print('P =', p)
print('Q =', q)
print('N =', n)
print('Phi =', phi)
print('E =', e)
print('D =', d)
print('(E*D)%Phi =', (e*d)%phi)