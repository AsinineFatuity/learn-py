#I have tested it works for all the positions of the bad name
name_of_sites = ['Kimende','Rukuma']
sites = {0: ['Ismael','Buyandi','Ateng&APOS;'],1:['Aming&APOS;a','Allylah']} 
good_sign = "'"
bad_sign = "&APOS;"
for key in sites:
    for name in sites[key]:
        if bad_sign in name:
            bad_name_index = sites[key].index(name)
            good_name = name.replace(bad_sign,good_sign)
            sites[key][bad_name_index] = good_name    
print(sites)
#method 2 with better Python code
for site,name in sites.items():
    if bad_sign in name:
        bad_name_index = sites[site].index(name)
        good_name = name.replace(bad_sign,good_sign)
        sites[site][bad_name_index] = good_name 
    for proper_name in name_of_sites:
        sites[proper_name] = sites.pop(site)   
print(sites)     

