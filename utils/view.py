from tkinter import *

login_1: str = "Artur"
login_2: str = "Zuzanna"
login_3: str = "Kamil"
login_4: str = "Mateusz"
login_5: str = "Mariusz"
login_6: str = "Wojciech"
login_7: str = "Kacper"
login_8: str = "Andrzej"
login_9: str = "Konrad"
login_10: str = "Martyna"
haslo_1: str = "Pracownik1"
haslo_2: str = "Pracownik2"
haslo_3: str = "Pracownik3"
haslo_4: str = "Pracownik4"
haslo_5: str = "Pracownik5"
haslo_6: str = "Pracownik6"
haslo_7: str = "Pracownik7"
haslo_8: str = "Pracownik8"
haslo_9: str = "Pracownik9"
haslo_10: str = "Pracownik10"

pracownicy = []


class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, lokalizacja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.lokalizacja = lokalizacja


def lista_uzytkownikow(listbox_lista_pracownikow):
    listbox_lista_pracownikow.delete(0, END)
    for idx, pracownik in enumerate(pracownicy):
        listbox_lista_pracownikow.insert(idx,
                                         f'{pracownik.imie}  {pracownik.nazwisko} {pracownik.stanowisko} {pracownik.lokalizacja}')


def dodaj_uzytkownika(entry_imie, entry_nazwisko, entry_stanowisko, entry_lokalizacja, listbox_lista_pracownikow):
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    stanowisko = entry_stanowisko.get()
    lokalizacja = entry_lokalizacja.get()
    print(imie, nazwisko, stanowisko, lokalizacja)
    pracownicy.append(Pracownik(imie, nazwisko, stanowisko, lokalizacja))
    lista_uzytkownikow(listbox_lista_pracownikow)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_stanowisko.delete(0, END)
    entry_lokalizacja.delete(0, END)

    entry_imie.focus()


def usun_uzytkownika(listbox_lista_pracownikow):
    i = listbox_lista_pracownikow.index(ACTIVE)
    print(i)
    pracownicy.pop(i)
    lista_uzytkownikow(listbox_lista_pracownikow)


def pokaz_szczegoly_uzytkownikow(listbox_lista_pracownikow, label_imie_szczegoly_obiektu_wartosc,
                                 label_nazwisko_szczegoly_obiektu_wartosc, label_stanowisko_szczegoly_obiektu_wartosc,
                                 label_lokalizacja_szczegoly_obiektu_wartosc):
    i = listbox_lista_pracownikow.index(ACTIVE)
    imie = pracownicy[i].imie
    label_imie_szczegoly_obiektu_wartosc.config(text=imie)
    nazwisko = pracownicy[i].nazwisko
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=nazwisko)
    stanowisko = pracownicy[i].stanowisko
    label_stanowisko_szczegoly_obiektu_wartosc.config(text=stanowisko)
    lokalizacja = pracownicy[i].lokalizacja
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=lokalizacja)


def edytuj_uzytkownika(listbox_lista_pracownikow, entry_imie, entry_nazwisko, entry_stanowisko, entry_lokalizacja,
                       button_dodaj_uzytkownika):
    i = listbox_lista_pracownikow.index(ACTIVE)
    entry_imie.insert(0, pracownicy[i].imie)
    entry_nazwisko.insert(0, pracownicy[i].nazwisko)
    entry_stanowisko.insert(0, pracownicy[i].stanowisko)
    entry_lokalizacja.insert(0, pracownicy[i].lokalizacja)

    button_dodaj_uzytkownika.config(text="Zapisz zmiany",
                                    command=lambda: aktualizuj_uzytkownika(i, entry_imie, entry_nazwisko,
                                                                           entry_stanowisko, entry_lokalizacja,
                                                                           button_dodaj_uzytkownika,
                                                                           listbox_lista_pracownikow))


