def NRmethod(init_approx : float):
    present_x = init_approx
    epsilon = 0.00001
    # print(present_x)
    fx = (present_x ** 3) - (5 * present_x) + 1
    diff = (3 * present_x ** 2) - 5
    nextx = present_x - fx / diff
    i = 1

    while abs(present_x - nextx) > epsilon and i < 100:
        print(f'{i} iteration: {nextx}')
        i += 1
        present_x = nextx
        fx = (present_x ** 3) - (5 * present_x) + 1
        diff = (3 * present_x ** 2) - 5
        nextx = present_x - fx / diff

    print(f'{i} iteration: {nextx}')


def CBmethod(init_approx: float):
    present_x = init_approx
    epsilon = 0.00001

    fx = (present_x ** 3) - (5 * present_x) + 1
    diff = (3 * present_x ** 2) - 5
    diff2 = 6 * present_x
    nextx = present_x - ((fx / diff) - (0.5 * (fx ** 2 / diff ** 3)) * diff2)
    # nextx = present_x - ((fx / diff) - (0.5 * (fx / diff)**2) * (diff2/diff) )

    # print(fx, diff, diff2, nextx)
    i = 1

    while abs(present_x - nextx) > epsilon and i < 100:
        print(f'{i} iteration: {nextx}')
        i += 1
        present_x = nextx
        fx = (present_x ** 3) - (5 * present_x) + 1
        diff = (3 * present_x ** 2) - 5
        diff2 = 6 * present_x
        nextx = present_x - ((fx / diff) - (0.5 * (fx ** 2 / diff ** 3)) * diff2)
        # nextx = present_x - ((fx / diff) - (0.5 * (fx / diff) ** 2) * (diff2 / diff))

    print(f'{i} iteration: {nextx}')


print(".....Chebyshev method......")
CBmethod(0.5)
print(".....Newton-Raphson method......")
NRmethod(0.5)
