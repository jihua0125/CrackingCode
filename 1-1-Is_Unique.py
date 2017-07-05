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

if __name__ == "__main__":
    print unique('1234')
    print unique('11234%^&')
