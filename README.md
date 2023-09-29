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

## Bibliotecas utilizadas

```bash
pygame==2.5.1
```

## Divisão de tarefas do projeto

| Time                                                  | Tarefas                                                                                |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [Esdras Albino](https://github.com/EsdrasAlbino/)     | Desenvolveu estados de controle do jogo e lógica envolvendo itens e inventário         |
| [Maria Fernanda Amorim](https://github.com/MariaFFA/) | Desenvolveu todas as responsividades do jogo                                           |
| [Tulio Oliveira](https://github.com/tuliooarauj/)     | Desenvolveu colisões entre todas os objetos do projeto                                 |
| [Matheus Borges](https://github.com/MathBorgess/)     | Desenvolveu telas iniciais, créditos e game over                                       |
| [Welton Felix](https://github.com/weltonfelix/)       | Principal code review, desenvolveu a classe base de entidades e movimentação do player |

## Conceitos utilizados

Aplicamos desde os fundamentos como listas e estruturas de repetição, até os tópicos avançados, incluindo os princípios iniciais da Programação Orientada a Objetos (POO).

A utiilização de funções, loops e condicionais foram cruciais para o desenvolvimento do jogo, visto que, contribuem imensamente para a escalabilidade e organização do código.

Além disso Orientação a objetos nos permitiu a estruturação e construção do código em torno da organização em classes e suas funções associadas, a capacidade de gerenciar cada objeto de forma independente simplificou o processo de escrita do código e significativamente aprimorou a sua legibilidade.

## Estrutura de Pastas

Arquitetura de pastas do projeto

### entities

Classes das entidades do jogo.
Ex.: `Player`, `Asteroid`, `Bullet`, `Throttle` etc.

```text
entities/
├── ammo_entity.py
├── asteroid_entity.py
├── bullet_entity.py
├── credits_screen_entity.py
├── crew_entity.py
├── entity.py
├── game_entity.py
├── initial_screen_entity.py
├── inventory_entity.py
├── item_entity.py
├── life_entity.py
├── player_entity.py
├── racetrack_entity.py
├── throttle_entity.py
```

### util

Arquivos de utilidades do jogo. Funções que podem ser usadas em qualquer lugar do projeto.

```text
util/
├── change_window_size_util.py
├── colors.py
├── image_render.py
├── update_coords..py
```

### assets

Arquivos de assets do jogo. Imagens, sons, etc.

```text
assets/

├── asteroid.png
├── bullet.png
├── player.png
├── background.png
├── commet.png
├── propellant.png
├── theme.mp3
```

# Desafios e Erros

Enfrentamos alguns desafios durante o projeto, especialmente relacionados ao planejamento e à priorização de tarefas dentro da equipe. Sendo o principal problema a falta de priorização nas tarefas fundamentais, o que nos levou a gastar um tempo considerável reescrevendo parte da base do código, juntamente com as implementações que já tínhamos concluído. Como resultado, enfrentamos diversos problemas de conflito e integração entre diferentes branches.

Todos do time com certeza levaram como maior lição que um bom planejamento com priorizações certas são tão cruciais quanto bons conhecimentos técnicos.

## Equipe

| <img src="https://avatars.githubusercontent.com/u/80992456?v=4&s=70" alt="Esdras Albino" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/125303577?v=4&s=70" alt="Maria Fernanda Amorim" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/116684279?v=4&s=70" alt="Matheus Borges" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/127243520?v=4&s=70" alt="Tulio Oliveira" width="70" height="70"> | <img src="https://avatars.githubusercontent.com/u/52381662?v=4&s=70" alt="Welton Felix" width="70" height="70"> |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| [Esdras Albino](mailto:ehas@cin.ufpe.br)                                                                         | [Maria Fernanda Amorim](mailto:mffa@cin.ufpe.br)                                                                          | [Matheus Borges](mailto:mbf3@cin.ufpe.br)                                                                          | [Tulio Araujo](mailto:toa@cin.ufpe.br)                                                                             | [Welton Felix](mailto:wplf@cin.ufpe.br)                                                                         |

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---

Projeto desenvolvido para a disciplina Introdução à Programação ([IF669](https://cin.ufpe.br/~if669)) do curso de Ciência da Computação do CIn - UFPE ![cin-logo](https://portal.cin.ufpe.br/wp-content/uploads/2020/06/cropped-iconecin-32x32.png).
