import csv
from matplotlib import pyplot as plt


# FUNKCJE 
def pobieranie_pliku_csv(plik_csv):

    # tworzymy pustą listę, do której będziemy dodawać kolejno wiersze
    plik = []
    # otwieramy plik csv i zapisujemy do zmiennej lokalnej 'f'
    with open(plik_csv,'r', encoding='utf-8')as f:
    # czytamy plik csv
        data = csv.reader(f)
    # wypisujemy każdy wiersz jako liste
        for row in data:
            plik.append(row)
    
    #zwraca liste kolejnych wierszy z pliku o formacie csv
    return plik


def tylko_2012_rok(zbior_list):

    # tworzymy pusty słownik 'crime_dict' gdzie potem dodamy kolejno zbrodnie z 2012 roku
    crime_dict = {}
    # zmienna lokalna na potrzebę liczenia wartości od drugiego wiersza
    header_read = False

    # tworzenie listy tylko z kolumnami o nagłówku 2012_...
    columns = []

    # przegladamy każdy wiersz w naszej tablicy
    for row in zbior_list:
        
        if header_read == True:
            # licznik dla sumowania ilości danych zbrodni w 2012 roku
            occurrences = 0

            for column in columns:
                # dodajemy wartość poszczególnych kolumn 
                occurrences += int(row[column])

            # jesli wystepuje już dana zbrodnia to dodajemy kolejną jej sumę
            if row[1] in crime_dict:
                crime_dict[row[1]] += occurrences
            else:
                # jak nie, to zostawiamy dana liczbę, która jest już wcześniej ustalona przy petli for
                crime_dict[row[1]] = occurrences

        # najpierw występuje wiersz z nagłówkami
        if header_read == False:
            for element in row:
                # sprawdzamy dla każdego elementu czy w nagłówku pierwsze cztery znaki to 2012, nastepnie dodajemy do listy columns
                if element[:4] == '2012':
                    columns.append(row.index(element))
            # skoro wiemy ile jest kolumn to zmieniamy wartość 'header_read' na true aby wykonać drugą petlę
            header_read = True

    # sposób wyświetlania słownika - jeden pod drugim
    for k, v in crime_dict.items(): 
        print(k, v)

    #zwracamy słownik, który ma daną zbrodnie i jej ilość w 2012 roku
    return crime_dict


# źródła do wykresów:
# source:https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.pie.html
# source: https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py

# def wykres_kolowy(dane):



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




