boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) != len(girls):
    print('Кто-то может остаться без пары!')
else:
    boys_sort = boys.sort()
    girls_sort = girls.sort()
    couples = zip(boys, girls)
    print('Идеальные пары:')
    for boys_items, girls_items in couples:
        print(f'{boys_items} и {girls_items}')