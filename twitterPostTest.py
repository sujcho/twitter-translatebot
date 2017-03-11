import unittest,sqlite3,random


from twitterPost import TwitterPost


class TwitterPostTest (unittest.TestCase) :

    def setUp(self):
        self.tweet = TwitterPost()


    #test successful retrieve
    def test_sqliteRetrieveSuccess(self):
        print("\nRunning sqllite Data Retrieve Success test")
        self.conn = sqlite3.connect(":memory:")

        self.assertEqual(self.tweet.sqlite_retrieve('spanish').__getitem__('consumer_key'),'rcIlpeAhFKSXlzhjnWqfkS9x7')
        self.assertEqual(self.tweet.sqlite_retrieve('spanish').__getitem__('consumer_secret'),'J96cwUhHWX93TvSxO7nBpmnqz8LCGuJLNQVFWKehg1bFQRysQe')
        self.assertEqual(self.tweet.sqlite_retrieve('spanish').__getitem__('access_token'),'838080768408612868-sLc6Uo8iAbdHrJTeEd5C2pjskaitgq6')
        self.assertEqual(self.tweet.sqlite_retrieve('spanish').__getitem__('access_token_secret'),'r1lj2ZT20H0aACoxqZdIHNq6nfBoWtCNwZNFrvAB6JOMn')


    def test_sqliteRetrievFailure(self):
        print("\nRunning sqllite Data Retrieve Failure test")
        self.conn = sqlite3.connect(":memory:")
        self.assertRaisesRegexp(self.tweet.sqlite_retrieve('spanish'),'AttributeError: ''NoneType'' object has no attribute ''items''')

    def test_getapi(self):
        print("\nRunning getapi test")
        self.authcfg=self.tweet.sqlite_retrieve('spanish')
        self.apihandle = self.tweet.get_authenticated(self.authcfg)

    def test_twitterpost(self):
        print("\nRunning twitter_post test")
        self.tweet_msg = "Posting twitter test message from unit tests  "+ str(random.random())
        self.tweet.twitter_post(self.tweet_msg,"spanish")

    def test_twitterpost_failure(self):
        print("\nRunning twitter_post test failure")
        self.tweet_msg = "Posting twitter test message from unit tests  "+ str(random.random())
        self.assertRaisesRegexp(self.tweet.twitter_post(self.tweet_msg,"gibberish"),
                                "error")

if __name__ == ' __main__ ':
    unittest.main()