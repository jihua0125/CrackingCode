import unittest


def string_compression(str_input):
    str_compressed=''
    prev=''
    num_cur=0

    for c in str_input:
        if prev=='':
            prev=c
            num_cur+=1
        else:
            if c!=prev:
                str_compressed=str_compressed+prev+str(num_cur)
                prev=c
                num_cur=1
            else:
                num_cur+=1

    str_compressed=str_compressed+prev+str(num_cur) ##adding the last character

    if len(str_compressed)<len(str_input):
        return str_compressed
    else:
        return str_input




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef'),
        ('abababababab','abababababab'),
        ('aaaaaaaaaa','a10')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
