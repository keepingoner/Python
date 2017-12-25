#coding:utf8

def qsort(seq):
    
    if seq == []:
        return []
    else:
        zhong = seq[0]
    
        les = qsort([x for x in seq[1:] if x<zhong])
      
        
        mas = qsort([x for x in seq[1:] if x>=zhong])
      
        
        return les+[zhong]+mas

if __name__ == '__main__':

    seq = [1,5,6,9,161,31,31,531,841]
    print(qsort(seq))

    