def aktualizuj_uzytkownika(i, entry_imie, entry_nazwisko, entry_stanowisko, entry_lokalizacja, button_dodaj_uzytkownia,
                           listbox_lista_pracownikow):
    pracownicy[i].imie = entry_imie.get()
    pracownicy[i].nazwisko = entry_nazwisko.get()
    pracownicy[i].stanowisko = entry_stanowisko.get()
    pracownicy[i].lokalizacja = entry_lokalizacja.get()
    lista_uzytkownikow(listbox_lista_pracownikow)
    button_dodaj_uzytkownia.config(text="Dodaj uzytkownikow", command=dodaj_uzytkownika)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_stanowisko.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()


def tworzenie_pracownicy_root(root):
    pracownicy_root = Toplevel(root)
    pracownicy_root.title("Pracownicy")
    pracownicy_root.geometry("800x500")

    # ramki do porządkowania struktury
    ramka_lista_pracownikow = Frame(pracownicy_root)
    ramka_formularz = Frame(pracownicy_root)
    ramka_szczegoly_obiektu = Frame(pracownicy_root)

    ramka_lista_pracownikow.grid(row=0, column=0, padx=50)
    ramka_formularz.grid(row=0, column=1)
    ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)

    # lista_pracownikow
    label_lista_pracownikow = Label(ramka_lista_pracownikow, text="Lista pracownikow: ")
    listbox_lista_pracownikow = Listbox(ramka_lista_pracownikow, width=50)
    button_pokaz_szczegoly = Button(ramka_lista_pracownikow, text="Pokaż szczegóły",
                                    command=lambda: pokaz_szczegoly_uzytkownikow(listbox_lista_pracownikow,
                                                                                 label_imie_szczegoly_obiektu_wartosc,
                                                                                 label_nazwisko_szczegoly_obiektu_wartosc,
                                                                                 label_stanowisko_szczegoly_obiektu_wartosc,
                                                                                 label_lokalizacja_szczegoly_obiektu_wartosc))
    button_usun_obiekt = Button(ramka_lista_pracownikow, text='Usuń obiekt',
                                command=lambda: usun_uzytkownika(listbox_lista_pracownikow))
    button_edytuj_obiektu = Button(ramka_lista_pracownikow, text='Edytuj obiekt',
                                   command=lambda: edytuj_uzytkownika(listbox_lista_pracownikow, entry_imie,
                                                                      entry_nazwisko, entry_stanowisko,
                                                                      entry_lokalizacja, button_dodaj_uzytkownia))

    label_lista_pracownikow.grid(row=0, column=0, columnspan=3)
    listbox_lista_pracownikow.grid(row=1, column=0, columnspan=3)
    button_pokaz_szczegoly.grid(row=2, column=0)
    button_usun_obiekt.grid(row=2, column=1)
    button_edytuj_obiektu.grid(row=2, column=2)

    # formularz
    label_formularz = Label(ramka_formularz, text="Fromularz")
    label_imie = Label(ramka_formularz, text="Imię: ")
    label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
    label_stanowisko = Label(ramka_formularz, text="Stanowisko: ")
    label_lokalizacja = Label(ramka_formularz, text="Lokalizacja")

    entry_imie = Entry(ramka_formularz)
    entry_nazwisko = Entry(ramka_formularz)
    entry_stanowisko = Entry(ramka_formularz)
    entry_lokalizacja = Entry(ramka_formularz)

    label_formularz.grid(row=0, column=0, columnspan=2)
    label_imie.grid(row=1, column=0, sticky=W)
    label_nazwisko.grid(row=2, column=0, sticky=W)
    label_stanowisko.grid(row=3, column=0, sticky=W)
    label_lokalizacja.grid(row=4, column=0, sticky=W)

    entry_imie.grid(row=1, column=1)
    entry_nazwisko.grid(row=2, column=1)
    entry_stanowisko.grid(row=3, column=1)
    entry_lokalizacja.grid(row=4, column=1)

    button_dodaj_uzytkownia = Button(ramka_formularz, text="Dodaj pracownika",
                                     command=lambda: dodaj_uzytkownika(entry_imie, entry_nazwisko, entry_stanowisko,
                                                                       entry_lokalizacja, listbox_lista_pracownikow))
    button_dodaj_uzytkownia.grid(row=5, column=1, columnspan=2)

    # szczegoly obiektu

    label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Szczegóły użytkownika: ")
    label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Imie: ")
    label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwisko: ")
    label_stanowisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Stanowisko: ")
    label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Lokalizacja: ")

    label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_stanowisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")

    label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
    label_imie_szczegoly_obiektu.grid(row=1, column=0, sticky=W)
    label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
    label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
    label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
    label_stanowisko_szczegoly_obiektu.grid(row=1, column=4)
    label_stanowisko_szczegoly_obiektu_wartosc.grid(row=1, column=5)
    label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
    label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)
    map_widget = tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=900, height=500)
    map_widget.set_position(52.2, 21)
    map_widget.set_zoom(8)
    # marker_WAT = map_widget.set_marker(52.25462674587218, 20.900225912403783, text="WAT")

    map_widget.grid(row=2, column=0, columnspan=8)

