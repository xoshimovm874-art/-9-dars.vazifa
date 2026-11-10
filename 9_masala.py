import matplotlib.pyplot as plt

oylar = [1, 2, 3, 4, 5, 6, 7]
savdo = [20, 25, 30, 28, 35, 40, 45]

plt.plot(oylar, savdo, marker="o")

plt.title("Oylik savdo")
plt.xlabel("Oylar")
plt.ylabel("Savdo")
plt.grid()

plt.savefig("natija.png")
plt.show()