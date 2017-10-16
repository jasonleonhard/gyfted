"""import create and query."""
from models import db, Ticket
db.create_all()
db.session.commit()
db  # <SQLAlchemy engine='postgresql://localhost/gyfted_dev'
print(Ticket.query.all())  # []
exit()
