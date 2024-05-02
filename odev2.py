# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

def main():
    input_list = [[1, 2], [3, 4], [5, 6, 7]]
    print(list_reverser(input_list))

def list_reverser(lst):
    output = lst
    for items in output:
        if isinstance(items, list):
            items.reverse()
    output.reverse()
    return output


if __name__ == "__main__":
    main()