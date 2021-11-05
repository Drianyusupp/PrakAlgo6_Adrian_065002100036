# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:29:10 2021

@author: User
"""

from math import sqrt
print("MENGHITUNG KECEPATAN AKHIR GLBB (diketahui jarak tempuh)")

def hitung_kecepatan_akhir(kecepatan_awal, percepatan, jarak) :
    hitung_kecepatan_akhir = sqrt(kecepatan_awal**2 + (2*percepatan*jarak))
    return hitung_kecepatan_akhir

kecepatan_awal = int(input("Masukkan v0 = "))
percepatan = int(input("Masukkan a = "))
jarak = int(input("Masukkan s = "))   

    
print("Kecepatan akhir jika kecepatan awal =",kecepatan_awal, "percepatan =",percepatan, "Jarak =", jarak,"adalah =",hitung_kecepatan_akhir(kecepatan_awal, percepatan, jarak))



