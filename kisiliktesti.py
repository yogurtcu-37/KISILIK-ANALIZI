print(" KISILIK TESTINE HOS GELDIN ")
print(" SORULARI YANITLA VE KISILIK ANALIZINI GOR")
puan = 0
print("Soru 1- Haftasonu bolca bos zamanin var hangisini tercih edersin?")

print("1- Arkadaslarimla disari cikariz sinema,avm vb. yerlere gidip egleniriz")
print("2- Evde kalir, film veya dizi izlerim, kitap okurum, kafami dinlerim ")
print("3- Bos zamanim olamaz her zaman mesgul olurum")

cevap1 = input("Cevabin ne 1/2/3? ")

if cevap1 == "1":
    puan += 3
elif cevap1 == "2":
  puan += 4
elif cevap1 == "3":
  puan += 5

print("GUNCEL PUANIN ", puan)

print("Soru 2- Kalabalik bir ortamda uzun bir sure durman gerekiyor ne hissedersin ")

print("1- Enerji dolu ve patlamaya hazir, ortami canlandirir ve neselendiririm")
print("2- Elimden geldigince ayak uydurmaya calisirim")
print("3- En kisa zamanda ortami terk ederim cok vakit gecirmem")

cevap2 = input("Cevabin ne 1/2/3? ")
if cevap2 == "1":
    puan += 3
elif cevap2 == "2":
    puan += 4
elif cevap2 == "3":
    puan += 5

print("GUNCEL PUANIN ", puan)

print("Soru 3- En sevdigin,keyif aldigin film/dizi turu?")

print("1- Aksiyon, suc, polisiye gibi hareketli turleri severim")
print("2- Dram, romantizm, komedi gibi gundelik hayati anlatan turleri severim")
print("3- Gerilim, psikoloji, kisisel gelisim odakli icsel/zihinsel turleri severim")

cevap3 = input("Cevabin ne 1/2/3? ")
if cevap3 == "1":
    puan += 3
elif cevap3 == "2":
    puan += 4
elif cevap3 == "3":
    puan += 5

print("GUNCEL PUANIN ", puan)

if puan in [9, 10]:
    kume = 'A'
    print(" 1. BOLUMDEN ALDIGINIZ PUANLA A KUMESINE GIRDINIZ")

elif puan in [11,12,13]:
    kume = 'B'
    print("1. BOLUMDEN ALDIGINIZ PUANLA B KUMESINE DUSTUNUZ")

elif puan in [14,15]:
    kume = 'C'
    print("1. BOLUMDEN ALDIGINIZ PUANLA C KUMESINE DUSTUNUZ")
puan2 = 0
print("BOLUM 2'DE TEMAMIZI BIRAZ DEGISTIRIYORUZ SORULARI YANITLAMAYA DEVAM EDIN AZ KALDI")

print("Soru 1- Beklenmedik buyuk bir problemle karsilasirsan ilk ne yaparsin")
print("1- Sakin kalir ve tum olasiliklari analiz eder en dogru karari vermeye calisirim")
print("2- Hizlica dogru hamleyi yapmaya calisirim")
print("3- Icgudulerime guvenerek hareket ederim")

cevap4 = input("Cevabin ne 1/2/3? ")

if cevap4 == "1":
    puan2 += 3
elif cevap4 == "2":
    puan2 += 4
elif cevap4 == "3":
    puan2 += 5
print("YENI PUANIN ", puan2)

print("Soru 2- Karmasik bir sistemle karsi karsiyasin ne yaparsin ")
print("1- Kurcalayip hata yapa yapa ogrenmeye calisirim")
print("2- Varsa kilavuz kural vb. gostergeleri takip ederek ogrenmeye calisirim")
print("3- Deneyimli bir kisi bulup ondan ogrenirim")

cevap5= input("Cevabin ne 1/2/3? ")
if cevap5 == "1":
    puan2 += 3
elif cevap5 == "2":
    puan2 += 4
elif cevap5 == "3":
    puan2 += 5
    print("YENI PUANIN ", puan2)

print("Soru 3- Sana tarihte sadece 1 olayi degistirme hakki veriliyor ne yapardin")
print("1- Kuresel olarak yasanan en buyuk facialari onlemeye calisirdim")
print("2- Kendi cikarlarima kullanirdim")
print("3- Her seyi yasandigi gibi birakirdim hic birseyi degistirmezdim")

cevap6 = input("Cevabin ne 1/2/3? ")
if cevap6 == "1":
    puan2 += 3
elif cevap6 == "2":
    puan2 += 4
