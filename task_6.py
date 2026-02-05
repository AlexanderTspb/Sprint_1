types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_duplikate(dict):
    for i in range(1, len(tickets)+1):
        for task in tickets[i]:
     #   print(task + ' ')
            for l in range(i+1, len(tickets)+1):
                for task_s in tickets[l]:
     #           print(task_s)
                    if task_s == task:
                        tickets[l].remove(task_s)
delete_duplikate(tickets)
#print(tickets)

tickets_by_type = {}
def sumdict(types, tickets):
    for key, value in types.items():
        for key_s in tickets.keys():
            if key == key_s:
                tickets_by_type[value] = tickets.get(key_s)
sumdict(types, tickets)        
print(tickets_by_type)