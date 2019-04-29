# -*- coding: cp1252 -*-

import time
###############################     FONCTIONS AUXILIAIRES      ############################################

def alpha(n):
    
    alphabt='abcdefgh'
    
    return(alphabt[n])

def copie(d):
    cop=[[d[i][j] for j in range(8)] for i in range(8)]
    return(cop)

def inv(coul):

    if coul=='n':
        return('b')
    elif coul=='b':
        return('n')
    else:
        return('')

def traduc(cp):## traduction du coup entrer par l'utilisateur en int   traduc : char*char*char*char -> int
    	##(e2,e4)->[6,4,4,4]   ligne : numero   colonne : chiffre
	(l_d,c_d)=(cp[2],cp[1])
	(l_a,c_a)=(cp[5],cp[4])
	return([ 7-(ord(l_d)-49) , ord(c_d)-97 , 7-(ord(l_a)-49) , ord(c_a)-97 ])

def retraduc(cp):## traduction inverse [6,4,4,4]->(e2,e4)
    retour=[]
    l_d=chr(49+(7-cp[0]))
    c_d=chr(97+cp[1])
    l_a=chr(49+(7-cp[2]))
    c_a=chr(97+cp[3])
    retour.append(c_d)
    retour.append(l_d)
    retour.append(c_a)
    retour.append(l_a)
    return (retour)

#######################################  DEPLACEMENT DES PIECES   ######################################
    
def pion(dam, origine): ## cases controles par le piont en 'origine' -> tableau

    deplacement=[]##[(n ligne, n colonne), ... liste des coord attake...]
    (l,c)=(origine[0],origine[1])
    
    case_o = dam[l][c] ##POUR L'instant le pion n'arrive pas au bout!
    coul=case_o[3]

    if(coul == 'n' and l<7):
        
        case_h = dam[l+1][c]
        if(case_h[2] == ' '):
            deplacement.append((l+1,c))
            
        if(l==1):
            case_hh = dam[l+2][c]
            if(case_hh[2] == ' ' and case_h[2] == ' '):
                deplacement.append((l+2,c))
            
        if(c > 0):
            if( dam[l+1][c-1][3] == inv(case_o[3]) ):
                deplacement.append((l+1,c-1))
        if(c < 7):
            if( dam[l+1][c+1][3] == inv(case_o[3]) ):
                deplacement.append((l+1,c+1))
            
    elif(coul == 'b' and l>0):
        
        case_b = dam[l-1][c]
        if(case_b[2] == ' '):
            deplacement.append((l-1,c))

        if(l==6):
            case_bb = dam[l-2][c]
            if(case_bb[2] == ' ' and case_b[2] == ' '):
                deplacement.append((l-2,c))
        
        
        if(c > 0):
            if( dam[l-1][c-1][3] == inv(coul) ):
                deplacement.append((l-1,c-1))
                
        if(c < 7):
            if( dam[l-1][c+1][3] == inv(coul) ):
                deplacement.append((l-1,c+1))

    
    
    return(deplacement)

def pion_attak(dam, origine):
    
    cases=[]
    (l,c)=(origine[0],origine[1])
    coul=dam[l][c][3]
    
    if(0<l<7):
        if(coul=='n'):
            if(c==0):
                if(dam[l+1][c+1][3]!=coul):
                	cases.append((l+1,c+1))
            elif(c==7):
                if(dam[l+1][c-1][3]!=coul):
                	cases.append((l+1,c-1))
            else:
                if(dam[l+1][c-1][3]!=coul):
                	cases.append((l+1,c-1))
                if(dam[l+1][c+1][3]!=coul):
                	cases.append((l+1,c+1))
        else:
            if(c==0):
                if(dam[l-1][c+1][3]!=coul):
                	cases.append((l-1,c+1))
            elif(c==7):
                if(dam[l-1][c-1][3]!=coul):
                	cases.append((l-1,c-1))
            else:
                if(dam[l-1][c-1][3]!=coul):
                        cases.append((l-1,c-1))
                if(dam[l-1][c+1][3]!=coul):
                        cases.append((l-1,c+1))
                
    return(cases)

def fou(dam, origine): ## cases controles par le fou en 'origine' -> tableau (case du fou non comprise!)

    deplacement=[]
    (l,c)=(origine[0],origine[1])
    
    case_o = dam[l][c]


    for i in range(l+1, 8): #diagonale avant droite
        if(c+i-l > 7):
            break
        if(dam[i][c+i-l][3] != case_o[3]):
            deplacement.append((i,c+i-l))
            if(dam[i][c+i-l][3] == inv(case_o[3])):
                break
        else:
            break

    for i in range(l+1, 8): #diagonale avant gauche
        if(c-i+l < 0):
            break
        if(dam[i][c-i+l][3] != case_o[3]):
            deplacement.append((i,c-i+l))
            if(dam[i][c-i+l][3] == inv(case_o[3])):
                break
        else:
            break

    for i in range(8-l+1, 9): #diagonale arriere droite
        if(c+i-8+l > 7):
            break
        if(dam[8-i][c+i-8+l][3] != case_o[3]):
            deplacement.append((8-i,c+i-8+l))
            if(dam[8-i][c+i-8+l][3] == inv(case_o[3])):
                break
        else:
            break

    for i in range(8-(l-1), 9): #diagonale arriere gauche
        if(c-(i-(8-(l-1)))-1 < 0):
            break
        if(dam[l-(i-(8-(l-1)))-1][c-(i-(8-(l-1)))-1][3] != case_o[3]):
            deplacement.append((l-(i-(8-(l-1)))-1,c-(i-(8-(l-1)))-1))
            if(dam[l-(i-(8-(l-1)))-1][c-(i-(8-(l-1)))-1][3] == inv(case_o[3])):
                break
        else:
            break

    return(deplacement)

