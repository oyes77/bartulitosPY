import os
import discord
from discord.ext import commands
import json
import colorsys
import time
from PIL import Image, ImageDraw, ImageFont
from json import loads
from discord import Embed, app_commands
from discord.ext.commands import has_permissions, MissingPermissions, is_owner
import random
import asyncio
import platform
import requests
import keep_alive
from itertools import cycle
# -------------INICIO DEL BOT-----------------------------------------------------------------------------------
status = cycle(["Feliz 2023!", "Soy Bartolo!"])

                                 

client = commands.Bot(command_prefix=commands.when_mentioned_or("B!", "b!"), case_insensitive=True, intents = discord.Intents.all())
# client.remove_command("send_embed")
async def on_ready():
  
  print("LISTO PAPÁAAAAA")
  try:
    synced = await client.tree.sync()
    print(f"SINCRONISAOS {len(synced)} COMANDOS PAPÁAAAA")
  except exception as t:
    print(t)
  
  @tasks.loop(seconds=10)
  async def change_status():
    await change_status.start()
    await bot.change_presence(activity=discord.Game(next(status)))




# IMAGE LISTS ----------------------------------------------------------------------------------------
  
image_compositions = ['en primer plano', 'en segundo plano', 'de cerca', 'de lejos', 'desde arriba', 'desde abajo', 'a través de una ventana', 'a través de un espejo', 'a través de una ventana rota', 'a través de una pared', 'a través de un túnel', 'a través de una puerta', 'a través de una reja', 'a través de un agujero', 'a través de una malla', 'a través de una cortina', 'en un ángulo', 'en diagonal', 'en línea recta', 'en forma de espiral', 'en forma de onda', 'en forma de curva', 'en forma de círculo', 'en forma de estrella', 'en forma de cuadro', 'en forma de triángulo', 'en forma de rombo', 'en forma de hexágono', 'en forma de octágono', 'en forma de cónica', 'en forma de cono', 'en forma de esfera', 'en forma de cilindro', 'en forma de cubo', 'en forma de prisma', 'en forma de pirámide']
art_styles = ['realista', 'surrealista', 'impresionista', 'expresionista', 'pop art', 'arte abstracto', 'arte conceptual', 'arte digital', 'arte urbano', 'arte contemporáneo', 'arte folclórico', 'arte medieval', 'arte renacentista', 'arte romántica', 'arte primitiva', 'arte india', 'arte china', 'arte']
aesthetics = ['feliz', 'triste', 'dramático', 'excitante', 'relajado', 'emocionante', 'intenso', 'dulce', 'amargo', 'cómico', 'romántico', 'sombrío', 'poderoso', 'misterioso', 'sutil', 'fantástico', 'apasionado', 'plácido', 'vibrante', 'dramático', 'sensual', 'sutil', 'siniestro', 'optimista', 'deprimente', 'tensión', 'hermoso', 'sombrío', 'lujoso', 'elegante', 'exótico', 'turbio', 'sutil', 'clásico', 'exótico', 'provocativo', 'sutil', 'maravilloso', 'mágico', 'inquietante']
time_spans = ['de día', 'de noche', 'al amanecer', 'al atardecer', 'en la madrugada', 'en el mediodía', 'en el crepúsculo', 'en la puesta del sol', 'en la oscuridad', 'en el alba', 'en el ocaso', 'en el albor', 'en una mañana fresca', 'en una tarde soleada', 'en una noche de luna llena', 'en una mañana nublada', 'en una tarde lluviosa', 'en una noche despejada', 'en una mañana neblinosa', 'en una tarde ventosa', 'en una noche calurosa', 'en una mañana fría', 'en una tarde cálida', 'en una noche helada', 'en una mañana temprano', 'en una tarde tardía', 'en una noche tardía', 'en una mañana temprana', 'en una tarde temprana', 'en una noche temprana', 'en una mañana de verano', 'en una tarde de verano', 'en una noche de verano', 'en una mañana de otoño', 'en una tarde de otoño', 'en una noche de otoño', 'en una mañana de invierno', 'en una tarde de invierno', 'en una noche de invierno', 'en una mañana de primavera', 'en una tarde de primavera', 'en una noche de primavera']
landscapes = ['ciudad futurista', 'desierto de arena', 'estación espacial', 'paisaje lunar', 'planeta desconocido', 'rascacielos de cristal', 'urbanización', 'playa de arena', 'bosque de hojas gigantes', 'desierto', 'tundra', 'selva', 'pradera', 'mar', 'montañas', 'ciudad', 'paisaje urbano', 'avenida', 'parque', 'calle', 'callejón', 'plaza', 'estacionamiento', 'oceano', 'isla tropical', 'volcán', 'geyser', 'cataratas', 'lago', 'río', 'arroyo', 'pantano', 'manglar', 'marañón', 'delta', 'canal', 'estuario', 'playa rocosa', 'playa de guijarros', 'playa de piedras', 'playa de conchas', 'playa de arena', 'ciudad futurista con rascacielos de cristal y drones voladores', 'desierto de arena con dunas y oasis escondidos', 'estación espacial con naves y astronautas flotando', 'paisaje lunar con cráteres y rocas volcánicas', 'planeta desconocido con extrañas criaturas y flora', 'urbanización con edificios de viviendas y parques', 'playa de arena con palmeras y aguas cristalinas', 'desierto con cactus y oasis escondidos', 'tundra con hielo y nieve interminable', 'selva con árboles gigantes y animales exóticos', 'pradera con flores y hierbas aromáticas', 'mar con olas y mares abiertos', 'montañas con cumbres nevadas y valles verdes']
  


