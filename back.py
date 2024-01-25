import pandas as pd


def get_games():
    df =pd.read_csv('bgg_dataset.csv',sep=';',encoding='utf8')
    df = df.drop(['Mechanics', 'Domains', "ID"], axis=1)
    games = {}
    columns = df.columns
    for value in df.values:
        games[value[0]] = {columns[1]:value[1], columns[2]:value[2], columns[3]:value[3], columns[4]:value[4], columns[5]:value[5], columns[6]:value[6],columns[7]:value[7], columns[8]:value[8], columns[9]:value[9]}

    return games

# Função para calcular a distância de Manhattan
def manhattan(game1, game2):
    distance = 0
    total = 0

    for key in game1:
        if key in game2:
            distance += abs(game1[key] - game2[key])
            total += 1
    return distance

# Função para recomendar música com base nas preferências do usuário
def recommend(game_name, games):
    games = get_games()
    userProfile = games[game_name]
    distances = []
    for game in games:
        if game != game_name:  # Não queremos comparar com a própria música
            distance = manhattan(games[game], userProfile)
            distances.append((distance, game))
    distances.sort()  # Ordena com base na distância (mais próximo primeiro)
    return distances