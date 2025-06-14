import numpy as np
rows=4
cols=4
mat1=np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1],[0,1,2,3,4,5,6,7,8,9,10,11,12],[0,1,4,9,16,25,36,49,64,81,100,121,144],[0,1,8,27,64,125,216,343,512,729,1000,1331,1728]])
mat=np.dot(mat1,mat1.transpose()).transpose()
mat2=np.array([[764.4],[5082.2],[37915.2],[290342.2]])
print(*mat)

main_mat=np.hstack((mat,mat2))
if np.linalg.det(mat)==0:
  print("\n\n\n\t\t\t\tNO EXACT SOLUTION\n\n")
  exit()

print('Coefficient matrix after pivoting= \n',main_mat)
def exchange(main_mat,x,y,z):
    rplc=np.zeros((1,y))
    k=cols+1-y
    for j in range (0,y):
        rplc[0,j]=main_mat[x,j+k]
        main_mat[x,j+k]=main_mat[z,j+k]
        main_mat[z,j+k]=rplc[0,j]

for l in range (0,rows):
  for m in range (l, rows):
    if abs(main_mat[l,l])<abs(main_mat[m,l]):
      exchange(main_mat=main_mat,x=l,y=cols+1-l,z=m)
  for k in range (l+1,rows):
    factor=main_mat[k,l]/main_mat[l,l]
    for i in range (l,cols+1):
     main_mat[k,i]=main_mat[k,i]-(main_mat[l,i]*factor)

xx=np.zeros((1,rows))
for i in range (0,cols):
 product=np.multiply(main_mat[rows-i-1,0:cols],xx)
 xx[0,cols-1-i]=(main_mat[rows-i-1,cols]-np.sum(product))/main_mat[rows-i-1,cols-i-1]
print('\n\nUpper Diagonal matrix:\n',main_mat)
print('\nsolution=',xx)

