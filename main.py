import random


print('Spēle: Elektriskais rallijs 2022')
print('------------------------------------------------------------------------')
print('Autori: Krists Apinis un Ričards Ābols')
print('------------------------------------------------------------------------')
print('Spēles noteikumi: Spēle sākas pie Valmieras Valsts ģimnāzijas, sausā laikā ar auto vari nobraukt 140km, lietainā laikā 80km, pirms apstāšanās priekš uzlādes. Kopumā ir 13 kontrolpunkti ieskaitot sākumu (VVĢ), un beigas (Liepāja) kuri  ir apskates vietas. Apstāšanās pie kontrolpunktiem ir obligāta. Kontrolpunktos tev ir jāatbild uz vienu jautājumu lai tiktu tālāk. Uzpildīties varēsi paceļam Circle K izveidotajās uzpildes stacijās.')
print('------------------------------------------------------------------------')
print('Lai sāktu/spēlētu spēli nospiežat vienu ciparu no dotajiem variantiem.')
print('------------------------------------------------------------------------')
laikapstākļi = ['Saulains/sauss laiks', 'Lietains/mitrs laiks']
laiki = random.choice(laikapstākļi)
print('Ceļojuma laiapstākļi ir', laiki)
a = 100
b = 140
print('Akumulators ir', a, '% pilns.')
if laiki == 'Saulains/sauss laiks':
  print('Jūs varat nobraukt 140 km')
else:
  print('Jūs varat nobraukt',b*4/7,'km')
  
#Tabula
from tabulate import tabulate
data = [("Valmiera - Stalbe", "29"),
       ("Stalbe - Cēsis","17"),
       ("Cēsis - Turaida", "42"),
       ("Turaida - Biriņi", "22"),
       ("Bīriņi - Carnikava", "36"),
       ("Carnikava - Melngalvju nams", "30"),
       ("Melngalvju nams - Majori", "20"),
       ("Majori - Tīreļi", "38"),
       ("Tīreļi - Brocēni", "70"),
       ("Brocēni - Skrunda", "38"),
       ("Skrunda - Aizpute", "42"),
       ("Aizpute - Lielais Dzintars", "48"),]
headers = ["Stacijas", "Attālums (km)"]
print(tabulate(data, headers=headers, tablefmt="grid"))


print ('Vai sākat spēlēt?')
print('1. Jā')
print('2. Nē')
a = input()
while a == ('1'):
  print("Vai gribi zināt bateriju?")
  c = input()
  if c == ('jā'): 
    print('Tavs baterijas līmenis ir 100%')
  else:
    print('baterijas līmenis netiek izvadīts')
  print ('Vai brauksiet?')
  print('1. Jā')
  print('2. Nē')
  a = input()
  if a == ('2'):
    break
  else:
    print('Uz kuru galapunktu brauksiet?')
    print('1. Stalbe')
    print('2. Nebraukšu')
    d = input()
    if d == ('1'):
      print('Kontrolpunkta jaut: a')
    else:
      break
# Iestatījumi
print('beigas')
#nobraukums1 = 80
#nobraukums2 = 140

#garums1 = 29
#garums2 = 17
#garums3 = 42
#garums4 = 22
#garums5 = 36
#garums6 = 30
#garums7 = 20
garums8 = 38
garums9 = 70
#garums10 = 38
#garums11 = 42
#garums12 = 48



