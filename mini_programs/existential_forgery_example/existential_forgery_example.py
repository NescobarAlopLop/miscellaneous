# from https://samsclass.info/141/proj/pCH-EFA.htm
import binascii


msg = bytearray("Project 16 from YOURNAME", 'utf8')
xe = msg.hex()
print(xe)
print(len(xe))


# Signing the Message
# public key
n = int("E37997C9E11A476DECD8C08A95E4DA3BF5E7A5DC2CCD4F02FCB34423BF0332F569A7E34EEA321C3844FC069F6DB2A59E1061E60445748"
        "67796CEA7B1A4252FE1", 16)
e = int("010001", 16)

# private key
d = int("8CEB8EF529D6B5D98B98DBEEFEDD3FB555A9A43EBA2296882B34834A01D361852C4E4D8338BCBE9A3A96F42F3AEF1F8282EF24F10743B"
        "4DC61844C4F98B2C7E1", 16)


x = int(xe, 16)
signature = pow(x, d, n)
signature_hex = hex(signature)
print("signature on \"{}\":\n\t{}".format(msg, signature_hex))


# Verifying the Signature
xpn = pow(signature, e, n)
print("Numerical x':", xpn)
xph = hex(xpn)
print("Hexadecimal string x':", xph)
xpt = xph[2:]
print("Trimmed hex string x':", xpt)
xpa = binascii.unhexlify(xpt)
print("ASCII x':", xpa)

print("n in hex {}\n".format(hex(n)))

# Performing the Existential Forgery Attack
signature = 0xf
xn = pow(signature, e, n)
xh = hex(xn)
print("Hexadecimal string x:", xh)
xt = xh[2:]
print("Trimmed hex string x:", xt)
xa = binascii.unhexlify(xt)
print("ASCII x':", xa)

# Verifying the Forged Signature
xpn = pow(0xf, e, n)
xph = hex(xpn)
print("Hexadecimal string x':", xph)
print("Hexadecimal string x :", xh)

print("n in hex", hex(n))
