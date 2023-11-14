import pytest
import mock
import builtins
import requests
from MovieBuddy import main_menu, search_movie, get_movie_data, display_movie_results, parse_movie_data

def test_main_menu():
    with mock.patch.object(builtins, 'input', lambda: "0"):
        with pytest.raises(SystemExit):
            main_menu()


def test_display_movie_results():
    outcome = [
        ["Movie1", 2020, 7.5, 100],
        ["Movie2", 2019, 8.0, 80],
    ]

    display_movie_results(outcome)
    expected_lines = [
        "Title        Year    IMDB rating    Votes",
        "Movie1       2020    7.5            100",
        "Movie2       2019    8.0             80",
        ""
    ]
   
def test_parse_movie_data():
    response = [{"title":"Zmowa","year":1990,"poster":"86\/86040184216664552","ids":{"simkl_id":1146340,"slug":"zmowa","tmdb":"621201"}}]
    parse_movie_data(response)
    expected_lines = [['Zmowa', 1990, 'N/A', 'N/A']]
