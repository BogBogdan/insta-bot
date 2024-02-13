import schedule
import time
import subprocess

def get_first_line(file_path):
    # Učitaj prvi red iz fajla
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()

    # Ukloni prvi red iz fajla
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        # Upisivanje svih linija osim prvog reda u fajl
        file.writelines(lines[1:])

    # Vrati učitani prvi red
    return first_line

def main_program():
    
    line = get_first_line("./uploadData.txt")
    url, text = line.split('|')
    # Formirajte komandu koja će pokrenuti test.py sa argumentima
    print("Uplodovanje")
    command = ["python", "AddReel.py", url, text]
    subprocess.run(command)

def schedule_main_program():
    # Zakazivanje posla da se izvrši svaka 2 dana u 12:00
    schedule.every(1).days.at("20:25").do(main_program)

    # Beskonačna petlja za izvršavanje poslova
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_main_program()