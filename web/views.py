from datetime import datetime
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .model import Agenda, Examen, Note
from . import db
import json
import mysql.connector

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def notas():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('La nota es muy corta', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Nota añadida!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/examenes', methods=['GET', 'POST'])
@login_required
def examenes():
    if request.method == 'POST':
        examen = request.form.get('examen')

        if len(examen) < 1:
            flash('La nota de examen es muy corta', category='error')
        else:
            new_examen = Examen(data=examen, user_id=current_user.id)
            db.session.add(new_examen)
            db.session.commit()
            flash('Examen añadido!', category='success')

    return render_template("examenes.html", user=current_user)

@views.route('/agenda', methods=['GET', 'POST'])
@login_required
def agenda():
    if request.method == 'POST':
        entrada = request.form.get('entrada')

        if len(entrada) < 1:
            flash('La entrada de agenda es muy corta', category='error')
        else:
            new_entrada = Agenda(data=entrada, user_id=current_user.id)
            db.session.add(new_entrada)
            db.session.commit()
            flash('Entrada añadida', category='success')

    return render_template("agenda.html", user=current_user)

@views.route('/estadisticas', methods=['GET'])
@login_required
def estadisticas():
    conn = mysql.connector.connect(user='pr_si2user', password="fascioli.2", host="195.235.211.197", database="prsi_2")
    crs = conn.cursor()
    sql_query = "SELECT * FROM AbandonoTempranoEspañaUE"
    crs.execute(sql_query)
    lista = crs.fetchall()

    sql_query2 = "SELECT * FROM AbandonoTempranoDeLaEducaciónFormacion"
    crs.execute(sql_query2)
    lista2 = crs.fetchall()

    sql_query3 = "SELECT * FROM NivelDeFormacionDeLaPoblacionAdultaDe25A64Años"
    crs.execute(sql_query3)
    lista3 = crs.fetchall()

    sql_query4 = "SELECT * FROM NivelDeFormacionDeLaPoblacionAdultaDe25A64AñosUE"
    crs.execute(sql_query4)
    lista4 = crs.fetchall()

    sql_query5 = "SELECT * FROM PoblacionDe30A34AñosConEducaciónSuperiorEnLaUE"
    crs.execute(sql_query5)
    lista5 = crs.fetchall()

    sql_query6 = "SELECT * FROM PJovenConSegundaEducacionSecundariaUE"
    crs.execute(sql_query6)
    lista6 = crs.fetchall()

    sql_query7 = "SELECT * FROM TasasNetasDeEscolarizaciónDe16a24Años"
    crs.execute(sql_query7)
    lista7 = crs.fetchall()

    sql_query8 = "SELECT * FROM TasasDeEscolarizacionPorEdadTotalEnseñanzas"
    crs.execute(sql_query8)
    lista8 = crs.fetchall()
    return render_template("estadisticas.html", user= current_user, lista= lista, lista2=lista2,lista3=lista3,lista4=lista4,lista5=lista5,lista6=lista6,lista7=lista7,lista8=lista8)


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

@views.route('/delete-examen', methods=['POST'])
def delete_examen():
    examen = json.loads(request.data)
    examenId = examen['examenId']
    examen = Examen.query.get(examenId)
    if examen:
        if examen.user_id == current_user.id:
            db.session.delete(examen)
            db.session.commit()

    return jsonify({})

@views.route('/delete-agenda', methods=['POST'])
def delete_agenda():
    agenda = json.loads(request.data)
    agendaId = agenda['agendaId']
    agenda = Agenda.query.get(agendaId)
    if agenda:
        if agenda.user_id == current_user.id:
            db.session.delete(agenda)
            db.session.commit()

    return jsonify({})

