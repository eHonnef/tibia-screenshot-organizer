"""
MIT License

Copyright (c) 2021 Honnef

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import shutil
import os
import json

# Configuration file
config_file = "./settings.json"
# Tibia screenshot dir
tibia_print_dir = ""
if "LOCALAPPDATA" in os.environ.keys():
    tibia_print_dir = "{}/Tibia/packages/Tibia/screenshots".format(os.environ["LOCALAPPDATA"])
# Destination dir of the screenshots
dest = "./Prints"
# Move screenshots or copy
copy = False
# Default operation
operation = shutil.move

if os.path.exists(config_file):
    j = json.load(open(config_file, "r", encoding="utf8"))
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


def split_SS_name(print_name: str) -> dict:
    spl_str = print_name.split("_")
    return {"char_name": spl_str[2], "ss_type": spl_str[3] if "." not in spl_str[3] else spl_str[3].split(".")[0]}


for pr in prints:
    ss_infos = split_SS_name(pr)
    # Get the char dir
    char_dir = dest + "/" + ss_infos["char_name"]
    # Get the print type (death, levelUP, etc)
    sstype_dir = char_dir + "/" + ss_infos["ss_type"]

    # Create a dir per char
    if not os.path.exists(char_dir):
        os.makedirs(char_dir)

    # Create a dir per type of screenshot
    if not os.path.exists(sstype_dir):
        os.makedirs(sstype_dir)

    # Move files to destination
    operation(pr, sstype_dir)

print("\nDONE!")
