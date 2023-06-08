slova = []
while (nslovo := str(input())) != "stop":
    if "ф" in nslovo or "Ф" in nslovo:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

