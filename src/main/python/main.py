import unittest

class CodingChallenge:

    def main(self):

        try:
            a = int(input("Please enter first number: "))
            b = int(input("Please enter second number: "))

            if (a != None or b != None):
                print("Sum of Numbers are: ", self.sumOfNumbers(a, b))
        except:
            print("Please enter only numbers.")



    # Create a function that takes two numbers as arguments and returns their sum.
    def sumOfNumbers(self, x, y):
        result = x+y
        return result

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
    C = CodingChallenge()
    C.main()


