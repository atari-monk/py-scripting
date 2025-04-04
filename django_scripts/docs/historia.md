# Opowieść o Django

## 2025-04-02

## Cel

- Chcę nauczyć się Django.
- Pisać skrypty automatyzujące.
- To druga wersja repozytorium, ponieważ pierwsza była zbyt skomplikowana.
- Ta historia jest napisana ręcznie (bez użycia AI), aby utrzymać kontekst i zachować prostotę (mam tendencję do zbaczania).

## Struktura projektu

Zobacz strukturę i zachowaj prostotę, ale w uporządkowany sposób.

```plaintext
C:\atari-monk\code\py-scripting
├── .gitignore
├── .vscode
│   └── launch.json
├── django_scripts
│   ├── __init__.py
│   ├── data
│   │   └── django_gitignore.txt
│   ├── delete_project.py
│   ├── docs
│   │   ├── historia.md
│   │   └── story.md
│   ├── generate_project.py
│   ├── meta_model.py
│   ├── model_class.py
│   └── setup_django.py
└── index.md
```

## Konfiguracja Django

- Chcę skrypt 'setup_django.py', który:
- sprawdzi, czy framework jest zainstalowany,
- wyświetli wersję, jeśli jest,
- zapyta o aktualizację i zaktualizuje, jeśli użytkownik chce,
- zainstaluje, jeśli nie jest zainstalowany,
- musi być możliwość uruchomienia go w dowolnym momencie i w większym skrypcie, gdy konieczne jest sprawdzenie frameworka,
- na razie pomijam kwestie środowisk wirtualnych/globalnych itp.

## Sposób używania skryptów

- To bardzo ważne,
- W folderze głównym znajdują się foldery ze skryptami: root/scripts, ..., root/django_scripts,
- Wielokrotnie pisałem nakładki z menu do uruchamiania skryptów,
- Te nakładki powodowały, że gubiłem wątek za każdym razem,
- NIE RÓB ICH, CHYBA ŻE NA PÓŹNIEJ, GDY SKRYPTY BĘDĄ DOJRZAŁE,
- również nie chcę używać subprocess do uruchamiania skryptów partiami, lepiej trzymać się pojedynczo,
- uruchom jeden skrypt i przetwórz zmiany - to dobra zasada.

## Generowanie projektu

- Chcę skrypt do generowania projektu Django 'generate_project.py',
- wykonuje się, jeśli Django jest zainstalowane,
- tworzy pliki i projekt w folderze głównym, który jest folderem repozytorium,
- dodaje sekcje .gitignore związane z projektem Django,
- musi być możliwość uruchomienia go zarówno samodzielnie, jak i w większym skrypcie,
- używa input, jeśli brak parametrów, lub argparse dla parametrów z cli,
- sprawdza, czy projekt już istnieje,
- opcjonalnie aplikuje migracje,
- opcjonalnie uruchamia serwer, w nowym cli, aby był niezależny.

## Usuwanie testowego projektu

- skrypt 'delete_project.py' usuwa db.sqlite3, linkshelf, manage.py.

## 2025-04-04

## Refaktoryzacja skryptów do generowania w wybranym repozytorium

- 'generate_project.py'

```sh
python -m django_scripts.generate_project C:\atari-monk\code\linkshelf --gitignore-template C:\atari-monk\code\py-scripting\data\django_gitignore.txt
```

- 'generate_app.py'

```sh
python -m django_scripts.generate_app -p linkshelf -a links -r C:\atari-monk\code\linkshelf
```

## 2025-04-05

## Generowanie modelu

- skrypt 'meta_model.py',
- generuje reprezentację json modelu danych,
- skrypt 'model_class.py',
- generuje reprezentację klasy py modelu danych.
