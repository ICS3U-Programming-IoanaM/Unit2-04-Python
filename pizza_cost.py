#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Oct. 3, 2022
# calculates the cost of a pizza

import constants


def main():
    # variables
    diameter = float(input("Enter diameter: "))

    # calculations
    subtotal = (
        constants.LABOUR_COST
        + constants.RENTAL_COST
        + diameter * constants.INGREDIANT_COST
    )
    tax = subtotal * constants.HST
    total = subtotal + tax

    # displays results
    print(f"The total cost (HST included): ${total:.2f}")


if __name__ == "__main__":
    main()
