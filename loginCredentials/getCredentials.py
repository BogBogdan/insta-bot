import json

def ucitaj_podatke_iz_fajla(putanja):
    try:
        with open(putanja, 'r') as fajl:
            podaci = json.load(fajl)
            return tuple(sorted(podaci.items()))  # Vraća uredjen par (tuple)
    except FileNotFoundError:
        print(f"Fajl na putanji '{putanja}' nije pronađen.")
    except json.JSONDecodeError:
        print(f"Greška prilikom dekodiranja JSON-a u fajlu na putanji '{putanja}'.")
    except Exception as e:
        print(f"Neočekivana greška: {e}")


def usernameNpassword():
    putanja_do_fajla = './credentials.json'
    password, username = ucitaj_podatke_iz_fajla(putanja_do_fajla)

    username = username[1]
    password = password[1]

    return username, password