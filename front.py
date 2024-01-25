import streamlit as st
from math import sqrt
from back import *

# Função para adicionar uma nova game à MyGames
def adicionar_game_MyGames(MyGames, nome_game, userProfile):
    MyGames[nome_game] = userProfile

# Streamlit frontend
st.title("Jogos de tabuleiro")

# Sidebar para escolher a game a ser adicionada à MyGames
st.sidebar.title("Escolha um jogo")
selected_game = st.sidebar.selectbox("Selecione um jogo:", list(get_games().keys()))

# MyGames inicial
MyGames = {}

# Adiciona a game escolhida à MyGames
if st.sidebar.button("Escolher jogo"):
    adicionar_game_MyGames(MyGames, selected_game, get_games()[selected_game])
    st.sidebar.success(f"O jogo '{selected_game}' foi escolhido!")

# Atualiza a MyGames com músicas similares à última adicionada
if MyGames:
    st.subheader("Seu jogo:")
    st.write(list(MyGames.keys()))

    # Obtém recomendações para a última música adicionada à MyGames
    ultima_game_adicionada = list(MyGames.keys())[-1]
    recomendacoes = recommend(ultima_game_adicionada, get_games())

    st.subheader("Jogos Baseados no jogo escolhido:")
    st.write([f"{game} - Distância: {distancia}" for distancia, game in recomendacoes])