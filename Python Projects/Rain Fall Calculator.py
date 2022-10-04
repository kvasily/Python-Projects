def main():
  get_statistics(get_month())

def get_month():
  """
get_month cycles through a list of months using a for loop
for each month an input is called using that month
a while loop runs inside the for loop checking againt negative ints
the value of our inputs gets appended to a list
function returns the list
"""
  MONTHS = ['Janurary', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  monthly_values = []
  for i in MONTHS:
    user_input = float(input(f'Enter the rainfall for {i}: '))
    while user_input < 0:
      print("Must be posative int")
      user_input = float(input(f'Enter the rainfall for {i}: '))
      print()
    monthly_values.append(user_input)
    
  return monthly_values

def get_statistics(months):
  """
get_statistics cycles through the list returned by get_month
every value in the list gets added together using a for loop
print statment prints out total value as total rainfall
print statement prints out the total value divided by 12 for average rainfall
print statement grabs list index of highest value and prints the month in the list of months using that index
print statement grabs list of index of lowest value and prints the month in the list of months using that index
"""
  MONTHS = ['Janurary', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  total_rainfall = 0
  for monthly_rainfall in months:
    total_rainfall += monthly_rainfall
  print(f"Total rainfall: {total_rainfall}")
  print(f"Average rainfall: {round((total_rainfall / 12), 2)}")
  print(f"Highest rainfall: {MONTHS[months.index(max(months))]}")
  print(f"Lowest rainfall: {MONTHS[months.index(min(months))]}")
  
main()
