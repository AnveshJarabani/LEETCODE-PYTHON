from collections import Counter
def word_count_engine(document):
  wrds=[''.join(char.lower() for char in wrd if char.isalpha()) for wrd in document.split(' ')]
  lst=[wrd for wrd in wrds if wrd.isalpha()]
  result=[[i,str(val)] for i,val in Counter(lst).items()]
  return sorted(result,key=lambda x: [-int(x[1]),lst.index(x[0])])