def cava(dam, origine):
    
    deplacement=[]
    (l,c)=(origine[0],origine[1])
    
    case_o = dam[l][c]

    if(l>1 and c>0):
        case_hg=dam[l-2][c-1]
        if(case_hg[3]!=case_o[3]):
            deplacement.append((l-2,c-1))

    if(l>1 and c<7):
        case_hd=dam[l-2][c+1]
        if(case_hd==0 or case_hd[3]!=case_o[3]):
            deplacement.append((l-2,c+1))
            
    if(l>0 and c>1):
        case_gh=dam[l-1][c-2]
        if(case_gh[3]!=case_o[3]):
            deplacement.append((l-1,c-2))
            
    if(l>0 and c<6):
        case_dh=dam[l-1][c+2]
        if(case_dh[3]!=case_o[3]):
            deplacement.append((l-1,c+2))
       
    if(l<6 and c>0):
        case_bg=dam[l+2][c-1]
        if(case_bg[3]!=case_o[3]):
            deplacement.append((l+2,c-1))
            
    if(l<6 and c<7):
        case_bd=dam[l+2][c+1]
        if(case_bd[3]!=case_o[3]):
            deplacement.append((l+2,c+1))
        
    if(l>7 and c>1):
        case_gb=dam[l+1][c-2]
        if(case_gb[3]!=case_o[3]):
            deplacement.append((l+1,c-2))
        
    if(l<7 and c<6):
        case_db=dam[l+1][c+2]
        if(case_db[3]!=case_o[3]):
            deplacement.append((l+1,c+2))
        
    return(deplacement)

def tour(dam, origine):

    deplacement=[]
    (l,c)=(origine[0],origine[1])
    
    case_o = dam[l][c]

    for i in range(c+1, 8): #ligne droite
        if(dam[l][i][3]!=case_o[3]):
            deplacement.append((l,i))
            if(dam[l][i][3]==inv(case_o[3])):
                break
        else:
            break
    for i in range(8-(c-1), 9): #ligne gauche
        if(dam[l][8-i][3]!=case_o[3]):
            deplacement.append((l,8-i))
            if(dam[l][8-i][3]==inv(case_o[3])):
                break
        else:
            break
    for i in range(l+1, 8): #colonne haut
        if(dam[i][c][3]!=case_o[3]):
            deplacement.append((i,c))
            if(dam[i][c][3]==inv(case_o[3])):
                break
        else:
            break
    for i in range(8-(l-1), 9): #colonne bas
        if(dam[8-i][c][3]!=case_o[3]):
            deplacement.append((8-i,c))
            if(dam[8-i][c][3]==inv(case_o[3])):
                break
        else:
            break

    return(deplacement)

def dame(dam, origine):
    deplacement=[]

    for i in tour(dam, origine):
        deplacement.append(i)
    for i in fou(dam, origine):
        deplacement.append(i)   
        
    return(deplacement)

def roi(dam, origine):#depalcement regulier du roi (pas le roc)
    
    deplacement=[]
    (l,c)=(origine[0],origine[1])
    
    case_o = dam[l][c]

    if(l>0):#bas
        if(dam[l-1][c][3]!=case_o[3]):
            deplacement.append((l-1,c))
    if(l<7):#haut
        if(dam[l+1][c][3]!=case_o[3]):
            deplacement.append((l+1,c))
    if(c>0):#gauche
        if(dam[l][c-1][3]!=case_o[3]):
            deplacement.append((l,c-1))
        if(l>0):#bas
            if(dam[l-1][c-1][3]!=case_o[3]):
                deplacement.append((l-1,c-1))
        if(l<7):#haut
            if(dam[l+1][c-1][3]!=case_o[3]):
                deplacement.append((l+1,c-1))
    if(c<7):#droite
        if(dam[l][c+1][3]!=case_o[3]):
            deplacement.append((l,c+1))
        if(l>0):#bas
            if(dam[l-1][c+1][3]!=case_o[3]):
                deplacement.append((l-1,c+1))
        if(l<7):#haut
            if(dam[l+1][c+1][3]!=case_o[3]):
                deplacement.append((l+1,c+1))

    return(deplacement)

def roc(d, origine, taille):#operation du roc(deplacement des pieces) origine:position du roi, taille: 'g' pour grand ou 'p' pour petit
	
    (l,c)=(origine[0],origine[1])
    case_o=d[l][c]
    coul=case_o[3]

    if(case_o[3]==1):#si le roi a deja bouge
        print('bloc1')
        return(d, False)#ce n'est pas possible
	
    if(taille=='p'):#petit roc
            
        if(d[l][c+1][2]!=' ' or d[l][c+2][2]!=' '):#si les cases entre la tour et le roi sont vides
            return(d, False)
    
        if(d[l][c+3][2]!='t' or d[l][c+3][4]==1):#si la tour est en place et n'a pas bouge)
            print('bloc2')
            return(d, False)
		
        cases_interdites=cases_attak(d, inv(coul))
        for x in cases_interdites:
            if(x==(l,c) or x==(l,c+1) or x==(l,c+2)):#si le roi sera pas en echec lors du deplacement
                return(d, False)

        d_hyp=jouer(d, [l,c+3,l,c+1])[0]
        d_hyp[l][c]=(case_o[0], case_o[1], ' ', ' ', 0)#on deplace le roi
        d_hyp[l][c+2]=('g', 8-l, 'r', coul, 1)

        return(d_hyp, True)#on retourne le damier apres roc

    if(taille=='g'):#petit roc
        if(d[l][c-4][2]!='t' or d[l][c-4][4]==1):#si la tour est en place et n'a pas bouge
            return(d, False)
        if(d[l][c-3][2]!=' ' and d[l][c-2][2]!=' ' and d[l][c-1][2]!=' '):#si les cases entre la tour et le roi sont vides
            return(d, False)
        cases_interdites=cases_attak(d, inv(coul))
        for x in cases_interdites:
            if(x==(l,c) or x==(l,c-1) or x==(l,c-2) or x==(l,c-3)):#si le roi sera pas en echec lors du deplacement
                return(d, False)

        d_hyp=jouer(d, [l,c-4,l,c-1])[0]
        d_hyp[l][c]=(case_o[0], case_o[1], ' ', ' ', 0)
        d_hyp[l][c-2]=('c', 8-l, 'r', coul, 1)

        return(d_hyp, True)
	

