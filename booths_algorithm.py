def booth(m, q, bits=8):
    M = m & 255
    Q = q & 255
    A = 0
    Q_1 = 0

    for i in range(bits):
        pair = (Q & 1) * 2 + Q_1

        if pair == 1:
            A = (A + M) & 255
            print("01 -> A = A + M")
        elif pair == 2:
            A = (A - M) & 255
            print("10 -> A = A - M")
        else:
            print("00/11 -> No operation")

        Q_1 = Q & 1
        sign = A & 128

        Q = (Q >> 1) | ((A & 1) << 7)
        A >>= 1

        if sign:
            A |= 128

        print("A =", format(A, "08b"), "Q =", format(Q, "08b"))

    result = (A << 8) | Q

    if result & (1 << 15):
        result -= 1 << 16

    print("Final Result:", result)


booth(-7, 3)
