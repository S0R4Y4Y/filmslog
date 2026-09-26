from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Review
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('views.diary'))
    return render_template("landing.html", user=current_user)


@views.route('/diary', methods=['GET', 'POST'])
@login_required
def diary():
    if request.method == 'POST':
        movie_title = request.form.get('movie_title')
        genre = request.form.get('genre')
        rating = request.form.get('rating')
        review_text = request.form.get('review_text')

        if not movie_title:
            flash('Movie title cannot be empty!', category='error')
        elif not rating or not rating.isdigit() or not (1 <= int(rating) <= 5):
            flash('Rating must be a number between 1 and 5!', category='error')
        else:
            poster_url = None
            poster = request.files.get('poster')
        if poster and poster.filename:
            from .s3 import upload_image
            poster_url = upload_image(poster)
            
        new_review = Review(
                movie_title=movie_title,
                      genre=genre,
                        rating=int(rating),
                            review_text=review_text,
                                poster_image=poster_url,
                                  user_id=current_user.id
        )
        db.session.add(new_review)
        db.session.commit()

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

@views.route('/edit-page', methods=['POST'])
@login_required
def edit_page():
    diary_title = request.form.get('diary_title')
    background = request.files.get('background')

    if diary_title:
        current_user.diary_title = diary_title

    if background and background.filename:
        from .s3 import upload_image
        url = upload_image(background)
        current_user.background_image = url

    db.session.commit()
    return redirect(url_for('views.diary'))

@views.route('/edit-review/<int:review_id>', methods=['POST'])
@login_required
def edit_review(review_id):
    review = Review.query.get(review_id)
    if review and review.user_id == current_user.id:
        review.movie_title = request.form.get('movie_title')
        review.genre = request.form.get('genre')
        review.rating = int(request.form.get('rating'))
        review.review_text = request.form.get('review_text')
        
        poster = request.files.get('poster')
        if poster and poster.filename:
            from .s3 import upload_image
            review.poster_image = upload_image(poster)
        
        db.session.commit()
    return redirect(url_for('views.diary'))