def cases_attak(dam, coul):## Retourne la liste des coordonees des cases attaquees par 'coul' (avec repetitions)

    cases=[]##[(coord1), ...]
    for i in range(8):
        for j in range(8):
            if(dam[i][j][3]==coul):
                if dam[i][j][2]=='p':
                    for x in pion_attak(dam,(i,j)):
                        cases.append(x)
                if dam[i][j][2]=='t':
                    for x in tour(dam,(i,j)):
                        cases.append(x)
                if dam[i][j][2]=='c':
                    for x in cava(dam,(i,j)):
                        cases.append(x)
                if dam[i][j][2]=='f':
                    for x in fou(dam,(i,j)):
                        cases.append(x)
                if dam[i][j][2]=='d':
                    for x in dame(dam,(i,j)):
                        cases.append(x)
                if dam[i][j][2]=='r':
                    for x in roi(dam,(i,j)):
                        cases.append(x)

    return(cases)
    
def tot(dam, coul):## ensemble des cases ou une pices 'coul' peut arriver avec repetition excluses
    
    depl=[]##[(coord1), ...]
    
    for i in range(8):
        for j in range(8):
            if( (dam[i][j][2],dam[i][j][3]) == ('r',coul) ):
                (l,c)=(i,j)## position du roi 'coul'
            if( (dam[i][j][2],dam[i][j][3]) == ('r',inv(coul)) ):
                (l2,c2)=(i,j)## position du roi 'inv(coul)'
    
    for i in range(8):
        for j in range(8):
            if(dam[i][j][3]==coul):#si on trouve une piece de sa couleur
                if dam[i][j][2]=='p':#si c'est un pion:
                    for x in pion(dam,(i,j)):#pour l'ensemble des coups que le pion jouer:
                        a=x[0]#on note (a,b) la case ou le pion peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaque
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le roi n'est pas attaque c'est bon et si on ne mange pas le roi adverse
                            case=(a,b)
                            depl.append(case)
                if dam[i][j][2]=='t':
                    for x in tour(dam,(i,j)):
                        a=x[0]#on note (a,b) la case ou le pion peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaque
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le roi n'est pas attaque c'est bon
                            case=(a,b)
                            depl.append(case)
                if dam[i][j][2]=='c':
                    for x in cava(dam,(i,j)):
                        a=x[0]#on note (a,b) la case ou le pion peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaque
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le roi n'est pas attaque c'est bon et si on ne mange pas le roi adverse
                            case=(a,b)
                            depl.append(case)
                if dam[i][j][2]=='f':
                    for x in fou(dam,(i,j)):
                        a=x[0]#on note (a,b) la case ou le pion peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaque
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le roi n'est pas attaque c'est bon et si on ne mange pas le roi adverse
                            case=(a,b)
                            depl.append(case)
                if dam[i][j][2]=='d':
                    for x in dame(dam,(i,j)):
                        a=x[0]#on note (a,b) la case ou la dame peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaque
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le roi n'est pas attaque c'est bon et si on ne mange pas le roi adverse
                            case=(a,b)
                            depl.append(case)
                if dam[i][j][2]=='r':#si le roi joue
                    for x in roi(dam,(i,j)):# x la case d'arrivee du roi
                        cases_interdites = cases_attak(jouer(dam, [i,j,x[0],x[1]])[0], inv(coul))# cases attaques par l'advairsaire apres deplacement du roi (cas ou le roi mangerait une piece advairse qui serait protegee)
                        if((x[0],x[1]) not in cases_interdites):# si le roi est sur une case attaquee par l'adversaire, on ne fait rien
                            if x not in depl:
                                depl.append(x)

    return(depl)

