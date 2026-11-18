class Noutbuklar_malumoti:

  def __init__(self, brend, model, narxi):
    self.brend = brend
    self.model = model
    self.narxi = narxi

  def malumotni_chiqar(self):
    return (
        f"Noutbuk: {self.brend} | Model: {self.model} | Narxi:"
        f" ${self.narxi}"
    )


noutbuk_1 = Noutbuklar_malumoti("Acer", "Aspire 7", 650)
noutbuk_2 = Noutbuklar_malumoti("HP", "Victus 15", 750)
noutbuk_3 = Noutbuklar_malumoti("ASUS", "TUF Gaming", 900)
noutbuk_4 = Noutbuklar_malumoti("Apple", "MacBook Air M2", 1100)

print(noutbuk_1.malumotni_chiqar())
print(noutbuk_2.malumotni_chiqar())
print(noutbuk_3.malumotni_chiqar())
print(noutbuk_4.malumotni_chiqar())
