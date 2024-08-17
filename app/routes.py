from flask import render_template, request, flash, redirect, url_for, current_app as app
import msal
import requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/herencia', methods=['GET', 'POST'])
def herencia():
    if request.method == 'POST':
        # Recoge la información del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']

        # Construir el mensaje de correo
        access_token = get_access_token()
        email_data = {
            "message": {
                "subject": f"Solicitud de Asesoramiento: {asunto}",
                "body": {
                    "contentType": "Text",
                    "content": f"""
                    Has recibido una nueva solicitud de asesoramiento:

                    Nombre Completo: {nombre}
                    Email: {email}
                    Teléfono: {telefono}

                    Asunto: {asunto}
                    Descripción del Problema:
                    {mensaje}

                    Este mensaje fue enviado desde el formulario de herencias en el sitio web.
                    """
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": "pedro.robles@estudiojuridicoprl.es"
                        }
                    }
                ]
            }
        }

        try:
            # Cambiar la URL a usar el user_id explícito en lugar de /me/sendMail
            response = requests.post(
                "https://graph.microsoft.com/v1.0/users/pedro.robles@estudiojuridicoprl.es/sendMail",  
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json"
                },
                json=email_data
            )
            response.raise_for_status()
            flash('Tu solicitud ha sido enviada con éxito. Nos pondremos en contacto contigo pronto.', 'success')
        except requests.exceptions.HTTPError as err:
            # Capturar y mostrar el error
            error_message = err.response.json().get("error", {}).get("message", str(err))
            flash(f'No se pudo enviar el correo electrónico. Error: {error_message}', 'danger')

        return render_template('herencia.html')

    return render_template('herencia.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Recoge la información del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']

        # Construir el mensaje de correo
        access_token = get_access_token()  # Asegúrate de que tienes una función para obtener el token
        email_data = {
            "message": {
                "subject": f"Nuevo Mensaje de Contacto: {asunto}",
                "body": {
                    "contentType": "Text",
                    "content": f"""
                    Has recibido un nuevo mensaje de contacto:

                    Nombre: {nombre}
                    Email: {email}

                    Asunto: {asunto}
                    Mensaje:
                    {mensaje}

                    Este mensaje fue enviado desde el formulario de contacto en el sitio web.
                    """
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": "pedro.robles@estudiojuridicoprl.es"
                        }
                    }
                ]
            }
        }

        try:
            # Enviar el correo usando Microsoft Graph API
            response = requests.post(
                "https://graph.microsoft.com/v1.0/users/pedro.robles@estudiojuridicoprl.es/sendMail",  
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json"
                },
                json=email_data
            )
            response.raise_for_status()
            flash('Tu mensaje ha sido enviado con éxito. Nos pondremos en contacto contigo pronto.', 'success')
        except requests.exceptions.HTTPError as err:
            # Capturar y mostrar el error
            error_message = err.response.json().get("error", {}).get("message", str(err))
            flash(f'No se pudo enviar el correo electrónico. Error: {error_message}', 'danger')

        return render_template('index.html')

    return render_template('index.html')


@app.route('/particiones', methods=['GET', 'POST'])
def particiones():
    if request.method == 'POST':
        # Recoge la información del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']

        # Construir el mensaje de correo
        access_token = get_access_token()
        email_data = {
            "message": {
                "subject": f"Solicitud de Asesoramiento: {asunto}",
                "body": {
                    "contentType": "Text",
                    "content": f"""
                    Has recibido una nueva solicitud de asesoramiento:

                    Nombre Completo: {nombre}
                    Email: {email}
                    Teléfono: {telefono}

                    Asunto: {asunto}
                    Descripción del Problema:
                    {mensaje}

                    Este mensaje fue enviado desde el formulario de particiones en el sitio web.
                    """
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": "pedro.robles@estudiojuridicoprl.es"
                        }
                    }
                ]
            }
        }

        try:
            # Cambiar la URL a usar el user_id explícito en lugar de /me/sendMail
            response = requests.post(
                "https://graph.microsoft.com/v1.0/users/pedro.robles@estudiojuridicoprl.es/sendMail",  
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json"
                },
                json=email_data
            )
            response.raise_for_status()
            flash('Tu solicitud ha sido enviada con éxito. Nos pondremos en contacto contigo pronto.', 'success')
        except requests.exceptions.HTTPError as err:
            # Capturar y mostrar el error
            error_message = err.response.json().get("error", {}).get("message", str(err))
            flash(f'No se pudo enviar el correo electrónico. Error: {error_message}', 'danger')

        return render_template('particiones.html')

    return render_template('particiones.html')

# Configurar MSAL
def get_msal_app():
    return msal.ConfidentialClientApplication(
        client_id=app.config['CLIENT_ID'],
        client_credential=app.config['CLIENT_SECRET'],
        authority=app.config['AUTHORITY']
    )

def get_access_token():
    app_msal = get_msal_app()
    result = app_msal.acquire_token_for_client(scopes=app.config['SCOPE'])
    if "access_token" in result:
        return result['access_token']
    else:
        raise Exception("No se pudo obtener un token de acceso")
