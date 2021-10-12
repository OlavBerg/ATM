import json
from dict_to_atm import dictToAtm

print("")

# Load ATM
loadStream = open("saved_atm.txt", "r")
atm = dictToAtm(json.load(loadStream))
loadStream.close()

# Run ATM
atm.run()

# Save ATM
saveStream = open("saved_atm.txt", "w")
json.dump(atm.toDict(), saveStream, indent = 4)
saveStream.close()

print("")