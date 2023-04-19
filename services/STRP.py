import stripe
from decouple import config

stripe.api_key = config("STRIPE_KEY")

#  Payment Session


class PaymentSession:
    def create_payment_session(self, name, price, quantity=1):
        payment_session = stripe.checkout.Session.create(
          line_items=[
            {
              "price_data": {
                "currency": "usd",
                "product_data": {"name": f"{name}"},
                "unit_amount": price,
              },
              "quantity": quantity,
            },
          ],
          mode="payment",
          success_url="http://localhost:5000/success.html",  # URL from the frontend app for successful payment
          cancel_url="http://localhost:5000/cancel.html",  # URL from the frontend app for unsuccessful payment
        )

        return payment_session

    @staticmethod
    def check_payment_processed(order_id):
        session_status_check = stripe.checkout.Session.retrieve(
            f"{order_id}",
        )

        return session_status_check["payment_status"]


# P = PaymentSession("Lilko", 2000)
#
# print(P.create_payment_session())

# x = stripe.checkout.Session.retrieve(
#   "cs_test_a1Ybvysaret8oazvDo1N3PVpI67yjR02oPPR8NRGd3DZb1rvTPh70FEFlN",
# )
#
# print(x["payment_status"])