jednostki = []


class Jednostka:
    def __init__(self, nazwa, pracownicy, lokalizacja_jednostek, map_widget):
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




def edytuj_jednostke(listbox_lista_jednostek, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostek, button_dodaj_jednostke):
    i = listbox_lista_jednostek.index(ACTIVE)
    entry_nazwa.insert(0, jednostki[i].nazwa)
    entry_pracownicy.insert(0, jednostki[i].pracownicy)
    entry_lokalizacja_jednostek.insert(0, jednostki[i].lokalizacja_jednostek)

    button_dodaj_jednostke.config(command=lambda: aktualizuj_jednostke(i, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostek, button_dodaj_jednostke, listbox_lista_jednostek))


def aktualizuj_jednostke(i, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostki,  button_dodaj_jednostke, listbox_lista_jednostek):
    jednostki[i].nazwa = entry_nazwa.get()
    jednostki[i].pracownicy = entry_pracownicy.get()
    jednostki[i].lokalizacja_jednostki = entry_lokalizacja_jednostki.get()
    lista_jednostek(listbox_lista_jednostek)
    button_dodaj_jednostke.config(
        command=lambda: aktualizuj_jednostke(i, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostki,
                                             button_dodaj_jednostke, listbox_lista_jednostek))
    entry_nazwa.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_jednostki.delete(0, END)
    entry_nazwa.focus()




