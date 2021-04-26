from app import app, db
from app.models import Users, LearnProgress, Attempt, Questions

# $ flask shell
@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Users": Users,
        "Progress": LearnProgress,
        "Attempt": Attempt,
        "Questions": Questions,
    }


if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)
