# File Compression: Write a Python program that compresses 
# a text file by replacing repeated characters with a single 
# character and a count of the number of repetitions. 
# For example, the string "aaabbbcccc" should be compressed 
# to "a3b3c4". Your program should prompt the user to enter 
# the name of the input file and the name of the output file

    

def compressFile():
    while True:
        input_file = input('Please enter the name of the input file\n')
        try: 
            with open(input_file) as in_file:
                output_file = input('now enter the name of the output file\n')
                with open(output_file, 'w') as out_file:        
                    for line in in_file:
                        last_char = None
                        char_count = 0
                        for char in line:
                            if char != last_char:
                                if last_char is not None:
                                    out_file.write(last_char + str(char_count))
                                last_char = char
                                char_count = 1
                            else:
                                char_count += 1
                        out_file.write(last_char + str(char_count))
                print(f'\nFile \'{input_file}\' successfully compressed on \'{output_file}\'\n')
                break
        except FileNotFoundError:
            print('Failed to open file!!')


compressFile()
