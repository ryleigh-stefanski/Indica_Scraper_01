import selenium_ascend as ascend
import selenium_ethos as ethos
import selenium_beyond_hello as beyondh
import time

line = "-------------------------------------------------------------------------------------------------"

#urls
ascend_url = "https://letsascend.com/menu/pa-scranton-menu-med/categories/flower"
ethos_url = "https://wilkesbarre.ethoscannabis.com/stores/ethos-wilkes-barre/products/flower"
beyondh_url = "https://www.iheartjane.com/embed/stores/1639/menu?filters%5Broot_types%5D%5B%5D=flower"

#returned item object looks like [name, price, size, brand]
ascend_returned_items = []

ethos_returned_items = []

beyondh_returned_items = []

search_key = ["Tahoe Apple", "Sled Dog", "Perfect Cell", "CannaConfusion"]

max_scrolls_to_bottom = 30
max_elements_checked = 300
wait_for_load_time = 0.1

found_at_ascend = False
found_at_ethos = False
found_at_beyondh = False

#returns the length of all items in a list
def depth_len(list):
    length = 0
    for ele in list:
        length += len(ele)
    return length

#search sites  

try:
    ascend_returned_items = ascend.sel_ascend_run(search_key, ascend_url, max_scrolls_to_bottom,max_elements_checked,wait_for_load_time)
except:
    print("Failed to search Ascend...")
   
try:
    ethos_returned_items = ethos.sel_ethos_run(search_key, ethos_url)
except:
    print("Failed to search Ethos...")

try:
    beyondh_returned_items = beyondh.sel_beyondh_run(search_key, beyondh_url)
except:
    print("Failed to search Beyond Hello...")

print(beyondh_returned_items)

#output results
dots_per_side = int((len(line) - 6 - depth_len(search_key)) / 2) * "."
print("\n\n%sResults for: %s%s" %  (dots_per_side, search_key, dots_per_side))
print(line)
#first layer of list has the strains i.e. l[0] = cream, l[1] = alien og
#second layer has information on each items of that strain  i.e. l[0][0] = first cream item, l[1][1] = second alien og item
print("\n\n%sAscend%s" % (dots_per_side, dots_per_side))
i = 0
for strain in ascend_returned_items:
    for element in ascend_returned_items[i]:
        print("....Strain: %s" % search_key[i])
        print(".......Price: %s" % element[0])
        print(".......Brand: %s" % element[2])
        print(".......Size : %s" % element[1])
    i += 1

print("\n\n%sEthos%s" % (dots_per_side, dots_per_side))
i = 0
for page in ethos_returned_items:
    for element in ethos_returned_items[i]:
        print("....Strain: %s" % element[0])
        print(".......Price: %s" % element[1][0])
        print(".......Brand: %s" % element[1][2])
        print(".......Size : %s" % element[1][1])
    i += 1
    
print("\n\n%sBeyond Hello%s" % (dots_per_side, dots_per_side))
i = 0
for element in beyondh_returned_items:
    print("....Strain: %s" % element[0])
    print(".......Price: %s" % element[1][0])
    print(".......Brand: %s" % element[1][2])
    print(".......Size : %s" % element[1][1])
    i += 1
  
print(line)