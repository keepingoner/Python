import bisect

def grade(score,gr=[60,70,80,90],grades='fecba'):
    i = bisect.bisect(gr,score)
    return grades[i]

if __name__=='__main__':
    print(grade(98))
    print(grade(88))
    print(grade(78))
    print(grade(68))
    print(grade(58))


