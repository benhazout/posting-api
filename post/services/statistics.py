from .. import models
from sqlalchemy.orm import Session


def top_creators(db: Session):
    # number of users to return
    number_of_users = 10

    # query that returns top {number_of_users} users (users with the most posts) in desc order in format of [user_id,
    # posts_amount]
    result = db.execute(f'SELECT COUNT(*) AS posts_amount, user_id FROM posts GROUP BY user_id ORDER BY posts_amount '
                        f'DESC LIMIT {number_of_users}')

    # unpack sqlalchemy Query object into list
    top_posts_amount_and_ids = [post_amount_and_id for post_amount_and_id in result]

    # get the user_ids into a list
    top_ids = [user.user_id for user in top_posts_amount_and_ids]

    # get users using top_ids list
    top_users = db.query(models.User).filter(models.User.id.in_(top_ids)).all()

    # merging users data (username and name) with user posts_amount in order to return a ShowTopCreators schema
    show_top_creators = [{'username': u.username, 'name': u.name, 'posts': top_posts_amount_and_ids[ind]['posts_amount']} for ind, u in enumerate(top_users)]
    return {'creators': show_top_creators}
