import json
import random
import secrets

import requests


class Bot:
    __slots__ = (
        '_number_of_users', '_max_posts_per_user', '_max_likes_per_user',
        '_base_url',
        '_users', '_posts'
    )

    def __init__(self):
        self._users = []
        self._posts = []

        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.loads(f.read())

        self._number_of_users = config['number_of_users']
        self._max_posts_per_user = config['max_posts_per_user']
        self._max_likes_per_user = config['max_likes_per_user']
        self._base_url = config['base_url']

    def signup_users(self):
        for _ in range(self._number_of_users):
            user_data = {
                'email': f'user_{random.randint(1, 100000)}@mail.com',
                'password': str(secrets.token_urlsafe())
            }

            user = requests.post(f'{self._base_url}/users/', data=user_data).json()
            self._users.append({
                'id': user['id'],
                **user_data
            })

    def create_posts(self):
        for user in self._users:
            tokens = requests.post(f'{self._base_url}/users/token/', data={
                'email': user['email'],
                'password': user['password'],
            }).json()
            for _ in range(self._max_posts_per_user):
                if random.randint(1, 4) == 2:
                    res = requests.post(f'{self._base_url}/posts/', data={
                        'title': f'Post-{random.randint(1, 100000)}',
                        'body': f'lorem ipsum {secrets.token_urlsafe()}'
                    }, headers={
                        'Authorization': f'Bearer {tokens["access"]}'
                    }).json()
                    self._posts.append(res)

    def like_random_posts(self):
        for user in self._users:
            liked_posts = 0
            tokens = requests.post(f'{self._base_url}/users/token/', data={
                'email': user['email'],
                'password': user['password'],
            }).json()
            for post in self._posts:
                if random.randint(1, 4) and liked_posts < self._max_likes_per_user:
                    requests.post(f'{self._base_url}/posts/{post["id"]}/like/', headers={
                        'Authorization': f'Bearer {tokens["access"]}'
                    })
                    liked_posts += 1

    def process(self):
        self.signup_users()
        self.create_posts()
        self.like_random_posts()


if __name__ == '__main__':
    bot = Bot()
    bot.process()
