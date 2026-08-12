def restoring(dividend, divisor, bits=8):
    A = 0
    Q = dividend

    print("RESTORING DIVISION")

    for i in range(bits):
        A = (A << 1) | ((Q >> 7) & 1)
        Q = (Q << 1) & 255
        A -= divisor

        if A < 0:
            A += divisor
        else:
            Q |= 1

    print("Quotient:", Q)
    print("Remainder:", A)


def non_restoring(dividend, divisor, bits=8):
    A = 0
    Q = dividend

    print("\nNON-RESTORING DIVISION")

    for i in range(bits):
        A = (A << 1) | ((Q >> 7) & 1)
        Q = (Q << 1) & 255

        if A >= 0:
            A -= divisor
        else:
            A += divisor

        if A >= 0:
            Q |= 1

    if A < 0:
        A += divisor

    print("Quotient:", Q)
    print("Remainder:", A)


restoring(20, 3)
non_restoring(20, 3)
