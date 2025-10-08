# file paths and directories

def read_lines(path):
      with open(path) as f:
        return f.read().splitlines()
      
def read(path):
      with open(path) as f:
        return f.read()

def write_file(path, content):
    with open(path, mode='w') as f:
        f.write(content)

def main():
    names = read_lines('./input/invited_names.txt')
    letter_content = read('./input/starting_letter.txt')
    for name in names:
        content = letter_content.replace('[name]', name)
        write_file(f'./output/letter_for_{name}.txt', content)
        pass
  
if __name__ == '__main__':
    main()