import selenium_ascend as ascend
import selenium_ethos as ethos
import time

line = "--------------------------------------------------------"

#urls
ascend_url = "https://letsascend.com/menu/pa-scranton-menu-med/categories/flower"
ethos_url = "https://wilkesbarre.ethoscannabis.com/stores/ethos-wilkes-barre/products/flower"

ascend_found = 0
ascend_price = 0
ascend_brand = 0
ascend_size = 0

ethos_found = 0
ethos_price = 0
ethos_brand = 0
ethos_size = 0

search_key = "Alien OG"

max_scrolls_to_bottom = 30
max_elements_checked = 300
wait_for_load_time = 0.005

found_at_ascend = False
found_at_ethos = False

try:
    ascend_found, ascend_price, ascend_size, ascend_brand = ascend.sel_ascend_run(search_key, ascend_url, max_scrolls_to_bottom,max_elements_checked,wait_for_load_time)
except:
    print("Failed to search Ascend...")
    
try:
    ethos_found = ethos.sel_ethos_run(search_key, ethos_url)
except:
    print("Failed to search Ethos...")


dots_per_side = int((len(line) - len(search_key)) / 2) * "."
print("\n\n%sResults for: %s%s" %  (dots_per_side, search_key, dots_per_side))
print(line)
print("In stock at Ascend: %s" % ascend_found)
if ascend_found:
    print(".......Price: %s" % ascend_price)
    print(".......Brand: %s" % ascend_brand)
    print(".......Size : %s" % ascend_size)

print("\nIn stock at Ethos: %s" % ethos_found)
print(line)