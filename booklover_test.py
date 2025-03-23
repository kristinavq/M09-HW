import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        booklover1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        booklover1.add_book("Dune", 5)
        
        self.assertIn("Dune", booklover1.book_list['book_name'].values)

    def test_2_add_book(self):
        booklover1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        booklover1.add_book("Dune", 5)
        booklover1.add_book("Dune", 5)
        
        self.assertEqual(booklover1.num_books_read(), 1)
                
    def test_3_has_read(self):
        booklover1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        booklover1.add_book("Exodus", 3)
        
        self.assertTrue(booklover1.has_read("Exodus"))
        
    def test_4_has_read(self):
        booklover1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        booklover1.add_book("Dune", 5)
        
        self.assertFalse(booklover1.has_read("Twilight"))
        
    def test_5_num_books_read(self):
        booklover1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        booklover1.add_book("Dune", 5)
        booklover1.add_book("Exodus", 3)
        
        self.assertEqual(booklover1.num_books_read(), 2)

    def test_6_fav_books(self):
        booklover1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        booklover1.add_book("War of the Worlds", 4)
        booklover1.add_book("Dune", 5)
        booklover1.add_book("Exodus", 3)
        
        fav_books = booklover1.fav_books()
        
        self.assertTrue(all(rating > 3 for rating in fav_books['book_rating']))
        self.assertTrue("War of the Worlds" in fav_books['book_name'].values)
        self.assertIn("Dune", fav_books['book_name'].values)
        self.assertFalse("Exodus" in fav_books['book_name'].values)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
