from app import db
from datetime import datetime, timezone

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    umuganda_id = db.Column(db.Integer, db.ForeignKey("umuganda.id"))
    message = db.Column(db.String(255))
    scheduled_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    sent = db.Column(db.Boolean, default=False)

    def return_dict(self):
        return {
            "id": self.id,
            "umuganda_id": self.umuganda_id,
            "message": self.message,
            "scheduled_at": self.scheduled_at,
            "sent": self.sent
        }