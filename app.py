from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados temporários (pode usar banco de dados depois)
personagem = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ficha', methods=['GET', 'POST'])
def ficha():
    global personagem
    if request.method == 'POST':
        # Captura os dados do formulário
        personagem = {
            "nome": request.form['nome'],
            "idade": request.form['idade'],
            "classe": request.form['classe'],
            "atributos": {
                "forca": request.form['forca'],
                "agilidade": request.form['agilidade'],
                "inteligencia": request.form['inteligencia'],
                "vontade": request.form['vontade'],
                "percepcao": request.form['percepcao']
            },
            "vida": 40 + int(request.form['vida']),
            "sanidade": 40 + int(request.form['sanidade']),
            "equipamento": request.form['equipamento']
        }
        return redirect(url_for('mostrar_ficha'))
    return render_template('ficha.html')

@app.route('/mostrar_ficha')
def mostrar_ficha():
    return render_template('mostrar_ficha.html', personagem=personagem)

if __name__ == '__main__':
    app.run(debug=True)