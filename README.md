# OT Harjoitus työ 🐍

## Dokumentaatio

[Määrittelydokumentti](./dokumentaatio/vaatimusmaarittely.md)

[Työnaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

[Changelog](./dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](./dokumentaatio/kayttoohje.md)

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

## Koodin laadun tarkastus

Koodin laadun tarkastuksen voi tehdä komennolla:

```bash
poetry run invoke lint
```
