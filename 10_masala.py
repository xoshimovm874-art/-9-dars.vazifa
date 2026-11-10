import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

plt.bar(ismlar, ballar, color="blue")

plt.title("O'quvchilar natijalari")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")
plt.grid(axis="y")

eng_yuqori = max(ballar)
eng_past = min(ballar)
ortacha = sum(ballar) / len(ballar)

print("Eng yuqori ball:", eng_yuqori)
print("Eng past ball:", eng_past)
print("O'rtacha ball:", ortacha)

plt.savefig("oquvchilar_natijasi.png")
plt.show()

print("1. Eng yuqori ball Azizada: 95.")
print("2. Eng past ball Sardorda: 65.")
print("3. O'rtacha ball 81.83.")