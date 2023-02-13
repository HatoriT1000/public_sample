import numpy as np
from sympy import *
from scipy.linalg import lu_factor, lu_solve

N=int(input("n元ヒルベルト行列生成 n="))

#行列サイズを受け取り，ヒルベルト行列AとそのベクトルBを生成する関数を定義
def hilbelt(N):
    a_mat,b_mat=[],[]
    #列の生成ループ
    for i in range(N):
        #リスト内包表記による行の生成ループ
        a_temp = [Rational(1,i+j+1) for j in range(N)]
        a_mat.append(a_temp)
        b_mat.append(sum(a_mat[i]))
    a_box, b_box = np.matrix(a_mat), np.array(b_mat)
    return a_box, b_box

#入力数値Nを引数として関数の実行
hilbelt_A,hilbec_B = hilbelt(N)
print(f'\n hilbelt_A = \n {hilbelt_A} \n \n hilbec_B = \n{hilbec_B}')

LU, pivot = lu_factor(hilbelt_A)
#LU分解結果は，かさばるのでデフォではコメントアウトしている。
#print("\n pivot = ",pivot)
#print(" LU = ",LU)

#前進後退代入により，解を算出
#解は本来、1になるはずだが....。
x = lu_solve((LU,pivot),hilbec_B)
print("\n x = \n", x)