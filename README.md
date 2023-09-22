# Crew

## Iniciando o projeto

Crie o virtual environment

```bash
python3 -m venv venv
```

Ative o virtual environment

```bash
source venv/bin/activate
```

Instale as dependências

```bash
pip install -r requirements.txt
```

### No Windows

Crie o virtual environment

```bash
python -m venv venv
```

Ative o virtual environment

```bash
venv\Scripts\activate.bat
```

Instale as dependências

```bash
pip install -r requirements.txt
```

## Instalando novas Dependências

Sempre que instalar uma nova dependência, atualize o arquivo `requirements.txt`.

```bash
pip freeze > requirements.txt
```

## Estrutura de Pastas

Arquitetura de pastas do projeto

### entities

Classes das entidades do jogo.
Ex.: `Player`, `Asteroid`, `Bullet`, `Throttle` etc.

``` text
entities/
├── asteroid_entity.py
├── bullet_entity.py
├── player_entity.py
```

### util

Arquivos de utilidades do jogo. Funções que podem ser usadas em qualquer lugar do projeto.

``` text
util/
├── collision.py
├── constants.py
```

### assets

Arquivos de assets do jogo. Imagens, sons, etc.

``` text
assets/
├── sprites/
│   ├── asteroid.png
│   ├── bullet.png
│   ├── player.png
│   └── space.png
└── sounds/
    ├── explosion.wav
    ├── laser.wav
    └── music.wav
```

## Equipe

| [![Esdras Albino](https://avatars.githubusercontent.com/u/80992456?v=4&s=70)](https://github.com/EsdrasAlbino/) | [![Maria Fernanda Amorim](https://avatars.githubusercontent.com/u/125303577?v=4&s=70)](https://github.com/MariaFFA/) | [![Matheus Borges](https://avatars.githubusercontent.com/u/116684279?v=4&s=70)](https://github.com/MathBorgess/) | [![Tulio  Oliveira](https://avatars.githubusercontent.com/u/127243520?v=4&s=70)](https://github.com/tuliooarauj/) | [![Welton Felix](https://avatars.githubusercontent.com/u/52381662?v=4&s=70)](https://github.com/weltonfelix/) |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [Esdras Albino](mailto:ehas@cin.ufpe.br)                                                                        | [Maria Fernanda Amorim](mailto:mffa@cin.ufpe.br)                                                                     | [Matheus Borges](mailto:mbf3@cin.ufpe.br)                                                                        | [Tulio Araujo](mailto:toa@cin.ufpe.br)                                                                            | [Welton Felix](mailto:wplf@cin.ufpe.br)                                                                       |

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---
Projeto desenvolvido para a disciplina Introdução à Programação ([IF669](https://cin.ufpe.br/~if669)) do curso de Ciência da Computação do CIn - UFPE ![cin-logo](https://portal.cin.ufpe.br/wp-content/uploads/2020/06/cropped-iconecin-32x32.png).
