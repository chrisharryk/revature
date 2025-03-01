import random

names = [
    'Chris Harry K',
    'Siddartha Kommu',
    'Mayank Pathak',
    'Balaji Pappala',
    'Sumanth Kumar Valluru',
    'Japa Harish',
    'Lakshmi Sahithi Vanga',
    'G.VANI',
    'Indukuru Sravani',
    'Sirneni Pavan Sai',
    'Suman Kumar Ghorai',
    'Yugesh Karoti',
    'chundi vishnu priya',
    'Sri Sanjana Indugula',
    'G Santosh Kumar',
    'GANGIREDLA KARTHIK',
    'Venkata Naidu Punnana',
    'pedapalli suresh',
    'Prathamesh Pahune',
    'Venkata Krishna kolli',
    'Ram Mishra'
]

# assign random role numbers
def func1():
    # select role number which is not visited
    # select name which is not selected
    # push into map
    # add role number to visited and name to visited
    visited_roles = visited_names = set()
    n = len(names)
    ans = {}
    while len(visited_roles) < n:
        random_role = random.randint(1, n+1)
        while random_role in visited_roles:
            random_role = random.randint(1, n+1)
        random_name = names[random.randint(0, n-1)]
        while random_name in visited_names:
            random_name = names[random.randint(0, n-1)]
        print(f'{random_role}: {random_name}')
        visited_roles.add(random_role)
        visited_names.add(random_name)
    return ans

def func2():
    ans = func1()
    n = len(names)
    batch1 = batch2 = visited = set()
    while len(visited) < n:
        random_role = random.randint(1, 21)
        while random_role in visited:
            random_role = random.randint(1, 21)
        visited.add(random_role)
        random_batch = random.randint(1, 2)
        if random_batch == 2:
            batch2.add(ans[random_role])
        else:
            batch1.add(ans[random_role])
    return (batch1, batch2)

print(func2())