
FILEPATH = "todo.txt"   #benefit's of this if any requirment of changin the name of file
# will change only here and it's reflect every where

def get_read_lines(filepath=FILEPATH) :
    with open(filepath,"r") as file:
        set_user_list = file.readlines()
    return set_user_list

 # non default parameter put first place and second place is default parameter this is right way
def get_write_lines(user_list_argument, filepath=FILEPATH):
    with open(filepath,'w') as file :
        file.writelines(user_list_argument)

if __name__ == "__main__" :
    print("Hello")
    print(get_read_lines())


