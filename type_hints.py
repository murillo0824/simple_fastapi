price: int = 100.1
tax: float = 10

def calc_price_including_tax(price: int, tax:float) -> int:
  return int(price*tax)

if __name__ == "__main__":
  print(f"{calc_price_including_tax(price=price, tax=tax)} 円")


#型ヒントはあくまで注釈なので、エラーは出ない
#変数のコメントアウトと同じ強制力
#fastAPIではこのアノテーション情報が重要になる
# また、Mypyなどのライブラリも存在する


