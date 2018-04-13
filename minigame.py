#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minigame.py
#  
#  Copyright 2018 20181bsi0121 <20181bsi0121@SR6192>
#  
# 

def main():

    a = 0; b=0; c=0;

    a = int(input())
    b = int(input())
    c = int(input())

    falta = '';
    cont = 1;

    while a >= 0:
      
        print(cont,'º) JOGO: (',a,', ',b,',',c,')')
        
        if c<=100:
            if a == b:
                falta = c
            elif b == c:
                falta = a
            elif a == c:
                falta = b
            else:
                falta = 'Intederminado'    
                
            print('Próxima Carta: ',falta)
        else:
            print('O valor C não pode ser maior que 100')

        print('----------------------------------')
        
        cont = cont +1 

        a = int(input())
        if a >= 0:
            b = int(input())
            c = int(input())

    return 0

if __name__ == '__main__':
	main()
