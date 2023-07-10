from datetime import datetime
def info (name,age,birthdate):
    print('{} is {} years old and she/he was born on {}'.format(name,age,birthdate))

people = []
oldest_age = None
youngest_age = None
oldest_name = None
youngest_name = None

while True :
  name = input('enter your name or exit : ')
  if name == 'exit' :
    break
  try:
    birthdate = datetime.strptime(input('enter your birthdate (dd-mm-yyyy) :'),'%d-%m-%Y')
  except ValueError:
    print('Invalid date')
    continue
  today = datetime.now()
  age = (today.year - birthdate.year) - (not(birthdate.day >= today.day)) or (birthdate.month >= today.month)



  if oldest_age is None or age > oldest_age :
    oldest_age = age
    oldest_name = name

  if youngest_age is None or age < youngest_age :
    oldest_age = age
    youngest_name = name


  people.append({
      'name' : name,
      'age' : age,
      'birthdate' : birthdate.strftime('%A')
      })


for person in people :
  info(**person)

if len(people) > 1 :
  print('The oldest one is',oldest_name)
  print('The youngest one is',youngest_name)
else :
  print('There is no oldest or youngest person')
print('Total People: ',len(people))

