import unittest

class CodingChallenge:

    def main(self):
        self.sumOfNumbers()

    def sumOfNumbers(self, x, y):

        try:



        except:
            print("Please enter only numbers.")

        result =
        print(result)

class CodingChallengeTest(unittest.TestCase):
    CC = CodingChallenge()

    def testProb1(self):
        sampleInput1 = 3
        sampleInput2 = 2

        actualValue = self.CC.sumOfNumbers(sampleInput1, sampleInput2)
        expectedValue = 5

        self.assertEqual(actualValue, expectedValue)
        print("test 1 completed: actual value is " + str(actualValue) + " and expected value is " + str(expectedValue))

if __name__ == '__main__':
    # unittest.main()
    C = CodingChallenge
    C.main()


