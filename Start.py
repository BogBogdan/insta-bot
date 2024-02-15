import schedule
import time
import subprocess
import AddReel 
import AddPicture 

def get_first_line(file_path):
    # Učitaj prvi red iz fajla
    with open(file_path, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()

    # Ukloni prvi red iz fajla
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        # Upisivanje svih linija osim prvog reda u fajl
        file.writelines(lines[1:])

    # Vrati učitani prvi red
    return first_line

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"Datoteka '{file_path}' nije pronađena.")
        return None
    except Exception as e:
        print(f"Došlo je do greške prilikom čitanja datoteke: {e}")
        return None

def main_program():
    
    line = get_first_line("./izlaz.txt")
    tags = read_file("./heshtags.txt")
    url, text = line.split('|')
    # Formirajte komandu koja će pokrenuti test.py sa argumentima
    print("Uplodovanje")
    if(url.endswith(".mp4")):
        AddReel.addReelOnInstagram(url, text+"\n"+tags)
        
    elif(url.endswith(".png") or url.endswith(".jpg")):
        AddPicture.addImageOnInstagram(url, text+"\n"+tags)

def schedule_main_program():
    # Zakazivanje posla da se izvrši svaka 2 dana u 12:00
    schedule.every(2).days.at("20:40").do(main_program)
    
    # Beskonačna petlja za izvršavanje poslova
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_main_program()