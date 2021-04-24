from app import create_app, db
from flask_migrate import Migrate, upgrade

from app.models import User, Word, Game


app = create_app("development")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Word=Word, Game=Game)


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()
