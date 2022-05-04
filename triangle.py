#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: May 2022
# This program uses user defined functions


def calculate_area(base, height):
    # calculate area

    # process
    area = (base * height) / 2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets length and width

    # input
    base_from_user = input("Enter the base of a rectangle (cm): ")
    height_from_user = input("Enter the height of a rectangle (cm): ")
    print("")

    # process
    try:
        height_int = int(height_from_user)
        base_int = int(base_from_user)
        # call functions
        calculate_area(base_int, height_int)
    except Exception:
        print("That is not an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
