from flask import Blueprint, request, jsonify
from app.models import Fine
from app import db
from datetime import datetime, timezone

fine_blue_print = Blueprint("fines", __name__)

# create
@fine_blue_print.route("/", methods=["POST"])
def create_fine():
    data = request.get_json()
    try:
        new_fine = Fine(
            user_id=data["user_id"],
            umuganda_id=data["umuganda_id"],
            amount=data.get("amount", 5000.0),
            reason=data["reason"],
            is_paid=data.get("is_paid", False),
            issued_on=datetime.now(timezone.utc)
        )

        db.session.add(new_fine)
        db.session.commit()
        return jsonify({"message": "Fine issued successfully", "fine": new_fine.return_dict()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# get-all
@fine_blue_print.route("/")
def get_all_fines():
    fines = Fine.query.all()
    return jsonify([fine.return_dict() for fine in fines])

# get-one
@fine_blue_print.route("/<int:fine_id>")
def get_fine_by_id(fine_id):
    fine = Fine.query.get_or_404(fine_id)
    return jsonify(fine.return_dict())

# update fine as paid or update reason/amount
@fine_blue_print.route("/<int:fine_id>", methods=["PUT"])
def update_fine(fine_id):
    fine = Fine.query.get_or_404(fine_id)
    data = request.get_json()

    fine.amount = data.get("amount", fine.amount)
    fine.reason = data.get("reason", fine.reason)
    fine.is_paid = data.get("is_paid", fine.is_paid)

    db.session.commit()
    return jsonify({"message": "Fine updated", "fine": fine.return_dict()})

# delete
@fine_blue_print.route("/<int:fine_id>", methods=["DELETE"])
def delete_fine(fine_id):
    fine = Fine.query.get_or_404(fine_id)
    db.session.delete(fine)
    db.session.commit()
    return jsonify({"message": f"Fine was deleted"})
