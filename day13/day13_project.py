
# Debugging
'''
    1. Define the problem
    2. Reproduce the bug
    3. Play as a computer
    4. Fix the errors
    5. Print is your friend
    6. Use a debugger
    7. Take a break
'''
# from random import randint
# randint(1, 2)

def my_function():
    '''Print numbers from 1 to 20'''
    for i in range(1, 20):
        print(i)

def main():
    # my_function()

    try:
        age = int(input("Enter age"))
        print(age)
    except ValueError as e:
        print(f'Invalid input - {e}')

if __name__ == '__main__':

    main()