'''
Armin Rajaee    Homework2 Data structure 
section doshanbe 07:30 
'''
import random
import time
import matplotlib.pyplot as plt

lst = [
 {'firstname': 'Raj', 'lastname': 'Nayyar'},
 {'firstname': 'Suraj', 'lastname': 'Sharma'},
 {'firstname': 'Karan', 'lastname': 'Kumar'},
 {'firstname': 'Jade', 'lastname': 'Canary'},
 {'firstname': 'Raj', 'lastname': 'Thakur'},
 {'firstname': 'Raj', 'lastname': 'Sharma'},
 {'firstname': 'Kiran', 'lastname': 'Kamla'},
 {'firstname': 'Armaan', 'lastname': 'Kumar'},
 {'firstname': 'Jaya', 'lastname': 'Sharma'},
 {'firstname': 'Ingrid', 'lastname': 'Galore'},
 {'firstname': 'Jaya', 'lastname': 'Seth'},
 {'firstname': 'Armaan', 'lastname': 'Dadra'},
 {'firstname': 'Ingrid', 'lastname': 'Maverick'},
 {'firstname': 'Aahana', 'lastname': 'Arora'}
]

def sort_name(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i]['firstname'] > lst[j]['firstname']:
                lst[i], lst[j] = lst[j], lst[i]
            elif lst[i]['firstname'] == lst[j]['firstname']:
                if lst[i]['lastname'] > lst[j]['lastname']:
                    lst[i], lst[j] = lst[j], lst[i]
    return lst

result = sort_name(lst)
print(result)

data_sizes = list(range(10, 1001, 10))
execution_times = []

for size in data_sizes:
    list_random = [{'firstname': random.randint(0, 1000), 'lastname': random.randint(0, 1000)} for _ in range(size)]
    
    start_time = time.time()
    sorted_list = sort_name(list_random)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

plt.plot(data_sizes, execution_times)
plt.xlabel('Data Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of sort_by_firstname_lastname Algorithm')
plt.show()