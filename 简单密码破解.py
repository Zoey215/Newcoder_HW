while True:
    try:
        psw = []
        old = input()
        for i in old:
            if ord(i) in range(ord('A'), ord('Z')):
                psw.append(chr(ord(i)+33))
            elif i in 'Z':
                psw.append('a')
            elif i in 'abc':
                psw.append('2')
            elif i in 'def':
                psw.append('3')
            elif i in 'ghi':
                psw.append('4')
            elif i in 'jkl':
                psw.append('5')
            elif i in 'mno':
                psw.append('6')
            elif i in 'pqrs':
                psw.append('7')
            elif i in 'tuv':
                psw.append('8')
            elif i in 'wxyz':
                psw.append('9')
            else:
                psw.append(i)
        print(''.join(psw))
    except:
        break




