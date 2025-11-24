from datetime import datetime

class Blocker:
    def __init__(self, host_path, redirect, website_list):
        self.host_path = host_path
        self.redirect = redirect
        self.website_list = website_list

    def block_condition(self, time_window=(0, 24), t=None): # Checks if the current time is in the specified time window
        if t == None:
            t = datetime.now().hour
        
        if time_window[0] <=  t < time_window[1]:
            return True
        else:
            return False
        
    def block(self):
        with open(self.host_path, "r") as f:
           host_content = f.read()
    
        websites_to_add = []
        for website in self.website_list:
            if website not in host_content:
                websites_to_add.append(f"\n{self.redirect} {website}")

        if to_add:
            with open(self.host_path, "a") as f:
                f.write("".join(to_add))

    def unblock(self):
        with open(self.host_path, "r+") as f:
            lines = f.readlines()

            f.seek(0)

            for line in lines:
                if not any(website in line for website in self.website_list):
                    f.write(line)
        
            f.truncate()
