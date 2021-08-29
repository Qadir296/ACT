from flask import Blueprint, render_template, request, flash, jsonify, redirect, Flask
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from Server import api
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        latitude = request.form.get('Latitude')
        longitude = request.form.get('Longitude')

        if len(latitude and  longitude) < 1:
            flash('Wrong Coordinates!', category='error')
        else:
            new_note = Note(data=longitude, user_id=current_user.id)
            new_note = Note(data=latitude, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Query Success!', category='success')
            return redirect("http://10.188.35.12:443/ControlService/location")
           

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})



