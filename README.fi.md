# Webots-viivanseuraajarobotti

Webots-robotiikkaprojekti, jossa e-puck-robotti seuraa viivaa kolmen pohja-anturin ja viritetyn PD-säätimen avulla.

## Projektin yhteenveto

Tavoitteena oli virittää viivanseuraajan säädin niin, että robotti ajaa radan mahdollisimman nopeasti, mutta ajettu matka ja käyttäytyminen pysyvät hallittuina.

Lopullinen vakaa viritystulos oli:

| Parametri | Lopullinen arvo |
|---|---:|
| `base_speed` | `5.6` |
| `Kp` | `7.0` |
| `Kd` | `0.85` |
| `SP` | `4.5` |
| Kierrosaika | `33.38 s` |
| Ajettu matka | `2.61 m` |

## Järjestelmä

- Simulaatioympäristö: Webots 2023b
- Robottimalli: e-puck
- Ohjauskieli: Python
- Anturit: kolme pohja-anturia
- Toimilaitteet: vasen ja oikea pyörämoottori
- Ohjaustapa: PD-säätö ja moottorinopeuden saturaatio

## Säätöidea

Säädin käyttää keskimmäistä pohja-anturia mittausarvona. Ohjaussignaali lasketaan PD-rakenteella:

```text
u = Kp * (SP - PV) - Kd * dPV
```

Ohjaussignaali jaetaan vasemman ja oikean pyörän nopeuksiin. Saturaatio pitää moottorikäskyt sallitun nopeusalueen sisällä.

## Viritysmenetelmä

Viritys tehtiin kokeellisesti:

1. Aloitus P-säädöllä.
2. `Kp`-arvon kasvatus vasteen parantamiseksi.
3. D-osan lisääminen nopeiden muutosten ja sahaamisen vaimentamiseksi.
4. `base_speed`-arvon kasvattaminen varovasti.
5. Kierrosajan, ajetun matkan ja vakauden vertailu.

Paras tulos ei ollut suurin mahdollinen nopeus. Lopullinen valinta oli kompromissi lyhyen kierrosajan, lyhyen ajomatkan ja vakaan käyttäytymisen välillä.

## Repositorion rakenne

```text
src/
  line_follow.py

docs/
  Robotics-viivanseuraaja.pdf

media/
  Task2_Vid.mp4

screenshots/
  best-result.png
```

## Todisteaineisto

Ohjainkoodi on tässä repositoriossa:

- [`src/line_follow.py`](src/line_follow.py)

Lisää nämä tiedostot GitHubin upload-toiminnolla, jotta repository on täydellinen:

- `docs/Robotics-viivanseuraaja.pdf` — tekninen raportti
- `media/Task2_Vid.mp4` — Webots-simulaation video
- `screenshots/best-result.png` — kuvakaappaus parhaasta tuloksesta

## Mitä projekti osoittaa

- anturipohjainen takaisinkytkentä
- PD-säätimen viritys
- Webots-robottisimulaatio
- Python-ohjauslogiikka
- suorituskyvyn vertailu
- tekninen dokumentointi

## English version

English description is available in [`README.md`](README.md).
