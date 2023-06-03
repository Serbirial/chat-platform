import random
import sys

def generate_basic_id(ids: list):
    try:
        biggest_id = max(ids)
    except ValueError:
        biggest_id = 5
    return biggest_id + 1


def generate_session_token():
    pass