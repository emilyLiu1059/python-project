import re
# Open the file and turn it into list
with open('emailbody2.txt', 'r') as file:
    lines = file.readlines()

# Produce a full file path if "K:\BatchLoadFile" is in the file
files = []
for line in lines:
    if "K:\\BatchLoadFile" in line:
        for line in lines: 
          match_nd = re.search(r'Batch_ND_\S+', line)
          if match_nd:
              new_string = "K:\\BatchLoadFile\\" + match_nd.group()
              if not new_string.endswith(".txt"):
                  new_string += ".txt"
              files.append(new_string)

#Extract the lines containing "TEST" and then add just the test string to [test], not the other strings before and after.
test = []
for line in lines:
    match_test = re.search(r'TEST\s*(\S+)', line)
    if match_test:
        test_string = match_test.group()
        test.append(test_string)

# Extract the lines containing a date and then add just the date to [date], not the other strings before and after.
date = []
for line in lines:
    match_date = re.search(r'(\b\d{1,2}/\d{1,2}/\d{4}\b)', line)
    if match_date:
        date.append(match_date.group())

#Extract the lines containing "BYD" and then add that string to [jobs], not the other strings before and after.
jobs = []
for line in lines: 
  if 'BYD' in line:
    jobs.append(re.findall(r'BYD\S*', line)[0])

# Write the relevant lines to a new file
with open('relevant_info.txt', 'w') as new_file:
    for line in files + test + date + jobs:
        new_file.write(line + '\n')