def tot_detail(dam, coul):## ensemble des mouvements possible de coul 
    
    depl=[]##[[n ligne depart, n colonne depart, n ligne arrivee, n colonne arrivee], ...]

    for i in range(8):
        for j in range(8):
            
            if (dam[i][j][2],dam[i][j][3]) == ('r',coul) :# determination de la position du roi 'coul'
                (l,c)=(i,j)
                
            if (dam[i][j][2],dam[i][j][3]) == ('r',inv(coul)) :# determination de la position du roi adverse 'inv(coul)'
                (l2,c2)=(i,j)

    
    if(dam[l][c][4]==0):## Ajout du roc: (deplacement 'non legal' du roi)

        if(roc(dam,(l,c),'p')[1]):#si faire le petit roc 
            if(dam[l][c][3]=='b'):#si on est blanc
                depl.append([7,4,7,6])#on ajout le petit roc blanc
            else:
                depl.append([0,4,0,6])#sinon on ajoute le petit roc noir
        if(roc(dam,(l,c),'g')[1]):#de meme pour le grand roc
                if(dam[l][c][3]=='b'):
                    depl.append([7,4,7,2])
                else:
                    depl.append([0,4,0,2])

    for i in range(8):
        for j in range(8):#on parcour le damier:
            if(dam[i][j][3]==coul):#si on tombe sur une piece de sa couleur:
                if dam[i][j][2]=='t':
                    for x in tour(dam,(i,j)):#pour l'ensemble des coups que la tour jouer:
                        a=x[0]#on note (a,b) la case ou le pion peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaque
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le roi n'est pas attaque c'est bon
                            case=[i,j,a,b]
                            depl.append(case)
                if dam[i][j][2]=='c':
                    for x in cava(dam,(i,j)):#pour l'ensemble des coups que le pion jouer:
                        a=x[0]#on note (a,b) la case ou le pion peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaque
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le roi n'est pas attaque c'est bon
                            case=[i,j,a,b]
                            depl.append(case)
                if dam[i][j][2]=='f':
                    for x in fou(dam,(i,j)):#pour l'ensemble des coups que le fou jouer:
                        a=x[0]#on note (a,b) la case ou le pion peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaque
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le roi n'est pas attaque c'est bon
                            case=[i,j,a,b]
                            depl.append(case)
                if dam[i][j][2]=='d':
                    for x in dame(dam,(i,j)):#pour l'ensemble des coups que la dame jouer:
                        a=x[0]#on note (a,b) la case ou le pion peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaque 
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le roi n'est pas attaque c'est bon
                            case=[i,j,a,b]
                            depl.append(case)
                if dam[i][j][2]=='p':#si c'est un pion:
                    for x in pion(dam,(i,j)):#pour l'ensemble des coups que le pion jouer:
                        a=x[0]#on note (a,b) la case ou le pion peu arriver
                        b=x[1]
                        d_hyp=copie(dam)
                        d_hyp[i][j]=(dam[i][j][0], dam[i][j][1], ' ', ' ')#on enleve la piece de la case de depart
                        d_hyp[a][b]=(dam[a][b][0], dam[a][b][0], dam[i][j][2], dam[i][j][3], dam[i][j][4])#on place la piece sur la case d'arrive
                        cases_interdites = cases_attak(d_hyp, inv(coul))#on regarde les cases attaques
                        if((l,c) not in cases_interdites and (a,b)!=(l2,c2) ):#si le coups est legal: c'est bon!
                            case=[i,j,a,b]
                            depl.append(case)
                if (i==l and j==c):#si c'est le roi
                    for x in roi(dam,(i,j)):#pour les dlpc du roi
                        cases_interdites = cases_attak(dam, inv(coul))# cases attaques par 'inv' coul apres deplacement du roi
                        if((x[0],x[1]) not in cases_interdites):
                            case=[i,j,x[0],x[1]]
                            depl.append(case)

    return(depl)
	
########################################   FONCTIONS d'etat   ############################################

def mat_aux(d, coul, seq, k):#renvoi un arbre de coups de prodondeur k

    if(k==1):#si on arrive aux feuilles
        return(tot_detail(d, coul))#on ajoute tout les deplacements possible de coul
    else:
        for i in range(len(tot_detail(d, coul))):#pour tout les coups possibles
            seq.append(tot_detail(d, coul)[i])#on ajoute a seq un coup
            seq[i].append(mat_aux(jouer(d, seq[i])[0], inv(coul), [], k-1))#pour ce coup, on ajoute toutes les reponces possibles de l'adversaire

    print('ok')
    return(seq)

def parcour_aux(seq):#renvoi un tableau d'indice menant a un tableau de seq
    portes=[]
    for i in range(len(seq)) :#pour les elements de la sequence
        if type(seq[i])==list:#si l'element est un tableau
            portes.append(i)#on repertorie l'emplacement du tableau de seq dans portes
    return(portes)
    

def parcour_aux2(seq, chemin, num_chemin):
    chemin_aux=[]
    for i in seq:
        if type(i)==int :
            chemin_aux.append(i)
        if type(i)==list :
            chemin.append(chemin_aux)
            if(len(i)==0):
                chemin.append([])
                comp
                break
            else:
                chemin.append(seq(i), chemin)
    return(chemin)

def echec(dam, coul):## determine si 'coul' est en echec et renvoie la liste des cases ou une piece coul peut arriver sert pour la ftc fin
               
    for i in range(8):
        for j in range(8):
            if( (dam[i][j][2],dam[i][j][3]) == ('r',coul) ):
                (l,c)=(i,j)## position du roi 'coul'
                break
            
    dpl_tot = tot(dam,inv(coul))
    if (l,c) in dpl_tot :
        return(True, dpl_tot)
    else:
        return(False, dpl_tot)

def fin(d, coul): #determine si la partie est fini et si 'coul' gagne (employer au tour de 'inv(coul)')

    (echc, dpl_tot)=echec(d, inv(coul))
    
    if(echc and dpl_tot==[]):#si inv(coul) est en echec et ne peut plus bouger
        return(True)#il a mat
    
    if(tot(d,coul) == [] and dpl_tot == [] and not echc):#si inv(coul) n'est pas en echec et qu'aucun joueur ne peut bouger
        return(True)#il y a pat
    
    return(False)#sinon la partie n'est pas fini

