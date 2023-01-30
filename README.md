# Tibia screenshot organizer

[Esse arquivo em PT-BR](README-PT-BR.md)

Script to organize the tibia's screenshot folder. It'll move (or copy) the screenshots from the tibia's screenshot folder to another folder and organize by `character name and screenshot type` (e.g.: LevelUP, DeathPVE, Hotkey, etc).

The folder's structure will look like this:

```
.
└── prints_organized/
    ├── Character 1/
    │   ├── DeathPVE/
    │   │   ├── print_1
    │   │   └── print_2
    │   ├── LevelUP/
    │   │   └── print_1
    │   └── SkillUP/
    │       └── print_1
    ├── Character 2/
    │   ├── DeathPVE/
    │   │   ├── print_1
    │   │   └── print_2
    │   ├── LevelUP/
    │   │   └── print_1
    │   └── SkillUP/
    │       └── print_1
    └── ... (and so on, you got the idea)
```

## Windows Download

There is a compiled version for Windows in the releases. [Link](https://github.com/eHonnef/tibia-screenshot-organizer/releases/latest).

Download the file `tibia_print_organizer.zip` and extract it in any folder of your system, then follow the instructions below.

## Usage

Change the values in the `settings.json` file:

- **print-dir**: Put the full path to tibia's screenshot folder
  - Windows: usually `C:/users/<your user>/AppData/Local/Tibia/packages/Tibia/screenshots`.
  - MacOS: usually `~/Library/Application Support/CipSoft GmbH/Tibia/packages/Tibia/screenshots`. (where `~` is your user’s home directory, i.e. `/Users/YourUserName`).
  - Linux: usually `~/.local/share/CipSoft\ GmbH/Tibia/packages/Tibia/screenshots`. You guys know better ;)
- **destination**: The destination folder that'll have all the organized screenshots.
- **copy**:
  - `True`: It'll keep the screenshots in tibia folder.
  - `False`: It'll remove the screenshots from tibia folder.

**It's recomended to do a backup of tibia's screenshot folder before using this script.**

## Requirements

Only Python 3+.

## TODO

A GUI to configure the `settings.json` file and to execute the program that works on Windows, Linux and MacOS.

## License

Licensed under MIT license, check the [License](LICENSE) file for more information.
