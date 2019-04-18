m = 52544240263489213319521825334419419391168959946460651046808951093331580864925337576823646249202867381357303129957
print(hex(m))

print(bytearray.fromhex(hex(m).split('x')[1]).decode())

'''
Bibliography:
BOAKGP (2017), ‘CTF-Writeups/PicoCTF 2017/ Level 3/ Cryptography/ Broadcast/ main.py’,
github, 25 June 2018, 
Available at: https://github.com/BOAKGP/CTF-Writeups/blob/master/PicoCTF%202017/Level%203/Cryptography/Broadcast/main.py
(Accessed 28 February 2019).

'''
