#!/usr/bin/python
import praw
import random
from pokemon_lists import *
import os


REDDIT_USERNAME = 'REDDITNAME'  # YOUR USERNAME as string
REDDIT_PASS = 'REDDITPASSWORD'  # YOUR PASSWORD as string



if not os.path.isfile("posts_saved.txt"):
    posts_saved = []

else:
    
    with open("posts_saved.txt", "r") as f:
        posts_saved = f.read()
        posts_saved = posts_saved.split("\n")
        posts_saved = filter(None, posts_saved)


while True:
    r = praw.Reddit('Pokereply 0.1')
    r.login(REDDIT_USERNAME, REDDIT_PASS)
    subreddit = r.get_subreddit('SUBREDDIT NAME')
    subreddit_comments = subreddit.get_comments()
    for comment in subreddit_comments:
        if comment.body == "!SuggestPokemon" and comment.id not in posts_saved:
            choice = random.choice(PokemonList)
            comment.reply(choice)
            posts_saved.append(comment.id)

