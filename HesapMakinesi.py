import tkinter as tk
#Ana Sayfanın Oluşturulması:
Sayfa = tk.Tk()
Sayfa.geometry("250x200+650+300")
#Sayı girişi için Entry hazırlanması:
SayıGirişi = tk.Entry(Sayfa, justify = 'center', width = 30)
SayıGirişi.pack()
SayıGirişi.place(x = 30, y = 20)
#Sayı butonlarının oluşturulması:
buton = []
def rakam(x):
    Sayı = len(SayıGirişi.get())
    SayıGirişi.insert(Sayı, x)
for Butonlar in range(1,10):
    buton.append(tk.Button(Sayfa, text = str(Butonlar), command = lambda x=Butonlar:rakam(x), width = 3, height = 1))
Sayaç = 0
for a in range(0,3):
    for b in range(0,3):
        buton[Sayaç].place(x = 30 + b * 35, y = 50 + a * 35)
        Sayaç += 1
Sıfır = tk.Button(Sayfa, text = 0, command = lambda x = 0:rakam(x), width = 3, height = 1)
Sıfır.place(x = 30, y = 155)
#Nokta Butonu Oluşturulması:
def NoktaButonu():
    Sayı = len(SayıGirişi.get())
    SayıGirişi.insert(Sayı, '.')
Nokta = tk.Button(Sayfa, text = ".", command = NoktaButonu, width = 3)
Nokta.place(x = 65, y = 155)
#Eşittir Butonu Oluşturulması:
Sayı2 = 0
def EşittirButonu():
    global Sayı2
    Sayı2 = float(SayıGirişi.get())
    global Hesap
    Sonuç = 0
    global Sayı
    if(Hesap == 0):
        Sonuç = Sayı + Sayı2
    elif(Hesap == 1):
        Sonuç = Sayı - Sayı2
    elif(Hesap == 2):
        Sonuç = Sayı * Sayı2
    elif(Hesap == 3):
        Sonuç = Sayı / Sayı2
    else:
        SayıGirişi.insert(0, "Lütfen bir değer girin.")
    SayıGirişi.delete(0, 'end')
    SayıGirişi.insert(0, str(Sonuç))
Eşittir = tk.Button(Sayfa, text = '=', command = EşittirButonu, width = 3, fg = 'BLUE')
Eşittir.place(x = 100, y = 155)
#Silme ve İşlemler Butonları Oluşturulması:
İşlem = []
Hesap = 0
Sayı = 0
def İşlemYapma(x):
    global Hesap
    Hesap = x
    global Sayı
    Sayı = float(SayıGirişi.get())
    SayıGirişi.delete(0, 'end')
for İşlemler in range(0,4):
    İşlem.append(tk.Button(Sayfa, width = 3, height = 1, command = lambda x = İşlemler:İşlemYapma(x)))
İşlem[0]['text'] = "+"
İşlem[1]['text'] = "-"
İşlem[2]['text'] = "*"
İşlem[3]['text'] = "/"
for a in range(0,4):
    İşlem[a].place(x = 140, y = 50 + 35 * a)
#Silme tuşu ve fonksiyonu:
def SilmeButonu():
    Silme = len(SayıGirişi.get())
    SayıGirişi.delete(Silme - 1,tk.END)
Silme = tk.Button(Sayfa, text = 'Sil', command = SilmeButonu, width = 3)
Silme.place(x = 175, y = 85)
#Temizleme tuşu ve fonksiyonu:
def TemizlemeTuşu():
    SayıGirişi.delete(0, 'end')
Temizle = tk.Button(Sayfa, text = 'CE', command = TemizlemeTuşu, width = 3)
Temizle.place(x = 175, y = 50)
#Ana Sayfanın Çalıştırılması:
Sayfa.mainloop()