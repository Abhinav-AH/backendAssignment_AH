from models import Country, CustomUser, State, City
import uuid

# Create Country instances
country1 = Country(id=uuid.uuid4(), name='United States', country_code='US', curr_symbol='$', phone_code='1')
country2 = Country(id=uuid.uuid4(), name='India', country_code='IND', curr_symbol='Rs', phone_code='1')
country1.save()
country2.save()

# Create State instances
state1 = State(id=uuid.uuid4(), name='California', state_code='CA', gst_code='06', country=country1)
state2 = State(id=uuid.uuid4(), name='Texas', state_code='TX', gst_code='48', country=country1)
state3 = State(id=uuid.uuid4(), name='Telangana State', state_code='TS', gst_code='12', country=country2)
state1.save()
state2.save()
state3.save()

# Create City instances
city1 = City(id=uuid.uuid4(), name='Los Angeles', city_code='LA', population=4000000, avg_age=35.0, num_of_adult_males=2000000, num_of_adult_females=2000000, state=state1)
city2 = City(id=uuid.uuid4(), name='Houston', city_code='HOU', population=2300000, avg_age=33.0, num_of_adult_males=1150000, num_of_adult_females=1150000, state=state2)
city3 = City(id=uuid.uuid4(), name='Hyderabad', city_code='HYD', population=2731571, avg_age=36.0, num_of_adult_males=1350000, num_of_adult_females=1381571, state=state3)
city1.save()
city2.save()
city3.save()



user1 = CustomUser(id=uuid.uuid4(), email='abhinavsinha@gmail.com', is_active=True, is_admin=True)
user2 = CustomUser(id=uuid.uuid4(), email='rajsharma@gmail.com', is_active=True, is_admin=True)
user3 = CustomUser(id=uuid.uuid4(), email='mdmurtaza@gmail.com', is_active=True, is_admin=True)
user4 = CustomUser(id=uuid.uuid4(), email='mohakgarg@gmail.com', is_active=True, is_admin=True)
user1.save()
user2.save()
user3.save()
user4.save()