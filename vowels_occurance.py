a=['A','E','I','O','U']

p=input("enter the text\n")
l=[]
s=p.upper()
c=list(s)
for i in range(len(c)):
  for j in range(len(a)):
    if c[i]==a[j]:
      l.append(c[i])
print('repetation of vowel A',l.count('A'))
print('repetation of vowel E',l.count('E'))
print('repetation of vowel I',l.count('I'))
print('repetation of vowel O',l.count('O'))
print('repetation of vowel U',l.count('U'))
print('vowels in the input string is:',set(l))
