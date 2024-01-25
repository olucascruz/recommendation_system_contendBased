import streamlit as st
from back import *

# Função para adicionar um novo jogo à MyGames
def adicionar_game_MyGames(MyGames, nome_game, userProfile):
    MyGames[nome_game] = userProfile

# Streamlit frontend
st.title("Jogos de Tabuleiro")

# Sidebar para escolher um jogo a ser adicionado à MyGames
st.sidebar.title("Escolha um jogo")
selected_game = st.sidebar.selectbox("Selecione um jogo:", list(get_games().keys()))

# MyGames inicial
MyGames = {}

# Adiciona um jogo escolhido à MyGames
if st.sidebar.button("Escolher jogo"):
    adicionar_game_MyGames(MyGames, selected_game, get_games()[selected_game])
    st.sidebar.success(f"O jogo '{selected_game}' foi escolhido!")

# Atualiza o MyGames com jogos similares ao último adicionado
if MyGames:
    st.subheader("Seus Jogos:")
    st.write(list(MyGames.keys()))

    # Obtém recomendações para o último jogo adicionado à MyGames
    ultima_game_adicionada = list(MyGames.keys())[-1]
    recomendacoes = recommend(ultima_game_adicionada, get_games())

    st.subheader("Jogos Baseados no Jogo Escolhido:")
    for distancia, game in recomendacoes:
        st.write(f"Nome do jogo: {game}, Distância: {distancia}")