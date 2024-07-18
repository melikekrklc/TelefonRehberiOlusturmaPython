kisiAdi=' '
while kisiAdi != 'sonlandır':
 F=open('D:/rehber.txt','r+')
 kisiAdi=input('Lütfen kisinin adını giriniz:')
 rehber=[]
 for l in F:
     ls=l.strip()
     ll=ls.split()
     if ll[0]==kisiAdi:
         print(l)
         break
     else:
         kayıt=input('Kisi kaydedilsin mi : ')
         if kayıt=='EVET' or 'evet':
          soyad=input('Kisinin soyadını giriniz: ')
          numara=input('Kisinin telefon numarasını giriniz: ')
          rehber.append([kisiAdi,soyad,numara])
          for a in rehber:
               for i in a: 
                 F.write(str(i)+' ')
               F.write('\n')
         else:
             continue
F.close()
