meme_dictonary = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Acemi, tecrübesiz kişi",
    "SHEESH": "Good Game, oyunun güzel geçtiğini belirtmek",
    "CREEPY": "Şüpheli davranış, Among Us oyununda kullanılan bir terim"
}
print("Merhaba ben sözlük  ")


for i in range(5):
    word = input("Anlamadığın bir kelime yaz kelimeyi yazın (hepsi BÜYÜK HARF olacak): ".format(i+1))
    word = word.strip().upper()   # girilen kelimeyi büyük harfe çeviriyoruz
    
    if word in meme_dictonary:
        print("Anlamı:", meme_dictonary[word])
    else:
        print("Malesef bu sözlükte kelime yok.")


