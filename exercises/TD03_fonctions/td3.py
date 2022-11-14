def tempsEnSeconde(temps):
    t = 24 * 3600 * temps[0] + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return t
temps=(3 , 23 , 1 , 34)
print(type(temps))
print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j = temps // 24*3600 
    return j
    temps = secondeEnTemps(100000)
print(temps[0] , "jours" , temps[1] ,"heures",temps[2],"minutes",temps[3],"secondes")



def afficheTemps(temps):
    if temps[0] > 1:
        print(temps[0],"jours",end=" ")
    elif temps[0] == 1 :
        print(temps[0],"jour",end=" ")
    if temps[1] > 1: 
        print(temps[1],"heures",end=" ")
    elif temps[1] == 1 :
        print(temps[1],"heure",end=" ")
    if temps[2] > 1:
        print(temps[2],"minutes",end=" ")
    elif temps [2] == 1 :
        print(temps[2],"minute",end=" ")
    if temps[3] > 1:
        print(temps[3],"secondes")
    elif temps[3] == 1:
        print(temps[3],"secondes")
   
afficheTemps((1,0,14,23))    


def demandeTemps(a):
    a[0]=int(input("Un nombre de jour"))
    if a[0] == 1:
        print(a[0], "jour",end=" ")
    else:
        print(a[0], "jours",end=" ")
    a[1]=int(input("Un nombre d'heure"))
    if a[1] > 23:
        print("Erreur",end=" ")
    elif a[1] == 1 :
        print(a[1], "heure",end=" ")
    else:
        print(a[1],"heures",end=" " )
    a[2]=int(input("Un nombre de minutes"))
    if a[2] > 59:
        print("Erreur",end=" ")
    elif a[2] == 1 :
        print(a[2], "minute",end=" ")
    else:
        print(a[2],"minutes",end=" " )
    a[3]=int(input("Un nombre de secondes"))
    if a[3] > 59:
        print("Erreur",end=" ")
    elif a[3] == 1 :
        print(a[3], "seconde",end=" ")
    else:
        print(a[3],"secondes",end=" " )
        



def sommeTemps(temps1,temps2):
    

sommeTemps((2,3,4,25),(5,22,57,1))
    

print(sommeTemps)


