"""
Basic Regex Parser
Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.
In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.
Explain your algorithm, and analyze its time and space complexities.
"""
def is_match(text, pattern):
  if len(pattern)==0 and pattern!=text:
    return False
  ptr_t,ptr_p=0,0
  while ptr_p<len(pattern):
    if ptr_t<len(text) and pattern[ptr_p]==text[ptr_t] or pattern[ptr_p]=='.':
      ptr_p+=1
      ptr_t+=1
    elif pattern[ptr_p]=='*':
      while ptr_t<len(text) and pattern[ptr_p-1]==text[ptr_t]:
        ptr_t+=1
      ptr_p+=1
    elif ptr_p+1<len(pattern) and pattern[ptr_p+1]=="*":
      ptr_p+=2
    else:
      return False
  if ptr_p>=len(pattern) and ptr_t>=len(text):
    return True
  else:
    return False
     
      
  
