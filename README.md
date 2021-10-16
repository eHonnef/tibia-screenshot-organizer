# Tibia screenshot organizer

[Esse arquivo em PT-BR](README-PT-BR.md)

Script to organize the tibia's screenshot folder. It'll move (or copy) the screenshots from the tibia's screenshot folder to another folder and organize by `character name and screenshot type` (e.g.: LevelUP, DeathPVE, Hotkey, etc).

## Release

There is a compiled version for Windows in the releases. [Link](https://github.com/eHonnef/tibia-screenshot-organizer/releases/tag/1.0.1)

## Requirements

Only Python 3+.

## Usage

Change the values in the `settings.json` file:

- print-dir: Put the full path to tibia's screenshot folder, usually `C:/Program files/Tibia/packages/Tibia/screenshots`.
- destination: The destination folder that'll have all the organized screenshots.
- copy: `True` - It'll keep the screenshots in tibia folder. `False` - It'll remove the screenshots from tibia folder.

**It's recomended to do a backup of tibia's screenshot folder before using this script.**

## License

Licensed under MIT license, check the [License](LICENSE) file for more information.
