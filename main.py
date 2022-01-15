from typing import Optional,List
from fastapi import FastAPI
from pydantic import BaseModel, Field
# バリデーション系のライブラリは基本的に、pydantic からimport する。
# pydantic のバリデーション機能とfastapi を組み合わせることで、とても簡単にエラー処理まで、対応できる。



# post method リクエストボディ
# request body have to send with json data 
class Item(BaseModel):
  name: str = Field(min_length=4, max_length=12)
  description: Optional[str]= None
  price: int
  tax: Optional[float] = None
#どのようなデータがたで入れるかを定義、
#type script の　interface のような形


class ShopInfo(BaseModel):
  name: str
  locacion: str


class Data(BaseModel):
  shop_info: Optional[ShopInfo]
  items: List[Item]

#データが入れ子になる場合は、それぞれのクラスを定義して、移動してあげる。

app = FastAPI()
# instance the fastapi to the app 

@app.post("/item/")
async def create_item(item: Item):
  return{"message": f"{item.name} is {int(item.price * item.tax)} with tax in"}

@app.post("/shops/")
async def shops(shop: Data):
  return{"data": shop}



# routing the app 
@app.get("/") #デコレーターの直下に配置した処理を実行する
async def index(): #async を頭につけることで、非同期処理にできる。　async function と同じ感じ
  return {"message": "Hellow world"}

@app.get("/hello") #デコレーターの直下に配置した処理を実行する
async def index(): #async を頭につけることで、非同期処理にできる。　async function と同じ感じ
  return {"message": "Hellow world"}




# パスが被る場合は上に記述されたものが優先。
@app.get("/countries/japan")
async def japan():
  return{"message":"This is japan"}

@app.get("/countries/{country_name}")
# path param を使用することで、引数としてパスを使用することができる。
async def country(country_name: int):
  country_list = ["america","India","Japan","Brasil"]
  if len(country_list) > country_name:
    return {"country":country_list[country_name]}
  
  else:
    return{"err":"the country no doesn't exists"}
# python 型ひんとを利用することで、パスパラメーターで受け取る値を限定できる。





# query params 
# パスパラメータがない状態で、関数の引数の値を入れるとクエリとして認識される。
# path params と　query params　両方使用することも可能
# 必須かどうかの場合は型を　Optional[kata] = None で表記する
@app.get("/query/")
async def query(query: str = 'default', country_no:Optional[str] = None):
  return {"query":query, "country_no": country_no}




