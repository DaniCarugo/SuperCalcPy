import functions as f
glob_arg=[]
std_operator={"+": f.sum, "-": f.sub, "*":f.mol, "/": f.div}

def catasta(args, operators):
    #aspetto un input
    while(True):
        new_arg=input("> ")
        #se è un operatore
        if new_arg in operators:
            #esegui la relativa funzione
            result=operators[new_arg](*list(map(int, args)))
            print("------------------------------------")
            print("> " + str(result))
            args=[result] 
        #se è un numero aggiungilo agli altri
        else:
            args.append(new_arg)
        
catasta(glob_arg, std_operator)
