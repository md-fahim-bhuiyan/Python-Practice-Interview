number = [1, 2, 3, 4, 5 ]
country = ['Bangladesh', 'India', 'Pakistan', 'Japan', 'Canada', 'USA']

print(number[2:5])

country.append('UK')
print(country)
print(len(number))
country.remove('USA')
print(country)

for i in country:
    print(i)