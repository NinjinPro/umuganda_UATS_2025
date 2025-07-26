# server/routes/payment.py

from flask import Blueprint, request, jsonify
from app.models import Payment, Fine
from app import db
from datetime import datetime, timezone

payment_blue_print = Blueprint("payments", __name__)

# create
@payment_blue_print.route("/", methods=["POST"])
def create_payment():
    data = request.get_json()
    try:
        fine = Fine.query.get(data["fine_id"])
        if not fine:
            return jsonify({"error": "Fine not found"}), 404

        payment = Payment(
            user_id=data["user_id"],
            fine_id=data["fine_id"],
            amount=data.get("amount", fine.amount),
            provider=data.get("provider", "MTN"),
            status="pending",
            paid_at=datetime.now(timezone.utc)
        )

        db.session.add(payment)
        db.session.commit()

        return jsonify({"message": "Payment created", "payment": payment.return_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# get-all
@payment_blue_print.route("/")
def get_all_payments():
    payments = Payment.query.all()
    return jsonify([payment.return_dict() for payment in payments])

# get-one
@payment_blue_print.route("/<int:payment_id>")
def get_payment_by_id(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    return jsonify(payment.return_dict())

# update -> status | provider | amount
@payment_blue_print.route("/<int:payment_id>", methods=["PUT"])
def update_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    data = request.get_json()

    if "status" in data: payment.status = data["status"]
    if "provider" in data: payment.provider = data["provider"]
    if "amount" in data: payment.amount = data["amount"]

    db.session.commit()
    return jsonify({"message": "Payment updated", "payment": payment.return_dict()})

# delete
@payment_blue_print.route("/<int:payment_id>", methods=["DELETE"])
def delete_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify({"message": f"Payment ID {payment_id} deleted"})
