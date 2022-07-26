import os,random,rich,json,requests,time

####----- buat random ua -----####
uas = ['ua,ua']

####----- menu -----####
def menu():
  os.system('clear')
  print(f'{ua}')  
  print(f'{ip}')
  print(f'{nama}')
  print('')
  print('[1] spam olx')
  print('[2] spam pizza')
  as = input('pilih : ')
  if as in ['1']:
    olx()
   elif as in ['2']:
    ## head pizza api
    
####----- lagu -----#####
def lagu():
  os.system('clear')
  print('musik 1')
  print('musik 2')
  shelly = input('pilih : ')
  if shelly in ['1']:
    os.system('play-audio lagu.mp3')
    menu()
  elif shelly in ['2']:
    os.system('play-audio lagu.mp3')
    menu()

 ####----- olx jangan di ubah headers nanti error -----####
def olx():
  print('Contoh 08xxx')
  z = input('Nomor : ')
  zex = int(input('Limit : ')
  head = {
    
    
           
  
  
