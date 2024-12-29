# Extrae archivos, videos, fotos, desde un chat (Chat privado, bots o Grupos donde puedas escribir) que no puedas reenviar las cosas

## Primero que todo ejecutar ```pip install -r requirements.txt```, para luego ejecutar el archivo sessionCreator.py, el cual crea la sesion con su numero de telefono (debe introducirlo con su prefijo y sin espacios, ejemplo para Cuba: 5355555555), su API HASH (obtener de my.telegram.org) y su API ID (obtener de my.telegram.org); ya que lo que se usara sera un userbot para automatizar la accion por usted

<p>Al ejecutar este archivo se te pedira un codigo que te enviara telegram por mensaje privado, solo un codigo de 5 digitos, lo ingresas y se te crea automaticamente la sesion <strong>PD: En caso de tener la verificacion en 2 pasos se te pedira igual, solo pones la password y todo listo</strong></p>

## Una vez tengas la sesion creada:

<p>Solo ejecutar el main.py en un host de internet que tengas, o si tienes buen internet, lo ejecutas de forma local y te queda guardado en la PC</p>

## FAQ

<p>P:/Que hace el bot?</p>
<p>R:/Paso por paso:</p>

    * Usas el comando .dl para descargar, respondiendo al archivo que quieres descargar
    * El bot enviara a tus mensajes guardados un mensaje una vez haya terminado de descargar el archivo, esto significa que el archivo comenzara a subirse
    * Una vez subido el archivo se enviara a sus mensajes guardados con un thumb de Jude Bellingham de EAFC 25 (esto es totalmente cambiable, mientras ponga una imagen que se llame igual al archivo original ("thumb.jpg")), o simplemente puede verlo en la carpeta downloads que ha creado el userbot para usted en su pc

<p>P:/Que riesgos de seguridad estoy corriendo al ejecutar un script que no conozco su procedencia?</p>
<p>R:/Pues con este, absolutamente ninguno, todo corre sobre Kurigram (antes Pyrogram) y Kurigram basicamente lo que hace es hacer mas facil la comunicacion entre el desarrollador y el wrapper oficial de Telegram que es totalmente codigo abierto</p>

<p>P:/Donde se guardan los archivos/fotos/videos?</p>
<p>R:/Estos se guardan en la carpeta downloads que se crea en este mismo directorio, o si lo quiere todo online, se le envia a sus mensajes privados</p>

## ToDo

    * Hacer que los archivos se suban con su nombre
    * Permitir la descarga de canales y grupos que no dejen escribir, sacandolos por su link