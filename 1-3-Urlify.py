import unittest

def urlify(str_test,str_len):

    actual_len=len(str_test)

    for i in reversed(range(str_len)):
        c=str_test[i]
        if c!=' ':
            str_test[actual_len-1]=c
            actual_len-=1
        else:
            str_test[actual_len-3:actual_len]='%20'
            actual_len-=3

    return str_test


class Test(unittest.TestCase):

    data = [(list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_url(self):

        for d in self.data:
            actual=urlify(d[0],d[1])
            #print actual
            self.assertEqual(actual,d[2])

if __name__ == "__main__":
    unittest.main()
