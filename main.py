meme_dictonary = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }


word = input("Anlamadığınız bir kelime yazın hepsi büyük harf olacak")

if word in meme_dictonary.keys():
    meaning = meme_dictonary[word]
    print('Anlamı:',meaning)
else:
    print("Malesef  bu  sözlükte kelime yok.")


