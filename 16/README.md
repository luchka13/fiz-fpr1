# Vrtenje in vztrajnostni moment telesa

**Datum meritev**: 27. 10. 2017

**Merila**:
- Žiga Patačko Koderman
- Ploj Yap

Meritve opravljene po navodilih v [vrtenje_in_vztrajnostni_moment_telesa.pdf](vrtenje_in_vztrajnostni_moment_telesa.pdf).

Vsebine map:
- `brez_dodatnih_koles` - samo glavno kolo, ki ga pospešeno vrti utež, katere teža je zapisana v imenu posamezne datoteke,
- `gibljivo_vpeta_dodatna_kolesa` - gibljivo vpeta_dodatna_kolesa, glavno kolo pa vrti utež, katere teža je zapisana v imenu posamezne datoteke,
- `togo_vpeta_dodatna_kolesa` - togo vpeta_dodatna_kolesa, glavno kolo pa vrti utež, katere teža je zapisana v imenu posamezne datoteke,
- `upor_lezaja` - kolo zavrteno z roko, da določimo približen upor ležaja,

Originalne meritve so bile zapisane narobe: Logger Pro je izvoz v csv (Comma Separated Values) naredil tako, da je vejico uporabil tako za ločilo med podatki kot za decimalno ločilo. Originalne datoteke so bile zato popravljene z programom `convert.py`, prepoznamo pa jih po predponi `'converted_'`.