import unittest
from api.slack_listener import user_registered_event


# isn't working
class MyTestCase(unittest.TestCase):
    def test_something(self, user: str):
        self.assertEqual(user_registered_event(user=user), f"{user} has registered with email address "
                                                                 f"Please spam this person incessantly.")


if __name__ == '__main__':
    unittest.main()
