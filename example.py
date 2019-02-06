from memes import MemesClient
import webbrowser

def run():
    print('Obteniendo memes...\n')

    memes_client = MemesClient('{ Tu nombre de usuario de Imgflip }', '{ Tu contraseña de Imgflip }')
    memes = memes_client.obtener_memes()

    for meme in memes:
        print('{}.- {}'.format(meme.id, meme.name))

    meme_id = input('\nIngresa el id del meme que quieres generar => ')
    meme_text = input('Escribe el texto que le quieres poner => ')

    meme_url = memes_client.generar_meme(meme_id, meme_text)
    print('\nGenerando meme...\n')

    webbrowser.open(meme_url)

run()
