from datetime import datetime, timezone
from sqlalchemy import and_
from flask import g, Blueprint
from flask_restful import Api, Resource, marshal_with
from auth.helper import token_required

from models import db, DailyEntry
from serializers import daily_entry_serializer

# initialize blueprint and api
bp = Blueprint("planner", __name__)
api = Api(bp)


class Today(Resource):
    """Create, retrieve, and update today's daily entry."""

    @token_required
    @marshal_with(daily_entry_serializer)
    def get(self):
        today = DailyEntry.query.filter(
            and_(
                DailyEntry.date == datetime.now(tz=timezone.utc).date(),
                DailyEntry.user_id == g.user.id,
            )
        ).first()

        if not today:
            # create an entry for the current user if one does not already exist
            today = DailyEntry(
                date=datetime.now(tz=timezone.utc).date(), user_id=g.user.id
            )
            db.session.add(today)
            db.session.commit()

        return today

    def put(self):
        pass


class DailyEntryRecord(Resource):
    """Retrieve and update daily entries."""

    @token_required
    @marshal_with(daily_entry_serializer)
    def get(self, id):
        return DailyEntry.query.filter_by(id=id, user_id=g.user.id)

    def put(self, id):
        pass


# make routes available to the api
api.add_resource(Today, "/today")
api.add_resource(DailyEntryRecord, "/<int:id>")
