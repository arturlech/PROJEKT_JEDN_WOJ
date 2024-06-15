pracownicy_Warszawa: list = [

    {"imie": "Artur", "nazwisko": "Lech", "stanowisko": "Dowódca", "lokalizacja": "Warszawa_(miasto)"},
    {"imie": "Kamil", "nazwisko": "Bednarek", "stanowisko": "Oficer", "lokalizacja": "Warszawa_(miasto)"},

]
print(pracownicy_Warszawa)

pracownicy_Lublin: list = [

    {"imie": "Zuzanna", "nazwisko": "Orkisz", "stanowisko": "Kapral", "lokalizacja": "Lublin_(miasto)"},
    {"imie": "Kacper", "nazwisko": "Trzcina", "stanowisko": "Dowódca", "lokalizacja": "Lublin_(miasto)"},

]
print(pracownicy_Lublin)

pracownicy_Poznan: list = [

    {"imie": "Konrad", "nazwisko": "Kowaliski", "stanowisko": "Podoficer", "lokalizacja": "Poznań_(miasto)"},
    {"imie": "Wojciech", "nazwisko": "Michalak", "stanowisko": "Podporucznik", "lokalizacja": "Poznań_(miasto)"},

]
print(pracownicy_Poznan)

pracownicy_Bialystok: list = [

    {"imie": "Andrzej", "nazwisko": "Iwniak", "stanowisko": "Podoficer", "lokalizacja": "Białystok_(miasto)"},
    {"imie": "Mateusz", "nazwisko": "Skrzypczak", "stanowisko": "Chorąży", "lokalizacja": "Białystok_(miasto)"},

]
print(pracownicy_Bialystok)

pracownicy_Bydgoszcz: list = [

    {"imie": "Mariusz", "nazwisko": "Piotruk", "stanowisko": "Sierżant", "lokalizacja": "Bydgoszcz_(miasto)"},
    {"imie": "Martyna", "nazwisko": "Tupikowska", "stanowisko": "Dowódca", "lokalizacja": "Bydgoszcz_(miasto)"}

]
print(pracownicy_Bydgoszcz)

jednostki_wojskowe: list = [
    {"nazwa": "Sztab Generalny Wojska Polskiego", "pracownicy": pracownicy_Warszawa,"lokalizacja_jednostki": "Warszawa_(miasto)" },
    {"nazwa": "2 Lubelska Brygada Obrony Terytorialnej", "pracownicy": pracownicy_Lublin, "lokalizacja_jednostki": "Lublin_(miasto)"},
    {"nazwa": "2 Skrzydło Lotnictwa Taktycznego", "pracownicy": pracownicy_Poznan, "lokalizacja_jednostki": "Poznań_(miasto)"},
    {"nazwa": "Wojewódzki Sztab Wojskowy w Białymstoku", "pracownicy": pracownicy_Bialystok, "lokalizacja_jednostki": "Białystok_(miasto)"},
    {"nazwa": "Wojewódzki Sztab Wojskowy w Bydgoszczy", "pracownicy": pracownicy_Bydgoszcz, "lokalizacja_jednostki": "Bydgoszcz_(miasto)"},
]
print(jednostki_wojskowe)

