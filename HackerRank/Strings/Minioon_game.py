def minion_game(string):
    vowels="AEIOU"
    
    stuart=0
    kelvin=0
    for i in range(0,len(string)):
        if string[i] in vowels:
            kelvin += len(string)-i
            
        else:
            stuart += len(string)-i
            
    if stuart>kelvin:
        print(f"Stuart {stuart}")
        
    elif kelvin>stuart:
        print(f"Kelvin {kelvin}")
    
    else:
        print("Game Draw!")
if __name__ == '__main__':
    s = input()
    minion_game(s)