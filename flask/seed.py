"""
Populate twitter database with fake data using the SQLAlchemy ORM.
"""

import random
import string
import hashlib
import secrets
from faker import Faker
from src.models import User, Fix, db
from src import create_app

USER_COUNT = 50
POST_COUNT = 100
LIKE_COUNT = 400

# assert LIKE_COUNT <= (USER_COUNT * TWEET_COUNT)


def random_passhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&',  # valid pw characters
            k=random.randint(8, 15)  # length of pw
        )
    )

    salt = secrets.token_hex(16)

    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()


def truncate_tables():
    """Delete all rows from database tables"""
    db.session.execute(User.delete())
    User.query.delete()
    db.session.commit()


def main():
    """Main driver function"""
    app = create_app()
    app.app_context().push()
    truncate_tables()
    fake = Faker()

    last_user = None  # save last user
    for _ in range(USER_COUNT):
        last_user = User(
            username=fake.unique.first_name().lower() + str(random.randint(1, 150)),
            password=random_passhash()
        )
        db.session.add(last_user)

    # insert users
    db.session.commit()

    last_post = None  # save last tweet
    for _ in range(POST_COUNT):
        last_post = Post(
            content=fake.sentence(),
            user_id=random.randint(last_user.id - USER_COUNT + 1, last_user.id)
        )
        db.session.add(last_post)

    # insert tweets
    db.session.commit()

#     user_tweet_pairs = set()
#     while len(user_tweet_pairs) < LIKE_COUNT:

#         candidate = (
#             random.randint(last_user.id - USER_COUNT + 1, last_user.id),
#             random.randint(last_post.id - TWEET_COUNT + 1, last_post.id)
#         )

#         if candidate in user_tweet_pairs:
#             continue  # pairs must be unique

#         user_tweet_pairs.add(candidate)

#     new_likes = [{"user_id": pair[0], "tweet_id": pair[1]}
#                  for pair in list(user_tweet_pairs)]
#     insert_likes_query = likes_table.insert().values(new_likes)
#     db.session.execute(insert_likes_query)

# # insert likes
# db.session.commit()


# run script
main()
