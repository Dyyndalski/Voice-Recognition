## Voice-Recognition - program do rozpoznawanie płci osoby po jej głosie.

### Uruchamianie algorytmu dla pojedynczego pliku:
```
$ python inf145336_inf143919.py test/nazwa_pliku.wav
```

### Uruchamianie algorytmu dla całego folderu:
```
$ python inf145336_inf143919.py folder nazwa_folderu
```
##### Podajemy argument "folder", a za nim nazwę folderu z plikami audio.
###### Algorytm dla plików audio z nazwami typu "001_K.wav" lub "023_M.wav" zlicza liczbę znalezionych wyników w porównaniu do rzeczywistej liczby osób danej płci, których głosy znajdują się w folderze, a następnie wyznacza na tej podstawie skuteczność algorytmu.

### Dźwięki nagrane dodatkowo: (do skopiowania):
```
$ python inf145336_inf143919.py test/Janek.wav
```
```
$ python inf145336_inf143919.py test/Kasia.wav
```
```
$ python inf145336_inf143919.py test/Kacper.wav
```

Wyniki dla nagranych przez nas głosów są poprawne.
