def minion_game(string):
    vowels= ['A','E','I','O','U']
    KEVIN,STUART=0,0
    for i,val in enumerate(string):
        if val in vowels: KEVIN+=len(string)-i
        else: STUART+=len(string)-i
        
    if KEVIN>STUART:
        return print(f"Kevin {KEVIN}")
    elif KEVIN<STUART:
        return print(f"Stuart {STUART}")
    else:
        return print('Draw')

minion_game('BANANA')

# if __name__ == '__main__':
    # s = input()
    # minion_game(s)