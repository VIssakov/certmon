from app import db

class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parameter = db.Column(db.String(100), unique=True, nullable=False)
    data = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Config {self.parameter}>'

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    chat_id = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'

class Certs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    subject = db.Column(db.String(500), nullable=False)
    not_before = db.Column(db.String(100), nullable=False)
    not_after = db.Column(db.String(100), nullable=False)
    issuer = db.Column(db.String(500), nullable=False)
    extension_count = db.Column(db.String(1000), nullable=True)
    subject_altName = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f'<Certificate {self.subject}>'
