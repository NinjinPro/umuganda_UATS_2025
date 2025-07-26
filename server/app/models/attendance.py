from app import db
from datetime import datetime, timezone
# this in future will be handled using a generted QR code (for mobile phones), or biometrics scans like  fingerprint-igikumwe, facial scan, or voice recognition)

class Attendance(db.Model):

    # __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    umuganda_id = db.Column(db.Integer, db.ForeignKey("umuganda.id"), nullable=False)

    status = db.Column(db.String(20), default="absent")  # absent, delay or present / 0 or 1
    format_used = db.Column(db.String(25), default="web_form") # web_form, qr_code, fingerprint, facial recognition, vocal recognition

    # marked_at = db.Column(db.DateTime) # i am thinking that it will work the same as arrived at attribute
    arrived_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)) # an immediate timestamp

    def return_dict(self):
        return {
            "attendance_id": self.id,
            "user_id": self.user_id,
            "umuganda_id": self.umuganda_id,
            "status": self.status,
            "format_used": self.format_used,
            "marked_at": self.marked_at,
            "arrived_at": self.arrived_at
        }

    @staticmethod
    def get_by_user(user_id):
        return Attendance.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_umuganda(umuganda_id):
        return Attendance.query.filter_by(umuganda_id=umuganda_id).all()

    @staticmethod
    def get_one(user_id, umuganda_id):
        return Attendance.query.filter_by(user_id=user_id, umuganda_id=umuganda_id).first()