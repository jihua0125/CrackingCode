import unittest
from collections import Counter

def check_palindrome_permutation(str_input):

    str_stripped=str_input.replace(' ','').lower()

    counter=Counter()
    for c in str_stripped:
        counter[c]+=1

    odd=1
    for key,value in counter.iteritems():
        if value%2 !=0:
            odd-=1

    if odd<0:
        return False
    else:
        return True

class Test(unittest.TestCase):

    dataT=[('Tact Coa'), ('jhsabckuj ahjsbckj'), ('Able was I ere I saw Elba'), ('no x in nixon'), ('azAZ')]
    dataF=[('So patient a nurse to nurse a patient so'), ('Random Words'), ('Not a Palindrome')]

    def test_pp(self):

        ## check true
        for str_test in self.dataT:
            actual=check_palindrome_permutation(str_test)
            self.assertTrue(actual)

        for str_test in self.dataF:
            actual=check_palindrome_permutation(str_test)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
