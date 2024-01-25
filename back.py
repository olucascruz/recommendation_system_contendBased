import pandas as pd

def get_games():
    df = pd.read_csv('amostra_aleatoria.csv', sep=',', encoding='utf8')
    # df = df.drop(['Mechanics', 'Domains', 'ID'], axis=1)
    games = {}
    columns = df.columns
    for value in df.values:
        # Tratar os valores NaN para garantir que tudo esteja certo
        games[value[0]] = {
            columns[1]: int(value[1]) if not pd.isna(value[1]) else 0,  # Converte para inteiro, se não for NaN
            columns[2]: int(value[2]) if not pd.isna(value[2]) else 0,
            columns[3]: int(value[3]) if not pd.isna(value[3]) else 0,
            columns[4]: int(value[4]) if not pd.isna(value[4]) else 0,
            columns[5]: int(value[5]) if not pd.isna(value[5]) else 0,
            columns[6]: int(value[6]) if not pd.isna(value[6]) else 0,
            columns[7]: float(value[7].replace(',', '.')) if not pd.isna(value[7]) else 0.0,
            columns[8]: int(value[8]) if not pd.isna(value[8]) else 0,
            columns[9]: float(value[9].replace(',', '.')) if not pd.isna(value[9]) else 0.0
        }

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

# Função para recomendar jogos com base nas preferências do usuário
def recommend(game_name, games):
    userProfile = games[game_name]
    distances = []
    for game in games:
        if game != game_name:  # Não queremos comparar com seu próprio jogo
            distance = manhattan(games[game], userProfile)
            distances.append((distance, game))
    distances.sort()  # Ordena com base na distância (mais próximo primeiro)
    return distances