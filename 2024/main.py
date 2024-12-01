import day1

def main():
    file_name = "input_day1_1.txt"

    with open(f"assets/{file_name}") as stream:
        input = stream.read()

        print(day1.day1_2(input))



if __name__ == "__main__":
    main()