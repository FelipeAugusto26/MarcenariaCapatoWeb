from web_marcenaria import db

class User(db.Model):
    __tablename__ = "users" # Definir o nome da minha tabela de usurários
    # colunas da tabela
    id = db.Column(db.Integer, primary_key=True) #chave primária
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    # Campos que eu considero como obrigatório
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username



class Cliente(db.Model):
    __tablename__="clientes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    endereco = db.Column(db.Text)
    telefone = db.Column(db.String, unique=True)

    # Campos que eu considero como obrigatório
    def __init__(self, name, endereco, telefone):
        self.name = name
        self.endereco = endereco
        self.telefone = telefone

    def __repr__(self):
        return "<Cliente %r>" % self.name


class Orcamento(db.Model):
    __tablename__="orcamentos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    telefone = db.Column(db.String)
    endereco = db.Column(db.Text)
