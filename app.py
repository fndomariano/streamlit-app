# -*- coding: utf-8 -*-

import streamlit as st
import seaborn as sns
import pandas as pd

OPTIONS = {
	'Pontos': 'PTS',
	'Rebotes': 'REB',
	'Assistências': 'AST',
}

def main():

	data = pd.read_csv('nba-stats.csv')

	options = ['Pontos', 'Rebotes', 'Assistências']
	players = data['PLAYER_NAME'].unique()

	st.sidebar.title("NBA Stats")

	player = st.sidebar.selectbox("Selecione o jogador", players)
	stat = st.sidebar.radio('Escolha uma estatística', options)

	st.title(player)
	
	player_stats = data[data['PLAYER_NAME'] == player]
	st.markdown(f'## {stat}')
	ax = sns.barplot(x="SEASON", y=OPTIONS[stat], data=player_stats)
	ax.set_ylabel(f"{stat}")
	ax.set_xlabel("Temporada")
	st.pyplot()

if __name__ == '__main__':
	main()