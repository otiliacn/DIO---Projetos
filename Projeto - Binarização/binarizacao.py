import matplotlib.pyplot as plt 
from PIL import Image

# função para converter imagem colorida para níveis de cinza
def conversao_para_cinza(imagem):
    width, height = imagem.size
    # cria uma nova imagem em escala de cinza
    imagem_cinza = Image.new('L', (width, height))
    for x in range(width):
        for y in range(height):
            # obtém os valores RGB do pixel
            r, g, b = imagem.getpixel((x, y))
            # conversao para cinza: média ponderada dos canais RGB
            tons_cinza = int(0.2989 * r + 0.587 * g + 0.114 * b) 
            # define o pixel na nova imagem
            imagem_cinza.putpixel((x, y), tons_cinza)
    return imagem_cinza

# função para converter imagem em níveis de cinza para binário
def conversao_para_binario(imagem_cinza, threshold = 128):
    width, height = imagem_cinza.size
    # cria uma nova imagem binária
    imagem_binaria = Image.new('1', (width, height))
    for x in range(width):
        for y in range(height):
            # obtém o valor de cinza do pixel
            cinza = imagem_cinza.getpixel((x, y))
            # aplica o limiar para determinar se o pixel será branco ou preto
            valor_binario = 255 if cinza >= threshold else 0
            imagem_binaria.putpixel((x, y), valor_binario)
    return imagem_binaria

# carregar a imagem colorida (original)
caminho = 'lena.jpg'
imagem_original = Image.open(caminho).convert('RGB')
# primeria conversao para tons de cinza
imagem_cinza = conversao_para_cinza(imagem_original)
# segunda conversão para binário
imagem_binaria = conversao_para_binario(imagem_cinza)

# apresentar as imagems geradas
fig = plt.figure(figsize = (15,5))
fig.canvas.manager.set_window_title("Desafio: Binarização")
# imagem original
plt.subplot(1, 3, 1)
plt.title("Imagem Colorida")
plt.imshow(imagem_original)
plt.axis("off")

# Imagem em níveis de cinza
plt.subplot(1, 3, 2)
plt.title("Imagem em Tons de Cinza")
plt.imshow(imagem_cinza, cmap = "gray")
plt.axis("off")

# Imagem binária
plt.subplot(1, 3, 3)
plt.title("Imagem Binária")
plt.imshow(imagem_binaria, cmap = "gray")
plt.axis("off")

# Mostrar o resultado
plt.tight_layout()
plt.show()