def damier(): ## initalisation du damier

    d=[[0 for j in range(8)] for i in range(8)]##[colonne1: [ligne1: (a,1,'t','b',0), ...], colonne2: ...]
    
    for i in range(8):
        if i<2 :
            c='n'
        if i>5 :
            c='b'
        for j in range(8):
            if(i==1 or i==6):
                d[i][j]=(alpha(j),8-i,'p',c,0)#le 0 a la fin indique si la piece a bouger ou pas (cela sert pour le roc)
                
            elif(i==0 or i==7):
                if(j==0 or j==7):
                    d[i][j]=(alpha(j),8-i,'t',c,0)
                if(j==1 or j==6):
                    d[i][j]=(alpha(j),8-i,'c',c,0)
                if(j==2 or j==5):
                    d[i][j]=(alpha(j),8-i,'f',c,0)
                if(j==3):
                    d[i][j]=(alpha(j),8-i,'d',c,0)
                if(j==4):
                    d[i][j]=(alpha(j),8-i,'r',c,0)
            else:
                d[i][j]=(alpha(j),8-i,' ',' ',0)

    return(d)
    

def jeu():# boucle principale du jeu
    
    dam=damier()
    joueur=True
    mat=False
    calculs=[]
    
    while(not (fin(dam,'n') or fin(dam,'b'))):
        
        if(echec(dam,'b')[0] or echec(dam,'n')[0]):
            print('echec!')
        
        if joueur :
            ok = False
            while(not ok):
                print(dam)
                coup = input("coup:")
                (dam,ok) = jouer(dam, traduc(coup))
            
        else :
            print('noir:')
            debut_calc=time.time()
            (dam, calculs) = robot(dam, calculs, 'n')
            fin_calc=time.time()
            print("temps de jeu des noirs:", fin_calc-debut_calc)

        joueur = not joueur
    
    if(ehec(dam,'b')):
        print('blanc gagne!')
    elif(echec(dam,'n')):
        print('noir gagne!')
    else:
        print('nul!')

    return()
    
def jouer(d, coup): # fonction deplace la piece jouee    coup=[n ligne depart, n colonne depart, n ligne arrivee, n colonne arrivee]

    case_d=d[coup[0]][coup[1]]
    case_a=d[coup[2]][coup[3]]

    if( case_d[2]==' ' ):#si la case demande est vide on ne fait rien
    #   or
    #    (case_d[2]=='p' and (coup[2],coup[3]) not in pion(d, (coup[0],coup[1])) )
    #   or
    #   (case_d[2]=='c' and (coup[2],coup[3]) not in cava(d, (coup[0],coup[1])) )
    #   or
    #   (case_d[2]=='f' and (coup[2],coup[3]) not in fou(d, (coup[0],coup[1])) )
    #   or
    #   (case_d[2]=='t' and (coup[2],coup[3]) not in tour(d, (coup[0],coup[1])) )
    #   or
    #   (case_d[2]=='d' and (coup[2],coup[3]) not in dame(d, (coup[0],coup[1])) )
    #   or
    #   (case_d[2]=='r' and (coup[2],coup[3]) not in roi(d, (coup[0],coup[1])))
        
        return((d,False))
    
    else:#sinon

        d_hyp=copie(d)
        d_hyp[coup[0]][coup[1]]=(case_d[0],case_d[1],' ',' ',0)#on deplace la piece
        d_hyp[coup[2]][coup[3]]=(case_a[0],case_a[1],case_d[2],case_d[3],1)

        if(case_d[2]=='p' and case_d[3]=='b' and case_a[1]==0):#Lorsque le pion du joueur arrive au bout
            d_hyp[coup[2]][coup[3]]=(case_a[0], 0, input('d,t,f,c?'), 'b', '1')#on demande au joueur ce qu'il veut
        if(case_d[2]=='p' and case_d[3]=='n' and case_a[1]==7):
            d_hyp=robo_dame(d,coup)
	
        if(coup==[7,4,7,6]):#si le coup est le petit roc blanc
            return(roc(d, (7,4), 'p'))#on appel la fct roc
        if(coup==[7,4,7,2]):
            return(roc(d, (7,4), 'g'))
        if(coup==[0,4,0,6]):
            return(roc(d, (0,4), 'p'))
        if(coup==[0,4,0,2]):
            return(roc(d, (0,4), 'g'))

        return((d_hyp,True))    

    
######################################## FONCTIONS Robot ############################################

