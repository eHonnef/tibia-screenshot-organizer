# Organizador de screenshots do Tibia

Script para organizar a pasta de screenshots do tibia. Ele irá mover ou copiar as screenshots da pasta do tibia para outra pasta de sua escolha organizada por `Nome do personagem e tipo de screenshot` (por exemplo, LevelUP, DeathPVE, Hotkey, etc).

## Release

Tem uma versão compilada para Windows nos Releases, nesse [Link](https://github.com/eHonnef/tibia-screenshot-organizer/releases/tag/1.0.1)

## Requerimentos

Apenas Python 3+ se não usar a versão compilada.

## Usage

Altere os valores no arquivo `settings.json`:

- print-dir: Coloque o caminho completo da pasta de screenshots do tibia, normalmente `C:/Program files/Tibia/packages/Tibia/screenshots`.
- destination: Coloque o caminho completo da pasta de destino, por exemplo, `C:/Users/usuario/Imagens/Tibia`.
- copy: `True` - ele irá manter uma cópia das screenshots na pasta do tibia. `False` - ele irá remover as screenshots da pasta do tibia.

**Recomendo fazer um backup da pasta de screenshots do tibia antes de usar o script.**

## Licença

Licenciada sob a licença do MIT, olhe o arquivo [License](LICENSE) para maiores informações.
