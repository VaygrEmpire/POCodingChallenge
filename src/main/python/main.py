import unittest

class CodingChallenge:

    def main(self):
        self.largestGap()

    def largestGap(self):
        lst = []

        try:
            while True:
                lst.append(int(input("Enter number of elements: ")))

        except:
            print("Please enter only numbers.")

        result = [x-lst[i-1] for i, x in enumerate(lst)][1:]
        print(result)

if __name__ == '__main__':
    C = CodingChallenge
    C.main()


