# TelegramBot_Messenger
Este código es un bot de Telegram escrito en Python que envía mensajes de buenos días y buenas noches a dos destinatarios. Se utiliza la biblioteca telegram para interactuar con la API de Telegram y la biblioteca requests para obtener mensajes de buenos días y buenas noches desde un sitio web.

El bot tiene dos funciones principales, send_morning_messages y send_night_messages, que envían mensajes de buenos días y buenas noches, respectivamente. Estas funciones extraen mensajes de un sitio web y eligen al azar un mensaje para enviar a cada destinatario.

Además, el código utiliza asyncio para manejar tareas asíncronas y enviar mensajes de forma simultánea a los destinatarios, mejorando la velocidad de envío. La función main se ejecuta periódicamente mediante el uso de la biblioteca azure.functions y verifica si es hora de enviar mensajes de buenos días o buenas noches.

En resumen, este código ofrece una solución fácil y eficiente para enviar mensajes diarios personalizados a destinatarios específicos a través de Telegram. ¡Mejore su relación con amigos y seres queridos enviándoles mensajes diarios de buenos días y buenas noches!
