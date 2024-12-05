import day1, day2, day3
import parser
import numpy as np

def main():
    file_name = "input_day3.txt"
    # file_name = "test_day3.txt"


    with open(f"assets/{file_name}") as stream:
        input = stream.read()

        # parsed_input = parser.day2(input)

        print(day3.day3_2(input))




if __name__ == "__main__":
    main()