from notifier.src.api_clients.fixtures_client import FixturesClient

fixtures_client = FixturesClient()

leagues = fixtures_client.get_leagues()

print(leagues)

response = leagues.as_dict["response"]

desired_leagues = []

# for league in response:
#     if league["country"]["name"]
