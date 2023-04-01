# OT Harjoitus työ 🐍

## Dokumentaatio

[Määrittelydokumentti](./dokumentaatio/vaatimusmaarittely.md)

[Työnaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

[Changelog](./dokumentaatio/changelog.md)

## Komentorivin komennot

Kaikki komentorivin komennnot edellyttävät, että olet asentanut poetryn komennolla:

```bash
poetry install
```

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

## Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

## Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```
