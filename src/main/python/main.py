import numpy
import unittest
import re


class CodingChallenge:

    sampleInput1 = [[1, 2, 3], [10, 15, 5], [100, 999, 500]]    
    sampleInput2 = "ab1231da"

    def main(self):
        for number in self.prob1(self.sampleInput1):
            print(number)
        print(" ")
        print(self.prob2(self.sampleInput2))

    # Write a program that accepts sets of three numbers and prints the second - maximum number among the three.
    def prob1(self, a):
        for i in a:
            i.sort()
            yield i[1]


    # Given an alphanumeric string made up of digits and lower case Latin characters only, find the sum of all the
    # digit characters in the string.
    def prob2(self, s):
        sum = 0
        for i in s:
            regex = re.findall(r"[0-9]", i)
            for a in regex:
                sum += int(a)
        return sum


class CodingChallengeTest(unittest.TestCase):
    CC = CodingChallenge()

    def testProb1(self):
        sampleInput = [[1, 2, 3], [10, 15, 5], [100, 999, 500]]

        actualValue = list(self.CC.prob1(sampleInput))
        expectedValue = [2, 10, 500]

        self.assertEqual(actualValue, expectedValue)
        print("test 1 completed: actual value is " + str(actualValue) + " and expected value is " + str(expectedValue))        

    def testProb2(self):
        sampleInput2 = "ab1231da"

        actualValue = self.CC.prob2(sampleInput2)
        expectedValue = 7

        self.assertEqual(actualValue, expectedValue)
        print("test 2 completed: actual value is " + str(actualValue) + " and expected value is " + str(expectedValue))        

if __name__ == '__main__':
    unittest.main()
    # CodingChallengeTest.main()
    # C = CodingChallenge()
    # C.main()
