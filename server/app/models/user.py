from app import db
from flask_login import UserMixin
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from .custom_types import JSONDict

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # used to make the umuganda persoanl id number for future attenendance redording

    first_name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(60), nullable=True)
    last_name = db.Column(db.String(30), nullable=False)
    
    gender = db.Column(db.String(10), nullable=True) # male, female, transgender
    
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    
    address = db.Column(JSONDict, nullable=False) # province -> district -> sector -> cell -> village -> isibo
    role = db.Column(db.String(20), nullable=False, default="citizen")  # citizen and admin by now in future (v2) fine_enforcer and attendance_guide must be added
    personal_recognition = db.Column(db.String(150), nullable=True) # basically, a string representing user finger print, facail imagery or vocal codes

    is_local = db.Column(db.Boolean(20), default=True) # user is Rwandan or not
    is_not_local = db.Column(db.String(40), nullable=True, default=True) # user is not Rwandan, hence provide their country
    
    is_verified = db.Column(db.Boolean, default=False) # msking sure if the user is verified
    
    password_hash = db.Column(db.String(128), nullable=False)

    registered_on = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    attendances = db.relationship("Attendance", backref="user", lazy=True, cascade="all, delete-orphan")
    fines = db.relationship("Fine", backref="user", lazy=True)
    payments = db.relationship("Payment", backref="user", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def return_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "role": self.role,
            "personal_recognition": self.personal_recognition,
            "is_local": self.is_local,
            "is_not_local": self.is_not_local,
            # "password_hash": self.password_hash,
            "registered_on": self.registered_on,
            # "attendances": self.attendances,
            # "fines": self.fines,
            # "payments": self.payments
        }