from flask import Blueprint, render_template, redirect, url_for, abort, request, jsonify
from app.models import User, Admin, Sector, Umuganda, Attendance, Fine, Notification
from flask_login import login_required, current_user
from functools import wraps
from app import db

def redirect_to_login():
    return redirect(url_for("users.login"))  or abort(403)

def role_required(role_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if current_user.role != role_name:
                abort(403)
            return view_func(*args, **kwargs)
        return wrapper
    return decorator

dashboard_blue_print = Blueprint("dashboard", __name__)

@dashboard_blue_print.route("/citizen")
@login_required
@role_required("citizen")
def citizen():                                              # still in production
    if current_user.role != "citizen":
        return redirect(url_for("users.login"))  # or a 403 page
    
    # hard coded data
    """
    # upcoming_umuganda = {
    #     "date": "2025-07-27",
    #     "location": "Kigali Sector",
    #     "start_time": "08:00 AM",
    #     "organizer": "Chairperson Mugisha"
    # }

    # attendance_history = [
    #     {"date": "2025-06-29", "status": "Attended"},
    #     {"date": "2025-05-25", "status": "Missed"},
    # ]

    # fines = [
    #     {"reason": "Missed June Umuganda", "amount": 500, "status": "Unpaid"},
    # ]

    # notifications = [
    #     "New umuganda scheduled for July 27",
    #     "You have an unpaid fine: 500 RWF"
    # ]

    # return render_template(
    #     "citizen/dashboard.html",
    #     upcoming_umuganda=upcoming_umuganda,
    #     attendance_history=attendance_history,
    #     fines=fines,
    #     notifications=notifications
    # )
    """
    
    # db data fetching
    next_umuganda = Umuganda.query.order_by(Umuganda.created_at.asc()).first()
    # attendance_count = Attendance.query.filter_by(user_id=current_user.id, attended=True).count()
    # missed_count = Attendance.query.filter_by(user_id=current_user.id, attended=False).count()
    total_fines = sum(f.amount for f in Fine.query.filter_by(user_id=current_user.id).all())
    # notifications = Notification.query.filter_by(user_id=current_user.id).order_by(Notification.date.desc()).limit(5)

    return render_template(
        "dashboard/citizen_v2.html",
        next_umuganda=next_umuganda,
        # attendance_count=attendance_count,
        # missed_count=missed_count,
        total_fines=total_fines,
        # notifications=notifications
    )

@dashboard_blue_print.route("/admin")
@login_required
@role_required("admin")
def admin():
    if current_user.role != "admin":
        return redirect_to_login()
    
    admin_record = Admin.query.filter_by(user_id=current_user.id).first()

    print(f"\n Admin record => {admin_record}")
    
    if not admin_record:
        return redirect_to_login()

    sector_info = None
    if admin_record.sector_id:
        sector_info = Sector.query.get(admin_record.sector_id)

    citizens = []
    admin_sector = current_user.address["sector"]
    if sector_info:
        citizens = (
            User.query.filter(User.role == "citizen", 
            admin_sector == sector_info.name).all()
        )
    citizens = User.query.filter_by(sector_id=sector_id, role="citizen").all()

    imiganda = Umuganda.query.filter_by(created_by=current_user.id).all()

    fines = None
    if citizens:
        for cit in citizens:
            fine = Fine.query.filter_by(user_id=cit.id).first()

    admin_address: list[list[str]] = [[k,v] for k, v in current_user.address.items()]

    return render_template(
        "dashboard/admin_v2.html",
        admin=admin_record,
        # sector=sector_info,
        sectorName=admin_sector,
        imiganda=[umuganda.return_dict() for umuganda in imiganda],
        citizens=citizens,
        address=admin_address,
        user=current_user
    )
    
    """ hard coded data """

    """
    umuganda_list = [
        {"id": 1, "date": "2025-07-27", "location": "Kimironko", "status": "Upcoming"},
        {"id": 2, "date": "2025-06-29", "location": "Gisozi", "status": "Completed"},
    ]

    fines_summary = [
        {"citizen": "Jean Uwase", "reason": "Missed Umuganda", "amount": 500, "status": "Unpaid"},
        {"citizen": "Alice Niyonsaba", "reason": "Late Arrival", "amount": 200, "status": "Paid"},
    ]

    attendance_records = [
        {"citizen": "Eric Mugabo", "umuganda_date": "2025-06-29", "status": "Attended"},
        {"citizen": "Grace Imanzi", "umuganda_date": "2025-06-29", "status": "Missed"},
    ]

    notifications_sent = [
        {"title": "Reminder", "content": "Umuganda on July 27 - Don’t miss!", "sent_on": "2025-07-23"},
        {"title": "Fine Notice", "content": "You have an unpaid fine", "sent_on": "2025-07-01"},
    ]

    payment_reviews = [
        {"citizen": "Grace Imanzi", "fine": "500 RWF", "status": "Pending Verification"},
        {"citizen": "Eric Mugabo", "fine": "200 RWF", "status": "Verified"},
    ]

    return render_template(
        "dashboard/admin_v2.html",
        umuganda_list=umuganda_list,
        fines_summary=fines_summary,
        attendance_records=attendance_records,
        notifications_sent=notifications_sent,
        payment_reviews=payment_reviews
    )
    """

@dashboard_blue_print.route("/admin/mark_attendance", methods=["POST"])
@login_required
@role_required("admin")
def mark_attendance():
    data = request.get_json()
    citizen_id = data.get("citizen_id")
    umuganda_id = data.get("umuganda_id")
    status = data.get("status")  # "present" or "absent"

    if not citizen_id or not umuganda_id or not status:
        return jsonify({"error": "Missing data"}), 400

    attendance = Attendance(
        citizen_id=citizen_id,
        umuganda_id=umuganda_id,
        status=status,
        timestamp=datetime.utcnow()
    )
    db.session.add(attendance)

    if status == "absent":
        fine = Fine(
            citizen_id=citizen_id,
            umuganda_id=umuganda_id,
            amount=500,  # Example fixed fine
            status="unpaid",
            created_at=datetime.utcnow()
        )
        db.session.add(fine)
    db.session.commit()
    return jsonify({"success": True})
