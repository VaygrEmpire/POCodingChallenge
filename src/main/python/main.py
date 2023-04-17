import unittest

class CodingChallenge:

    def main(self):

        print(self.getInput())

    def getInput(self):
        try:
            inputNum = int(input("Please enter the number: "))

            if (inputNum != None):
                print("number results in: ", self.fizz_buzz(inputNum))

        except Exception:
            print("Please enter only numbers.")
            self.getInput()

    # Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

    # If the number is a multiple of 3 the output should be "Fizz".
    # If the number given is a multiple of 5, the output should be "Buzz".
    # If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
    # If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
    # The output should always be a string even if it is not a multiple of 3 or 5.

    # Examples

    # fizz_buzz(3) ➞ "Fizz"
    # fizz_buzz(5) ➞ "Buzz"
    # fizz_buzz(15) ➞ "FizzBuzz"
    # fizz_buzz(4) ➞ "4"

    # Notes
    # Try to be precise with how you spell things and where you put the capital letters.
    def fizz_buzz(self, num):

        if (num % 3 != 0 and num % 5 != 0):
            result = str(num)
            return result

        if (num % 3 == 0 and num % 5 != 0):
            result = "Fizz"
            return result

        if (num % 5 == 0 and num % 3 != 0):
            result = "Buzz"
            return result

        if (num % 3 == 0 and num % 5 == 0):
            result = "FizzBuzz"
            return result

class CodingChallengeTest(unittest.TestCase):
    CC = CodingChallenge()

    def testProb1(self):
        sampleInput1 = 3
        actualValue = self.CC.fizz_buzz(sampleInput1)
        expectedValue = "Fizz"
        self.assertEqual(actualValue, expectedValue)
        print("test 1 completed: actual value is " + str(actualValue) + " and expected value is " + str(expectedValue))

        sampleInput2 = 5
        actualValue = self.CC.fizz_buzz(sampleInput2)
        expectedValue = "Buzz"
        self.assertEqual(actualValue, expectedValue)
        print("test 1 completed: actual value is " + str(actualValue) + " and expected value is " + str(expectedValue))

        sampleInput3 = 15
        actualValue = self.CC.fizz_buzz(sampleInput3)
        expectedValue = "FizzBuzz"
        self.assertEqual(actualValue, expectedValue)
        print("test 1 completed: actual value is " + str(actualValue) + " and expected value is " + str(expectedValue))

        sampleInput4 = 4
        actualValue = self.CC.fizz_buzz(sampleInput4)
        expectedValue = "4"
        self.assertEqual(actualValue, expectedValue)
        print("test 1 completed: actual value is " + str(actualValue) + " and expected value is " + str(expectedValue))

if __name__ == '__main__':
    # unittest.main()
    C = CodingChallenge()
    C.main()


