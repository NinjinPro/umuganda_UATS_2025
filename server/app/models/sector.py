from app import db

class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True) 
    admins = db.relationship("Admin", back_populates="sector")

    def __repr__(self):
        return f"<Sector {self.name}>"
