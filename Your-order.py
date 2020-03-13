def order(sentence):
  thislist = sentence.split()
  zin = []
  
  q = 1
  while q <= len(thislist):
      for i in thislist:
          for j in i:
              if j.isdigit() and j == str(q):
                  zin.append(i)
                  q +=1
      
  return ' '.join(zin)
