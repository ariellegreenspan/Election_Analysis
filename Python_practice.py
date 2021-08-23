counties = ["Araphoe", "Denver", "Jefferson"]
if "Araphoe" in counties:
    print("true")
else:
    print("false")
if "El Paso" in counties:
    print("true")
else:
    print("false")
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else: 
    print("El Paso is not in the list of counties")
if "Araphoe" in counties and "El Paso" in counties:
    print("Araphoe and El Paso are in the list of counties.")
else:
    print("Araphoe or El Paso are not in the list of counties.")
if "Araphoe" or "El Paso" in counties:
    print("Araphoe or El Paso is in the list of counties.")
else:
    print("Araphoe or El Paso is not in the list of counties")


counties_dict = {"Araphoe":369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters.")


#How many votes did you get?
candidate_votes = int(input("How many votes did you get in the election?"))
#Total votes in the election
total_votes = int(input("What is the total number of votes in the election?"))
#Calculate the percentage of votes you received
message_to_candidate = (
    f"You received {candidate_votes:,} in the election."
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county in voting_data:
    print(f"{'county:registered voters'} has registered voters.") 




