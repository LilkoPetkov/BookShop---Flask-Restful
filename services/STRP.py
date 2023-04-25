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
          success_url=f"http://127.0.0.1:5000/success.html",
          cancel_url="http://localhost:5000/cancel.html",
        )

        return payment_session

    @staticmethod
    def check_payment_processed(order_id):
        session_status_check = stripe.checkout.Session.retrieve(
            f"{order_id}",
        )

        return session_status_check["payment_status"]

    
    
"""
The code below can be used for implementation of authomatic payments and renewals. 
The User's table would need to be extended to receive the CC details.
"""

# stripe.api_key = config("STRIPE_KEY")

# class Stripe:
#     PM = None
#     CUSTOMER = None
#     PI = None

#     def __init__(self, card_number, exp_month, exp_year, cvv, email, name, phone, city=None, country=None, \
#                 line1=None, line2=None, postal_code=None, state=None,):
        
#         self.card_number = card_number
#         self.exp_month = exp_month
#         self.exp_year = exp_year
#         self.cvv = cvv
#         self.email = email
#         self.name = name
#         self.phone = phone 
#         self.city = city
#         self.country = country
#         self.line1 = line1
#         self.line2= line2
#         self.postal_code = postal_code
#         self.state = state

#     def create_payment_method(self):
#         my_pm = stripe.PaymentMethod.create(
#             type="card",
#             card={
#                 "number": f"{self.card_number}",
#                 "exp_month": self.exp_month,
#                 "exp_year": self.exp_year,
#                 "cvc": f"{self.cvv}",
#             }, billing_details={
#                 "address": {
#                 "city": self.city,
#                 "country": self.country,
#                 "line1": self.line1,
#                 "line2": self.line2,
#                 "postal_code": self.postal_code,
#                 "state": self.state,
#                 },
#                 "email": self.email,
#                 "name": self.name,
#                 "phone": self.phone,
#             },
#         )

#         self.PM = my_pm

#     def create_customer(self):
#         customer = stripe.Customer.create(
#             description="Test charge (created for API docs at https://www.stripe.com/docs/api)",
#             email=self.email,
#             name=self.name,
#             payment_method=self.PM,
#             phone=self.phone,
#         )
        
#         self.CUSTOMER = customer
    
#     def create_payment_intent(self):
#         payment_intent = stripe.PaymentIntent.create(
#             amount=2000,
#             currency="bgn",
#             automatic_payment_methods={"enabled": True},
#             payment_method=self.PM,
#             customer=self.CUSTOMER,
#             receipt_email=self.email
#         )

#         self.PI = payment_intent
    
#     def confirm_payment_intent(self):
#         confirm_pi = stripe.PaymentIntent.confirm(
#             self.PI,
#             return_url="https://yourdomain.com/success",
#         )

#         return confirm_pi
    
#     def capture_payment(self):
#         capture_payment_intent = stripe.PaymentIntent.capture(
#             self.PI,
#         )

#         return capture_payment_intent
    
#     def cancel_payment_intent(self):
#         cancel_pm = stripe.PaymentIntent.cancel(
#             self.PI,
#         )

#         return cancel_pm


# S = Stripe(
#     "5200828282828210", 4, 2028, 133, "lp@gmail.com", "LP", "+3590879851"\
#         , "Plovdiv", "BG", postal_code=4000
# )

# S.create_payment_method()
# S.create_customer()
# S.create_payment_intent()
# S.confirm_payment_intent()
# print(S.capture_payment())
#print(S.cancel_payment_intent())
