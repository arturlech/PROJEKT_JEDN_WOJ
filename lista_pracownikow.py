jednostki = []


class Jednostka:
    def __init__(self, nazwa, pracownicy, lokalizacja_jednostek):
        self.nazwa = nazwa
        self.pracownicy = pracownicy
        self.lokalizacja_jednostek = lokalizacja_jednostek


def lista_jednostek(listbox_lista_jednostek):
    listbox_lista_jednostek.delete(0, END)
    for idx, jednostka in enumerate(jednostki):
        listbox_lista_jednostek.insert(idx, f'{jednostka.nazwa}  {jednostka.pracownicy} {jednostka.lokalizacja_jednostek}')


def dodaj_jednostke(entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostek,listbox_lista_jednostek):
    nazwa = entry_nazwa.get()
    pracownicy = entry_pracownicy.get()
    lokalizacja_jednostek = entry_lokalizacja_jednostek.get()
    print(nazwa, pracownicy, lokalizacja_jednostek)
    jednostki.append(Jednostka(nazwa, pracownicy, lokalizacja_jednostek))
    lista_jednostek(listbox_lista_jednostek)

    entry_nazwa.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_jednostek.delete(0, END)


    entry_nazwa.focus()


def usun_jednostke(listbox_lista_jednostek):
    i = listbox_lista_jednostek.index(ACTIVE)
    print(i)
    jednostki.pop(i)
    lista_jednostek(listbox_lista_jednostek)


def pokaz_szczegoly_jednoski(listbox_lista_jednostek, label_nazwa_szczegoly_obiektu_wartosc, label_pracownicy_szczegoly_obiektu_wartosc,label_lokalizacja_jednostek_szczegoly_obiektu_wartosc):
    i = listbox_lista_jednostek.index(ACTIVE)
    nazwa = jednostki[i].nazwa
    label_nazwa_szczegoly_obiektu_wartosc.config(text=nazwa)
    pracownicy = jednostki[i].pracownicy
    label_pracownicy_szczegoly_obiektu_wartosc.config(text=pracownicy)
    lokalizacja_jednostek = jednostki[i].lokalizacja_jednostek
    label_lokalizacja_jednostek_szczegoly_obiektu_wartosc.config(text=lokalizacja_jednostek)




def edytuj_jednostke(listbox_lista_jednostek, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostki, button_dodaj_jednostke):
    i = listbox_lista_jednostek.index(ACTIVE)
    entry_nazwa.insert(0, jednostki[i].nazwa)
    entry_pracownicy.insert(0, jednostki[i].pracownicy)
    entry_lokalizacja_jednostki.insert(0, jednostki[i].lokalizacja)

    button_dodaj_jednostke.config(text="Zapisz zmiany", command=lambda: aktualizuj_jednostke(i, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostki, button_dodaj_jednostke, listbox_lista_jednostek))


def aktualizuj_jednostke(i, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostki,  button_dodaj_jednostke, listbox_lista_jednostek):
    jednostki[i].nazwa = entry_nazwa.get()
    jednostki[i].pracownicy = entry_pracownicy.get()
    jednostki[i].lokalizacja_jednostki = entry_lokalizacja_jednostki.get()
    lista_jednostek(listbox_lista_jednostek)
    button_dodaj_jednostke.config(text="Dodaj jednostke", command=dodaj_jednostke())
    entry_nazwa.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_jednostki.delete(0, END)
    entry_nazwa.focus()


