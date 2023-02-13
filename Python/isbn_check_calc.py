# isbnの積算したやつの総和を入れるために変数を定義
isbn_sum_number=0

# isbnとチェックデジットを入力させる(チェックデジットは最後の一桁)
isbn_num=(input("please input isbn_number >>"))
check_digit=int(input("please input check digit_number >>"))
print(f'isbn_number={isbn_num}')


# 奇数か偶数か(２で割れるかで判断)で分岐させ桁のウェイトを掛ける
# ついでにその桁のウェイトを掛けた結果を表示させてる
for i in range(len(isbn_num)):
    if i%2==0:
        tmp_num=int(isbn_num[i])*1
        isbn_sum_number+=tmp_num
        print(f'左から{i+1}桁目の積算結果は {tmp_num} ')
    
    else:
        tmp_num=int(isbn_num[i])*3
        isbn_sum_number+=tmp_num
        print(f'左から{i+1}桁目の積算結果は {tmp_num} ')

# 「モジュラス10,ウェイト1,3」に従い計算でチェックデジットを求める
clc_check_digit=10-(isbn_sum_number%10)

# 求めた結果を表示して確認する
print(f'\n積(*1,*3,...する奴)の総和は {isbn_sum_number} です')
print(f'計算により求めたチェックデジットの数は {clc_check_digit} です')

# 最後に入力したチェックデジットと計算で出したモノを比較し一致しているかどうで表示を分岐
if int(clc_check_digit)==check_digit:
    print(f'\n計算結果とチェックデジットが一致')

else:
    print(f'\n計算結果とチェックデジットが不一致')