def tworzenie_jednostki_wojskowe_root(root):
    jednostki_wojskowe_root = Toplevel(root)
    jednostki_wojskowe_root.title("Jednostki Wojskowe")
    jednostki_wojskowe_root.geometry("800x500")

    # ramki do porządkowania struktury
    ramka_lista_jednostki_wojskowe = Frame(jednostki_wojskowe_root)
    ramka_formularz = Frame(jednostki_wojskowe_root)
    ramka_szczegoly_obiektu = Frame(jednostki_wojskowe_root)

    ramka_lista_jednostki_wojskowe .grid(row=0, column=0, padx=50)
    ramka_formularz.grid(row=0, column=1)
    ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)

    # lista_pracownikow
    label_lista_jednostki_wojskowe = Label(ramka_lista_jednostki_wojskowe, text="Lista jednostek wojskowych: ")
    listbox_lista_jednostki_wojskowe = Listbox(ramka_lista_jednostki_wojskowe, width=50)
    button_pokaz_szczegoly_jedn = Button(ramka_lista_jednostki_wojskowe, text="Pokaż szczegóły",
                                         command=lambda: pokaz_szczegoly_jednoski(listbox_lista_jednostki_wojskowe,
                                                                                  label_nazwa_szczegoly_obiektu_jedn_wartosc,
                                                                                  label_pracownicy_szczegoly_obiektu_jedn_wartosc,
                                                                                  label_lokalizacja_jednostki_szczegoly_obiektu_jedn_wartosc))
    button_usun_obiekt_jedn = Button(ramka_lista_jednostki_wojskowe, text='Usuń obiekt', command=lambda: usun_jednostke(listbox_lista_jednostki_wojskowe))
    button_edytuj_obiektu_jedn = Button(ramka_lista_jednostki_wojskowe, text='Edytuj obiekt',
                                        command=lambda: edytuj_jednostke(listbox_lista_jednostki_wojskowe, entry_nazwa,
                                                                         entry_pracownicy, entry_lokalizacja_jednostki,
                                                                         button_dodaj_jednostke))

    label_lista_jednostki_wojskowe.grid(row=0, column=0, columnspan=3)
    listbox_lista_jednostki_wojskowe.grid(row=1, column=0, columnspan=3)
    button_pokaz_szczegoly_jedn.grid(row=2, column=0)
    button_usun_obiekt_jedn.grid(row=2, column=1)
    button_edytuj_obiektu_jedn.grid(row=2, column=2)

    # formularz
    label_formularz = Label(ramka_formularz, text="Fromularz")
    label_nazwa = Label(ramka_formularz, text="Nazwa jednostki: ")
    label_pracownicy = Label(ramka_formularz, text="Pracownicy: ")
    label_lokalizacja_jednostki = Label(ramka_formularz, text="Lokalizacja jednostki wojskowej")

    entry_nazwa = Entry(ramka_formularz)
    entry_pracownicy = Entry(ramka_formularz)
    entry_lokalizacja_jednostki = Entry(ramka_formularz)

    label_formularz.grid(row=0, column=0, columnspan=2)
    label_nazwa.grid(row=1, column=0, sticky=W)
    label_pracownicy.grid(row=2, column=0, sticky=W)
    label_lokalizacja_jednostki.grid(row=3, column=0, sticky=W)

    entry_nazwa.grid(row=1, column=1)
    entry_pracownicy.grid(row=2, column=1)
    entry_lokalizacja_jednostki.grid(row=3, column=1)


    button_dodaj_jednostke = Button(ramka_formularz, text="Dodaj jednostke", command=lambda: dodaj_jednostke(entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostki, listbox_lista_jednostki_wojskowe))
    button_dodaj_jednostke.grid(row=5, column=1, columnspan=2)

    # szczegoly obiektu

    label_szczegoly_obiektu_jedn = Label(ramka_szczegoly_obiektu, text="Szczegóły użytkownika: ")
    label_nazwa_szczegoly_obiektu_jedn = Label(ramka_szczegoly_obiektu, text="Nazwa jednostki: ")
    label_pracownicy_szczegoly_obiektu_jedn = Label(ramka_szczegoly_obiektu, text="Pracownicy: ")
    label_lokalizacja_jednostki_szczegoly_obiektu_jedn = Label(ramka_szczegoly_obiektu, text="Lokalizacja jednostki: ")

    label_nazwa_szczegoly_obiektu_jedn_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_pracownicy_szczegoly_obiektu_jedn_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_lokalizacja_jednostki_szczegoly_obiektu_jedn_wartosc = Label(ramka_szczegoly_obiektu, text="...")

    label_szczegoly_obiektu_jedn.grid(row=0, column=0, sticky=W)
    label_nazwa_szczegoly_obiektu_jedn.grid(row=1, column=0, sticky=W)
    label_nazwa_szczegoly_obiektu_jedn_wartosc.grid(row=1, column=1)
    label_pracownicy_szczegoly_obiektu_jedn.grid(row=1, column=2)
    label_pracownicy_szczegoly_obiektu_jedn_wartosc.grid(row=1, column=3)
    label_lokalizacja_jednostki_szczegoly_obiektu_jedn.grid(row=1, column=4)
    label_lokalizacja_jednostki_szczegoly_obiektu_jedn_wartosc.grid(row=1, column=5)

pododdzialy = []


class Pododdzial:
    def __init__(self, nazwa_pododdzialu, nazwa_jednostki, pracownicy, lokalizacja_pododdzialu):
        self.nazwa_pododdzialu = nazwa_pododdzialu
        self.nazwa_jednostki = nazwa_jednostki
        self.pracownicy = pracownicy
        self.lokalizacja_pododdzialu = lokalizacja_pododdzialu


