## define function
def unique(input_str):
    if len(input_str)>128: ## more than total number of ASCII characters
        return False

    char_dict={}
    for i in range(len(input_str)):
        if char_dict.get(input_str[i],None)!=None:
            return False
        else:
            char_dict[input_str[i]]=1

    return True

if __name__ == "__main__":
    print unique('1234')
    print unique('11234%^&')
