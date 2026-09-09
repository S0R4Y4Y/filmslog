from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Review
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        movie_title = request.form.get('movie_title')
        genre = request.form.get('genre')
        rating = request.form.get('rating')
        review_text = request.form.get('review_text')

        if not movie_title:
            flash('Movie title cannot be empty!', category='error')
        elif not rating or not rating.isdigit() or not (1 <= int(rating) <= 10):
            flash('Rating must be a number between 1 and 10!', category='error')
        else:
            new_review = Review(
                movie_title=movie_title,
                genre=genre,
                rating=int(rating),
                review_text=review_text,
                user_id=current_user.id
            )
            db.session.add(new_review)
            db.session.commit()
            flash('Review added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-review', methods=['POST'])
@login_required
def delete_review():
    data = json.loads(request.data)
    review_id = data['reviewId']
    review = Review.query.get(review_id)
    if review and review.user_id == current_user.id:
        db.session.delete(review)
        db.session.commit()
    return jsonify({})



