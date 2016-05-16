
l = ["hello", "world", "banana"]

"""
def len_of_str(x):
    return len(x)

len_of_words = map(len_of_str, l)
"""

len_of_words = [len(x) for x in l]
#[op for x in list]
print(len_of_words)

# map: function, list(str) > list(int)
# function: (str) > (int)


"""
double_items = []
for item in l:
    transformed_item = op(item)
    new_list.append(transformed_item)

print(double_items)
"""
"""
double_items = map(op, l)
print(double_items)
"""

"""
users = ['john@gmail.com', 'mary@hotmail.com']

def send_email_to_user(user):
    # try to send the email
    # True or False
    pass

results = map(send_email_to_user, users)
[True, False]
"""





