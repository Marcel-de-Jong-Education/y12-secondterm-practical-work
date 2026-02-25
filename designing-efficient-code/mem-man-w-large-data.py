def read_all_lines(file_path):
    with open(file_path, 'r') as file:
        lines = []
            while True:
                line = file.readlines() #
                if not line:
                    break # Stop when end of file is reached
                print(line.strip())

