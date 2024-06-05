import selenium_ascend as ascend
import selenium_ethos as ethos
import time

#urls
ascend_url = "https://letsascend.com/menu/pa-scranton-menu-med/categories/flower"
ethos_url = "https://wilkesbarre.ethoscannabis.com/stores/ethos-wilkes-barre/products/flower"

search_key = "Gello"

max_scrolls_to_bottom = 30
max_elements_checked = 300
wait_for_load_time = 0.15

found_at_ascend = False
found_at_ethos = False

try:
    found_at_ascend = ascend.sel_ascend_run(search_key, ascend_url, max_scrolls_to_bottom,max_elements_checked,wait_for_load_time)
except:
    print("Failed to search Ascend...")
    
try:
    found_at_ethos = ethos.sel_ethos_run(search_key, ethos_url)
except:
    print("Failed to search Ethos...")

print("------------------------------------------------------------------------")
print("In stock at Ascend: %s" % found_at_ascend)
print("In stock at Ethos: %s" % found_at_ethos)
print("------------------------------------------------------------------------")
