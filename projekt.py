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
    
    # zwraca liste kolejnych wierszy z pliku o formacie csv
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

def wykres_kolowy(dane):

    # podzielenie naszego słownika dane na dwie krotki
    krotki = list(dane.items())

    # sortowanie od najwiekszej do najmniejszej .......
    krotki.sort(key=lambda x: x[1], reverse=True)

    # tworzenie dwóch list, które będą pełnić funkcję argumentów(nazwy) i wartości(count) na naszym diagramie
    nazwy = []
    count = []

    # wybranie 20 największych, gdyż diagram z 107 zbrodni jest nieczytelny
    top_20 = krotki[:20]

    # z każdej krotki kolejno klucz dodawane są do argumentów i ilość to wartości
    for k, v in top_20:

        nazwy.append(k[:12])
        count.append(v)

    # tworzenie diagramu kołowego
    plt.pie(count, labels=nazwy, autopct='%1.1f%%')
    # wyświetlenie go
    plt.show()


def dany_wiersz(dane, nazwa):
    # w każdym wierszu naszej tablicy
    for row in dane:
        # szukamy gdzie znajduje sie wiersz z daną zbrodnią 'nazwa'
        if row[1] == nazwa:
            return dane[0], row


def do_pliku_tekstowego(wynik, plik_txt):
    # metodą w+ tworzymy i wpisujemy do nowego pliku tekstowego i zapisujemy lokalnie jako ext_file
    with open(plik_txt, 'w+', encoding='utf-8') as ext_file:
        # licznik
        i = 0
        # na początku dajemy nagłówki dla poszczególnych kolumn
        ext_file.write('okres   ilość \n')
        # scalamy lata i ilość wystąpień danej brodni w słownik oraz operujemy na dwóch zmiennych lokalnych
        for a, b in zip(wynik[0], wynik[1]):
            # dla pierwszego wiersza zostawiamy miejsce na nagłówek, który określiliśmy wyżej
            if i > 1:
                # nasze a to jest rok, w którym została popełniona dana zbrodnia
                ext_file.write(a + ' ')
                # nasze b to jest ilość występowania danej zbrodni
                ext_file.write(b + '\n')
            # zwiększamy licznik do momentu gdy a i b bedą znajdować się w naszym zestawieniu danej zbrodni
            i += 1

def wykres_liniowy(dane):

    # przypisujemy do labels nasze argumenty tj rok
    labels = dane[0][2:]
    # przypisujemy do vals nasze wartości tj ilość wystąpień podanej zbrodni
    vals = dane[1][2:]

    # tworzymy krotki z naszego słownika, który powstał przy użyciu zip()
    tups = list(zip(labels, vals))
    # sortujemy krotki od najmniejszej do największej
    tups.sort(key=lambda x: x[0])
    # ......
    labels, vals = zip(*tups)
    # Stworzenie listy z wartosci ?
    vals = [int(val) for val in vals]

    # rysowanie wykresu - wyświetlamy co 10-ty argument i co 10-tą wartośći, gdyż jest za dużo danych
    plt.plot(labels[::10], vals[::10]) 
    # dla lepszego widoku wykresu
    plt.xticks(rotation=90)
    # wyświetlamy wykres
    plt.show()




# PROGRAM
# pobranie pliku csv - wywołanie funkcji - pobieranie_pliku_csv i zapisujemy plik do zmiennej globalnej tablica
tablica1 = pobieranie_pliku_csv('crime-in-france.csv')

# print(type(tablica1))

# stworzenie diagramu kołowego dla zbrodni popełnionych w 2012 roku - tylko top 20
wynik_2012 = tylko_2012_rok(tablica1)
wykres_kolowy(wynik_2012)

# zapisanie do nowego pliku tekstowego 'tabelki' z ilością popełnienia zbrodni 'Violations de domicile' w kolejnych miesiącach i latach
wynik_violation = dany_wiersz(tablica1, 'Violations de domicile')
do_pliku_tekstowego(wynik_violation, 'Violation.txt')

# stworzenie wykresu liniowego dla zbrodni 'Autres vols avec armes blanches' w kolejnych miesiacach i latach
wynik_autres= dany_wiersz(tablica1, 'Autres vols avec armes blanches')
wykres_liniowy(wynik_autres)

# dowolne zestawienie...
# Homicides pour voler et à l'occasion de vols, Homicides pour d'autres motifs
# https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
# grupowy barchart




