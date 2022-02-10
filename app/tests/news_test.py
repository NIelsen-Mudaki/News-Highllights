import unittest
from app.models import News



class NewsTest(unittest.TestCase):

    def setUp(self):

        self.new_news = News('null', 'TMZ', 'TMZ staff', 'Kanye sells', 'Car sales happen every day, but how often can you say you bought a tank from Kanye West???', '"https://www.tmz.com/2022/01/31/kanye-west-ripsaw-tank-diesel-brothers-truck/', '"https://imagez.tmz.com/image/59/16by9/2022/01/27/590a96f1a1214ce7aa55f2f71f1c5dc3_xl.jpg', '2022-01-31T09:00:00Z', 'Lorem Ipsum')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_news, News))

        return super().setUp()

if __name__ == '__main__':
    unittest.main()