#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Method that determines if a given data set
        represent a valid UTF-8 encoding
    """
    num_byt = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7

        if num_byt == 0:
            while mask_byte & i:
                num_byt += 1
                mask_byte = mask_byte >> 1

            if num_byt == 0:
                continue

            if num_byt == 1 or num_byt > 4:
                return False

        else:
            if not (i & mask1 and not (i & mask2)):
                return False

        num_byt -= 1

    if num_byt == 0:
        return True

    return False
