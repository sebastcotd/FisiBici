from flask import jsonify, session
from models.user import User
from utils.utils import json_message

class GetCurrentUser:

    def __call__(self):

        if "user_id" in session:
            current_user_id = session['user_id']

            if current_user_id is not None:
                user_obj = User.objects(
                    id=current_user_id
                ).first()

                if user_obj is not None:
                    return jsonify({"user": user_obj.json()})

                return json_message("El usuario que habia iniciado sesion no ha sido encontrado")

            return json_message("Ningun usuario ha iniciado sesion")

        return json_message("Ningun usuario ha iniciado sesion")