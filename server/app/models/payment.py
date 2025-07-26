from app import db
from datetime import datetime, timezone

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    fine_id = db.Column(db.Integer, db.ForeignKey("fine.id"))
    amount = db.Column(db.Float, nullable=False, default=5000.0)
    provider = db.Column(db.String(50))  # MTN or Airtel but we prefer mtn at first and later all
    status = db.Column(db.String(20), default="pending")  # success, failed, pending
    paid_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    def return_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "fine_id": self.fine_id,
            "amount": self.amount,
            "provider": self.provider,
            "status": self.status,
            "paid_at": self.paid_at
        }