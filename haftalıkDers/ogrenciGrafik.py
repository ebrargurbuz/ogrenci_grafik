import matplotlib.pyplot as plt
import numpy as np


def calisma_programi(dosya_adi, ogrenci_adi):
    with open(dosya_adi,"w",encoding = "utf-8") as dosya:
        dosya.write(f"Ogrenci Adi: {ogrenci_adi}\n")
        dosya.write("Sinif: 1.sinif\n")
        dosya.write("Haftalik Calisma Programi: \n")
    
        dersler = ["Matematik","Fizik","Programlama"]
        
        for ders in dersler:
            saat = int(input(f"{ders} icin haftada kac saat ayirdiniz ?"))
            dosya.write(f"{ders}: {saat} saat\n")
            
    print(f"{ogrenci_adi} icin veriler dosyaya yazildi.")

calisma_programi("ebrar.txt", "Ebrar")
calisma_programi("eren.txt", "Eren")
calisma_programi("ela.txt", "Ela")
    
def veri_oku(dosya_adi):
    ders_saatleri = {}
    with open(dosya_adi,"r",encoding = "utf-8") as dosya:
        
        for satir in dosya:
            
            if "Matematik" in satir:
                saat = int(satir.strip().split(":")[1].split()[0])
                ders_saatleri["Matematik"] = saat
            elif "Fizik" in satir:
                saat = int(satir.strip().split(":")[1].split()[0])
                ders_saatleri["Fizik"] = saat
            elif "Programlama" in satir:
                saat = int(satir.strip().split(":")[1].split()[0])
                ders_saatleri["Programlama"] = saat
                
    return ders_saatleri

ogrenciler = {
    "Ebrar" : veri_oku("ebrar.txt"),
    "Eren" : veri_oku("eren.txt"),
    "Ela" : veri_oku("ela.txt")
}    
print(ogrenciler)               

ogrenci_isimleri = list(ogrenciler.keys())
dersler = ["Matematik","Fizik","Programlama"]

x = np.arange(len(dersler))

width = 0.25

plt.figure(figsize=(10, 6))
colors = ["#DDF92AFF", "#5B27D5", "#DE1375"]
for i, ogrenci in enumerate(ogrenci_isimleri):
    saatler = [ogrenciler[ogrenci][ders] for ders in dersler]
    plt.bar(x + i * width, saatler, width = width, label= ogrenci, color = colors[i])
    
plt.xlabel("Dersler")
plt.ylabel("Haftalik Calisma Saati")
plt.title("Ogrencilerin Haftalik Calisma Saatleri")
plt.xticks(x + width, dersler)
plt.legend()
plt.grid(axis = 'y', linestyle = '--', alpha = 0.5)
plt.tight_layout()

plt.show()


       
     