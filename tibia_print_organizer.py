import shutil
import os
import json

# Configuration file
config_file = "./settings.json"
# Tibia screenshot dir
tibia_print_dir = "{}/Tibia/packages/Tibia/screenshots".format(os.environ["LOCALAPPDATA"])
# Destination dir of the screenshots
dest = "./Prints"
# Move screenshots or copy
copy = False
# Default operation
operation = shutil.move

if os.path.exists(config_file):
  j = json.load(open(config_file, "r"))
  tibia_print_dir = j.get("print-dir", tibia_print_dir)
  dest = j.get("destination", dest)
  copy = j.get("copy", copy)
  print("\nLoaded config file:")
else:
  print("\nUsing default values:")

if not os.path.exists(tibia_print_dir):
  print("Screenshot directory doesn't exist: {}\n".format(tibia_print_dir))
  print("Check the settings.json file and change the print-dir variable value.")
  exit()

if copy:
  operation = shutil.copy
  op_str = "Operation: copy"
else:
  op_str = "Operation: move (screenshots will be removed from tibia's folder)"

# Print configurations
print("""
Screenshot directory: {}
Destination directory: {}
{}
""".format(tibia_print_dir, dest, op_str))

# Create the destination dir if doesn't exist
if not os.path.exists(dest):
  os.makedirs(dest)

# List screenshots in tibia's dir
prints = [f.path for f in os.scandir(tibia_print_dir) if not f.is_dir()]

for pr in prints:
  prs = pr.split("_")
  # Get the char dir
  char_dir = dest + "/" + prs[-2]
  # Get the print type (death, levelUP, etc)
  sstype_dir = dest + "/" + prs[-2] + "/" + prs[-1].split(".")[0]

  # Create a dir per char
  if not os.path.exists(char_dir):
    os.makedirs(char_dir)

  # Create a dir per type of screenshot
  if not os.path.exists(sstype_dir):
    os.makedirs(sstype_dir)

  # Move files to destination
  operation(pr, sstype_dir)

print("\nDONE!")
