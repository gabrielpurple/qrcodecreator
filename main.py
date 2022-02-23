import qrcode
import io

#criar qrcode e inserir link
img = qrcode.make('suaurl')
#inserir tipo de qrcode
print(type(img))
#tamanho
print(img.size)

img.save('zap.png')