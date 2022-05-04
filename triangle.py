#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Oct 2019
# This program uses user defined functions


def calculate_area(length, width):
    # calculate area

    # process
    area = (length * width) / 2

    # output
    print("The area is {0} cm²".format(area))
    print("\nDone.")


def main():
    # this function gets length and width

    # input
    base_from_user = int(input("Enter the base of a rectangle (cm): "))
    height_from_user = int(input("Enter the height of a rectangle (cm): "))
    print("")

    # call functions
    calculate_area(base_from_user, height_from_user)


if __name__ == "__main__":
    main()
