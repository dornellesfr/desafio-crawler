import unittest
from src.Movie import Movie
from tests.utils import open_file

class TestMovie(unittest.TestCase):
    def test_get_title(self):
        html = open_file('tests/mock/Clube_da_Luta_(1999)_IMDb.html')
        fight_club = Movie(html)
        
        self.assertEqual(fight_club.__get_title, 'Clube da Luta')

        

if __name__ == "__main__":
    unittest.main()
