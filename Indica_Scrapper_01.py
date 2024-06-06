import selenium_ascend as ascend
import selenium_ethos as ethos
import time

line = "-------------------------------------------------------------------------------------------------"

#urls
ascend_url = "https://letsascend.com/menu/pa-scranton-menu-med/categories/flower"
ethos_url = "https://wilkesbarre.ethoscannabis.com/stores/ethos-wilkes-barre/products/flower"

#returned item object looks like [name, price, size, brand]
ascend_returned_items = []

ethos_found = 0
ethos_price = 0
ethos_brand = 0
ethos_size = 0

search_key = ["Cream", "Alien OG", "P Punch"]

max_scrolls_to_bottom = 30
max_elements_checked = 300
wait_for_load_time = 0.1

found_at_ascend = False
found_at_ethos = False

try:
    ascend_returned_items = ascend.sel_ascend_run(search_key, ascend_url, max_scrolls_to_bottom,max_elements_checked,wait_for_load_time)
except:
    print("Failed to search Ascend...")
    
try:
    ethos_found = ethos.sel_ethos_run(search_key[0], ethos_url)
except:
    print("Failed to search Ethos...")


#output results
dots_per_side = int((len(line) - 12 - len(search_key)) / 2) * "."
print("\n\n%sResults for: %s%s" %  (dots_per_side, search_key, dots_per_side))
print(line)
#first layer of list has the strains i.e. l[0] = cream, l[1] = alien og
#second layer has information on each items of that strain  i.e. l[0][0] = first cream item, l[1][1] = second alien og item
i = 0
for strain in ascend_returned_items:
    for element in ascend_returned_items[i]:
        print("....Strain: %s" % search_key[i])
        print(".......Price: %s" % element[0])
        print(".......Brand: %s" % element[2])
        print(".......Size : %s" % element[1])
    i += 1
    
print("\nIn stock at Ethos: %s" % ethos_found)
print(line)