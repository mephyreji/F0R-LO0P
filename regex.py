import re
txt="the train is intrhetyjry8o spain"
#x=re.search("^the.* spain$",txt)
#x=re.search("[9]",txt)
#x=re.search("[^bog]",txt)#evide eth search caiyathe erikkan vnde anu eth use chaiyunne

#x=re.search("trai?.d",txt)to search the last letter is present


x=re.search("tra.*",txt)#0 to more
#x=re.search("trai.+",txt)#to check the  2 or more letter
if x:
    print("found")
else:
    print("not found")
#$is used for the end word....* is used for the middle
#^ is used for starting
#sequence of charater that from a search pattern....it is used to chechk if a string is a string contain the specified search pattern
print("....................................................................................")
#4 function
#findall,search,split,sub
#/s is denoted as space]