def robot(d, calculs, coul):

    point_r1 = []
    
    racourcie = []
    
    if(calculs != []):#Utilisation du racourcie!
        pos_debut=-1

        for k in range(len(calculs)):#on parcours le tableau : [(damier,coup,[(d_hyp,coup_hyp),...]),...]
            if(d==calculs[k][0]):#si on trouve un damier qui coincide avec un damier deja calcule
                pos_debut=k# on marque la position du premier damier qui coincide
                pos_fin=k 
                while(d==calculs[pos_fin][0]):#on cherche la dernier position du damier qui coincide
                    pos_fin+=1
                    if(pos_fin==len(calculs)):
                        break
                break
            
        if(pos_debut != -1):#si on a trouver un damier qui coincide
            
            coup_envisage = [ calculs[k][1] for k in range(pos_debut,pos_fin+1)]#on retrouve tout les coups qui ont etaient envisage
            print('racourcie utile!')

            bon_coup = []
            
            compt=-1
            point_r1=[]
            for r1 in coup_envisage:#pour tout les coups qu'on a calculer pour ce tour, on recommence le minimax
                compt+=1
                if(fin(jouer(d,r1)[0],coul)):#si on peut mater, on joue le coup
                    bon_coup=r1
                    return(jouer(d,r1)[0],[])
                
                point_r2=[]
                for k in range(len(calculs[pos_debut+compt][2])):#pour tout les damiers accessibles 2 coups plus loin
                    r2=calculs[pos_debut+compt][2][k][1]#on considere qu'on a jouer le coup qui nous aurait qui nous aurait ete possible apres une reponce non elage de j1
                    d_hyp3=jouer(calculs[pos_debut+compt][2][k][0],r2)[0]#on considere qu'on a jouer le coup r2

                    racourcie_hyp=[]
                    
                    point_j2=[]
                    for j2 in coups(d_hyp3,inv(coul)):
                        d_hyp4=jouer(d_hyp3,j2)[0]#damier surlequel on sera probablement ds 4 tours

                        if(point_j2!=[]):#sert pour l'elagage qui suit
                            min_j2=min(point_j2)
                        else
                            min_j2=1000
                        
                        point_r3=[]
                        for r3 in coups(d_hyp4, inv(coul)):
                            d_hyp5=jouer(d_hyp4, r3)[0]
                            note=evaluer(d_hyp5, coul)
                            point_r3.append(note)
                            racourcie_hyp.append((d_hyp4, r3))
                            if(note>min_j2):#elagage
                                break
                            
                        
                        if(point_r3!=[]):
                            point_j2.append(max(point_r3))
                        else:
                            point_j2.append(-100)

                        if(point_r2!=[] and point_r3!=[]):#elagage
                            if(max(point_r3)<=max(point_r2)):
                                break

                    if(point_j2!=[]):
                        point_r2.append(min(point_j2))
                    else:
                        point_r2.append(100)
                        
                    racourcie.append((calculs[pos_debut+compt][2][k][0], r2, racourcie_hyp))

                if(point_r2!=[]):
                    point_r1.append(min(point_r2))
                else:
                    point_r1.append(-100)

            m=max(point_r1)
            for i in range(len(point_r1)):
                if(m==point_r1[i]):
                    bon_coup=calculs[pos_debut+i][1]
                    break
                
            print(retraduc(bon_coup))
            return(jouer(d, bon_coup)[0],racourcie)
                
    print('racourci pas utile!')#on n'utilise pas le recourcie!

    max_r1=-1000
    min_j1=1000
    for r1 in tot_detail(d, coul):#pour tout les coups qu'on peut jouer
        d_hyp1=jouer(d, r1)[0]#on joue le coup
        
        if(point_r1!=[]):#si ce n'est pas le premier coups qu'on envisage
            max_r1=max(point_r1)#on releve le maximum qui exite deja (utile pour les coupures profonde ds la derniere boucle)
            
        if(fin(d_hyp1, coul)):#si il y a mat
            return(jouer(d, r1)[0])#c'est le bon coup, on le bon coup
        #on ne reteste pas cette condition a cause du temps de calcul
        
        point_j1=[]
        for j1 in coups(d_hyp1, inv(coul)):#pour tout les coups que le joueur peut faire
            d_hyp2=jouer(d_hyp1, j1)[0]#on joue le coup

            if(point_j1!=[]):#si il existe deja un minimum parmis les coups j1
                min_j1=min(point_j1)#on l'enregistre
            
            point_r2=[]
            for r2 in tot_detail(d_hyp2, coul):#
                d_hyp3=jouer(d_hyp2, r2)[0]
                racourcie_hyp=[] #on cree un tableau qui va contenir toutes les positions possibles 2 coups apres le coup r2
                
                point_j2=[]
                for j2 in coups(d_hyp3, inv(coul)):
                    d_hyp4=jouer(d_hyp3, j2)[0]
                    
                    point_r3=[]
                    for r3 in coups(d_hyp4, coul):
                        d_hyp5=jouer(d_hyp4, r3)[0]
                        note=evaluer(d_hyp5, coul)
                        point_r3.append(note)#evaluation a simplifier au maximum!
                        racourcie_hyp.append((d_hyp4,r3))#on ajoute la position obtenu apres les coups r2 et r3
                        if(note>=min_j1):#coupure profonde relatif à j1
                            break
                    
                    if(point_r3!=[]):
                        point_j2.append(max(point_r3))#on cree un tableaux de point point_j2[i] -> meilleur coup r3 possible
                    else:
                        point_j2.append(0)
                        
                    #elagage 3 ! on est dans la boucle J2, reponces possibles au coup r2
                    if(point_r2 != []):
                        if(max(point_r3)<=max(point_r2) or max(point_r3)<=max_r1):#elagage normal+profondeur
                            break
                        
                racourcie.append((d_hyp2,r2,racourcie_hyp))#on cree le tableau qui sera lue au prochain tour de jeu du robot
                #et qui contiend a priori un couple avec la position dans laquel le robot sera a son prochain tour, les coups qu'il peut jouer et tout les damiers possible 2 tours suivant
                #on ajoute au racourcie le tableau des damiers possibles 2 coups apres
                #prblm d'elagage!
                
                if(point_j2 != []):
                    point_r2.append(min(point_j2))#j2 va repondre de la pire maniere pour nous possible
                else:
                    point_r2.append(0)
                
                #elagage 2 ! on est dans la boucle R2, reponces possibles au coup j1
                if(point_j1 != []):
                    if(min(point_j2)>min(point_j1)):#si le minimum de ce qu'on vient de recuperer est plus grand que le minimum existant de point_j1, il ne sera pas retenu
                        break#inutile d'aller voir les autres coups de r2, il ne seront pas pris en compte
            
            if(point_r2 != []):
                point_j1.append(max(point_r2))
            else:
                point_j1.append(0)

            #elagage 1 ! on est dans la boucle J1, reponces possibles au coup r1
            if(point_r1 != []):#si point_r1 n'est pas vide
                if(max(point_r2)<=max(point_r1)):#si la nouvelle valeur de j1 est plus petite que le max existant de point_r1, cette valeur sera dans le noeud r1 et donc pas retenu car on ne retiend que le max
                    break#inutiles d'aller voir toute les autres reponces de j1

        if(point_j1 != []):
            point_r1.append(min(point_j1))
        else:
            point_r1.append(0)

    m=max(point_r1)
    for i in range(len(point_r1)):
        if(point_r1[i]==m):
            bon_coup=tot_detail(d,coul)[i]

    print(retraduc(bon_coup))
    return(jouer(d, bon_coup)[0], racourcie)
                   
