def multiply_and_greet(*numbers,**students):
    multiple=1
    for num in numbers:
        multiple*=num
        print (multiple)
    print(f"Hello {students}")
    