m = 52544240263489213319521825334419419391168959946460651046808951093331580864925337576823646249202867381357303129957
print(hex(m))

print(bytearray.fromhex(hex(m).split('x')[1]).decode())
#Source: https://github.com/BOAKGP/CTF-Writeups/blob/master/PicoCTF%202017/Level%203/Cryptography/Broadcast/main.py
