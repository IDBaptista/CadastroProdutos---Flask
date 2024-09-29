from flask import Flask, render_template, request, redirect
 
app = Flask (__name__)
 
@app.route("/")
def index ():
    return render_template ("index.html")
 
@app.route("/calcular_notas", methods=[ 'GET', 'POST'])
def calcular_notas():
     nome_aluno = request.form ["nome_aluno"]
     nota_um = float (request.form ["nota_um"])
     nota_dois = float ( request.form ["nota_dois"])
     nota_tres = float (request.form ["nota_tres"])
 
     soma = nota_um + nota_dois + nota_tres
     media = soma/3
 
     caminho_arquivo = 'models/notas.txt'
 
     with open(caminho_arquivo, 'a' ) as arquivo:
        arquivo.write(f"{nome_aluno};{nota_um};{nota_dois};{nota_tres};{media}\n")
   
     return render_template ("index.html")

@app.route("/consulta")
def consulta():
    notas = []
    caminho_arquivo = 'models/notas.txt'
 
    with open(caminho_arquivo, 'r')as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            if len (item) == 5:
                notas.append({
                'nome_aluno': item [0],
                'nota_um': item [1],
                'nota_dois': item [2],
                'nota_tres': item [3],
                'media': item [4]
                 
         })
            
    return render_template("vernotas.html" , notas=notas)

 
app.run(host='127.0.0.1', port=80, debug=True)