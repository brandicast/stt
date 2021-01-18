from simhash import Simhash
from CHlikelihood.likelihood import Likelihood

# 求兩篇文章相似度
def similarity(text1,text2):
    """
    :param tex1: 文本1
    :param text2: 文本2
    :return: 返回兩篇文章的相似度
    """
    aa_simhash = Simhash(text1)
    bb_simhash = Simhash(text2)

    # 打印simhash值二進制
    #print(bin(aa_simhash.value))
    #print(bin(bb_simhash.value))

    # 漢明距離
    #distince = aa_simhash.distance(bb_simhash)
    #print(distince)

    a = float(aa_simhash.value)
    b = float(bb_simhash.value)

    if a > b:
        similar= b / a
    else:
        similar= a / b

    return similar

def likelihood (text1, text2):
    a = Likelihood()
    return a.likelihood(text1, text2)