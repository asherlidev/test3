from apscheduler.schedulers.background import BackgroundScheduler
from .transaction import run_async_func
import atexit
scheduler = BackgroundScheduler()
scheduler.add_job(func=run_async_func, trigger="interval", seconds=60)
atexit.register(lambda: scheduler.shutdown())

