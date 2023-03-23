import unittest

class TriangleArea:

    def main(self):
        try:
            _base = int(input("Please enter base of triangle: "))
            _height = int(input("Please enter height of triangle: "))
            print(f"Area of triangle is: {self.tri_area(_base, _height)}")

        except:
            print("Please enter in a numerical format: ")
            return

        # Write a function that takes the base and height of a triangle and return its area.
        # Examples
        # tri_area(3, 2) ➞ 3
        # tri_area(7, 4) ➞ 14
        # tri_area(10, 10) ➞ 50

        # Notes:
        # The area of a triangle is: (base * height) / 2
        # Don't forget to return the result.

    def tri_area(self, base, height):
        area = int((base*height)/2)
        return area

class TriangleAreaTest(unittest.TestCase):
    TA = TriangleArea()

    def testProb1(self):
        sampleInput1 = 3
        sampleInput2 = 2
        sampleInput3 = 7
        sampleInput4 = 4
        sampleInput5 = 10
        sampleInput6 = 10

        actualValue1 = self.TA.tri_area(sampleInput1, sampleInput2)
        expectedValue1 = 3

        actualValue2 = self.TA.tri_area(sampleInput3, sampleInput4)
        expectedValue2 = 14

        actualValue3 = self.TA.tri_area(sampleInput5, sampleInput6)
        expectedValue3 = 50

        self.assertEqual(actualValue1, expectedValue1)
        print("test 1 completed: actual value is " + str(actualValue1) + " and expected value is " + str(expectedValue1))
        self.assertEqual(actualValue2, expectedValue2)
        print("test 2 completed: actual value is " + str(actualValue2) + " and expected value is " + str(expectedValue2))
        self.assertEqual(actualValue3, expectedValue3)
        print("test 2 completed: actual value is " + str(actualValue3) + " and expected value is " + str(expectedValue3))

if __name__ == '__main__':
    # unittest.main()
    TA = TriangleArea()
    TA.main()


