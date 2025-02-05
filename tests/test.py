from trialapp.index import guess
import random
import unittest

class testingfunction(unittest.TestCase):

    def testcase(self):
        ans = guess(50, fix = 50)
        self.assertEqual(ans, "You have guessed it right!")

    def testcase2(self):
        ans = guess(60, fix = 50)
        self.assertEqual(ans, "You have guessed it wrong! The number was 50")

    def testcase3(self):
        ans = guess(101, fix = 50)
        self.assertEqual(ans, "You have guessed it wrong! The number was 50")

    def testcase4(self):
        fix = random.randint(1, 100)
        op =random.randint(1, 100)
        ans = guess(op, fix = fix)
        if op == fix:
            self.assertEqual(ans, "You have guessed it right!")
        else:
            self.assertEqual(ans, f"You have guessed it wrong! The number was {fix}")
            
if __name__ == '__main__':
    unittest.main()