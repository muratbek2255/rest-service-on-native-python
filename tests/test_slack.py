import unittest
from api.slack_listener import post_slack_message


# isn't working
class MyTestCase(unittest.TestCase):
    def test_something(self, user: str):
        channel = "sales"
        msg = "yes baby"
        self.assertEqual(post_slack_message(channel, msg), f"{channel}, {msg}")


if __name__ == '__main__':
    unittest.main()
