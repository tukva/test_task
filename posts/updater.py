from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import reset_upvotes


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reset_upvotes, "interval", minutes=1440)
    scheduler.start()
