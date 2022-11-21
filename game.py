
tabela_planszy = []
czlowiek = "x"
komputer = "o"

def plansza_przyklad():
    print(""" 
        człowiek - x
        komputer - o
                0  |  1  |  2
                -------------- 
                3  |  4  |  5
                --------------
                6  |  7  |  8   
        """)


def nowa_plansza():
    for i in range(0,9):
        tabela_planszy.append(" ")


def plansza_gra(tabela_planszy):
    print(f'  {tabela_planszy[0]} | {tabela_planszy[1]} | {tabela_planszy[2]}')
    print(f'  ----------')
    print(f'  {tabela_planszy[3]} | {tabela_planszy[4]} | {tabela_planszy[5]}')
    print(f'  ----------')
    print(f'  {tabela_planszy[6]} | {tabela_planszy[7]} | {tabela_planszy[8]}')
    print(f'================\n')


def kto_zaczyna():
    response = None
    while response not in ("t", "n"):
        response = input("Chcesz zaczynać? t/n")
    if response == "t":
        return czlowiek
    else:
        return komputer


def prawidlowe_ruchy(tabela_planszy):
    tabela_prawidlowe_ruchy = []
    for i in range(0,9):
        if tabela_planszy[i] == " ":
            tabela_prawidlowe_ruchy.append(i)
    return tabela_prawidlowe_ruchy

def wygrany(tabela_planszy):
    tupla_wygranych = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))
    for i in tupla_wygranych:
        if tabela_planszy[i[0]] == tabela_planszy[i[1]] == tabela_planszy[i[2]] !=  " ":
            wygrany = tabela_planszy[i[0]]
            return wygrany
    if " " not in tabela_planszy:
        remis = "remis"
        return remis
    return None
def ruch_czlowieka(tabela_planszy, czlowiek):
    prawidlowy = prawidlowe_ruchy(tabela_planszy)
    ruch = None
    while ruch not in prawidlowy:
        ruch = int(input("które pole wybierasz?"))
        if ruch not in prawidlowy:
            print("Pole zajęte - wybierz inne!")
    return ruch

def ruch_komputera(tabela_planszy, czlowiek, komputer):
    tabela_planszy = tabela_planszy[:]
    najlepsze_ruchy = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    for ruch in prawidlowe_ruchy(tabela_planszy):
        tabela_planszy[ruch] = komputer
        if wygrany(tabela_planszy) == komputer:
            return ruch
        tabela_planszy[ruch] = " "
    for ruch in prawidlowe_ruchy(tabela_planszy):
        tabela_planszy[ruch] = czlowiek
        if wygrany(tabela_planszy) == czlowiek:
            return ruch
        tabela_planszy[ruch] = " "
    for ruch in najlepsze_ruchy:
        if ruch in prawidlowe_ruchy(tabela_planszy):
            return ruch


def nastepna_kolejka(kolejka):
    if kolejka == czlowiek:
        return komputer
    else:
        return czlowiek


def gratulacje(zwyciezca, czlowiek, komputer):
    if zwyciezca != "remis":
        print(zwyciezca, 'Jest zwyciężcą!')
    else:
        print("Remis")


def main():
    plansza_przyklad()
    kolejka = kto_zaczyna()
    nowa_plansza()
    plansza_gra(tabela_planszy)

    while not wygrany(tabela_planszy):

        if kolejka == czlowiek:
            ruch = ruch_czlowieka(tabela_planszy,czlowiek)
            tabela_planszy[ruch] = czlowiek
        else:
            ruch = ruch_komputera(tabela_planszy, czlowiek, komputer)
            tabela_planszy[ruch] = komputer
        plansza_przyklad()
        plansza_gra(tabela_planszy)
        kolejka = nastepna_kolejka(kolejka)
    zwyciezca = wygrany(tabela_planszy)
    gratulacje(zwyciezca, czlowiek, komputer)

main()