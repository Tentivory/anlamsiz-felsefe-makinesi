#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin Anlamsız Felsefe Makinesi
Bu kod, insanlığın binlerce yıldır aradığı anlamı 0.003 saniyede bulur.
Bulamaz. Çünkü yoktur. Ama yine de çalışır.
"""

import random
import time
import base64

ozneler = [
    "Varlık", "Hiçlik", "Kahve", "Zaman", "İnsan", "Kedi", 
    "Güneş", "Rüzgar", "Düşünce", "Sandviç", "Sessizlik", "Gürültü"
]
fiiller = [
    "düşünür", "kaybolur", "bekler", "dans eder", "ağlar", 
    "güler", "sorar", "cevaplamaz", "uçar", "düşer", "susar", "bağırır"
]
nesneler = [
    "anlamı", "boşluğu", "kahvesini", "geleceği", "geçmişi", 
    "kedisini", "gölgesini", "hayatını", "ekmeğini", "soruyu", "cevapı", "hiçbir şeyi"
]

def derin_soz_uret():
    return f"{random.choice(ozneler)} {random.choice(fiiller)} {random.choice(nesneler)}."

def main():
    print("=" * 50)
    print("   EVRENİN ANLAMSIZ FELSEFE MAKİNESİ")
    print("         Sürüm 42.0 - Son Sürüm")
    print("=" * 50)
    print("\nSistem başlatılıyor...")
    print("Anlam aranıyor...")
    time.sleep(1.2)
    print("Anlam bulunamadı. Beklendiği gibi.")
    print("\n--- Derin Sözler Üretiliyor ---\n")
    
    for i in range(7):
        soz = derin_soz_uret()
        print(f"  [{i+1}] {soz}")
        time.sleep(0.4)
    
    print("\n" + "=" * 50)
    print("SONUÇ: Anlam, sandviçin içindeydi. Yedik.")
    print("Makine kapanıyor. Ya da kapanmıyor. Fark etmez.")
    print("=" * 50)
    
    # Gizli mesaj (base64): siyasi olmayan bir şey gibi görünür ama...
    gizli = "QmlyIGvDvG4gYmlyaW1pIGJpcmkgZ8O8bsO8biBiaXJpIG1pPw=="
    # print(base64.b64decode(gizli).decode())  # Açmak isteyen açar

if __name__ == "__main__":
    main()