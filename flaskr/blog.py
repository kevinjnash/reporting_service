from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT POST_ID AS "ID", POST_TITLE, POST_BODY, CRT_TS AS "CREATED", AUTHOR_ID, USERNAME FROM T_POST P JOIN T_USER U ON P.AUTHOR_ID = U.USER_ID ORDER BY CRT_TS DESC'
    ).fetchall()
    return render_template('blog/index.html')

