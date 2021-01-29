from link import singly_linked_list

items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')


for val in items.iterate_item():
    print(val)