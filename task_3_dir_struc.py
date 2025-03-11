import colorama, sys
from pathlib import Path



def struc_dir(dir, count_tab):
 
    total_tab = len(str(dir).split('\\')) - count_tab + 1  # calculate in totaly how many tab need for formating each string
   
    for item in dir.iterdir(): # find folder and file
       
        if item.is_file(): # check if item is file
         
            print(colorama.Fore.GREEN + '\t' * (total_tab), item.name)
         
        elif item.is_dir(): # check if otem is folder
      
            print(colorama.Fore.BLUE + "{} {}/".format('\t' * total_tab, item.name))

            struc_dir(item, count_tab) # recursion for sub-folders

    
    return None



if __name__ == "__main__":
    try:
        dir = Path(sys.argv[1]) # get directory from cmd

        count_tab = len(str(dir).split('\\')) # calculate how many tabulation is needs for formating string 

        print(colorama.Fore.BLUE + f"{dir.name}/") # display folder which struc need to display
          
        struc_dir(dir, count_tab) # call func whitch display struc of folder   
          
    except FileNotFoundError:
        print("File not found")

    print(colorama.Style.RESET_ALL) # reset style cmd to default