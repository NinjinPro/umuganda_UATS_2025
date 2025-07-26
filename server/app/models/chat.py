from app import db
from datetime import datetime, timezone

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    receiver_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    message = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    def return_dict(self):
        return {
            "id": self.id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "message": self.message,
            "sent_at": self.sent_at,
        }