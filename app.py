from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'SENHA-MUITO-SECRETA'


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/exemplo_get')
def exemplo_get():
	"""
	Função que exemplifica como receber valores enviados pelo método GET no Flask
	"""
	usuario = request.args.get('usuario')
	senha = request.args.get('senha')
	if usuario and senha:  # condição que testa se usuario e senha NÃO são strings vazias
		# retornamos uma string simples com os dados recebidos
		return "Retorno da rota: usuario={0} e senha={1}".format(usuario, senha)
	else:
		# caso usuario ou senha não tenham sido enviados, carregamos o formulário novamente:
		return render_template("exemplo_get.html")


@app.route('/exemplo_post', methods=['GET', 'POST'])
def exemplo_post():
	"""
	Função que exemplifica como receber valores enviados pelo método POST no Flask.
	Note que essa rota precisa especificar de maneira explícita que ela aceita POST.

	Ela receberá requisições por GET para carregar o formulário, e o formulário por sua vez
	enviará os dados para a mesma rota, usando o verbo POST.
	"""
	usuario = request.form.get('usuario')
	senha = request.form.get('senha')
	if usuario and senha:  # condição que testa se usuario e senha NÃO são strings vazias
		# retornamos uma string simples com os dados recebidos
		return "Retorno da rota: usuario={0} e senha={1}".format(usuario, senha)
	else:
		# caso usuario ou senha não tenham sido enviados, carregamos o formulário novamente:
		return render_template("exemplo_post.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
	msg_erro = ''
	if request.method == 'POST':  # verifica se a requisição utiliza o método 'POST'
		usuario = request.form.get('usuario')
		senha = request.form.get('senha')
		if usuario == 'rafael' and senha == '1234':  # verifica as credenciais do usuário 'rafael'
			session['usuario'] = 'rafael'
			return redirect('/area_logada')
		elif usuario == 'maria' and senha == '4321':  # verifica as credenciais do usuário 'maria'
			session['usuario'] = 'maria'
			return redirect('/area_logada')
		else:
			msg_erro = 'Usuário e/ou senha inválidos'
	# Note que o return abaixo só será executado se nenhum outro retorn foi executado antes
	return render_template('login.html', erro=msg_erro)


@app.route('/area_logada')
def area_logada():
	if 'usuario' in session:  # checa se existe a chave 'usuario' no dicionário da sessão (condição para o usuário estar logado)
		nome_pessoa = ''
		media_pessoa = 0.0
		if session['usuario'] == 'rafael':
			nome_pessoa = 'Rafael Will'
			media_pessoa = 7.5
		elif session['usuario'] == 'maria':
			nome_pessoa = 'Maria dos Santos'
			media_pessoa = 8.6
		return render_template('area_logada.html', nome=nome_pessoa, media=media_pessoa)
	else:
		return redirect('/login')  # redireciona usuários não logados para a rota de login


@app.route('/sair')
def sair():
	session.clear()  # limpa o objeto de sessão
	return redirect('/login')


if __name__ == '__main__':
	app.run(debug=True)
