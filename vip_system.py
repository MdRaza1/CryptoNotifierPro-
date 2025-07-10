import json, datetime
DB = "vip_db.json"
PLANS = {
 "starter": {"days":7,"price":699},
 "smart": {"days":15,"price":1299},
 "pro": {"days":30,"price":1999},
 "elite": {"days":90,"price":3999},
 "ultra": {"days":180,"price":6499},
 "prime": {"days":365,"price":9999},
 "legend": {"days":36500,"price":14999},
}
def load(): 
    try: return json.load(open(DB))
    except: return {}
def save(d): json.dump(d, open(DB,"w"))
def choose_plan(): return "starter"  # For demo; expand logic
def activate(uid, plan):
    d=load()
    d[str(uid)]={"plan":plan,"exp":(datetime.datetime.now()+datetime.timedelta(days=PLANS[plan]["days"])).isoformat()}
    save(d)
def is_vip(uid):
    d=load().get(str(uid))
    if not d: return False
    if datetime.datetime.fromisoformat(d["exp"])<datetime.datetime.now():
        d=load(); d.pop(str(uid),None); save(d); return False
    return True
