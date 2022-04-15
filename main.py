class Main(object):
    def __init__(self, scores, name):
        self.scores = scores
        self.name = name
with open('egyszam.txt') as f:
    data_read = [i.strip().split(' ') for i in f.readlines()]

data = []
k = len(data_read[0])
for i in data_read:
    data.append(Main(i[0:k-1], i[-1]))

#3.fel
print("3.Feladat: Játékosok száma:", len(data))
#4.Fel
print("4.Feladat: Fordulók száma:", len(data[0].scores))
#5.fel
for i in data:
    if i.scores[0] == '1':
        print("5.Feladat: Az első fordulóban volt egyes tipp")
        break
#6.fel
legnagyobb = 0
for i in data:
    for k in i.scores:
        if int(k) > int(legnagyobb):
            legnagyobb = k
print("6.feladat A legnagyobb tipp a fordulók során:", legnagyobb)
#7.fel
score_in = input("7.Feladat: Kérem a forduló sorszámát [1-" + str(len(data)) + "]: ")
if int(score_in) > len(data):
    print('Error')
#Meguntam majd folyt kov
