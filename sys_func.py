def cut(string, c):
    """Restituisce la parte numerica o testuale di una variabile"""
    counter=0
    for el in string:
        try:
            el=int(el)
            counter+=1

        except Exception:
            break
    if c=="text":
        print(string[counter:])
    else:
        print(string[:counter])

