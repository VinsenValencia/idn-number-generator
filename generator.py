import random
# Made by CR4CK3D
# FOLLOW ME ON GITHUB :D
print( """                                                                                                                                
                 NumberGenerator
                 Made By CRACKED
 
""")
def generate_indonesian_numbers():
    num_count = int(input("How many numbers do you need? "))
# Made BY CR4CK3D    
    numbers = []
    for _ in range(num_count):
        number = "+62" + str(random.randint(8000000000, 8999999999))
        numbers.append(number)
# recode boleh asal ngasih copyright anjg    
    file_name = input("Enter the file name to save the numbers: ")
    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(number + '\n')
# Made BY Egalsa    
    print(f"{num_count} random Indonesian numbers have been generated and saved in {file_name}.")

generate_indonesian_numbers()
