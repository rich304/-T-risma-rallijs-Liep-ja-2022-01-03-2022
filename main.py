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

pilsetas= ['Stalbe', 'Cēsis', 'Turaida', 'Bīriņi', 'Carnikava', 'Melngalvju nams', 'Majori', 'Tīreļi', 'Brocēni', 'Skrunda', 'Aizpute', 'Lielais Dzintars']

i = 0

jaut = ['Kurā novadā atrodas Stalbe?', 'Kāds iespaidīgs sarunu festivāls notiek reizi gadā Cēsīs?', 'Kuram Turaidas pils tika celta?','Kuram latviešu seriālam Bīriņu muiža bija kā galvenā māja/bāze?', 'Kurš Carnikavas dabas parks tika iekļauts Eiropas Savienības īpaši aizsargājamo teritoriju tīklā "Natura 2000"?', 'Kura tirgotāju biedrība izmantoja Melngalvju namu oar savu bāzi Rīgā un dzīru namu?','Kā sauc Majoru centrālo un visdzīvīgāko ielu?', 'Kādās nozīmīgas 1. Pasaules kara Krievijas impērijas un Vācijas kaujas notika Tīreļu purvā un apkaimē?', 'Kādu izejvielu ieguva Cieceres ezera krastā?', 'Kādām vajdzībam Padomju Savienība cēla pilsētu Skrunda-1?', 'Kura ordeņa pils atrodas Aizputē?', 'Cik stāvu ir koncertzālē Lielais Dzintars?']

j = 0

atbildes = ['Cēsu', 'Lampa', 'Rīgas arhibīskapam', 'Ugunsgrēkam', 'Piejūras', 'Hanzas', 'Jomas iela', 'Ziemassvētku kaujas', 'kaļķakmeni', 'militārām', 'Aizputes ordeņa', '8']

x = 0

print ('Vai sākat spēlēt? Spiediet taustiņu 1 vai 2!')
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
  print ('Vai brauksiet? Spiediet taustiņu 1 vai 2!')
  print('1. Jā')
  print('2. Nē')
  a = input()
  if a == ('2'):
    break
  else:
    print('Uz kuru galapunktu brauksiet?')
    print('1.', pilsetas[i])
    i= i+1
    print('2. Nebraukšu')
    d = input()
    if d == ('1'):
      print('Kontrolpunkta jaut: ', jaut[j])
      j = j+1
      k = input()
      while k != atbildes[x]:
        print('Nav pareizi, mēģini vēlreiz.')   
        k = input()
      else:
        print('Atbilde ir pareiza!')
        x = x+1
        if x>11:
          break
    else:
      break
if a == ('2'):
  print ('beigas')
elif a == ('1'):
  print('Malacis! Tu esi uzveicis Elektrisko Tūrisma Ralliju Liepāja 2022! Pateicamies par Jūsu dalību rallijā.')
else:
  print ('Nepareizā poga, mēģini vēlreiz!')