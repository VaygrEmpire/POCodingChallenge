import unittest

class CodingChallenge:

    def main(self):

        try:
            a = int(input("Please enter length: "))
            b = int(input("Please enter width: "))

            if (a != None or b != None):
                print("perimeter of rectangle is: ", self.find_perimeter(a, b))
        except:
            print("Please enter only numbers.")



    # Create a function that takes length and width and finds the perimeter of a rectangle.
    def find_perimeter(self, length, width):
        result = (length*2)+(width*2)
        return result

class CodingChallengeTest(unittest.TestCase):
    CC = CodingChallenge()

    def testProb1(self):
        sampleInput1 = 6
        sampleInput2 = 7

        actualValue = self.CC.find_perimeter(sampleInput1, sampleInput2)
        expectedValue = 26

        self.assertEqual(actualValue, expectedValue)
        print("test 1 completed: actual value is " + str(actualValue) + " and expected value is " + str(expectedValue))

if __name__ == '__main__':
    # unittest.main()
    C = CodingChallenge()
    C.main()


