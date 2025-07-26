from app import db
from app.models import Admin, Sector

def create_admin(user_id, sector_name):
    admin_count = Admin.query.count()
    sector_count = Sector.query.count()

    if sector_count >= 416:
            raise ValueError("Cannot create more than 416 sectors.")
    
    new_sector = Sector(name=sector_name)
    db.session.add(new_sector)
    db.session.commit()

    # sector_id = Sector.query.filter_by(name=sector_name).first()
    sector_id = new_sector.id

    if admin_count >= 416:
        raise ValueError("Cannot create more than 416 admins.")

    new_admin = Admin(user_id=user_id, sector_id=sector_id)
    db.session.add(new_admin)
    db.session.commit()


    return new_admin
