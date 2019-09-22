from flask import Flask, render_template, request,   redirect, url_for, session
from werkzeug.utils import secure_filename

import mysql.connector as MS 
connection = MS.connect(user='root', password='root', host='127.0.0.1', buffered=True)
cursor = connection.cursor()
utiliser_bd = "USE BDprojet" 
cursor.execute(utiliser_bd)
app = Flask(__name__) 

app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/ajouter_classe', methods=["GET", "POST"])
def ajouter_classe():
    error = None

    if request.method == 'GET':
        return render_template('ajouterclasse.html')

    if request.method == 'POST':

        """Informations de la Classe"""

        id_classe = request.form['numero']
        Numeroclasse = request.form['numero']
        Nomclasse = request.form['nom']
        Nombre = request.form['nombre']

        #"""0n enregistre les informations de la classe dans la BD"""
        req_ajouter_classe = 'INSERT INTO Classe (IdClasse, Numeroclasse, Nomclasse, Nombre)VALUES(%s,%s,%s,%s)'
        cursor.execute (req_ajouter_classe, (id_classe, Numeroclasse, Nomclasse, Nombre))
        connection.commit()
        
    return render_template('index.html')

@app.route('/ajouter_eleve',methods=["GET", "POST"])
def ajouter_eleve():
    error = None

    if request.method == 'GET':
        return render_template('ajoutereleve.html')

    if request.method == 'POST':

        """Informations de l'éléve"""

        id_eleve = request.form['numero']
        Numeroeleve = request.form['numero']
        Nom = request.form['nom']
        Prenom = request.form['prenom']
        Classe = request.form['classe']

        #"""On enregistre les informations de l'éléve dans la BD"""
        req_ajouter_eleve = 'INSERT INTO Eleve (IdEleve, Numeroeleve, Nom, Prenom, Classe)VALUES(%s,%s,%s,%s,%s)'
        cursor.execute (req_ajouter_eleve, (id_eleve, Numeroeleve, Nom, Prenom, Classe))
        connection.commit()
    return render_template('index.html')

@app.route('/liste_classe', methods=['GET', 'POST'])
def liste_classe():
    if request.method == 'GET':

        requete_information_classe = 'SELECT C.Numeroclasse, C.Nomclasse, C.Nombre FROM Classe as C'
        cursor.execute(requete_information_classe)
        resultat_requete_information_classe = cursor.fetchall()
       
        print(resultat_requete_information_classe)
        return render_template('/listeclasse.html', resultat_requete_information_classe=resultat_requete_information_classe)

@app.route('/liste_eleve', methods=['GET', 'POST'])
def liste_eleve():
    if request.method == 'GET':

        requete_information_eleve = 'SELECT C.Numeroeleve, C.Nom, C.Prenom, C.Classe FROM Eleve as C'
        cursor.execute(requete_information_eleve)
        resultat_requete_information_eleve = cursor.fetchall()
       
        print(resultat_requete_information_eleve)
        return render_template('/listeleve.html', resultat_requete_information_eleve=resultat_requete_information_eleve)


@app.route('/modifier_classe', methods=['GET', 'POST'])
def modifier_classe():
    if request.method == 'GET':

        requete_information_classe = 'SELECT C.Numeroclasse, C.Nomclasse, C.Nombre FROM Classe as C'
        cursor.execute(requete_information_classe)
        resultat_requete_information_classe = cursor.fetchall()
        print(resultat_requete_information_classe)

        
    if request.method == 'POST':  

        Nom = request.form['nom']

        requette_avoir_id_classe = "SELECT IdClasse FROM Classe WHERE Nomclasse = '%s'"
        cursor.execute(requette_avoir_id_classe % Nom)

        id_classe = cursor.fetchone()

        requete_modifier_classe = 'UDATE Classe SET Numeroclasse=Numroclasse, Nomclasse=Nomclasse, Nombre=Nombre WHERE IdClasse=id_classe'
        cursor.execute(requete_modifier_classe)
        resultat_requete_modifier_classe = cursor.fetchall()
        print(resultat_requete_modifier_classe)

    return render_template('/modifierclasse.html', resultat_requete_information_classe=resultat_requete_information_classe)

@app.route('/supprimer_classe', methods=['GET', 'POST'])
def supprimer_classe():
    if request.method == 'GET':

        requete_information_classe = 'SELECT C.Numeroclasse, C.Nomclasse, C.Nombre FROM Classe as C'
        cursor.execute(requete_information_classe)
        resultat_requete_information_classe = cursor.fetchall()
        print(resultat_requete_information_classe)

    if request.method == 'POST':  
        Nom = request.form['nom']

        requette_avoir_id_eleve = "SELECT IdClasse FROM Eleve WHERE Nom = '%s' "
        cursor.execute(requette_avoir_id_eleve % Nom)

        id_eleve = cursor.fetchone()
        
        requete_supprimer_classe = 'DELETE FROM Classe WHERE IdEleve=id_eleve'
        cursor.execute(requete_supprimer_classe)
        resultat_requete_supprimer_classe = cursor.fetchall() 
        print(resultat_requete_supprimer_classe)

    return render_template('/supprimerclasse.html', resultat_requete_information_classe=resultat_requete_information_classe)

if __name__=='__main__':
        app.run(debug=True)