def lista_pododdzialow(listbox_lista_pododdzialow):
    listbox_lista_pododdzialow.delete(0, END)
    for idx, pododdzial in enumerate(pododdzialy):
        listbox_lista_pododdzialow.insert(idx,
                                          f'{pododdzial.nazwa_pododdzialu} {pododdzial.nazwa_jednostki} {pododdzial.pracownicy} {pododdzial.lokalizacja_pododdzialu}')


def dodaj_pododdzial(entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy, entry_lokalizacja_pododdzialu,
                     listbox_lista_pododdzialow):
    nazwa_pododdzialu = entry_nazwa_pododdzialu.get()
    nazwa_jednostki = entry_nazwa_jednostki.get()
    pracownicy = entry_pracownicy.get()
    lokalizacja_pododdzialu = entry_lokalizacja_pododdzialu.get()
    print(nazwa_pododdzialu, pracownicy, lokalizacja_pododdzialu)
    pododdzialy.append(Pododdzial(nazwa_pododdzialu, nazwa_jednostki, pracownicy, lokalizacja_pododdzialu))
    lista_pododdzialow(listbox_lista_pododdzialow)

    entry_nazwa_pododdzialu.delete(0, END)
    entry_nazwa_jednostki.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_pododdzialu.delete(0, END)

    entry_nazwa_pododdzialu.focus()


def usun_pododdzial(listbox_lista_pododdzialow):
    i = listbox_lista_pododdzialow.index(ACTIVE)
    print(i)
    pododdzialy.pop(i)
    lista_pododdzialow(listbox_lista_pododdzialow)


def pokaz_szczegoly_pododdzialu(listbox_lista_pododdzialow, label_nazwa_pododdzialu_szczegoly_obiektu_wartosc,
                                label_nazwa_jednostki_szczegoly_obiektu_wartosc,
                                label_pracownicy_szczegoly_obiektu_wartosc,
                                label_lokalizacja_jednostek_szczegoly_obiektu_wartosc):
    i = listbox_lista_pododdzialow.index(ACTIVE)
    nazwa_pododdzialu = pododdzialy[i].nazwa_pododdzialu
    label_nazwa_pododdzialu_szczegoly_obiektu_wartosc.config(text=nazwa_pododdzialu)
    nazwa_jednostki = pododdzialy[i].nazwa_jednostki
    label_nazwa_jednostki_szczegoly_obiektu_wartosc.config(text=nazwa_jednostki)
    pracownicy = pododdzialy[i].pracownicy
    label_pracownicy_szczegoly_obiektu_wartosc.config(text=pracownicy)
    lokalizacja_pododdzialu = pododdzialy[i].lokalizacja_pododdzialu
    label_lokalizacja_jednostek_szczegoly_obiektu_wartosc.config(text=lokalizacja_pododdzialu)


def edytuj_pododdzial(listbox_lista_pododdzialow, entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy,
                      entry_lokalizacja_pododdzialu, button_dodaj_pododdzial):
    i = listbox_lista_pododdzialow.index(ACTIVE)
    entry_nazwa_pododdzialu.insert(0, pododdzialy[i].nazwa_pododdzialu)
    entry_nazwa_jednostki.insert(0, pododdzialy[i].nazwa_jednostki)
    entry_pracownicy.insert(0, pododdzialy[i].pracownicy)
    entry_lokalizacja_pododdzialu.insert(0, pododdzialy[i].lokalizacja_pododdzialu
                                         )

    button_dodaj_pododdzial.config(
        command=lambda: aktualizuj_pododdzial(i, entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy,
                                              entry_lokalizacja_pododdzialu, button_dodaj_pododdzial,
                                              listbox_lista_pododdzialow))


