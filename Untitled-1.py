class Kutuphane():
    def __init__(self,dosya_adi) -> None:
        self.dosya_adi=dosya_adi
        self.dosya=open(self.dosya,"a+")

    def kitap_ekle(self,kitap_adi,yazar):
        self.dosya_adi.write("{kitap_adi} - {yazar}\n")
    def kitaplari_listele(self):
        self.dosya.seek(0)
        kitaplar=self.dosya.read().splitlines()
        return kitaplar
    
    def dosya_adi(self):
        self.dosya.seek(0)
        return self.dosya.readlines()
    
    def dosyayi_kapat(self):
        self.dosya.close()

    def __del__(self):
        self.dosyayi_kapat()

kutuphane = Kutuphane("kitaplar.txt")
kutuphane.kitap_ekle("Beyaz Gemi","Cengiz Aytmatov")
kutuphane.kitap_ekle("Suç ve Ceza","Dostoyevski")
kitap_adi = input("Kitap adını girin: ")
yazar = input("Yazar adını girin: ")
sayfa_sayisi = input("Sayfa sayısını girin: ")
kutuphane.kitap_ekle(kitap_adi, yazar, sayfa_sayisi)
hedef_baslik=input("Kaldırmak istediğiniz kitabın başlığını girin:")
kutuphane.kitap_kaldir(hedef_baslik)
print("Kalan Kitaplar:")


#kitapları listeleme
print("kitaplar:")
kutuphane.kitaplari_listele()
kutuphane.dosyayi_kapat
lib=Kutuphane("kitaplar.txt")
def main():
    
    lib = Kutuphane("kitaplar.txt")
    def main():
  

    while True:
        # Menüyü göster
        menu_goster()

        # Kullanıcıdan seçim yapmasını iste
        secim = input("Lütfen bir seçenek seçin (1/2/3): ")

        # Kullanıcının seçimine göre ilgili işlemi gerçekleştir
        if secim == "1":
            print("\nKitaplar:")
            lib.kitaplari_listele()
        elif secim == "2":
            kitap_adi = input("Kitap adını girin: ")
            yazar = input("Yazar adını girin: ")
            sayfa_sayisi = input("Sayfa sayısını girin: ")
            lib.kitap_ekle(kitap_adi, yazar, sayfa_sayisi)
            print("Kitap eklendi!")
        elif secim == "3":
            hedef_baslik = input("Kaldırmak istediğiniz kitabın başlığını girin: ")
            lib.kitap_kaldir(hedef_baslik)
            print("Kitap kaldırıldı!")
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

    while True:
        # Menüyü göster
        menu_goster()

        # Kullanıcıdan seçim yapmasını iste
        secim = input("Lütfen bir seçenek seçin (1/2/3): ")

        # Kullanıcının seçimine göre ilgili işlemi gerçekleştir
        if secim == "1":
            print("\nKitaplar:")
            lib.kitaplari_listele()
        elif secim == "2":
            kitap_adi = input("Kitap adını girin: ")
            yazar = input("Yazar adını girin: ")
            sayfa_sayisi = input("Sayfa sayısını girin: ")
            lib.kitap_ekle(kitap_adi, yazar, sayfa_sayisi)
            print("Kitap eklendi!")
        elif secim == "3":
            hedef_baslik = input("Kaldırmak istediğiniz kitabın başlığını girin: ")
            lib.kitap_kaldir(hedef_baslik)
            print("Kitap kaldırıldı!")
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
