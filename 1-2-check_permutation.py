import unittest

def check_permutation(str_test):
    str_x=str_test[0]
    str_y=str_test[1]

    if len(str_x)!=len(str_y):
        return False

    check_dict={}

    for i in range(len(str_x)):
        if check_dict.get(str_x[i],None)==None:
            check_dict[str_x[i]]=1
        else:
            check_dict[str_x[i]]+=1

    for i in range(len(str_y)):
        if check_dict.get(str_y[i],None)==None:
            return False
        else:
            if check_dict[str_y[i]]<=0:
                return False
            check_dict[str_y[i]]-=1

    return True

class Test(unittest.TestCase):

    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),(['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f']),(['aaaabb','baaaaa'])]

    def test_cp(self):
        ## True check
        for test_string in self.dataT:
            actual=check_permutation(test_string)
            self.assertTrue(actual)

        ## False check
        for test_string in self.dataF:
            actual=check_permutation(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
