#input com impedimentos de valores invalidos e floats
while True:
    try:
        Height = int(input("How many layers do you want in your column?"))
        if Height <= 0 or Height == 9:
            print("type a valid value")
        else:
            break
    except ValueError:
        print("type a int number")

#piramide de hash com espaçamento duplo
x = str("#")

if Height == 9:
    for i in range (3):
        if i == 0:
            pass
        else:
            i+1
            j = 3 - i
            print(" "*j+ x*i+"  " +x*i)
else:
    for i in range(Height+1):

        if i == 0:
            pass

        else:
            i+1
            j = Height - i
            print(" "*j+ x*i+"  " +x*i)
