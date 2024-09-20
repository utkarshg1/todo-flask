from database import db
from datetime import datetime
import pytz


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone("Asia/Kolkata"))
    )

    def __repr__(self):
        return f"<Task {self.id}>"
