def read_int(prompt, min, max):
    try:
        data = int(input(prompt))
        if data <= max and data >= min:
            print(f"The number is: {data}")
        else:
            print(f"Error: the value is not within permitted range ({min}..{max})")
    except ValueError:
        print('Error: wrong input')
        
v = read_int("Enter a number from -10 to 10: ", -10, 10)

