# projekt-Python
projekt na zaliczenie z przedmiotu 'Wstęp do programowania' - Modelowanie Matematyczne i Analiza Danych na Uniwersytecie Gdańskim


### Zestawić dane typu:

* Sporządzić wykres kołowy poszczególnych przestępstw popełnionych w roku 2012 w stosunku do wszystkich w tym roku.
    * pobrac plik csv(funkcja-pobieranie_pliku_csv), zaznaczyć tylko rok 2012(kolumny) - funkcja-tylko_2012_rok, stworzyć wykres kołowy z biblioteki matplotlib(funkcja-wykres_kolowy) - dodać legende - poszczególne przestępstwa, kolorki itd...

* Przedstawić dane w pliku ”Violation.txt” ilość wystąpień przestępstwa Violation de domicile w danym
okresie.
    * pobrac plik csv(funkcja-pobieranie_pliku_csv), zaznaczyć tylko Violation de domicile(wiersze) - funkcja-dany_wiersz, skopiowanie danych do pliku 'Violation.txt' - funkcje-do_pliku_tekstowego,wyswietl_dokument(według danego okresu)

* Sporządzić wykres liniowy dla przestępstwa Autres vols avec armes blanches, ile wystąpień w danym
okresie.
    * pobrac plik csv(funkcja-pobieranie_pliku_csv), zaznaczyć tylko Autres vols avec armes blanches(wiersze) - funkcja-dany_wiersz, stworzyć wykres liniowy z biblioteki matplotlib(funkcja-wykres_liniowy) - dodać legende - poszczególny okres, kolorki itd...

*  Własne zestawienie z wykresem. (Pokusić się o przetłumaczenie poszczególnych przestępst wykorzystanych w analizie).
    * pobrac plik csv(funkcja-pobieranie_pliku_csv), dowolne zestawienie + wykres
    * zestawienie dwóch rodzaji zabójstw - Homicides pour voler et à l'occasion de vols (Zabójstwa za kradzież i rozbój), Homicides pour d'autres motifs (Zabójstwa z innych powodów) , a więc zaznaczyć tylko te dwa wiersze - funkcja - dany_wiersz, stworzyć wykres barchart z biblioteki matplotlib (funkcja - wykres_barchart) - dodać legende - poszczególne okresy, kolorki itd...


### Wymagania:
* max 3 strony dokumentacji w LateX (tytul projektu, nazwy autorow, treść projektu, funkcje(opis), przykładowe - wyniki, wykresy, dane) - wygenerować plik pdf 'nazwa_zespolu.pdf' 
* dane do projektu - https://www.kaggle.com/government-of-france/crimes-in-france/version/1
* plik pythona z funkcjami + plik tekstowy .txt
