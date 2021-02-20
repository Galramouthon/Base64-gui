## 한글로 변환 ##
import base64
h = '테스트'
# h = '😃'
s = h.encode('utf-8')
a = base64.b64encode(s)
print(a)



# ----------- ##

# sitename_base64_str  = '7JWI64WV7ZWY7IS47JqUIOuFuOustO2YhOyeheuLiOuLpCDil4Eg4peAIOKWtyDilrYg4pmkIOKZoCDimaEg4pmlIOKZpyDimaMg4oqZIOKXiCDilqMg4peQIOKXkSDilpIg4pakIOKWpSDilqgg4panIOKWpiDilqkg4pmoIOKYjyDimI4g4picIOKYniDCtiDigKAg4oChIOKGlSDihpcg4oaZIOKGliDihpgg4pmtIOKZqSA='
# sitename_bytes = base64.b64decode(sitename_base64_str )
# sitename = sitename_bytes.decode('utf-8')

# print(sitename)

