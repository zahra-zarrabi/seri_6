
def read_from_database():
    try:
        products=[]
        f=open('f:\python/database.CSV')
        big_text=f.read()
        product_list=big_text.split('\n')
        for i in range(len(product_list)):
            info=product_list[i].split(',')
            products.append({'id':info[0],'name':info[1],'price':info[2],'count':info[3]})
    except Exception as e:
        products = []
        print(e)
    return products

def my_add():
    id = input("enter id: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    for product in products:
        if product['id']==id or product['name']==name:
            print('This product has already been added to the database.')
            break
    else:
        products.append({'id':id,'name':name,'price':price,'count':count})
        print('This product was added to the database.')



def my_search():
    user_input=input('enter a id or name to search:')
    for product in products:
        if product['id']==user_input or product['name']==user_input:
            print(product)
            break
    else:
        print('not found')


def my_edit():
    user_input=input('enter a id or name to edit')
    for product in products:
        if product['id']==user_input or product['name']==user_input:
            print(product)
            name = input("enter name: ")
            price = input("enter price: ")
            count = input("enter count: ")
            products.remove(product)
            products.append({'id': product['id'], 'name': name, 'price': price, 'count': count})
            print('Product information editing was done')
            break
    else:
        print('This product is not available in the database.')



def my_remove():
    user_input=input('enter a id or name to remove')
    for product in products:
        if product['id']==user_input or product['name']==user_input:
            print(product)
            products.remove(product)

def buy(products):
    p=int(input('tedad product'))
    u,t =0,0
    factor = []
    for m in range(p):
        user_input = input('enter a id kala to buy: ')
        flage = False

        for product in products:
            if product['id'] == user_input:
                flag = True
                print(product)
                u_c=int(input('count'))
                if u_c > int(product['count']):
                    print('You imported a large number of commodity.')
                    break
                else:
                    produc=int(product['count'])-int(u_c)
                    print('done')
                    products.remove(product)
                    products.append({'id': product['id'], 'name':product['name'], 'price':product['price'], 'count':str(produc)})
                    factor.append({'id': product['id'], 'name':product['name'], 'price':product['price'], 'count': str(produc)})
                    break

        if flag is False:
            print('There is no product with this code.')
        i += 1
        u+=u_c
        t+=u_c*int(product['price'])

    print('customer factor', factor)
    print('number of commodity Buy',u)
    print('Total prices',t)




def show_all(products):
    for product in products:
        print(product)


def my_exit():
    f = open('f:\python/database.CSV', 'w')
    for product in products:
        f.write(str(product['id'] + ',' + product['name'] + ',' + product['price'] + ',' + product['count'] + '\n'))
    exit()




def show_menu():
    print('welcome to zari store\n1 add new product\n2 search\n3 edit\n4 remove\n5 buy\n6 show all\n7 exit')


products=read_from_database()
while True:
    show_menu()
    choice=input('enter your choice: ')
    if choice=='1':
        my_add()
    elif choice =='2':
        my_search()
    elif choice=='3':
        my_edit()
    elif choice=='4':
        my_remove()
    elif choice=='5':
        buy(products)
    elif choice=='6':
        show_all(products)
    elif choice=='7':
        my_exit()


