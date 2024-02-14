import random

def shuffle_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:  # Ovdje koristimo utf-8 karakter set
        lines = file.readlines()
        random.shuffle(lines)
    
    with open(output_file, 'w', encoding='utf-8') as file:  # Ovdje također koristimo utf-8 karakter set
        for line in lines:
            file.write(line)

input_file = 'uploadData.txt'  # Postavite ime vašeg ulaznog datoteke
output_file = 'izlaz.txt'  # Postavite ime vašeg izlaznog datoteke

shuffle_lines(input_file, output_file)
print("Linije su izmiješane i spremljene u izlaznu datoteku.")
