import unittest

class CodingChallenge:

    a = 4
    b = "4"
    c = 29348
    def main(self):

        try:

            print(f"input a is {self.a}")
            print(f'input b is "{self.b}"\n')

            if (self.a != None or self.c != None):
                print(f'convert int to str is: "{self.int_to_str(self.a)}"')
                print(f'convert int to str is: "{self.int_to_str(self.c)}"')
            if (self.b != None):
                print(f"convert str to int is: {self.str_to_int(self.b)}\n")

            self.printOutput(str(self.a), "s", 0)
            self.printOutput(str(self.b), "s", 1)
            self.printOutput(int(self.a), "i", 0)
            self.printOutput(int(self.b), "i", 1)

        except:
            print("Try again")
            return

    # Python got drunk and the built-in functions str() and int() are acting odd:
    # str(4) ➞ 4
    # str("4") ➞ 4
    # int("4") ➞ "4"
    # int(4) ➞ "4"
    #
    # You need to create two functions to substitute str() and int().
    # A function called int_to_str() that converts integers into strings and a function called str_to_int() that converts strings into integers.

    # Examples:
    # int_to_str(4) ➞ "4"
    # str_to_int("4") ➞ 4
    # int_to_str(29348) ➞ "29348"

    def int_to_str(self, x):
        result = "{}".format(x)
        print("type of int_to_str output is: ", type(result))
        return result

    def str_to_int(self, x):
        result = 0

        for i in x:
            result = result * 10 + (ord(i) - 48)

        print("type of str_to_int output is: ", type(result))
        return result

    # de-drunk Python
    def str(self, x):
        return x.__str__()

    def int(self, x):
        return x.__int__()

    def printOutput(self, function, s, i):

        if (s == "s"):
            if (i == 0):
                print(f'de-drunk: output of str({self.a}) is "{function}" and type of str(a) output is {type(function)}')
            elif (i == 1):
                print(f'de-drunk: output of str("{self.b}") is "{function}" and type of str(b) output is {type(function)}')
        else:
            if (i == 0):
                print(f"de-drunk: output of int({self.a}) is {function} and type of int(a) output is {type(function)}")
            elif (i == 1):
                print(f'de-drunk: output of int("{self.b}") is {function} and type of int(b) output is {type(function)}')

class CodingChallengeTest(unittest.TestCase):
    CC = CodingChallenge()

    def testProb1(self):
        sampleInput1 = 4
        sampleInput2 = '4'

        actualValue1 = self.CC.int_to_str(sampleInput1)
        expectedValue1 = '4'

        actualValue2 = self.CC.str_to_int(sampleInput2)
        expectedValue2 = 4

        self.assertEqual(actualValue1, expectedValue1)
        print("test 1 completed: actual value is " + str(actualValue1) + " and expected value is " + str(expectedValue1))
        self.assertEqual(actualValue2, expectedValue2)
        print("test 2 completed: actual value is " + str(actualValue2) + " and expected value is " + str(expectedValue2))

if __name__ == '__main__':
    # unittest.main()
    C = CodingChallenge()
    C.main()


