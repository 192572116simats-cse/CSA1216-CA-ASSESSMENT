import struct

def ieee(value):
    bits = struct.unpack("!I", struct.pack("!f", value))[0]

    sign = bits >> 31
    exponent = (bits >> 23) & 255
    fraction = bits & 0x7FFFFF

    return sign, exponent, fraction


a = 100000000.0
b = 0.000001

sa, ea, fa = ieee(a)
sb, eb, fb = ieee(b)

print("A:", a)
print("Sign:", sa)
print("Exponent:", ea)
print("Fraction:", format(fa, "023b"))

print("\nB:", b)
print("Sign:", sb)
print("Exponent:", eb)
print("Fraction:", format(fb, "023b"))

print("\nSingle Precision Result:", struct.unpack(
    "!f", struct.pack("!f", a + b))[0]
)

print("Double Precision Result:", a + b)
