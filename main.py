import csv
from matplotlib import pyplot as plt

# funkcje


def pobieranie_pliku_csv(plik_csv):

    plik = []
    # otwieramy plik csv i zapisujemy do zmiennej lokalnej f
    with open(plik_csv, 'r', encoding='utf-8')as f:
        # encoding='latin1'
    # ogarnac en-codin na znaki we francuskim
    # czytamy plik csv
        data = csv.reader(f)
    # wypisujemy kazdy wiersz jako liste
        for row in data:
            plik.append(row)

    return plik


def tylko_2012_rok(zbior_list):

    crime_dict = {}
    header_read = False

    columns = []

    for row in zbior_list:

        if header_read == True:

            occurrences = 0

            for column in columns:
                occurrences += int(row[column])

            if row[1] in crime_dict:
                crime_dict[row[1]] += occurrences
            else:
                crime_dict[row[1]] = occurrences


        if header_read == False:
            for element in row:
                if element[:4] == '2012':
                    columns.append(row.index(element))

            header_read = True

    for k, v in crime_dict.items():  # sposób wyświetlania słownika
        print(k, v)

    return crime_dict


# source:https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.pie.html
# source: https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py


def wykres_kolowy(dane):

    krotki = list(dane.items())

    krotki.sort(key=lambda x: x[1], reverse=True)

    nazwy = []
    count = []

    top_20 = krotki[:20]

    for k, v in top_20:

        nazwy.append(k[:12])
        count.append(v)

    plt.pie(count, labels=nazwy, autopct='%1.1f%%', shadow=True)
    plt.show()



def dany_wiersz(dane, nazwa):

    for row in dane:
        if row[1] == nazwa:
            return dane[0], row



def do_pliku_tekstowego(wynik, plik_txt):

    with open(plik_txt, 'w+', encoding='utf-8') as ext_file:

        i = 0

        ext_file.write('okres   ilość \n')

        for a, b in zip(wynik[0], wynik[1]):

            if i > 1:
                ext_file.write(a + ' ')
                ext_file.write(b + '\n')

            i += 1


def wykres_liniowy(dane):

    labels = dane[0][2:]
    vals = dane[1][2:]

    tups = list(zip(labels, vals))

    tups.sort(key=lambda x: x[0])

    labels, vals = zip(*tups)

    vals = [int(val) for val in vals]

    plt.plot(labels[::10], vals[::10])  # wybieranie ile i co ile wyświetlamy daty etc
    plt.xticks(rotation=90)
    plt.show()


# PROGRAM
# pobranie pliku csv - wywolanie funkcji - pobieranie_pliku_csv i zapisujemy plik do zmiennej globalnej tablica
tablica1 = pobieranie_pliku_csv('crimes.csv')

wynik_2012 = tylko_2012_rok(tablica1)
wykres_kolowy(wynik_2012)

wynik_violation = dany_wiersz(tablica1, 'Violations de domicile')

do_pliku_tekstowego(wynik_violation, 'Violation.txt')

wynik_autres= dany_wiersz(tablica1, 'Autres vols avec armes blanches')
wykres_liniowy(wynik_autres)
