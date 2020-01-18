#import necessary modules
import csv


# FUNKCJE 
def pobieranie_pliku_csv(plik_csv):
    plik = []
    # otwieramy plik csv i zapisujemy do zmiennej lokalnej f
    with open(plik_csv,'r')as f:
        # encoding='latin1'
    # ogarnac en-codin na znaki we francuskim
    # czytamy plik csv
        data = csv.reader(f)
    # wypisujemy kazdy wiersz jako liste
        for row in data:
            plik.append(row)
    print(plik)


# def tylko_2012_rok(zbior_list):
    #znalezc dany indeks kolumny ktory posiada w sobie 2012_...

    #wypisac dane


# def wykres_kolowy(dane):
    #wprowadzic dane
    #zadeklarowac legende
    #wyswietlic wykres kolowy przy uzyciu biblioteki


# def dany_wiersz(dane, nazwa):
    #wypisanie kolejnych wartosci z dane o wierszu nazwa


# def do_pliku_tekstowego(wynik, plik_txt)
    # wpisanie do pliku txt naszych wynikow
    # odpowiednio to przedstawic - rok, ilosc itd...


#def wykres_kolowy(dane):
    #wprowadzic dane
    #zadeklarowac legende
    #wyswietlic wykres liniowy przy uzyciu biblioteki

# PROGRAM
# pobranie pliku csv - wywolanie funkcji - pobieranie_pliku_csv i zapisujemy plik do zmiennej globalnej tablica
tablica1 = pobieranie_pliku_csv('crime-in-france.csv')

print(type(tablica1))

# wynik_2012 = tylko_2012_rok(tablica1)
# kolowy = wykres_kolowy(wynik1)

# tablica2 = pobieranie_pliku_csv('crime-in-france.csv')

# wynik_violation = dany_wiersz(tablica2,'Violation de domicile')
# wynik_doc = do_pliku_tekstowego(wynik_violation,'Violation.txt')

# tablica3 = pobieranie_pliku_csv('crime-in-france.csv')

# wynik_autres= dany_wiersz(tablica3,'Autres vols avec armes blanches')
# liniowy = wykres_liniowy(wynik_autres)




