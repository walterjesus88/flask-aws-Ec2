from flask import Flask, render_template_string
import boto3

app = Flask(__name__)

# Configuración de boto3 para interactuar con S3
s3 = boto3.client('s3')

# Datos de tu bucket y archivo en S3
BUCKET_NAME = 'bucket2024-09-04'
IMAGE_KEY = 'mioso.jpg'

@app.route('/')
def home():
    # Generar un enlace temporal a la imagen en S3 (válido por un tiempo limitado)
    image_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': BUCKET_NAME, 'Key': IMAGE_KEY},
        ExpiresIn=3600  # El enlace será válido durante 1 hora (3600 segundos)
    )

    # Usamos HTML simple para mostrar la imagen
    return render_template_string('''
        <h1>Hola amigo</h1>
        <img src="{{ image_url }}" alt="Imagen de S3">
    ''', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