def generate_color_palette(num_colors):
  palette = []
  for i in range(num_colors):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    palette.append(color)
  return palette

@client.tree.command(name= "bartolo_que_dibujo", description= "La mente brillante (y babosa) de Bartolo te da ideas sobre qué dibujar!")
async def bqd(interaction: discord.Interaction):
  num_colors = random.randint(4, 6)
  color_palette = generate_color_palette(num_colors)
  image = Image.new("RGBA", (1020, 400), (255, 255, 255, 0))
  draw = ImageDraw.Draw(image)
  x, y = 0, 0
  width = (1000 - (12 * (num_colors - 1))) // num_colors
  radius = 20 
  for color in color_palette:
    draw.rounded_rectangle((x, y, x+width, y+396), radius, fill=color)
    x += width + 14
    
#  generator msg
  image.save("color_palette.png")
  
  landscape = random.choice(landscapes)
  image_composition = random.choice(image_compositions)
  art_style = random.choice(art_styles)
  aestethics = random.choice(aesthetics)
  time_span = random.choice(time_spans)

# embed 
  embedBQD = discord.Embed (
    title = "**inspírate de lo siguiente para dibujar!**",
    description = "Usa esta información como punto de partida para tu obra de arte y recuerda añadir tu propio toque creativo! mi misión ayudarte a tener ideas e inspiración, así que puedes usar esto de la manera que más te convenga <:Nixxlov:859453695464833034>",
    color = 0xff42e6)
  embedBQD.set_author(name=f"bartolo te ha contestado, {interaction.user.name}:")
  embedBQD.add_field(name="ubicado en...", value=f'{landscape} con un ambiente {aestethics} <:NoProblema:937723133006331965>', inline=True)
  embedBQD.add_field(name="usando una composición...", value=(image_composition + " " + time_span), inline=True)
  embedBQD.add_field(name="en un estilo...", value=f"{art_style} <:ummm:1042436738947227689>" , inline=True)
  embedBQD.add_field(name="con colores...", value=f'prueba usar estos colores en tu dibujo! <a:star:1044026309799579728>', inline=False)
  embedBQD.set_thumbnail(url= interaction.guild.icon.url)
  embedBQD.set_image(url='attachment://color_palette.png')
  await interaction.response.send_message(file=discord.File('color_palette.png'), embed = embedBQD)
  os.remove("color_palette.png")



  
# -----------------Create a dictionary that maps the names of the JSON files to their data--------------------
json_data = {
    "ownerstest.json": {"name": "File 1", "data": {}},
    "reglas1.json": {"name": "File 2", "data": {}},
    "reglas2.json": {"name": "File 3", "data": {}},
}

# Load the data from each JSON file into the dictionary
for file_name, file_data in json_data.items():
    with open(file_name, "r") as f:
        file_data["data"] = json.load(f)


