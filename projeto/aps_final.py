import string
import random

caracter = ' ' + string.punctuation + string.digits + string.ascii_letters + 'çáàâãéèêíìîóòôõúùûÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛ'

caracter = list(caracter)
chave = caracter.copy()
random.shuffle(chave)


def criptografia(mensagem_original):
    texto_criptografado = ' '

    for letras in mensagem_original:
        indice = caracter.index(letras)
        texto_criptografado += chave[indice]
        texto_criptografado += random.choice(caracter)

    return texto_criptografado


def descriptografia(texto_criptografado):
    mensagem_original = ' '

    for i in range(0, len(texto_criptografado), 2):
        letra_criptografada = texto_criptografado[i]
        indice = chave.index(letra_criptografada)
        mensagem_original += caracter[indice]

    return mensagem_original


def main():
    mensagem_original = input('Digite uma mensagem para ser criptografada: ')
    mensagem_criptografada = criptografia(mensagem_original)

    print(f'\nA mensagem original é: {mensagem_original}')
    print(f'A mensagem criptografada é: {mensagem_criptografada}')

    mensagem_criptografada = input('\nDigite a mensagem criptografada para ser descriptografada: ')
    mensagem_descriptografada = descriptografia(mensagem_criptografada)

    print(f'A mensagem descriptografada é: {mensagem_descriptografada}')


main()