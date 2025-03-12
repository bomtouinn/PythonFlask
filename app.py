from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur ma page d'accueil !"

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # Récupérer la sélection de l'utilisateur
        destination = request.form.get('destination')
        # Création d'une carte centrée sur Calais
        m = folium.Map(location=[50.95,1.88], zoom_start=13)
        # Ajouter un marqueur pour Calais
        folium.Marker([50.95,1.88], popup='ULCO Calais').add_to(m)
        # Ajouter des marqueurs et un chemin en fonction de la sélection
        if destination == 'gareCalaisVille':
            folium.Marker([50.955, 1.855], popup='Gare de Calais Ville').add_to(m)
            folium.PolyLine([(50.95,1.88), (50.955, 1.855)], color="blue", dash_array='5').add_to(m)
        elif destination == 'gareCalaisFrethun':
            folium.Marker([50.93, 1.85], popup='Gare de Calais Frethun').add_to(m)
            folium.PolyLine([(50.95,1.88), (50.93, 1.85)], color="green", dash_array='5').add_to(m)
        # Sauvegarder la carte dans le dossier static
        m.save('static/carte.html')
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)