import tkinter as tk
from tkinter import *

def distance(entry1_val, option1_val , option2_val, option3_val):

    min_distance = 0
    max_distance = 0
    min_distance2 = 0
    max_distance2 = 0


    if entry1_val == 0:
        if option1_val is True and option2_val is False and option3_val is False:
            min_distance = 0
            max_distance = 3
        elif option2_val is True and option1_val is False and option3_val is False:
            min_distance = 3
            max_distance = 7
        elif option3_val is True and option1_val is False and option2_val is False:
            min_distance = 7
            max_distance = 10
        elif option1_val is True and option2_val is True and option3_val is True:
            min_distance = 0
            max_distance = 10
        elif option1_val is True and option2_val is True and option3_val is False:
            min_distance = 0
            max_distance = 7
        elif option1_val is False and option2_val is True and option3_val is True:
            min_distance = 3
            max_distance = 10
        elif option1_val is True and option2_val is False and option3_val is True:
            min_distance = 0
            max_distance = 10
            min_distance2 = 3
            max_distance2 = 7
    else:
        min_distance = 0
        max_distance = entry1_val

    # print([min_distance, max_distance, min_distance2, max_distance2])
    return [min_distance, max_distance, min_distance2, max_distance2]

if __name__ == '__main__':
    distance()