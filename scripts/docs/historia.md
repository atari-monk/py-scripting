### Historia o sktyptach w pythonie

**2025-04-03**

---

## markdown_to_text.py

- skrypt pobierający markdown ze schowka
- konwertuje go na zwykły tekst
- umieszcza go z powrotem w schowku

## remove_comments.py

- skrypt usuwa komentarze z pliku `.py` i zapisuje go ponownie
- jedna funkcja obsługuje tylko jeden typ komentarzy
- pobiera ścieżkę pliku z `argparse` lub wejścia

- TO SPRAWIŁO MI OGROMNY PROBLEM
- komentarze w Pythonie są naprawdę złożone, mają wiele struktur
- rozwiązania generowane przez AI zawodziły
- zacząłem od najprostszego pliku
- najprostsza funkcja do usunięcia najprostszego komentarza
- uruchomiłem skrypt, by go przetestować, i wygenerowałem `unittest`
- nie chcę używać `re` ani żadnej biblioteki, tylko proste przetwarzanie tekstu
- wejście i wyjście jasno pokazuje, jakie komentarze można usunąć
- jest wiele wyjątków, więc wykrywam je i pomijam takie przypadki
- jeśli nie jest to proste, to nie zadziała

## testy w Pythonie

- chcę skonfigurować testy jednostkowe w Pythonie
- `test_remove_comments.py`
- uruchamianie:

```sh
python -m unittest .\tests\test_remove_comments.py
```

- debugowanie w VSCODE za pomocą `launch.json`

## fs_tree.py

- drukuje strukturę katalogów i plików w podanej ścieżce
- pobiera ścieżkę pliku z `argparse` lub wejścia
- zapisuje wynik do pliku `.md` oraz schowka
