# Webots-viivanseuraajarobotti

Webots-robotiikan case study, jossa e-puck-robotti seuraa viivaa kolmen pohja-anturin ja viritetyn PD-säätimen avulla.

## Portfolio case study

- [Portfolio-sivu](https://www.jibranhussain.com/projects/line-following-robot/)
- [English README](README.md)

## Projektin yhteenveto

Tavoitteena oli virittää viivanseuraajan säädin niin, että robotti suorittaa radan mahdollisimman nopeasti, mutta ajettu matka ja käyttäytyminen pysyvät hallittuina.

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

## Insinööriongelma

Viivanseuraajarobotin täytyy reagoida rataan nopeasti ilman, että liike muuttuu epävakaaksi. Liian heikko korjaus tekee robotista hitaan. Liian suuri nopeus tai vahvistus voi aiheuttaa sahaamista, moottorien saturaatiota tai epätasaista viivanseurantaa.

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

## Todisteaineisto

| Todiste | Tiedosto |
|---|---|
| Python-ohjain | [`line_follow.py`](line_follow.py) |
| Tekninen raportti | [`Robotics-viivanseuraaja.pdf`](Robotics-viivanseuraaja.pdf) |
| Simulaatiovideo | [`Task2_Vid.mp4`](Task2_Vid.mp4) |
| Tuloskuva | [`best possible scenario.png`](best%20possible%20scenario.png) |

## Mitä projekti osoittaa

- anturipohjainen takaisinkytkentä
- PD-säätimen viritys
- Webots-robottisimulaatio
- Python-ohjauslogiikka
- suorituskyvyn vertailu
- tekninen dokumentointi

## Huomio

Tämä repository toimii portfolio-projektin todistepakettina. Portfolio-sivu esittää projektin rekrytoijalle sopivassa muodossa, ja tämä repository sisältää lähdetiedostot, raportin, simulaatiovideon ja tuloskuvan tarkempaa tarkastelua varten.
