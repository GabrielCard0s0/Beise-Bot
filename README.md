# Beise-Bot
Um bot para Discord que permite tocar músicas diretamente do YouTube em canais de voz, com funcionalidades para gerenciar a reprodução e limpar arquivos temporários.


# Discord Music Bot

Este é um bot para Discord que permite aos usuários tocar músicas em um canal de voz diretamente do YouTube. O bot utiliza a biblioteca `discord.py` para interação com a API do Discord e `yt-dlp` para extração de áudio dos vídeos.

## Funcionalidades

- **Entrar em Canal de Voz**: O bot pode se conectar ao canal de voz em que o usuário está.
- **Tocar Música**: Os usuários podem tocar músicas usando URLs do YouTube.
- **Parar Música**: É possível interromper a música que está sendo tocada.
- **Sair do Canal de Voz**: O bot pode desconectar-se do canal de voz a qualquer momento.
- **Limpeza de Arquivos**: Após tocar uma música, o bot remove os arquivos MP3 gerados para manter a pasta limpa.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas: `discord.py`, `yt-dlp`, `ffmpeg`

## Como Usar

1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Adicione seu token do bot na linha correspondente do código.
4. Execute o bot com `python main.py`.
5. Use os comandos `!join`, `!play <URL>`, `!stop`, e `!leave` para interagir com o bot.

## Comandos

- `!join`: Faz o bot entrar no canal de voz em que você está.
- `!play <URL>`: Toca a música do URL especificado.
- `!stop`: Para a música que está tocando.
- `!leave`: Faz o bot sair do canal de voz.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
