from pathlib import Path

def total_salary(salary_file):
    
    # create variable for total money and dictionary of salary list
    total_money = 0
    salary_dict = dict()

    try: 
        # open the file safty
        with open(salary_file, 'r', encoding = "utf-8") as file:

            salary_list = file.readlines() # read the strings of salary in the file
            salary_list = [item.strip() for item in salary_list] # remove '/n' in each lines
        
          
            for i in range(len(salary_list)):

                salary_list[i] = salary_list[i].split(',') # split the name of worker and salary
              
                # convert the list of worker and salry into the 'dict' 
                # where 'key' is the Name of worker 'value' is his salary
                salary_dict[salary_list[i][0]] = float(salary_list[i][1])

             
            # calculate the sum of the salary of all workers
            for v in salary_dict.values():
                total_money += v 

            #calculate the average of the salary of all workers
            average_salary = total_money // len(salary_dict.keys())

            return (total_money, average_salary)
        
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Salary isn't a number")
    except ZeroDivisionError:
        print("Zero division")






