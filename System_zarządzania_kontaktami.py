# -*- coding: utf-8 -*-

import csv
import re

nazwa_pliku = r"E:\PROJECT\MONEVOWO\System_zarządzania_kontaktami\kontakty.csv"

class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, {self.telefon}, {self.email}"



def walidacja_telefonu(telefon):
    # Sprawdzenie, czy numer telefonu ma 9 cyfr
    return re.match(r'^\d{9}$', telefon) is not None



def walidacja_email(email):
    # Sprawdzenie, czy adres email ma odpowiedni format
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None



def wczytaj_kontakty_z_pliku(nazwa_pliku):
    kontakty = []
    try:
        with open(nazwa_pliku, mode='r', newline='', encoding='utf-8-sig') as plik:
            czytnik = csv.reader(plik)
            next(czytnik)  # Pomijamy nagłówek
            for wiersz in czytnik:
                # Sprawdzamy, czy wiersz ma dokładnie 4 elementy
                if len(wiersz) == 4:
                    imie, nazwisko, telefon, email = wiersz
                    kontakt = Kontakt(imie, nazwisko, telefon, email)
                    kontakty.append(kontakt)
                else:
                    print(f"Zignorowano nieprawidłowy wiersz: {wiersz}")
    except FileNotFoundError:
        print("Plik nie istnieje, zostanie utworzony nowy.")
    return kontakty




def zapisz_kontakty_do_pliku(nazwa_pliku, kontakty):
    with open(nazwa_pliku, mode='w', newline='', encoding='utf-8-sig') as plik:
        pisarz = csv.writer(plik)
        pisarz.writerow(['Imie', 'Nazwisko', 'Telefon', 'Email'])  # Poprawiony nagłówek
        for kontakt in kontakty:
            pisarz.writerow([kontakt.imie, kontakt.nazwisko, kontakt.telefon, kontakt.email])



def dodaj_kontakt(kontakty, imie, nazwisko, telefon, email):
    if not walidacja_telefonu(telefon):
        print("Blad: Nieprawidlowy format numeru telefonu.")
        return
    if not walidacja_email(email):
        print("Blad: Nieprawidlowy format adresu email.")
        return
    nowy_kontakt = Kontakt(imie, nazwisko, telefon, email)
    kontakty.append(nowy_kontakt)
    print("Kontakt zostal dodany.\n")



def edytuj_kontakt(kontakty, indeks, imie, nazwisko, telefon, email):
    if indeks < 0 or indeks >= len(kontakty):
        print("Blad: Kontakt o podanym indeksie nie istnieje.")
        return
    if not walidacja_telefonu(telefon):
        print("Blad: Nieprawidlowy format numeru telefonu.")
        return
    if not walidacja_email(email):
        print("Blad: Nieprawidlowy format adresu email.")
        return
    kontakt = kontakty[indeks]
    kontakt.imie = imie
    kontakt.nazwisko = nazwisko
    kontakt.telefon = telefon
    kontakt.email = email
    print("Kontakt zostal zaktualizowany.\n")



def usun_kontakt(kontakty, indeks):
    if indeks < 0 or indeks >= len(kontakty):
        print("Blad: Kontakt o podanym indeksie nie istnieje.")
        return
    kontakty.pop(indeks)
    print("Kontakt zostal usuniety.\n")



def wyswietl_kontakty(kontakty):
    if not kontakty:
        print("Brak zapisanych kontaktow.\n")
        return
    for i, kontakt in enumerate(kontakty):
        print(f"{i + 1}. {kontakt}")



def main():
    nazwa_pliku = "kontakty.csv"
    kontakty = wczytaj_kontakty_z_pliku(nazwa_pliku)

    while True:
        print("---MENU---")
        print("\n1. Wyswietl kontakty")
        print("2. Dodaj kontakt")
        print("3. Edytuj kontakt")
        print("4. Usun kontakt")
        print("5. Zapisz i wyjdz")
        wybor = input("Wybierz opcje: ")

        if wybor == '1':
            wyswietl_kontakty(kontakty)
        
        elif wybor == '2':
            imie = input("\nPodaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            telefon = input("Podaj telefon: ")
            email = input("Podaj email: ")
            dodaj_kontakt(kontakty, imie, nazwisko, telefon, email)
        
        elif wybor == '3':
            wyswietl_kontakty(kontakty)
            indeks = int(input("\nPodaj numer kontaktu do edytowania: ")) - 1
            imie = input("Podaj nowe imie: ")
            nazwisko = input("Podaj nowe nazwisko: ")
            telefon = input("Podaj nowy telefon: ")
            email = input("Podaj nowy email: ")
            edytuj_kontakt(kontakty, indeks, imie, nazwisko, telefon, email)
       
        elif wybor == '4':
            wyswietl_kontakty(kontakty)
            indeks = int(input("\nPodaj numer kontaktu do usuniecia: ")) - 1
            usun_kontakt(kontakty, indeks)
        
        elif wybor == '5':
            zapisz_kontakty_do_pliku(nazwa_pliku, kontakty)
            print("\nDane zostaly zapisane. Do widzenia!")
            break
       
        else:
            print("\nBlad: Nieprawidlowa opcja.")

if __name__ == "__main__":
    main()
