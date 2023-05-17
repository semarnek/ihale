def result(sozluk):
    max_bid = 0
    win = ""
    for key in sozluk:
        if sozluk[key] > max_bid:
            max_bid = sozluk[key]
            win = key
    return win, max_bid


print("Gizli müzayedeye hoşgeldiniz.")

name = ""
bid = 0
answer = ""
winner = []
dicti = {}

while answer != "h" and  answer != "hayır":
    name = input("İsminiz nedir?: ")
    bid = int(input("Teklifiniz nedir?: $"))
    answer = input("Başka teklif veren var mı? 'evet' veya 'hayır' yazınız.\n")
    dicti[name] = bid

winner = result(dicti)
print(f"Verilen ${winner[1]} teklifle ihalenin kazananı: {winner[0]}.")