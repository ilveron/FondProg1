def main ():
    mat1=[[1,6,3,4,8,3,9],[1,6,3,4,8,3,9],[2,7,3,5,5,4,2],[5,2,7,8,4,5,1],[5,2,7,8,4,5,1],[5,2,7,8,4,5,1]]
    mat2=[[1,6,3,4,8,3,9],[1,6,3,4,8,3,9],[1,6,3,4,8,3,9],[5,2,7,8,4,5,1],[5,2,7,8,4,5,1],[5,2,7,8,4,5,1]]
    mat3=[[1,6,3,4,8,3,9],[1,6,4,4,8,3,9],[2,7,3,5,5,4,2],[2,7,4,5,5,4,2],[5,2,4,8,4,5,1],[5,2,7,8,4,5,1]]
    A=int(input('Quale matrice vuoi testare?'))
    if A==1:
        pivot=(checkpivot (mat1,7,6,0,0))+1
        checkbande= checklinee (mat1,pivot,7,6,pivot,0,2)
        if checkbande==True:
            print ('La matrice è a bande orizzontali da', pivot)
        else:
            print ('La matrice non è a bande orizzontali')
    elif A==2:
        pivot=(checkpivot (mat2,7,6,0,0))+1
        checkbande= checklinee (mat2,pivot,7,6,pivot,0,2)
        if checkbande==True:
            print ('La matrice è a bande orizzontali da', pivot)
        else:
            print ('La matrice non è a bande orizzontali')
    elif A==3:
        pivot=(checkpivot (mat3,7,6,0,0))+1
        checkbande= checklinee (mat3,pivot,7,6,pivot,0,2)
        if checkbande==True:
            print ('La matrice è a bande orizzontali da', pivot)
        else:
            print ('La matrice non è a bande orizzontali')

            
def checklinee (matrice,pivot,A,B,i,j,cont):
    if i<B-1:
        if j<=A-1:
            if matrice[i][j]==matrice[i+1][j]:
                return checklinee (matrice,pivot,A,B,i,j+1,cont)
            elif matrice[i][j]!=matrice[i+1][j]:
                if i+1==cont*pivot:
                    return checklinee(matrice,pivot,A,B,i+1,0,cont+1)
                else:
                    return False
        else:
            return checklinee (matrice,pivot,A,B,i+1,0,cont)
    elif i>=B-1 and i+1==cont*pivot:
        return True
        

def checkpivot (matrice,A,B,i,j):
    if i<B-1:
        if j<=A-1:
            if matrice[i][j]==matrice[i+1][j]:
                return checkpivot (matrice,A,B,i,j+1)
            else:
                return i
        else:
            return checkpivot (matrice,A,B,i+1,0)


main ()
