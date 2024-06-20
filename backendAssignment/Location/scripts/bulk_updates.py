from models import Country, State, City
from django.db.models import F

''' 
Bulk update countries
'''
Country.objects.filter(country_code='US').update(name='USA')
Country.objects.filter(country_code='CA').update(name='CAN')

''' 
Bulk update states
'''
State.objects.filter(state_code='CA').update(name='California State')
State.objects.filter(state_code='TX').update(name='Texas State')

''' 
Bulk update cities
'''
City.objects.filter(city_code='LA').update(population=F('population') + 100000)
City.objects.filter(city_code='HOU').update(population=F('population') - 50000)
