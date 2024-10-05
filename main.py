import discord, yt_dlp, os
from discord.ext import commands

# Ativando os intents necessários
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot está pronto para ser utilizado!')
    # Enviar uma mensagem para um canal específico
    channel = bot.get_channel(0)  # Substitua 0 pelo ID real do canal
    if channel:
        await channel.send('Bot está pronto para ser utilizado!')


# Configurações do YoutubeDL
ytdl_format_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'restrictfilenames': True,
    'noplaylist': True,
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f'Entrei no canal de voz: {channel.name}')
    else:
        await ctx.send('Você não está em um canal de voz!')

@bot.command()
async def play(ctx, url):
    if ctx.voice_client is None:
        await ctx.send('Você precisa estar em um canal de voz primeiro!')
        return

    if ctx.voice_client.channel != ctx.author.voice.channel:
        await ctx.send('Você precisa estar no mesmo canal de voz que eu para tocar música!')
        return

    async with ctx.typing():
        try:
            info = ytdl.extract_info(url, download=True)
            audio_url = info['url']  # URL do stream de áudio
            
            # Tocar a música
            ctx.voice_client.play(discord.FFmpegPCMAudio(audio_url, **ffmpeg_options),
                                   after=lambda e: remove_mp3_files())

            await ctx.send(f'Tocando agora: {info["title"]}')
        except Exception as e:
            await ctx.send(f'Ocorreu um erro ao tentar tocar a música: {str(e)}')

@bot.command()
async def stop(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send('Música parada.')
    else:
        await ctx.send('Não estou tocando nada.')

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send('Saí do canal de voz.')
    else:
        await ctx.send('Não estou em um canal de voz.')

def remove_mp3_files():
    # Remove todos os arquivos .mp3 na pasta do script
    for filename in os.listdir('.'):
        if filename.endswith('.mp3'):
            os.remove(filename)
            print(f'Arquivo removido: {filename}')

bot.run('TOKEN_DO_BOT')#Crie seu bot em https://discord.com/developers e substitua  o TOKEN_DO_BOT pelo token real do seu bot.
