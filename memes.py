import requests

# Clase personalizada para memes
class Meme:
    
    def __init__(self, id, name):
        self.name = name
        self.id = id

# Definir cliente para obtener y crear memes
class MemesClient:
    
    # Método de inicialización (para obtener las credenciales del usuario)
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    # Obtener una lista de todos los memes disponibles
    def obtener_memes(self):
        response = requests.get('https://api.imgflip.com/get_memes')
        
        # Asegurarse de que se obtuvieron los memes
        if response.status_code == 200:
            data = response.json()['data']
            memes = data['memes']
            
            meme_objects = []
            
            for meme_data in memes:
                # Obtener los datos de cada meme
                meme_id = meme_data['id']
                meme_name = meme_data['name']
                
                # Inicializar y agregar meme a una lista
                meme = Meme(meme_id, meme_name)
                meme_objects.append(meme)
        
            return meme_objects
    
    # Definir función para crear un nuevo meme
    def generar_meme(this, meme_id, text):
        data = {
            'template_id': meme_id,
            'username': this.username,
            'password': this.password,
            'text1': text
        }
        
        response = requests.post('https://api.imgflip.com/caption_image', data)
        
        # Asegurarse de que la petición tuvo éxito
        if response.status_code == 200:
            try:
                return response.json()['data']['url']
            except:
                raise ValueError('Las credenciales o el id del meme no son correctos.')
        else:
            # Devolver un error si los datos no son válidos
            raise ValueError('Ocurrió un error al crear el meme.')