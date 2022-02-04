"""CalcPy by Daniele Carugo - Versione 1.1.1"""

import functions as f
import sys_func as sys_f
glob_arg=[]
std_operator={"+": f.sum, "-": f.sub, "*":f.mol, "/": f.div}

def canBeFloat(var):
    try:
        var=float(var)
        return True
    except Exception:
        return False

def launch(operators, operator):
    global glob_arg
    #esegui la relativa funzione
    result=operators[operator](*list(map(float, glob_arg)))
    print("------------------------------------")
    print("> " + str(result))
    glob_arg=[result]

def catasta(operators):
    global glob_arg 
    #aspetto un input
    while(True):
        new_arg=input("> ")
        #se è un operatore
        if new_arg in operators:
            #lancio la funzione
            launch(operators, new_arg)
        else:
            #se è un numero aggiungilo agli altri
            if canBeFloat(new_arg)== True:
                new_arg=float(new_arg)
                glob_arg.append(new_arg)

            else:
            #altrimenti controlla che ci sia un operatore (num+operatore)
                arg_part=0
                oper_part=""
                counter=-1

                for elem in new_arg:
                    if canBeFloat(elem) == True:
                        counter +=1
                    #salto il punto per i decimali
                    elif elem == ".":
                        counter +=1
                    else:
                        #dividi argomento in numero e operatore
                        arg_part=float(new_arg[:counter+1])
                        oper_part=new_arg[counter+1:]
                        #aggiungi l'argomento
                        glob_arg.append(arg_part)
                        #esegui operatore
                        if oper_part in operators:
                            launch(operators, oper_part)
                            break

catasta(std_operator)
