import unittest

class CodingChallenge:

    def main(self):
        self.sumOfNumbers()

    def sumOfNumbers(self, x, y):
        lst = []

        try:
            while True:
                lst.append(int(input("Enter number of elements: ")))

        except:
            print("Please enter only numbers.")

        result = [x-lst[i-1] for i, x in enumerate(lst)][1:]
        print(result)

class CodingChallengeTest(unittest.TestCase):
    CC = CodingChallenge()



if __name__ == '__main__':
    # unittest.main()
    C = CodingChallenge
    C.main()


