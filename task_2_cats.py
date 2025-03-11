from pathlib import Path

def get_cats_info(path):
 
    try:
        # open the file safty
        with open(path, 'r', encoding = "utf-8") as file:

            cats_list = file.readlines() # read the strings of cats in the file

            cats_list = [item.strip() for item in cats_list] # remove '/n' in each lines
        
            for i in range(len(cats_list)):

                cats_list[i] = cats_list[i].split(',') # split the cats data of worker and salary
              
                cats_dict = {"id": None, "Name": None, "age": None} # create dict for each cat

                if len(cats_dict.keys()) == len(cats_list[i]): # check if len dict and len list equal
                    for key, j in zip(cats_dict.keys(), range(len(cats_list[i]))):
                 
                        cats_dict[key] = str(cats_list[i][j]) # convert cats data into the dict

                cats_list[i] = cats_dict # add cats dict into the list
                      
            return cats_list     

    except FileNotFoundError:
        print("File not found")     