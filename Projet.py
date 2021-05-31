def verif(ch):
    if(2<len (ch)<11):
        test=True
        i=0
        while(((test) and (i<len(ch)))):
            test= ((ord(ch[i])<123) and (ord(ch[i])>96))
            i=i+1
        return(test)
    else:
        return(False)
    
def position(l,char):
    j=0
    while (j in range(len(l))):
        if (l[j]==char):
            return j
        else:
            j+=1

def dessiner(d):
    if(d==1):
        f=open('dessin.txt',"w")
        f.write("_|_")
        f.close()
    elif((d==2) or (d==3)):
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        for i in range(2):
           s=" |\n"
           l[0:0]=s
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()    
    elif(d==4):
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        s=" _ _\n"
        l[0:0]=s
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()
    elif(d==5):
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        s=" _ _ _ _ \n"
        l[0:1]=s 
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        s=" |    |\n"
        l[1:2]=s
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()
    elif(d==6):
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        s=" |    o\n"
        l[2:3]=s
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()
    elif(d==7):
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        s=" |    |\n"
        l[3:4]=s
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()
    elif(d==8):
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        s=" |   /|\n"
        l[3:4]=s
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()
    elif(d==9):
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        s=" |   /|\ \n"
        l[3:4]=s
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()
    elif(d==10):
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        s=" |   / \n"
        l[4:5]=s
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()
    else:
        file=open('dessin.txt',"r")
        l=file.readlines()
        file.close()
        s=" |   / \ \n"
        l[4:5]=s
        file2=open('dessin.txt',"w")
        file2.writelines(l)
        file2.close()
           
        
def affiche(a,char):
    l1[a]=char
    j=0
    ch1=""
    for j in range(len(l1)):
        ch1=ch1+l1[j]
    return(ch1)
def affiche_dessin():
    f=open('dessin.txt',"r")
    print(f.read())
    f.close()

    
if __name__=='__main__':
    import os
    ch=input("ecrire un mot ")
    t=verif(ch)
    if (t==False):
        while(t==False):
            print("\t \t *** Le mot ne peut comprendre que des lettres minuscules et de taille entre 3 et 10***")
            ch=input("ecrire un mot ")
            t=verif(ch) 
    os.system('cls')
    ch1=""
    for i in range(len(ch)):
        ch1=ch1+"-"
    print("le jeu commence...")
    print(""" \t \t REMARQUE: Le mot ne contient que des lettres en minuscule! \n \t \t \t *** BONNE CHANCE *** """)
    print(ch1)
    l1=list(ch1)
    l2=list(ch)
    test=True
    res=0
    i=0
    f=open('dessin.txt',"w")
    f.close()

    while ((i<12)and(test)):
        char=input("Votre choix: ")
        if (char in l2):
            print("  \t ---> *** C'EST VRAI ***IL VOUS RESTE {} FAUTES POSSIBLES!!!".format(11-i))
            res+=1
            test=res!=len(l2)
            x=position(l2,char)
            ch1=affiche(x,char)
            l2[x]="*"
            print('*')
            affiche_dessin()
            if (test==False):
                print("""\n *     ^^ vous avez gagné!!!
                            mot: {}""".format(ch))
            else:
                print('\n *',ch1)                
        else:
            print("  \t ---> *** C'EST FAUX ***IL VOUS RESTE {} FAUTES POSSIBLES!!! ".format(11-i))
            i+=1
            dessiner(i)
            print('*')
            affiche_dessin()
            if(i==12):
                print("""\n *     Perdu!!
                            Solution: {}""".format(ch))
            else:
                print('\n *',ch1)
    

   
   
    
    

        
    
    
