def add(a, b):
    bits = 8
    mask = 255

    A = a & mask
    B = b & mask
    R = (A + B) & mask

    print("A :", format(A, "08b"))
    print("B :", format(B, "08b"))
    print("R :", format(R, "08b"))

    overflow = ((A ^ R) & (B ^ R) & 128) != 0

    if R & 128:
        result = R - 256
    else:
        result = R

    print("Result:", result)
    print("Overflow:", overflow)


add(120, 50)