def aktualizuj_pododdzial(i, entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy,
                          entry_lokalizacja_pododdzialu, button_dodaj_pododdzial, listbox_lista_pododdzialow):
    pododdzialy[i].nazwa_pododdzialu = entry_nazwa_pododdzialu.get()
    pododdzialy[i].nazwa_jednostki = entry_nazwa_jednostki.get()
    pododdzialy[i].pracownicy = entry_pracownicy.get()
    pododdzialy[i].lokalizacja_jednostki = entry_lokalizacja_pododdzialu.get()
    lista_pododdzialow(listbox_lista_pododdzialow)
    button_dodaj_pododdzial.config(
        command=lambda: aktualizuj_pododdzial(i, entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy,
                                              entry_lokalizacja_pododdzialu,
                                              button_dodaj_pododdzial, listbox_lista_pododdzialow))
    entry_nazwa_pododdzialu.delete(0, END)
    entry_nazwa_jednostki.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_pododdzialu.delete(0, END)
    entry_nazwa_pododdzialu.focus()


def tworzenie_pododdzialy_root(root):
    pododdzialy_root = Toplevel(root)
    pododdzialy_root.title("Pododdziały")
    pododdzialy_root.geometry("800x500")

    # ramki do porządkowania struktury
    ramka_lista_pododdzialy = Frame(pododdzialy_root)
    ramka_formularz = Frame(pododdzialy_root)
    ramka_szczegoly_obiektu = Frame(pododdzialy_root)

    ramka_lista_pododdzialy.grid(row=0, column=0, padx=50)
    ramka_formularz.grid(row=0, column=1)
    ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)

    # lista_pracownikow
    label_lista_pododdzialy = Label(ramka_lista_pododdzialy, text="Lista pododziałów: ")
    listbox_lista_pododdzialy = Listbox(ramka_lista_pododdzialy, width=50)
    button_pokaz_szczegoly_pododdzialu = Button(ramka_lista_pododdzialy, text="Pokaż szczegóły",
                                                command=lambda: pokaz_szczegoly_pododdzialu(listbox_lista_pododdzialy,
                                                                                            label_nazwa_pododzialu_szczegoly_obiektu_wartosc,
                                                                                            label_nazwa_jednostki_szczegoly_obiektu_wartosc,
                                                                                            label_pracownicy_szczegoly_obiektu_wartosc,
                                                                                            label_lokalizacja_pododdzialu_szczegoly_obiektu_wartosc))
    button_usun_obiekt = Button(ramka_lista_pododdzialy, text='Usuń obiekt', command=lambda: usun_pododdzial(listbox_lista_pododdzialy))
    button_edytuj_obiektu = Button(ramka_lista_pododdzialy, text='Edytuj obiekt',
                                        command=lambda: edytuj_pododdzial(listbox_lista_pododdzialy, entry_nazwa_pododdzialu, entry_nazwa_jednostki,
                                                                         entry_pracownicy, entry_lokalizacja_pododdzialu,
                                                                         button_dodaj_pododdzial))
    label_lista_pododdzialy.grid(row=0, column=0, columnspan=3)
    listbox_lista_pododdzialy.grid(row=1, column=0, columnspan=3)
    button_pokaz_szczegoly_pododdzialu.grid(row=2, column=0)
    button_usun_obiekt.grid(row=2, column=1)
    button_edytuj_obiektu.grid(row=2, column=2)

    # formularz
    label_formularz = Label(ramka_formularz, text="Fromularz")
    label_nazwa_pododzialu = Label(ramka_formularz, text="Nazwa pododdziału: ")
    label_nazwa_jednostki = Label(ramka_formularz, text="Nazwa jednostki wojskowej: ")
    label_pracownicy = Label(ramka_formularz, text="Pracownicy: ")
    label_lokalizacja_pododdzialu = Label(ramka_formularz, text="Lokalizacja pododdziału")

    entry_nazwa_pododdzialu = Entry(ramka_formularz)
    entry_nazwa_jednostki = Entry(ramka_formularz)
    entry_pracownicy = Entry(ramka_formularz)
    entry_lokalizacja_pododdzialu = Entry(ramka_formularz)

    label_formularz.grid(row=0, column=0, columnspan=2)
    label_nazwa_pododzialu.grid(row=1, column=0, sticky=W)
    label_nazwa_jednostki.grid(row=2, column=0, sticky=W)
    label_pracownicy.grid(row=3, column=0, sticky=W)
    label_lokalizacja_pododdzialu.grid(row=4, column=0, sticky=W)

    entry_nazwa_pododdzialu.grid(row=1, column=1)
    entry_nazwa_jednostki.grid(row=2, column=1)
    entry_pracownicy.grid(row=3, column=1)
    entry_lokalizacja_pododdzialu.grid(row=4, column=1)

    button_dodaj_pododdzial = Button(ramka_formularz, text="Dodaj pododdział",
                                     command=lambda: dodaj_pododdzial(entry_nazwa_pododdzialu, entry_nazwa_jednostki,
                                                                      entry_pracownicy, entry_lokalizacja_pododdzialu,
                                                                      listbox_lista_pododdzialy))
    button_dodaj_pododdzial.grid(row=5, column=1, columnspan=2)

    # szczegoly obiektu

    label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Szczegóły użytkownika: ")
    label_nazwa_pododzialu_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwa pododziału: ")
    label_nazwa_jednostki_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwa jednostki wojskowej: ")
    label_pracownicy_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Pracownicy: ")
    label_lokalizacja_pododdzialu_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Lokalizacja pododdziału: ")

    label_nazwa_pododzialu_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_nazwa_jednostki_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_pracownicy_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_lokalizacja_pododdzialu_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")

    label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
    label_nazwa_pododzialu_szczegoly_obiektu.grid(row=1, column=0, sticky=W)
    label_nazwa_pododzialu_szczegoly_obiektu_wartosc.grid(row=1, column=1)
    label_nazwa_jednostki_szczegoly_obiektu.grid(row=1, column=2)
    label_nazwa_jednostki_szczegoly_obiektu_wartosc.grid(row=1, column=3)
    label_pracownicy_szczegoly_obiektu.grid(row=1, column=4)
    label_pracownicy_szczegoly_obiektu_wartosc.grid(row=1, column=5)
    label_lokalizacja_pododdzialu_szczegoly_obiektu.grid(row=1, column=6)
    label_lokalizacja_pododdzialu_szczegoly_obiektu_wartosc.grid(row=1, column=7)

