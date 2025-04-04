# Historia o Django

## **2025-04-02**

## Cel

- Chcę nauczyć się Django.
- Pisać skrypty automatyzujące.
- To jest druga wersja repozytorium, ponieważ pierwsza była zbyt skomplikowana.
- Ta historia jest pisana ręcznie (bez AI), aby utrzymać kontekst i zachować maksymalną prostotę (mam tendencję do odbiegania od tematu).

## Struktura projektu

Zachowaj strukturę prostą, ale dobrze zorganizowaną.

```plaintext
C:\atari-monk\code\learn-django
├── docs
│   └── story.md
├── index.md
└── script
    ├── generate_project.py
    └── setup_django.py
```

## Konfiguracja Django

- Chcę skrypt `setup_django.py`, który:
  - sprawdzi, czy framework jest zainstalowany,
  - wypisze wersję, jeśli jest,
  - zapyta o aktualizację i zaktualizuje, jeśli użytkownik wyrazi zgodę,
  - zainstaluje Django, jeśli nie jest zainstalowane,
  - musi być możliwy do uruchomienia w każdej chwili oraz w większym skrypcie, gdy framework wymaga sprawdzenia,
  - na razie pominąłem kwestię środowiska wirtualnego/globalnego i podobnych rzeczy,
  - przetestowany.

## Sposób używania skryptów

- To jest bardzo ważne.
- W folderze głównym znajduje się folder `script`.
- Uruchamiam skrypty za pomocą:

  ```sh
  python .\script\setup_django.py
  ```

- Czyszczę konsolę poleceniem:

  ```sh
  cls
  ```

- Wiele razy pisałem wrappery z menu do uruchamiania skryptów.
- Te wrappery do uruchamiania skryptów za każdym razem powodowały, że traciłem wątek.
- **NIE PISZ ICH**, **CHYBA ŻE** **DUŻO PÓŹNIEJ, GDY SKRYPTY SĄ DOJRZAŁE**.
- Nie chcę używać `subprocess` do uruchamiania skryptów w serii — lepiej robić to pojedynczo.
- **Reguła:** Uruchom jeden skrypt, przetwórz zmiany — to dobre podejście.

## Generowanie projektu

- Chcę skrypt do generowania projektu Django: `generate_project.py`.
- Skrypt znajduje się w `root/script`.
- Tworzy pliki i projekt w katalogu głównym.
- Dodaje sekcje `.gitignore` związane z projektem Django.
- Musi działać zarówno samodzielnie, jak i w większym skrypcie.
- Nagłówek funkcji:

  ```python
  def generate_project(project_name=None, skip_migrations=False, skip_runserver=False):
  ```

- Jeśli argumenty są `None`, używa `input()`, a dla CLI używa `argparse`.
- Sprawdza, czy projekt już istnieje.
- Opcjonalnie stosuje migracje.
- Opcjonalnie uruchamia serwer w nowym terminalu, aby działał niezależnie.
- Użycie:

  ```sh
  python .\script\generate_project.py myproject
  ```

  lub opcjonalnie:

  ```sh
  python .\script\generate_project.py myproject --skip-migrations --skip-runserver
  ```

- Przetestowany.

## .gitignore

- Ignorowany projekt `linkshelf` podczas testowania skryptów.
- Ignorowany folder `helpers` zawierający tymczasowe skrypty pomocnicze.
- Ignorowany `manage.py` z testowego projektu Django.

## Usuwanie testowego projektu

- Skrypt `delete_project.py` usuwa `db.sqlite3`, `linkshelf`, `manage.py`.
- Przetestowany.

**2025-04-03**

---
