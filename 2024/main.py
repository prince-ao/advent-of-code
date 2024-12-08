import day1, day2, day3, day4
import parser
import numpy as np

def main():
    file_name = "input_day4.txt"
    # file_name = "test_day4.txt"


    with open(f"assets/{file_name}") as stream:
        input = stream.read()

        parsed_input = parser.day4(input)

        print(day4.day4_2(parsed_input))




if __name__ == "__main__":
    main()