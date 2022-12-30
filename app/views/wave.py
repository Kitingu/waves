from app.models.wave import Wave as WaveModel
from app.utils.validator import WaveSchema
from flask import request, jsonify, Blueprint
from marshmallow import ValidationError
from flask_jwt_extended import get_jwt_identity, jwt_required
from datetime import date
wave = Blueprint('wave', __name__)


@wave.route('/wave', methods=['post'])
@jwt_required()
def create_wave():
    new_wave = request.get_json()
    try:
        WaveSchema().load(new_wave)
        title = new_wave['title']
        description = new_wave['description']
        user = get_jwt_identity()
        category = new_wave['category']
        wavy = WaveModel(title, description, category,user_id=user, date_created=date.today().strftime("%d/%m/%Y"))
        wavy.create_wave()
        return jsonify({
            'message': 'wave created successfully'
        }), 201

    except ValidationError as err:
        return jsonify({"Message": err.messages}), 400


@wave.route("/wave", methods=['GET'])
@jwt_required()
def get_waves():
    waves = WaveModel.get_waves()
    serialized_waves = WaveSchema(many=True,exclude=["user"]).dump(waves)
    return jsonify(
        {"message": serialized_waves}
    )
