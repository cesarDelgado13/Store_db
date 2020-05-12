from controller.controller import Controller

c = Controller()
c.start() 
    


#from model.model import Model

#m = Model()

#m.create_client('Ivan','Delgado', 'Alfaro', 'Santuario', '102',None, 'Rinconada' ,'76000','ci.delgado@ugto.mx', '4641678417')
#m.create_client('Atziri','Santarrosa', 'Rangel', 'Obispos', '210',None, 'Expiatorio' ,'76000','a.rangel@ugto.mx', '4642347429')
#m.create_client('Michell','Zavala', 'Andrade', 'San juan', '217',12, 'Guanajuato' ,'36000','m.zavala@ugto.mx', '4644897539')

#m.create_client('Ivan','Delgado', 'Alfaro', 'Santuario', '102',None, 'Rinconada' ,'76000','ci.delgado@ugto.mx', '4641678417')

#m.delete_client(4)
#client = m.read_all_clients()
#print(client)

#m.create_product('jabon', 'la corona', 'jabon de 1kg', 35)
#m.create_product('Leche', 'Lala', 'Presentacion Tetrapack', 22.5)
#m.create_product('Clorox 1L', 'Clorox', 'Limpiador Liquido', 37.5)

#fields = ('p_price = %s',)
#vals = (20.5, 3)
#m.delete_product(3)
#products = m.read_all_products ()
#print(products) 

#m.create_zip('76000', 'Queretaro','Queretaro')
#m.create_zip('76001', 'Queretaro','Queretaro')
#m.create_zip('36000', 'Celaya','Guanajuato')

#data = m.read_all_zips()

#m.update_zips('76001', 'San Juan del rio','')
#data = m.read_all_zips()
#print(data)

#m.update_zips('76001','','Sonora')
#data = m.read_all_zips()
#print(data)

#data = m.read_zips_city('Queretaro')
#print(data)

#m.delete_zip('76001')
#data = m.read_all_zips()
#print(data)
#print(data)

#m.close_db()

#m.create_client('Cesar','Delgado', 'Alfaro', 'Santuario', '102',None, 'Rinconada' ,'36760','ci.delgadolafaro@ugto.mx', '4641678417')
#m.create_client('Atziri','Santarrosa', 'Rangel', 'Obispos', '210',None, 'Expiatorio' ,'36765','a.rangel@ugto.mx', '4642347429')
#m.create_client('Michell','Zavala', 'Andrade', 'San juan', '217',12, 'Guanajuato' ,'36780','m.zavala@ugto.mx', '4644897539')

#client = m.read_all_clients()
#print(client)
#m.delete_client(5)
#client = m.read_all_clients()
#print(client)
#m.close_db()
#client = m.read_all_clients()
#print(client)

#client = m.read_clients_zip('36760')
#print(client)

#fields = ('c_phone = %s',)
#vals = (8712864242,5)
#m.update_client(fields, vals)
#client = m.read_all_clients()
#print(client)

#m.delete_client(6)
#client = m.read_all_clients()
#print(client)

#Tener cuidado con los zips porque al ser llaves foraneas
#si se registra un zip que no esta dado de alta marca un error y no agrega correctamente

#m.create_product('jabon', 'la corona', 'jabon de 1kg', 35)
#m.create_product('Leche', 'Lala', 'Presentacion Tetrapack', 22.5)
#m.create_product('Clorox 1L', 'Clorox', 'Limpiador Liquido', 37.5)

#products = m.read_products_price_range(30,40)
#print(products)

#products = m.read_a_product(13)
#print(products)

#products = m.read_all_products()
#print(products)

#fields = ('p_price = %s',)
#vals = (20.5,9)
#products = m.update_product(fields, vals)
#print(products)

#products = m.read_a_product(13)
#print(products)

#m.delete_product(13)
#products = m.read_all_products()
#print(products)
#m.create_zip('76000', 'Queretaro','Queretaro')
#m.create_zip('76001', 'Queretaro','Queretaro')
#m.create_zip('36000', 'Celaya','Guanajuato')


#data = m.read_all_zips()
#print(data)

#m.update_zips('76001', 'San Juan del rio','')
#data = m.read_all_zips()
#print(data)

#m.update_zips('76001','','Sonora')
#data = m.read_all_zips()
#print(data)

#data = m.read_zips_city('Queretaro')
#print(data)

#m.delete_zip('76001')
#data = m.read_all_zips()
#print(data)

#m.close_db()