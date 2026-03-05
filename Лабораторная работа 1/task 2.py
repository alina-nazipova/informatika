list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count_of_players = len(list_players) // 2 # находим количество игроков, которое будет в каждой команде
team_1 = list_players[:count_of_players] # разделяем список (с 1-го по 3-го участника
team_2 = list_players[count_of_players:] # разделяем список с 4-го до 6-го участника
print(team_1) # выводим на экран первую команду
print(team_2) # выводим на экран вторую команду
