from models import Country, State, City

''' 
Fetch all countries
'''
countries = Country.objects.all()

''' 
Fetch all states
'''
states = State.objects.all()

''' 
Fetch all cities
'''
cities = City.objects.all()
