from flask import Flask, render_template, request

app = Flask(__name__)

# Página de login
@app.route("/", methods=['GET'])
def login():
  return render_template('login.html')

# Página com os dados do usuário (login, senha)
@app.route("/dados_usuario", methods=['POST'])
def dados_usuario():
  usuario = request.form.get('usuario')
  senha = request.form.get('senha')
  if not usuario:
    return render_template('erro.html', message='Usuario Vazio')
  if not senha:
    return render_template('erro.html', message='Senha Vazia')
  return render_template('dados_usuario.html',usuario=usuario,senha=senha)


# Colocar o site no ar
if __name__ == "__main__":
  app.run(debug=True)

