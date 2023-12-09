def root(x, n):
  if x == 0: return 0
  probs= []
  val=1
  while val<=x:
    probs.append(val)
    val+=0.001
  l,r=0,len(probs)-1
  act=x ** (1.0/n)
  while l<r:
    mid= (l+r)//2
    if abs(probs[mid]-act)<=0.001:
      return probs[mid]
    elif probs[mid]<act:
      l=mid
    else:
      r=mid

print(root(7,3))