pododdzialy: list = [
    {"nazwa_pododdziału": "Kompania Transportowa Sztabu Generalnego", "nazwa_jednostki": "Sztab Generalny Wojska Polskiego",
     "pracownicy": pracownicy_Warszawa, "lokalizacja_pododdzialu": "Warszawa_(miasto)"},
    {"nazwa_pododdziału": "Pluton Łączności Sztabu Generalnego", "nazwa_jednostki": "Sztab Generalny Wojska Polskiego",
     "pracownicy": pracownicy_Warszawa, "lokalizacja_pododdzialu": "Warszawa_(miasto)"},

    {"nazwa_pododdziału": "21. Batalion Lekkiej Piechoty w Lublinie", "nazwa_jednostki": "2 Lubelska Brygada Obrony Terytorialnej",
     "pracownicy": pracownicy_Lublin, "lokalizacja_pododdzialu": "Lublin_(miasto)"},
    {"nazwa_pododdziału": "Drużyna Strzelecka 22. Batalionu Lekkiej Piechoty",
     "nazwa_jednostki": "2 Lubelska Brygada Obrony Terytorialnej", "pracownicy": pracownicy_Lublin, "lokalizacja_pododdzialu": "Lublin_(miasto)"},

    {"nazwa_pododdziału": "Pluton Łączności 31. Bazy Lotnictwa Taktycznego ",
     "nazwa_jednostki": "2 Skrzydło Lotnictwa Taktycznego", "pracownicy": pracownicy_Poznan, "lokalizacja_pododdzialu": "Poznań_(miasto)"},
    {"nazwa_pododdziału": "Kompania Techniczna 32. Bazy Lotnictwa Taktycznego",
     "nazwa_jednostki": "2 Skrzydło Lotnictwa Taktycznego", "pracownicy": pracownicy_Poznan, "lokalizacja_pododdzialu": "Poznań_(miasto)"},

    {"nazwa_pododdziału": "15. Mazowiecka Brygada Obrony Terytorialnej","nazwa_jednostki": "Wojewódzki Sztab Wojskowy w Białymstoku",
     "pracownicy": pracownicy_Bialystok, "lokalizacja_pododdzialu": "Białystok_(miasto)"},
    {"nazwa_pododdziału": "Kompania Łączności 16. Pomorskiej Brygady Zmechanizowanej",
     "nazwa_jednostki": "Wojewódzki Sztab Wojskowy w Białymstoku", "pracownicy": pracownicy_Bialystok, "lokalizacja_pododdzialu": "Białystok_(miasto)"},

    {"nazwa_pododdziału": "Pluton Rozpoznawczy 16. Pomorskiej Brygady Zmechanizowanej",
     "nazwa_jednostki": "Wojewódzki Sztab Wojskowy w Białymstoku", "pracownicy": pracownicy_Bydgoszcz, "lokalizacja_pododdzialu": "Bydgoszcz_(miasto)"},
    {"nazwa_pododdziału": "16. Pomorska Brygada Zmechanizowana im. Króla Kazimierza Jagiellończyka", "nazwa_jednostki": "Wojewódzki Sztab Wojskowy w Białymstoku", "pracownicy": pracownicy_Bydgoszcz,
     "lokalizacja_pododdzialu": "Bydgoszcz_(miasto)"},
]
print(pododdzialy)


pracownicy: list = [
    {"imie": "Artur", "nazwisko": "Lech", "stanowisko": "Dowódca", "lokalizacja": "Warszawa_(miasto)"},
    {"imie": "Kamil", "nazwisko": "Bednarek", "stanowisko": "Oficer", "lokalizacja": "Warszawa_(miasto)"},
    {"imie": "Zuzanna", "nazwisko": "Orkisz", "stanowisko": "Kapral", "lokalizacja": "Lublin_(miasto)"},
    {"imie": "Kacper", "nazwisko": "Trzcina", "stanowisko": "Dowódca", "lokalizacja": "Lublin_(miasto)"},
    {"imie": "Konrad", "nazwisko": "Kowaliski", "stanowisko": "Podoficer", "lokalizacja": "Poznań_(miasto)"},
    {"imie": "Wojciech", "nazwisko": "Michalak", "stanowisko": "Podporucznik", "lokalizacja": "Poznań_(miasto)"},
    {"imie": "Andrzej", "nazwisko": "Iwniak", "stanowisko": "Podoficer", "lokalizacja": "Białystok_(miasto)"},
    {"imie": "Mateusz", "nazwisko": "Skrzypczak", "stanowisko": "Chorąży", "lokalizacja": "Białystok_(miasto)"},
    {"imie": "Mariusz", "nazwisko": "Piotruk", "stanowisko": "Sierżant", "lokalizacja": "Bydgoszcz_(miasto)"},
    {"imie": "Martyna", "nazwisko": "Tupikowska", "stanowisko": "Dowódca", "lokalizacja": "Bydgoszcz_(miasto)"}
]
print(pracownicy)