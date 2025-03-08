from pathlib import Path

def get_cats_info(path):
 
    try:
        # open the file safty
        with open(path, 'r', encoding = "utf-8") as file:

            cats_list = file.readlines() # read the strings of cats in the file

            cats_list = [item.strip() for item in cats_list] # remove '/n' in each lines
        
            for i in range(len(cats_list)):

                cats_list[i] = cats_list[i].split(',')
              
                cats_dict = {"id": None, "Name": None, "age": None}

                if len(cats_dict.keys()) == len(cats_list[i]):
                    for key, j in zip(cats_dict.keys(), range(len(cats_list[i]))):
                 
                        cats_dict[key] = str(cats_list[i][j])

                cats_list[i] = cats_dict
                                       
            return cats_list
                    





    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    dir = Path(__file__).parent 
    cats_file = Path(dir / "cats.txt") #get the path of file with cats

    print(get_cats_info(cats_file))
        