import unittest

class CodingChallenge:
    lst = []

    def main(self):
        self.largestGap(self.lst)

    def largestGap(self, a):

        try:
            while True:
                n = int(input("Enter length of list: "))
                for i in range(0, n):
                    self.lst.append(int(input("Enter number of elements: ")))
                break

        except:
            print("Please enter only numbers.")

        self.lst.sort()
        differencesList = [x-self.lst[i-1] for i, x in enumerate(self.lst)][1:]
        result = max(differencesList)
        return result

class CodingChallengeTest(unittest.TestCase):
    CC = CodingChallenge()

    def testProb1(self):
        sampleInput = [9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]

        actualValue = self.CC.largestGap(sampleInput)
        expectedValue = 11

        self.assertEqual(actualValue, expectedValue)
        print("test 1 completed: actual value is " + str(actualValue) + " and expected value is " + str(expectedValue))

if __name__ == '__main__':
    unittest.main()
    # C = CodingChallenge()
    # C.main()


