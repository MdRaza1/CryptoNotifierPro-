from instamojo_wrapper import Instamojo
import config, vip_system

api = Instamojo(api_key=config.IM_API_KEY, auth_token=config.IM_AUTH_TOKEN)

PLANS = vip_system.PLANS

def create_link(uid):
    plan = vip_system.choose_plan()
    resp = api.payment_request_create(
        purpose=f"{plan} VIP plan",
        amount=str(PLANS[plan]["price"]),
        redirect_url="",
        webhook="https://<YOUR_RENDER_SUBDOMAIN>.onrender.com/instamojo-webhook",
        allow_repeated_payments=False
    )
    return resp["payment_request"]["longurl"]

def validate(data):
    return data.get("mac") == config.WEBHOOK_SECRET

def process(data):
    uid = int(data["buyer_name"])
    plan = data["purpose"].split()[0].lower()
    vip_system.activate(uid, plan)
    return uid, plan