def coups(dam, coul):## ensemble des mouvements possible de coul 
    
    depl=[]##[[n ligne depart, n colonne depart, n ligne arrivee, n colonne arrivee], ...]
    case_attak=[]##[(l,c),...] ensembles cases attaques par l'ennemi
    (l,c) = (-1,-1)##(l,c) position du roi coul
    
    for i in range(8):
        for j in range(8):#on parcour le damier
            
            if dam[i][j][2]=='d':
                if(dam[i][j][3]==coul):#si on tombe sur une piece de sa couleur:
                    for x in dame(dam,(i,j)):#pour l'ensemble des coups que la dame jouer:
                        if(dam[x[0]][x[1]][2]!='r'):#on n'a pas le droit de manger un roi
                            depl.append([i,j,x[0],x[1]])
                else:
                    case_attak.append(dame(dam,(i,j)))#si on tombe sur la dame adverse, on ajoute les cases attaques par cette dame
                        
            if dam[i][j][2]=='t':
                if(dam[i][j][3]==coul):#si on tombe sur une piece de sa couleur:
                    for x in tour(dam,(i,j)):#pour l'ensemble des coups que la tour jouer:
                        if(dam[x[0]][x[1]][2]!='r'):#on n'a pas le droit de manger un roi
                            depl.append([i,j,x[0],x[1]])
                else:
                    case_attak.append(tour(dam,(i,j)))#si on tombe sur la tour adverse, on ajoute les cases attaques par cette tour

            if dam[i][j][2]=='c':
                if(dam[i][j][3]==coul):#si on tombe sur une piece de sa couleur:
                    for x in cava(dam,(i,j)):#pour l'ensemble des coups que le pion jouer:
                        if(dam[x[0]][x[1]][2]!='r'):#on n'a pas le droit de manger un roi
                            depl.append([i,j,x[0],x[1]])
                else:
                    case_attak.append(cava(dam,(i,j)))#si on tombe sur le cavalier adverse, on ajoute les cases attaques par ce cava

            if dam[i][j][2]=='f':
                if(dam[i][j][3]==coul):#si on tombe sur une piece de sa couleur:  
                    for x in fou(dam,(i,j)):#pour l'ensemble des coups que le fou jouer:
                        if(dam[x[0]][x[1]][2]!='r'):#on n'a pas le droit de manger un roi
                            depl.append([i,j,x[0],x[1]])
                else:
                    case_attak.append(fou(dam,(i,j)))
                    
            if dam[i][j][2]=='p':#si c'est un pion:
                if(dam[i][j][3]==coul):#si on tombe sur une piece de sa couleur:
                    for x in pion(dam,(i,j)):#pour l'ensemble des coups que le pion jouer:
                        if(dam[x[0]][x[1]][2]!='r'):#on n'a pas le droit de manger un roi
                            depl.append([i,j,x[0],x[1]])
                else:
                    case_attak.append(pion(dam,(i,j)))

                       
            if dam[i][j][2]=='r':#si c'est le roi
                if(dam[i][j][3]==coul):#si on tombe son roi:
                    (l,c)=(i,j)#on enregistre la position de son roi
                else:#sinon
                    case_attak.append(roi(dam,(i,j)))#on ajoute les cases attaque par le roi adverse
        
    for x in roi(dam,(l,c)):#pour les dlpc de son roi
        if((x[0],x[1]) not in case_attak):#si le roi n'est pas dans l'ensemble des cases attaquees par l'ennemi
            depl.append([l,c,x[0],x[1]])#on ajoute le dplc du roi
                
    if(dam[l][c][4]==0):##Ajout du roc : si le roi n'a pas encore bouge, on envisage le roc:
            
        if(dam[l][c][3]=='b'):#si on est blanc
            #petit roc:
            if(dam[l][c+1][3]=='' and dam[l][c+2][3]==''):#si les cases entre la tour et le roi sont vides:
                if(dam[l][c+3][2]=='t' and dam[l][c+3][4]==0):#et si la tour est en place et n'a pas bouge:
                    if((l,c) not in case_attak and (l,c+1) not in case_attak and (l,c+2) not in case_attak):#si le roi ne passera par une case attaque par l'ennemi
                        depl.append([7,4,7,6])#on ajoute le petit roc blanc
            #grand roc:
            if(dam[l][c-1][3]=='' and dam[l][c-2][3]=='' and dam[l][c-3][3]==''):#si les cases entre la tour et le roi sont vides:
                if(dam[l][c-4][2]=='t' and dam[l][c-4][4]==0):#et si la tour est en place et n'a pas bouge:
                    if((l,c) not in case_attak and (l,c-1) not in case_attak and (l,c-2) not in case_attak):#si le roi ne passera par une case attaque par l'ennemi
                            depl.append([7,4,7,2])#on ajoute le grand roc blanc
        else:#si on est noir
            #petit roc:
            if(dam[l][c+1][3]=='' and dam[l][c+2][3]==''):#si les cases entre la tour et le roi sont vides:
                if(dam[l][c+3][2]=='t' and dam[l][c+3][4]==0):#et si la tour est en place et n'a pas bouge:
                    if((l,c) not in case_attak and (l,c+1) not in case_attak and (l,c+2) not in case_attak):#si le roi ne passera par une case attaque par l'ennemi
                        depl.append([0,4,0,6])#on ajoute le petit roc noir
            #grand roc:
            if(dam[l][c-1][3]=='' and dam[l][c-2][3]=='' and dam[l][c-3][3]==''):#si les cases entre la tour et le roi sont vides:
                if(dam[l][c-4][2]=='t' and dam[l][c-4][4]==0):#et si la tour est en place et n'a pas bouge:
                    if((l,c) not in case_attak and (l,c-1) not in case_attak and (l,c-2) not in case_attak):#si le roi ne passera par une case attaque par l'ennemi
                        depl.append([0,4,0,2])#on ajoute le grand roc noir
    return(depl)
                       
