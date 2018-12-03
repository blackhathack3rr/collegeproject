def show_rating(context, rating_key):
    rating, created = Rating.objects.get_or_create(key=rating_key)
    return {
            'rating_key': rating_key,
            'total_votes': rating.total_votes,
            'total_ratings': rating.total_rating,
            'rating': rating.get_star_rating(),
            'percent': rating.get_percent(),
            'max_stars': rating.max_stars
            }
register.inclusion_tag("plaza/ratings.html", takes_context=True)(show_rating)