import unittest

## define function
def unique(input_str):
    if len(input_str)>128: ## more than total number of ASCII characters
        return False

    char_set=[False for _ in range(128)]

    for i in range(len(input_str)):
        key=ord(input_str[i])
        if char_set[key]==True:
            return False
        else:
            char_set[key]=True

    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
