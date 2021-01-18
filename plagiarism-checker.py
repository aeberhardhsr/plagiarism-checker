import os
import csv
import sys
import argparse

# script will be divided into some main parts


# function to store every word in the document in an array in order as its occurrence
# function returns set of elements
def load_origin_txt(origin_txt_file):
    origin_word_list = []
    with open(origin_txt_file) as file:
        for line in file:
            for word in line.split():
                origin_word_list.append(word)
    return origin_word_list

# function to store every word in the document in an array in order as its occurrence. 
# function returns set of elements
def load_check_txt(check_txt_file):
    check_word_list = []
    with open(check_txt_file) as file:
        for line in file:
            for word in line.split():
                check_word_list.append(word)
    return check_word_list

# function to combine both documents within one list, join the second list with unique values
def combined_list():
    set_1 = set(load_origin_txt(args.original_file))
    set_2 = set(load_check_txt(args.check_file))
    list_2_items_not_in_list_1 = list(set_2 - set_1)
    unique_list = load_origin_txt(args.original_file) + list_2_items_not_in_list_1
    return unique_list

# function return 0 or 1 if compared word pairs are equally or not
def compare_words_com_org(comb_list, org_file):
    com_org = []
    for i in range(0, len(org_file)):
        if comb_list[i] == org_file[i]:
            com_org.append(1)
        else:
            com_org.append(0)
    return com_org

# function return 0 or 1 if compared word pairs are equally or not
def compare_words_com_chk(comb_list, chk_file):
    com_chk = []
    for i in range(0, len(chk_file)):
        if comb_list[i] == chk_file[i]:
            com_chk.append(1)
        else:
            com_chk.append(0)
    return com_chk

# function to define the value of similarity
def cosine_similarity(vector_a, vector_b):
    pass

# main part of the script
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--original', dest='original_file', type=str, help='Input file which contains original content', required=True)
    parser.add_argument('-c', '--check', dest='check_file', type=str, help='Input file which contains the content to check', required=True)
    args = parser.parse_args()
    
    #print(combined_list())

    #print(min(len(combined_list())))


    print(compare_words_com_org(combined_list(),load_origin_txt(args.original_file)))

    print("=========================================")

    print(compare_words_com_chk(combined_list(),load_check_txt(args.check_file)))
