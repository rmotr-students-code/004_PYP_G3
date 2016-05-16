"""
def my_fun():
    print("Hello")
    
# a = my_fun


def transform_my_func_1(a_func):
    def new_func():
        print("Executing a func: {}".format(a_func))
        a_func()
    return new_func

transformed_function = transform_my_func_1(my_fun)

transformed_function()

"""
"""
def ask_to_save_work():
    # ask the user to save?
    # if she said yes:
    #    save it
    # close the tab
    pass 


cross_icon_cliked(ask_to_save_work)

"""

def send_email_to_users(users):
    del users[0]
    pass

users = ['john@gmail.com', 'mary@hotmail.com']

send_email_to_users(users)