def evaluer(d, coul):#fonction d'evaluation d'une situation en faveur de coul

    pieces_j=[]
    pieces_a=[]
    
    pnt_j=0
    pnt_a=0
    
    case_j=0
    case_a=0
    
    for i in range(8):
        for j in range(8):
            if(d[i][j][3]==coul):
                pnt_j += eval_piece(d, i, j)
            elif(d[i][j][3]==inv(coul)):
                pnt_a += eval_piece(d, i, j)

    return(pnt_j-pnt_a)

def eval_piece(d, l, c):
    piece=d[l][c][2]
    avantage_centre=0
    if(2<l<5 and 2<c<5):
        avantage_centre = 1
    if(2<c<5):
        avantage_centre = 1
    if(piece=='p'):
        return(64+len(pion(d,(l,c)))+avantage_centre)
    if(piece=='c'):
        return(67+len(cava(d,(l,c)))+avantage_centre)
    if(piece=='f'):
        return(67+len(fou(d,(l,c)))+avantage_centre)
    if(piece=='t'):
        return(69+len(tour(d,(l,c)))+avantage_centre)
    if(piece=='d'):
        return(74+len(dame(d,(l,c)))+avantage_centre)
    if(piece=='r'):
        return(100+len(pion(d,(l,c)))+avantage_centre)
    
def robo_dame(d,coup):

    d_dame=copie(d)
    d_dame[coup[2]][coup[3]][2]='d'
                 
    d_cava=copie(d)
    d_cava[coup[2]][coup[3]][2]='c'

    if(evaluer(d_dame,'n') >= evaluer(d_cava,'n')):
        return(d_dame)
    else:
        return(d_cava)


def jeu_rb():# boucle principale du jeu
    
    dam=damier()
    joueur=True
    mat=False

    calculs_b=[]
    calculs_n=[]

    debut_partie=time.time()
    while(not (fin(dam,'n') or fin(dam,'b'))):
        
        if(echec(dam,'b')[0] or echec(dam,'n')[0]):
            print('echec!')
        
        if joueur :
            debut_coup=time.time()
            (dam, calculs_b) = robot(dam, calculs_b, 'b')
            fin_coup=time.time()
            print('temps de jeu des blanc:',fin_coup-debut_coup)
            
        else :
            debut_coup=time.time()
            (dam, calculs_n) = robot(dam, calculs_n, 'n')
            fin_coup=time.time()
            print('temps de jeu des noir:',fin_coup-debut_coup)

        joueur = not joueur

    fin_partie=time.time()
    
    if(ehec(dam,'b')):
        print('blanc gagne!')
    elif(echec(dam,'n')):
        print('noir gagne!')
    else:
        print('nul!')


    return(fin_partie-debut_partie)

def jeu_rd():# jeu random
    
    dam=damier()
    joueur=True
    mat=False

    calculs_b=[]
    calculs_n=[]

    debut_partie=time.time()
    while(not (fin(dam,'n') or fin(dam,'b'))):
        
        if(echec(dam,'b')[0] or echec(dam,'n')[0]):
            print('echec!')
        
        if joueur :
            debut_coup=time.time()
            (dam, calculs_b) = robot(dam, calculs_b, 'b')
            fin_coup=time.time()
            print('temps de jeu des blanc:',fin_coup-debut_coup)
            
        else :
            debut_coup=time.time()
            dam = robot_rd(dam, 'n')
            fin_coup=time.time()
            print('temps de jeu des noir:',fin_coup-debut_coup)

        joueur = not joueur

    fin_partie=time.time()
    
    if(ehec(dam,'b')):
        print('blanc gagne!')
    elif(echec(dam,'n')):
        print('noir gagne!')
    else:
        print('nul!')


    return(fin_partie-debut_partie)

def robot_rd(dam, coul):
    coup=tot_detail(dam,coul)[0]
    print(retraduc(coup))
    return(jouer(dam,coup)[0])
        

d_test=damier()
d_test[1][4]=('e', 1, ' ', ' ')
d_test[3][4]=('e', 3, 'p', 'b')
d_echec=[[(alpha(i),j,' ',' ') for i in range(8)] for j in range(8)]
d_echec[0][0]=('a',0,'r','b')
d_echec[5][1]=('b',5,'d','n')
d_echec[2][0]=('a',2,'r','n')

print('ok')
#a1='(e2,e4)'b1='(e7,e5)'c1='(f1,c4)'d1='(c7,c5)'e1='(d1,f3)'f1='(a7,a6)'g1='(f3,f7)'
