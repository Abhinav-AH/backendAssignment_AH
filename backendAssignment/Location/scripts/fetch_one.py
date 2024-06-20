from models import Country, City, State

''' 
Fetch all cities of a state
'''
state = State.objects.get(id='state_id')
cities_of_state = state.cities.all()

''' 
Fetch all states of a country
'''
country = Country.objects.get(id='country_id')
states_of_country = country.states.all()

''' 
Fetch a city with minimum population
'''
country = Country.objects.get(name='Country Name')
min_population_city = City.objects.filter(state__country=country).order_by('population').first()

''' 
Fetch a city with maximum population
'''
max_population_city = City.objects.filter(state__country=country).order_by('-population').first()
