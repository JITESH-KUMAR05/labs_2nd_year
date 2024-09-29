def combine_strings(s1, s2):  
    def middle_char(s):  
        length = len(s)  
        if length == 0:
            return ''
        elif length % 2 == 0:  
            return s[length//2 - 1]  
        else:  
            return s[length//2]  

    first_s1 = s1[0] if len(s1) > 0 else ''  
    middle_s1 = middle_char(s1)  
    last_s1 = s1[-1] if len(s1) > 0 else ''  

    first_s2 = s2[0] if len(s2) > 0 else ''  
    middle_s2 = middle_char(s2)  
    last_s2 = s2[-1] if len(s2) > 0 else ''  

    return first_s1 + first_s2 + middle_s1 + middle_s2 + last_s1 + last_s2  

def main():  
    s1 = input()  
    s2 = input()  
    result = combine_strings(s1, s2)  
    print(result)

if __name__ == "__main__":
    main()