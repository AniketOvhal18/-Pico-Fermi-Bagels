# final  code
#
import random
a='qwertyuiopasdfghjklzxcvbnm!!@#$%^^^&*()'
input_no = int(input('enter the size/length of digit u want to genrate '))
genrated_no=0

while True:
  if input_no==3:
    genrated_no=random.randint(100,999)
  elif input_no==4:
    genrated_no=random.randint(1000,9999)
  elif input_no==5:
    genrated_no=random.randint(10000,99999)
  if len(set(str(genrated_no))) == len(str(genrated_no)):

     break
  else :
    continue
while True:
  user_guess=input('enter the guess no')
  if user_guess.isdigit():
    u=[i for i in user_guess ]
    g=[j for j in str(genrated_no)]
  else:
    print('invalid char')
    break
  if len(user_guess)!=input_no:
    print(input_no,'digits only')
    break
  print(u)
  for i in range(0,len(user_guess)):
    no_count=0
    for j in user_guess:
      if u[i]==j:
        no_count+=1

  if no_count>1:
      print('invalid move',j,'no is repeted')
      break
  op= [ 'FERMI' if u[i]==g[i] else 'PICO' for i in range(0,len(u))if u[i] in g ]
  if len(op)==0:
    print('BAGEL')
  fermi_count=0
  pico_count=0
  begal_count=0
  for i in op:
    if i=='FERMI':
      fermi_count+=1
    elif i=='PICO':
      pico_count+=1
  if fermi_count==input_no:
    
    print('!!! YOU WON !!!!!')
    break
  if pico_count==input_no:
    break
  print(op)