elif cevap6 == "3":
    puan2 += 5
print("YENI PUANIN ", puan2)

if puan2 == 9 or 10:
    kume2 = 'X'
    print("2. BOLUMDEN ALDIGINIZ PUANLA X KUMESINE DUSTUNUZ")
elif puan2 == 11 or 12 or 13:
    kume2 = 'Y'
    print("2. BOLUMDEN ALDIGINIZ PUANLA Y KUMESINE DUSTUNUZ")
elif puan2 == 14 or 15:
    kume2 = 'Z'
    print("2. BOLUMDEN ALDIGINIZ PUANLA Z KUMESINE DUSTUNUZ")

print("TEBRIKLER, TESTI TAMAMLADINIZ. SONUCLARINIZ:")

if kume == 'A' and kume2 == 'X':
    print("""Tebrikler, siz tam bir 'STRATEJIST LIDER'siniz. Sosyal ortamlarda enerjisiyle parlayan ama karar anlarında 
buz gibi soğukkanlı ve analitik kalan tip. Toplulukları peşinden sürüklerken arkasındaki mantık ağını kusursuz örer.""")

if kume == 'A' and kume2 == 'Y':
    print("""Tebrikler, siz tam bir 'Karizmatik Pragmatist'siniz. Ortamlara rahatça uyum sağlar, sohbeti başlatırsın ama
kimsenin seni kendi planlarından alıkoymasına izin vermezsin. Sosyalliği bir araç veya keyif olarak görür, odağını her
zaman kendi hedeflerinde tutarsın.""")

if kume == 'A' and kume2 == 'Z':
    print("""Tebrikler siz tam bir 'Spontane Sovmen'siniz. Bir şeyi uzun uzun analiz etmek veya detaylı planlar yapmak 
sana göre değil. Sezgilerine güvenir, anın tadını çıkarır ve doğaçlama yaşarsın. İnsanlar senin yanındayken asla
sıkılmaz çünkü ne zaman ne yapacağın kestirilemez.""")

if kume == 'B' and kume2 == 'X':
    print("""Tebrikler, siz tam bir 'Sessiz Mantikci'siniz. Boş konuşmalardan veya gereksiz kalabalıklardan hoşlanmazsın
Bir konu hakkında konuşuyorsan arkasında mutlaka mantıklı bir gerekçe veya veri vardır. Tarafsız, objektif ve güvenilir
bir gözlemcisin.""")

if kume == 'B' and kume2 == 'Y':
    print("""Tebrikler, siz tam bir 'Bagimsiz Gozlemci'siniz. Denge senin anahtar kelimen. Çevrendeki insanlarla aran
iyidir ama kimsenin iç dünyana müdahale etmesine izin vermezsin. Kendi standartlarına göre yaşar, başkalarının
beklentilerine göre şekil almazsın.""")

if kume == 'B' and kume2 == 'Z':
    print("""Tebrikler, siz tam bir 'Keyifci'siniz. Stressiz bir yaşam senin için en doğrusudur. Bir problem çıktığında
paniklemez veya teoriler üretmezsin; içgüdün ne diyorsa onu yapar ve akışına bırakırsın. Rahatlığın ve doğallığın
çevrendekilere de huzur verir.""")

if kume == 'C' and kume2 == 'X':
    print("""Tebrikler, siz tam bir 'Derin Mimar'siniz. Kalabalıklar enerjini tüketir; senin en verimli olduğun yer
kendi zihnindir. Karmaşık problemleri tek başına çözmekte, verileri birleştirmekte ve mantıksal derinlik yakalamakta
üstüne yoktur. Tam bir "arkadaki gizli beyin" profilisin.""")

if kume == 'C' and kume2 == 'Y':
    print("""Tebrikler siz tam bir 'Yalniz Kurt'sunuz. Kendi kendine yetebilmek senin en büyük gücün. Başkalarının
onayına veya sosyal etkileşime ihtiyaç duymazsın. Kendi kurallarını koyar, kendi sınırlarında sessizce ve kararlılıkla
ilerlersin.""")

if kume =='C' and kume2 == 'Z':
    print("""Tebrikler, siz tam bir 'Mistik Hayalperest'siniz. Klasik kalıplara veya katı kurallara uymak sana zor
gelir. Dünyayı mantıkla değil, hislerinle ve sezgilerinle algılarsın. Kendi kabuğunda, dış dünyanın gürültüsünden uzak
durarak kendi içsel rehberini takip edersin.""")

input("Testimize zaman ayirdiginiz icin cok tesekkur ederim dusunceleriniz nelerdir? ")