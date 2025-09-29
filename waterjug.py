def water_jug():
    a = 0
    b = 0
    print("Start: A =", a, ", B =", b)

    b = 5
    print("Fill B: A =", a, ", B =", b)

    transfer = min(b, 3 - a)
    b = b - transfer
    a = a + transfer
    print("Pour B -> A: A =", a, ", B =", b)

    a = 0
    print("Empty A: A =", a, ", B =", b)

    transfer = min(b, 3 - a)
    b = b - transfer
    a = a + transfer
    print("Pour B -> A: A =", a, ", B =", b)

    b = 5
    print("Fill B: A =", a, ", B =", b)

    transfer = min(b, 3 - a)
    b = b - transfer
    a = a + transfer
    print("Pour B -> A: A =", a, ", B =", b)

    print("Final: A =", a, ", B =", b)
    if a == 4 or b == 4:
        print("Reached 4 liters!")

water_jug()
