def all_useful_item_list (all_item_list,remove_list):
    all_useful_item_list=[]
    for useful_item in all_item_list:
        if useful_item not in remove_list:
            all_useful_item_list.append(useful_item)
    return all_useful_item_list
