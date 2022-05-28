def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]
    
    # ここから記述
    
    if len(array) > 1:
        pivot_count = 0  # 基準値と同じものの個数
        left =[] #分割後左の行列
        right = [] #分割後右の行列
    
        for i in array:
            #基準値より小さいものは左へ
            if i < pivot:
                left.append(i)
            
            #基準値より大きいものは右へ
            elif i > pivot:
                right.append(i)
                
            #基準値と同じ大きさの個数 
            else:
                pivot_count += 1
        
        #各配列の長さが1以上の場合，再帰で各グループに対して処理を行う
    if len(left) > 1:
        left = sort(left)
    if len(right) >1:
        right = sort(right)
        
    return left + [pivot] * pivot_count + right


    # ここまで記述

if __name__ == '__main__':
    main()



