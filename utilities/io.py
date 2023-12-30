import os

def read_input_as_lines(day, strip=True):
    with open(f"inputs\\day{day}.txt") as f:
        return [line.strip() if strip else line[:-1] for line in f]
    
def read_example_as_lines(day, strip=True):
    with open(f"inputs\\day{day}_ex.txt") as f:
        return [line.strip() if strip else line[:-1] for line in f]
    
def create_blank_input_files():
    for i in range(1, 26):
        if not os.path.exists(f"inputs\\day{i}.txt"):
            with open(f"inputs\\day{i}.txt", "w") as f:
                f.write(f"This is a blank input file for problem {i}")

        if not os.path.exists(f"inputs\\day{i}_ex.txt"):
            with open(f"inputs\\day{i}_ex.txt", "w") as f:
                f.write(f"This is a blank input file for the example for proble"
                        f"m {i}")