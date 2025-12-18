# Name: Maxwell Beutel
# Date: 2/6/2025
# Data Serialization/File Formats

# import the only lib we need for this asignmnet
import json

# now to open the CSV file
# Note: Change the file path value for x.csv for whatever file you want it to read
filePath = "Meteorite_Landings_AssignmentMeteorite_Landings_Assignment.csv"
# Open the csv file
with open(filePath, 'r') as f:
        # Skip the header row, since we dont want to read that. 
        next(f)
        # Make a array for storing the dicitonary.
        dictResults = []
        for line in f:
                # any whitespace and newline characters
                # strip() removes leading and trailing characters from a string.
                words = line.strip().split(',')

                # Create a dictionary
                # Note: for anything that is none string we must account for none Traditional input. 
                # This is the same as writting a if else statement. 
                thisdict = dict(
                    name=words[0],  # string
                    id=int(words[1])if words[1] else None,  # Convert to integer
                    nametype=words[2],  # string
                    mass_g=float(words[3]) if words[3] else None,  # Convert to float
                    fall=words[4],  # string
                    year=int(words[5]) if words[5] else None,  # Convert to integer
                    reclat=float(words[6]) if words[6] else None,  # Convert to float
                    reclong=loat(words[7]) if words[7] else None  # Convert to float
                )

                # Append the dictionary to the list
                dictResults.append(thisdict)

# Now create the json object
jsonData = json.dumps(dictResults)
# If we want a cleaner look then we can dump using the following command.
# jsonData = json.dumps(dictResults, indent=4)
# Link where I found that code, https://stackoverflow.com/questions/72801608/dumps-not-write-to-json-file-pretty-print-i-already-using-indent-4-i-added-jso

# write output.json file
with open('output.json', 'w') as jsonFile:
        jsonFile.write(jsonData)