def logowanie():
    while True:
        login = input("Podaj nazwę użytkownika: ")
        haslo = input("Podaj hasło: ")

        if (login == login_1 and haslo == haslo_1) or \
                (login == login_2 and haslo == haslo_2) or \
                (login == login_3 and haslo == haslo_3) or \
                (login == login_4 and haslo == haslo_4) or \
                (login == login_5 and haslo == haslo_5) or \
                (login == login_6 and haslo == haslo_6) or \
                (login == login_7 and haslo == haslo_7) or \
                (login == login_8 and haslo == haslo_8) or \
                (login == login_9 and haslo == haslo_9) or \
                (login == login_10 and haslo == haslo_10):
            print("Zalogowano pomyślnie!")

            root = Tk()
            root.title("Menu główne")
            root.geometry("800x500")

            label = Label(root, text="Wybierz opcję:")
            label.grid(row=0, column=0, columnspan=3)

            button1 = Button(root, text="Jednostki wojskowe",
                             command=lambda: tworzenie_jednostki_wojskowe_root(root))
            button1.grid(row=1, column=0)

            button2 = Button(root, text="Pracownicy",
                             command=lambda: tworzenie_pracownicy_root(root))
            button2.grid(row=1, column=1)

            button3 = Button(root, text="Pododdziały w jednostce",
                             command=lambda: tworzenie_pododdzialy_root(root))
            button3.grid(row=1, column=2)

            root.mainloop()

            break
        else:
            print("Błędne dane logowania. Spróbuj ponownie.")


logowanie()
