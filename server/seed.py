from app import create_app, db
from app.models.user import User
from app.models.umuganda import Umuganda
from app.models.attendance import Attendance
from app.models.fine import Fine

from datetime import datetime, timedelta, timezone
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    """ =======================   citizens    ==============================  """

    # seeding users
    admin = User(
        first_name="Ineza",
        middle_name="Alice",
        last_name="Muban",
        gender="female",
        email="alice1@uats.bibare.com",
        phone = "4444444444",
        role = "admin",
        address = {
            "province": "Kigali",
            "district": "gasabo",
            "sector": "kimironko",
            "cell": "bibare",
            "village": "inyange",
            "isibo": "",
        },
    )

    citizen1 = User(
        first_name="Kamanzi",
        middle_name="",
        last_name="Ebenezer",
        email="Kamanzi@uats.bibare.com",
        phone = "1111111111",
        role = "citizen",
        address = {
            "province": "Kigali",
            "district": "gasabo",
            "sector": "kimironko",
            "cell": "bibare",
            "village": "inyange",
            "isibo": "",
        },
    )

    citizen2 = User(
        first_name="Mugisha",
        middle_name="Bob",
        last_name="Johnathan",
        email="bob12e34@gmail.com",
        phone = "2222222222",
        role = "citizen",
        address = {
            "province": "Kigali",
            "district": "gasabo",
            "sector": "kimironko",
            "cell": "bibare",
            "village": "inyange",
            "isibo": "",
        },
    )

    citizen3 = User(
        first_name="Kaneza",
        middle_name="",
        last_name="Chalrlen",
        email="charlie43rf32s@gmail.com",
        phone = "3333333333",
        role = "citizen",
        address = {
            "province": "Kigali",
            "district": "gasabo",
            "sector": "kimironko",
            "cell": "bibare",
            "village": "inyange",
            "isibo": "",
        }
    )

    citizen1.set_password("citizen1")
    citizen2.set_password("citizen2")
    citizen3.set_password("citizen3")
    admin.set_password("admin-kimironko")

    for user in [admin, citizen1, citizen2, citizen3]:
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"\n Error : {str(e)}\n Failed to seed user namde  at {user.first_name}")

    print("✅ users seed data inserted successfully.")

    """ =======================   imiganda    ==============================  """

    # seeding imiganda
    start = datetime.now(timezone.utc) + timedelta(days=5, hours=8)
    end = start + timedelta(hours=3)

    umuganda1 = Umuganda(
        title="Umuganda wa Kimironko, Bibare",
        description="Isuka, igitiyo, umwiko cg umukubuzo",
        umuganda_date=datetime.now(timezone.utc) + timedelta(days=5), # in  next 5 days
        created_by=admin.id,
        location="kimironko sector office",
        start_time=start,
        end_time=end,
    )
    
    end = start + timedelta(hours=2.5)
    umuganda2 = Umuganda(
        title="Umuganda wa Kimironko, Nyagatovu",
        description="Isuka, umwiko cg ingorofani",
        umuganda_date=datetime.now(timezone.utc) + timedelta(days=5), # in  next 5 days
        created_by=admin.id,
        location="kimironko sector office",
        start_time=start,
        end_time=end,
    )

    for umu in [umuganda1, umuganda2]:
        try:
            db.session.add(umu)
            db.session.commit()
            print(f"\n Duration of {umu.title} is {umu.count_duration_hours}")
        except Exception as e:
            db.session.rollback()
            print(f"\n Error : {str(e)}\n Failed to seed umuganda titled  {umu.title}")

    print("✅ Umuganda seed data inserted successfully.")

    print(f"\n Duration of {umuganda1.title} is {umuganda1.count_duration_hours}")



    """ =======================   attendance    ==============================  """



    # Record attendance
    attendance1 = Attendance(umuganda_id=umuganda1.id, user_id=citizen1.id, status="present")
    attendance2 = Attendance(umuganda_id=umuganda1.id, user_id=citizen2.id)
    attendance3 = Attendance(umuganda_id=umuganda2.id, user_id=citizen3.id)
    db.session.add_all([attendance1, attendance2, attendance3])
    db.session.commit()
    print("✅ Attendance seed data inserted successfully.")
    
    
    """ =======================   fines    ==============================  """



    # Generate fine for citizen1 (absent)
    fine1 = Fine(
        user_id=citizen2.id,
        umuganda_id=umuganda1.id,
        amount=2000,
        reason="delayed 20 minutes",
        issued_on=datetime.now(timezone.utc)
    )
    fine2 = Fine(
        user_id=citizen1.id,
        umuganda_id=umuganda2.id,
        amount=2000,
        reason="absent",
        issued_on=datetime.now(timezone.utc)
    )
    fine2 = Fine(
        user_id=citizen3.id,
        umuganda_id=umuganda2.id,
        # amount=2000,  let the db give this user a fine 5000 as default
        reason="lied",
        issued_on=datetime.now(timezone.utc)
    )
    try:
        db.session.add_all([fine1, fine2])
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f" Failed to record seed data of fines")
    print("✅ fines seed data inserted successfully.")


    """ =======================   done    ==============================  """


    print("\n\n✅ Done see you again \n.")
