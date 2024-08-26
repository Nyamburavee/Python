import qrcode
 
data = 'You are Aweome'

try:
    img = qrcode.make(data)
    img.save('C:/Users/ADMIN/Documents/Python/new/myqr.png')
    print('Successful!')
except Exception as e:
    print(f'Error: {e}')

