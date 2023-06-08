from random import randint
while true:
    a = randint(1, 100)
    b = randint(1, 100)
    print(f"{a} + {b} = ", end="")
    res = imput()
    while not res.isdigit() and res != "stop":
        print("something went wrong", end="")
        res = imput(
    if res == "stop":
        break
    res = int(res)
    if a+b == res:
        print("right!")
    else:
        print("wrong..")