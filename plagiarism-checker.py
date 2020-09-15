import os
import csv
import sys
import numpy as np

# script will be divided into some main parts
# sys args from the user input


# function to load a txt document
def load_origin_txt(origin_txt_file):
    origin_word_list = []
    with open(origin_txt_file) as file:
        for line in file:
            for word in line.split():
                origin_word_list.append(word)
    return origin_word_list

# function to store every word in the document in an array in order as its occurrence
def load_check_txt(check_txt_file):
    check_word_list = []
    with open(check_txt_file) as file:
        for line in file:
            for word in line.split():
                check_word_list.append(word)
    return check_word_list

# function to join both lists and eliminate duplicates
# each word from each document occurs exactly once
# result is sorted ascending
def list_combining(origin_list, check_list):
    return sorted(np.unique(origin_list + check_list))
    
# function returns 0 or 1 if the word occurs in origin document
def find_word_origin(combined_word_list, origin_word_list ):
    pass

# function returns 0 or 1 if the word occurs in check document
def find_word_check(combined_word_list, check_word_list):
    pass

# main part of the script
if __name__ == "__main__":
    origin_file = load_origin_txt('origin-file.txt')
    check_file = load_check_txt('file-to-check.txt')
    #print(check_word_list)
    #print(list_combining(load_origin_txt('origin-file.txt'), load_check_txt('file-to-check.txt')))
    combined_list = list_combining(load_origin_txt('origin-file.txt'), load_check_txt('file-to-check.txt'))
    find_word_origin(combined_list, origin_file)
    find_word_check(combined_list, check_file)