import streamlit as st
from api_handler import FootballAPI

# Configura l'API
API_KEY = "dcbc8bcf4bmsh0a1bf8eef94569ep13c016jsn39edf0cb3157"  # Sostituisci con la tua API Key
football_api = FootballAPI(API_KEY)

def calculate_shot_prediction(stats, injuries_home, injuries_away):
    # Calcola la previsione dei tiri
    try:
        home_shots = stats['response'][0]['statistics'][0]['value']  # Tiri squadra di casa
        away_shots = stats['response'][1]['statistics'][0]['value']  # Tiri squadra ospite
    except (IndexError, KeyError):
        home_shots, away_shots = 0, 0

    home_injury_penalty = len(injuries_home['response']) * 0.1
    away_injury_penalty = len(injuries_away['response']) * 0.1

    predicted_home_shots = home_shots * (1 - home_injury_penalty)
    predicted_away_shots = away_shots * (1 - away_injury_penalty)

    return predicted_home_shots, predicted_away_shots

# Interfaccia Streamlit
st.title("Previsione Tiri - Partite in Corso")
st.sidebar.header("Opzioni")
update_button = st.sidebar.button("Aggiorna Dati")

if update_button:
    st.write("Aggiornamento in corso...")
    matches = football_api.get_live_matches()

    if matches['response']:
        for match in matches['response']:
            match_id = match['fixture']['id']
            home_team = match['teams']['home']['name']
            away_team = match['teams']['away']['name']

            stats = football_api.get_match_stats(match_id)
            injuries_home = football_api.get_injuries(match['teams']['home']['id'])
            injuries_away = football_api.get_injuries(match['teams']['away']['id'])

            predicted_home, predicted_away = calculate_shot_prediction(stats, injuries_home, injuries_away)

            st.subheader(f"{home_team} vs {away_team}")
            st.write(f"Tiri previsti - {home_team}: **{predicted_home:.2f}**")
            st.write(f"Tiri previsti - {away_team}: **{predicted_away:.2f}**")
            st.write("---")
    else:
        st.write("Nessuna partita in corso al momento.")
        if __name__ == "__main__":
            import streamlit as st
            st.write("Benvenuto nella tua app Streamlit!")