import requests

class FootballAPI:
    def __init__(self, api_key):
        self.base_url = "https://api-football-v1.p.rapidapi.com/v3"
        self.headers = {
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
            "x-rapidapi-key": api_key,
        }

    def get_live_matches(self):
        # Recupera le partite in corso
        url = f"{self.base_url}/fixtures?live=all"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_match_stats(self, match_id):
        # Recupera le statistiche di una specifica partita
        url = f"{self.base_url}/fixtures/statistics?fixture={match_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_injuries(self, team_id):
        # Recupera gli infortuni di una specifica squadra
        url = f"{self.base_url}/injuries?team={team_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()