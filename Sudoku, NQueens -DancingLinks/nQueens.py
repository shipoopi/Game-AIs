import dancingLinks as dl

def getMatrix(n):
  m1 = rowConstrain(n)
  m2 = colConstrain(n)
  m3 = diag1Constrain(n)
  m4 = diag2Constrain(n)
#  m5 = boxNumConstrain(n)
  l = len(m1)

  return [m1[i] + m2[i] + m3[i] + m4[i] for i in range(l)]
  
def rowConstrain(n):
  mat = []
  l = n
  for i in range(n):
    for j in range(n):
      b = i
      mat.append([0]*b + [1] + [0]*(l-b-1))
  for i in range(4*n-6):
    mat.append([0]*l)
  return mat

def colConstrain(n):
  mat = []
  l = n
  for i in range(n):
    for j in range(n):
      b = j
      mat.append([0]*b + [1] + [0]*(l-b-1))
  for i in range(4*n-6):
    mat.append([0]*l)
  return mat

def diag1Constrain(n):
  mat = []
  l = 2*n - 3
  avoid = [(0,n-1),(n-1,0)]
  for i in range(n):
    for j in range(n):
      b = j-i + n - 2
      if not (i,j) in avoid:
        mat.append([0]*b + [1] + [0]*(l-b-1))
      else:
        mat.append([0]*l)
  for i in range(2*n-3):
    mat.append([0]*i + [1] + [0]*(l-i-1))
  for i in range(2*n-3):
    mat.append([0]*l)
  return mat

def diag2Constrain(n):
  mat = []
  l = 2*n - 3
  avoid = [(0,0),(n-1,n-1)]
  for i in range(n):
    for j in range(n):
      b = j+i - 1
      if not (i,j) in avoid:
        mat.append([0]*b + [1] + [0]*(l-b-1))
      else:
        mat.append([0]*l)
  for i in range(2*n-3):
    mat.append([0]*l)
  for i in range(2*n-3):
    mat.append([0]*i + [1] + [0]*(l-i-1))
  return mat

def getSolution(mat):
  dlx = dl.DancingLinks(mat)
  sol = dlx.danceOnce()
  return sol

def prettyPrint(mat):
  print '\n'.join(map(lambda x:''.join(map(str,x)), mat))


if __name__ == '__main__':
  #prettyPrint(diag2Constrain(4)) 
  #print '\n'.join(map(lambda x:''.join(map(str,x)), getMatrix(4,4,4,2,2)))
  size = 17
  #mat = getMatrix(4)
  #prettyPrint(getMatrix(4))
  print filter (lambda x: x< size*size, getSolution(getMatrix(size)))
