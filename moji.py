import sys,json
mappings = json.loads(open("mappings.json").read())
#print(mappings)
script = open(sys.argv[1]).read()
compiled = ""
for char in script:
  if char in mappings:
    compiled += mappings[char]
  else:
    compiled += char
exec(compiled)
