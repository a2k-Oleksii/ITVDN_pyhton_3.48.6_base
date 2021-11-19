def main():
    while True:
        try:
            first_num = float(input("First number = "))
            second_num = float(input("Second number = "))
            print("Result = ", first_num / second_num)
            break
        except (ValueError, ZeroDivisionError) as error:
            print("Error: ", error)
            print("Please try again!")


if __name__ == '__main__':
    main()



