from flask import Flask, render_template, request, redirect
 
app = Flask (__name__)
 
@app.route("/")
def index ():
    return render_template ("index.html")

@app.route("/calcular_imc", methods=[ 'GET', 'POST'])
def calcular_imc():
     nome = request.form ["nome"]
     peso = float (request.form ["peso"])
     altura = float ( request.form ["altura"])

     multiplicacao = altura**2
     imc = peso/multiplicacao
 
     caminho_arquivo = 'models/imc.txt'
 
     with open(caminho_arquivo, 'a' ) as arquivo:
        arquivo.write(f"{nome};{peso};{altura};{multiplicacao};{imc}\n")
   
     return render_template ("index.html")

@app.route("/consulta")
def consulta():
    imc = []
    caminho_arquivo = 'models/imc.txt'
 
    with open(caminho_arquivo, 'r')as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            if len (item) == 5:
                imc.append({
                'nome': item [0],
                'peso': item [1],
                'altura': item [2],
                'multiplicacao': item [3],
                'imc': item [4]
                 
         })
            
    return render_template("verimc.html" , imc=imc)
    

app.run(host='127.0.0.1', port=80, debug=True)