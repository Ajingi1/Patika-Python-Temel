# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
# Elemanları birden çok katmanlı listelerden ([[3],2] gibi) 
# oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]

def main():
    # output = []
    input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    
    print(list_remover(input_list))

def list_remover(lst):
    output = []
    for e in lst:
        if isinstance(e, list):
            output.extend(list_remover(e))
        else:
            output.append(e)
    return output

if __name__ == "__main__":
    main()
