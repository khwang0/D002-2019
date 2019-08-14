collection = ["Pikachu", "Bulbasaur", "Squirtle", "Nidoqueen"]
newly_caught = ["Bulbasaur", "Kakuna", "Arbok", "Jigglypuff"]

for i in newly_caught:
    if  not i in collection:
        collection = collection + [i]
  
print(collection)
