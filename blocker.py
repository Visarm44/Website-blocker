import time
from classes import Blocker

host_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com"]
hours_window = (8, 17)

blocker = Blocker(host_path, redirect, website_list)

while True:
    if blocker.block_condition(hours_window):
        blocker.block()
    else:
        blocker.unblock()
    
    time.sleep(5)