from app import db
from datetime import datetime, timezone

class Fine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    umuganda_id = db.Column(db.Integer, db.ForeignKey("umuganda.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False, default=5000.0)
    reason = db.Column(db.String(100), nullable=False) # absent without a reason, with a reason, late arrival(must be measured according on the umuganda duration)
    is_paid = db.Column(db.Boolean, default=False)
    issued_on = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    def return_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "umuganda_id": self.umuganda_id,
            "amount": self.amount,
            "reason": self.reason,
            "is_paid": self.is_paid,
            "issued_on": self.issued_on
        }