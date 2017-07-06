import unittest
from collections import Counter

## define one_away function, input: 2 strings, output: boolean value
def one_away(str_input):

    str1=str_input[0]
    str2=str_input[1]

    if (len(str1)+1<len(str2)) or (len(str2)<len(str1)-1):
        return False

    counter=[0 for _ in range(128)]
    #counter=Counter()

    for i in range(len(str1)):
        counter[ord(str1[i])]+=1

    for i in range(len(str2)):
        counter[ord(str2[i])]-=1

    sum=0
    for i in range(len(counter)):
        sum+=abs(counter[i])

    if sum>2:
        return False
    else:
        return True


class Test(unittest.TestCase):
    dataT=[(['bale','pale']),(['bale','bal']),(['bale','bale%'])]
    dataF=[(['bale','kali']),(['apple','app']),(['peach','ba  $$'])]

    def test_one_away(self):
        # true check
        for test_string in self.dataT:
            #print test_string
            actual = one_away(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = one_away(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
