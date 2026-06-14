#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list
    a = new_list.count(search)
    new_list.replace(search, replace, a)
    return new_list