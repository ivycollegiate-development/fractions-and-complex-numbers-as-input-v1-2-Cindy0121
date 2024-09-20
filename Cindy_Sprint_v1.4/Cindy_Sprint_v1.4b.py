try:
    z = complex(input("Please input a com;lex number, (ex: 2+3)"))
    print(z)
except ValueError:
    print("Incalid input. Please no spaces between a+b")