import os

path = os.getcwd()

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)


    # Read in the file
    with open(f, 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('challengeType', 'type')
    filedata = filedata.replace('description', 'text')

    # Write the file out again
    with open(f, 'w') as file:
      file.write(filedata)
