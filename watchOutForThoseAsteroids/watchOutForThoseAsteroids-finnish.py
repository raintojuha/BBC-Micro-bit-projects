'''
Juha Rainto
2023
'''
# Kirjastot
from microbit import *
import random

'''
Tällä hetkellä pelaajan on mahdollista liikkua vasemmalle ja oikealle A ja B-painikkeilla
pelaaja siirretään laidasta toiseen, mikäli pelaaja ylittää pelialueen reunan

Väistettäviä esteitä luodaan loputtomasti, yksi kerrallaan
Mikäli pelaaja osuu esteeseen, näytölle tuodaan pelaajan tulos (väistetyt esteet)
'''

# TEHTÄVÄÄ
# Luo ennen peliä näytettävä ikkuna / animaatio
# Odota, että pelaaja aloittaa pelin

# Lisää mahdollisuus aloittaa peli uudelleen


# JATKOKEHITYS
# Pelin vaikeuden nostaminen
# - pelin nopeus
# - useita esteitä kerralla


class Pelaaja:
    # Pelaajan sijainti
    x = 2
    y = 4 #muuttumaton

    
    def __init__(self):
        # Piirrä pelaaja näytölle alustuksen yhteydessä
        display.set_pixel(self.x, self.y ,9)

    def liikuta(self, liike):
        # Sammuta LED pelaajan nykyisessä sijainnissa
        display.set_pixel(self.x, self.y, 0)

        # Liikuta pelaajaa
        # Jos pelaaja liikkuu rajojen ulkopuolelle, siirrä toiseen laitaan
        if self.x + liike > 4:
            self.x = 0
        elif self.x + liike < 0:
            self.x = 4
        else:
            self.x += liike

        # Sytytä LED pelaajan uudessa sijainnissa
        display.set_pixel(self.x, self.y, 9)

        

class Este:
    # Esteen sijainti
    x = 0
    y = 0

    def __init__(self):
        # Arvo esteelle satunnainen sarake jota pitkin liikkua
        self.x = random.randint(0, 4)
        # Piirrä este alustuksen yhteydessä
        display.set_pixel(self.x, self.y, 9)

    def liikuta(self):
        # Sammuta LED nykyisessä sijainnissa
        display.set_pixel(self.x, self.y, 0)

        # Jos este ei ole vielä viimeisellä rivillä
        if self.y < 4:
            # Liiku alaspäin
            self.y += 1
        else:
            # Jos este on saavuttanut pelialueen pohjan, palauta False
            return False

        # Sytytä LED uudessa sijainnissa
        display.set_pixel(self.x, self.y, 9)
        # Estettä on liikutettu, palauta True
        return True


def main():
    # Initialize player and Obstacle objects
    pelaaja = Pelaaja()
    este = Este()

    # Laske silmukan kierrokset
    kierros = 0

    # Pelaajan tulos
    tulos = 0

    # Pelisilmukka
    while True:
        # Liikuta pelaajaa jos painiketta painetaan
        # -1 liiku vasemmalle
        # +1 liiku oikealle
        if button_a.was_pressed():
            pelaaja.liikuta(-1)
        if button_b.was_pressed():
            pelaaja.liikuta(+1)

        # Kun silmukka on suoritettu 50 kertaa, liikuta estettä
        if kierros >= 50:
            # Jos estettä ei voi liikuttaa (lue. este on saavuttanut pelialueen pohjan)
            if este.liikuta() == False:
                # Luo uusi este-objekti
                este = Este()
                # Lisää piste tulokseen
                tulos += 1
            # Aloita silmukan kierrosten lasku alusta
            kierros = 0
        else:
            kierros += 1

        if osuma(pelaaja, este):
            gameOver(tulos)

        # Sleep for 10ms
        sleep(10)


# Clear entire display
def clearDisplay():
    display.show(Image('00000:'
                       '00000:'
                       '00000:'
                       '00000:'
                       '00000:'))

# Tarkasta onko pelaaja osunut esteeseen
def osuma(pelaaja, este):
    # Jos pelaajan ja esteen koordinaatit ovat samat
    if pelaaja.x == este.x and pelaaja.y == este.y:
        return True
    else:
        return False

# Peli loppunut
def gameOver(tulos):
    # Näytä pelaajan tulos
    display.scroll('Tulos: ' + str(tulos), delay=100, loop=True)


main()
    