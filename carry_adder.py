def ripple_carry(a, b, bits=8):
    carry = 0
    result = 0

    print("RIPPLE CARRY ADDER")

    for i in range(bits):
        A = (a >> i) & 1
        B = (b >> i) & 1

        P = A ^ B
        G = A & B

        S = P ^ carry
        carry = G | (P & carry)

        result |= S << i

        print(f"Bit {i}: Carry = {carry}")

    print("Result:", result)
    print("Delay:", bits, "carry stages")


def carry_lookahead(a, b, bits=8):
    P = []
    G = []

    for i in range(bits):
        A = (a >> i) & 1
        B = (b >> i) & 1

        P.append(A ^ B)
        G.append(A & B)

    carry = [0] * (bits + 1)

    for i in range(bits):
        carry[i + 1] = G[i] | (P[i] & carry[i])

    result = 0

    for i in range(bits):
        result |= (P[i] ^ carry[i]) << i

    print("\nCARRY LOOK-AHEAD ADDER")
    print("Result:", result)
    print("Delay: Reduced using parallel carry calculation")


ripple_carry(120, 50)
carry_lookahead(120, 50)
