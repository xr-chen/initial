class matrix():
    def __init__(self,matrixlist):
        self.content=[]
        self.content=matrixlist.copy()

    def __add__(self,other):
        result=[[0 for jj in range(len(self.content[0]))] for ii in range(len(self.content))]
        for i,rows in enumerate(self.content):
            for j,element in enumerate(rows):
                result[i][j]=self.content[i][j]+other.content[i][j]
        return matrix(result)
        
    def show(self):#显示矩阵
        flag=1
        d2=str(len(str(max(max(self.content))))+7)
        d1=str(len(str(max(max(self.content))))+3)
        form2='%'+d2+'.4f'
        form1='%'+d1+'d'
        for row in self.content:
            for element in row:
                if (int(element)==element) and flag:
                    form=form1
                else:
                    form=form2
                    flag=0
        for row in self.content:
            for element in row:
                print(form%element,end='')
            print()
        print()
        
    def __mul__(self,other):
        arows=len(self.content)
        acolumns=len(self.content[0])
        brows=len(other.content)
        bcolumns=len(other.content[0])
        result=[[0 for jj in range(bcolumns)] for ii in range(arows)]
        result=matrix(result)
        
        if acolumns!=brows:
            print('矩阵维度不同')
            return
        
        for i in range(arows):
            for j in range(bcolumns):
                a=self.content[i]
                b=[row[j] for row in other.content]
                c=[a[it]*b[it] for it in range(acolumns)]
                result.content[i][j]=sum(c)
        return result

if __name__=='__main__':    
    A=matrix([[1,2],[3,4],[6,6]])
    B=matrix([[2,3],[4,5],[7,8]])
    D=matrix([[1,2,3,4],[5,6.01,7,8]])
    D.show()
    A.show()
    B.show()
    C=A+B
    C.show()
    E=A*D
    E.show()