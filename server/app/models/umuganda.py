# from server.app.models import db
from app import db
from datetime import datetime, timezone
from sqlalchemy import CheckConstraint

class Umuganda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, default="Umuganda ...") # set to default as "Umuganda ..."
    description = db.Column(db.Text)
    umuganda_date = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False) #c the assigned user
    location = db.Column(db.String(100)) # salle y'inama, ishuri , ikigo, aho umaganda uzabera nyamukuru, any where
    duration = db.Column(db.String(60)) # measured in hours but will be hundled weel using the frontend

    start_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)

    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    attendances = db.relationship("Attendance", backref="umuganda", lazy=True, cascade="all, delete-orphan")
    fines = db.relationship("Fine", backref="umuganda", lazy=True)
    notifications = db.relationship("Notification", backref="umuganda", lazy=True)

    __table_args__ = (CheckConstraint("end_time > start_time", name="check_end_after_start"),)

    @property
    def count_duration_hours(self):
        if self.start_time and self.end_time:
            delta = self.end_time - self.start_time
            return round(delta.total_seconds() / 3600, 2)
        return None

    def return_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "umuganda_date": self.umuganda_date.strftime("%Y-%m-%d %H:%M"),
            "created_by": self.created_by,
            "location": self.location,
            "duration": self.count_duration_hours,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # "attendances": self.attendances,
            # "fines": self.fines,
            # "notifications": self.notifications
        }