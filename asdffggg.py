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
                             command=lambda: tworzenie_pododdzialy_root(root))
            button1.grid(row=1, column=0)

            button2 = Button(root, text="Pracownicy",
                             command=lambda: tworzenie_pododdzialy_root(root))
            button2.grid(row=1, column=1)

            button3 = Button(root, text="Pododdziały w jednostce",
                             command=lambda: tworzenie_pododdzialy_root(root))
            button3.grid(row=1, column=2)

            root.mainloop()

            break
        else:
            print("Błędne dane logowania. Spróbuj ponownie.")


logowanie()
