from app import db
from datetime import datetime, timezone

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, unique=True)  
    assigned_date = db.Column(db.DateTime(timezone=True), default = lambda:datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean, default=True)

    sector_id = db.Column(db.Integer, db.ForeignKey("sector.id"), nullable=False)
    sector = db.relationship("Sector", back_populates="admins")

    def __repr__(self):
        return f"<Admin user_id={self.user_id} sector_id={self.sector_id}>"
