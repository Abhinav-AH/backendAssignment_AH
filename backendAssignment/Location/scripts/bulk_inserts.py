from models import Country, State, City
import uuid

''' 
Create Country instances
'''
countries = [
    Country(id=uuid.uuid4(), name='United States', country_code='US', curr_symbol='$', phone_code='1'),
    Country(id=uuid.uuid4(), name='Canada', country_code='CA', curr_symbol='$', phone_code='1')
]
Country.objects.bulk_create(countries)


''' 
Create State instances
'''
states = [
    State(id=uuid.uuid4(), name='California', state_code='CA', gst_code='06', country=countries[0]),
    State(id=uuid.uuid4(), name='Texas', state_code='TX', gst_code='48', country=countries[0]),
    State(id=uuid.uuid4(), name='Ontario', state_code='ON', gst_code='ON', country=countries[1])
]
State.objects.bulk_create(states)


''' 
Create City instances
'''
cities = [
    City(id=uuid.uuid4(), name='Los Angeles', city_code='LA', phone_code='213', population=4000000, avg_age=35.0, num_of_adult_males=2000000, num_of_adult_females=2000000, state=states[0]),
    City(id=uuid.uuid4(), name='Houston', city_code='HOU', phone_code='713', population=2300000, avg_age=33.0, num_of_adult_males=1150000, num_of_adult_females=1150000, state=states[1]),
    City(id=uuid.uuid4(), name='Toronto', city_code='TOR', phone_code='416', population=2731571, avg_age=36.0, num_of_adult_males=1350000, num_of_adult_females=1381571, state=states[2])
]
City.objects.bulk_create(cities)
