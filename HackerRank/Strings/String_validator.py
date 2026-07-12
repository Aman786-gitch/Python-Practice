if __name__ == '__main__':
    s = input()
    
    print(any(ch.isalnum() for ch in s))
    print(any(ch.isalpha() for ch in s))
    print(any(ch.isdigit() for ch in s))
    print(any(ch.islower() for ch in s))
    print(any(ch.isupper() for ch in s))
    
           #OR
    # alnum=False
    # alpha=False
    # digit=False
    # lower=False
    # upper=False
    
    # for i in s:
    #     if i.isalnum():
    #         alnum=True
            
    #     if i.isalpha():
    #         alpha=True
            
    #     if i.isdigit():
    #         digit=True
            
    #     if i.islower():
    #         lower=True
            
    #     if i.isupper():
    #         upper=True
            
            
    # print(alnum)
    # print(alpha)
    # print(digit)
    # print(lower)
    # print(upper)
        
         
    
