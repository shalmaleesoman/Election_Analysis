counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Pasonis in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else: 
    print("Arapahoe and El Paso are not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_tuple = ("Arapahoe", "Denver", "Jefferson")

for i in range(len(counties_tuple)):
    print(counties_tuple[i])
    
for county in counties_tuple:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for county in counties_dict:
    print(county)


for voters in counties_dict.values():
    print(voters)


for county in counties_dict:
    print(counties_dict[county])


for county in counties_dict:
    print(counties_dict.get(county))


voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}],


for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) + " registered voters. ") 

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")














