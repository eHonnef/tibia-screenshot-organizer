# Organizador de screenshots do Tibia

Script para organizar a pasta de screenshots do tibia. Ele irá mover ou copiar as screenshots da pasta do tibia para outra pasta de sua escolha organizada por `Nome do personagem e tipo de screenshot` (por exemplo, LevelUP, DeathPVE, Hotkey, etc).

A estrutura ficará parecida com:

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

## Download para Windows

Há uma versão para Windows nos Releases, nesse [Link](https://github.com/eHonnef/tibia-screenshot-organizer/releases/latest).

Baixe o arquivo `tibia_print_organizer.zip` e extraia em qualquer pasta do sistema e siga as instruções abaixo.

## Usage

Altere os valores no arquivo `settings.json`:

- **print-dir**: Coloque o caminho completo da pasta de screenshots do tibia
  - Windows: normalmente `C:/users/<your user>/AppData/Local/Tibia/packages/Tibia/screenshots`.
  - MacOS: normalmente `~/Library/Application Support/CipSoft GmbH/Tibia/packages/Tibia/screenshots`. (onde `~` é o diretório raiz do teu usuário, exemplo: `/Users/YourUserName`).
  - Linux: normalmente `~/.local/share/CipSoft\ GmbH/Tibia/packages/Tibia/screenshots`. You guys know better ;)
- **destination**: Coloque o caminho completo da pasta de destino, por exemplo, `C:/Users/usuario/Imagens/Tibia`.
- **copy**:
  - `True`: irá manter uma cópia das screenshots na pasta do tibia.
  - `False`: irá remover as screenshots da pasta do tibia.

**Recomendo fazer um backup da pasta de screenshots do tibia antes de usar o script.**

## Requerimentos

Apenas Python 3+ se não usar a versão compilada.

## TODO

Uma GUI para configurar o arquivo `settings.json` e executar o programa, a GUI deve funcionar para Windows, Linux e MacOS.

## Licença

Licenciada sob a licença do MIT, veja o arquivo [License](LICENSE) para maiores informações.
