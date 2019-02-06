# Generador de memes

### Uso
Coloca el archivo memes.py en el mismo directorio en el que está tu archivo principal e importalo. Recuerda instalar la dependencia 'requests' en Thonny.

```python
  from memes import MemesClient
```

Para generar memes inicializa un objeto MemesClient. Para esto debes usar las credenciales de tu cuenta de imgflip.

```python
  memes_client = MemesClient('{ Tu nombre de usuario de Imgflip }', '{ Tu contraseña de Imgflip }')
```

### Obtener la lista de memes

Usa la función 'obtener_memes' de memes_client para obtener una lista de objetos Meme. El objeto Meme contiene su id y su nombre.

```python
  memes = memes_client.obtener_memes()
```

### Crear un meme

Usa la función 'generar_meme' de memes_client para generar una imagen y obtener su url.

```python
  meme_url = memes_client.generar_meme('{ Ingresa el id de tu meme aquí }', '{ Escribe el texto que le quieres poner a tu meme }')
  # Ahora la variable meme_url contiene la url de tu meme.
```