@client.command()
async def embed(ctx, file_name: str, aliases=["send","emb"]):
  await ctx.message.delete()
  await asyncio.sleep(1)
  file_name = file_name + ".json"
# Load the JSON file
  with open(file_name, 'r') as file:
    if file_name not in json_data:
        await ctx.send("Archivo inválido")
        return

# Extract the necessary data from the JSON file
  data = json_data[file_name]["data"]
  embeds = data['embeds']

  # Iterate through each embed in the list
  for embed_data in embeds:
        # Extract the necessary data for the embed
        fields = embed_data.get('fields', [])
        title = embed_data.get('title', '')
        description = embed_data.get('description', '')
        color = embed_data.get('color', 0)


        # Create the embed using the extracted data
        embed = Embed(title=title, description=description, color=color)

        # Add the fields to the embed
        for field in fields:
            name = field['name']
            value = field['value']
            inline = field['inline']
            embed.add_field(name=name, value=value, inline=inline)

        # Check if there is an image in the embed data
        if 'image' in embed_data:
            image_url = embed_data['image']['url']
            embed.set_image(url=image_url)

        # Check if there is a footer in the embed data
        if 'footer' in embed_data:
            footer_text = embed_data['footer']['text']
            embed.set_footer(text=footer_text)

        # Send the embed to the channel where the command was used
        await ctx.send(embed=embed)
        
        

#------------------------------------------------------------------------------------------

@client.command()
async def rs(ctx, title: str, description: str, field_value_1: str, field_value_2: str):
  await ctx.message.delete()
  embed=discord.Embed(title=title, description=description, color=0xd400e8)
  embed.add_field(name="Fecha de participación: ", value=field_value_1, inline=True)
  embed.add_field(name="Fecha Límite para subir el dibujo: ", value=field_value_2, inline=True)
  embed.set_footer(text=f"reto creado por {ctx.message.author.name}")
  embed.set_author(name="Nuevo Reto Semanal!", icon_url="https://media.discordapp.net/attachments/887422706411257856/1031333789642805318/info-2872331-2389489.png")
  message = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ @everyone"
  await ctx.send(message, embed=embed)

  
# --------------------------------------------------------------------------------

@client.command()
async def paleta(ctx):
    
    response = requests.get(f"https://lospec.com/palette-list/json?count=1")
    if response.status_code != 200:
        await ctx.send("Hubo un error al obtener la paleta de colores. Por favor, inténtalo de nuevo más tarde.")
        return
    
    data = response.json()
    if data.get("error"):
        await ctx.send("No se encontró ninguna paleta con esa cantidad de colores. Por favor, elige una cantidad diferente.")
        return
    
    palette = data[0]
    color_palette = palette["colors"]
    palette_name = palette["name"]
    palette_creator = palette["author"]

  
    image = Image.new("RGBA", (1020, 400), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    x, y = 0, 0
    width = (1000 - (12 * (num_colors - 1))) // num_colors
    radius = 20 
    for color in color_palette:
        draw.rounded_rectangle((x, y, x+width, y+396), radius, fill=color)
        x += width + 14
        
    image.save("LOSPEC_palette.png")

    # Create an embed with the palette data
    embed = discord.Embed(title=palette_name, description=f"La paleta de colores llamada {palette_name} fue creada por {palette_creator} y tiene {num_colors} colores diferentes. Cada uno de estos colores ha sido cuidadosamente seleccionado y combinado para crear una paleta única y atractiva. ¡Hazle honor a esta paleta en tu próximo dibujo!", color=0xff42e6)
    embed.add_field(name="Creador de la paleta:", value=palette_creator, inline=False)
    embed.set_image(url="attachment://LOSPEC_palette.png")
    with open("LOSPEC_palette.png", "rb") as f:
        await ctx.send(file=discord.File(f, filename="LOSPEC_palette.png"), embed=embed)
    os.remove("LOSPEC_palette.png")





    
keep_alive.keep_alive()  
try:
  client.run(os.getenv("TOKEN"))
except discord.errors.HTTException:
  print("\nBLOQUEADO PUTO!\n\nReiniciando XD")
  os.system("kill 1")
  os.system("python restart.py")