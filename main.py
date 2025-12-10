import mysql.connector as sqcon
con_ob=sqcon.connect(host='localhost', user='root', passwd='<ENTER_YOUR_SQL_PASSWORD>', db='pracdb')

# 0. Defining a function for auto-increment of id columns
def get_next_id(table_name, id_col):
    cursor=con_ob.cursor()
    query = "select max({}) from {}".format(id_col, table_name)
    cursor.execute(query)
    max_id=cursor.fetchone()[0] # type: ignore
    if max_id is None:
        return 1
    else:
        return max_id+1 # type: ignore

# 0.1. Login Screen for domain
def login_screen(con_ob):
    cursor=con_ob.cursor()
    attempts=0
    max_attempts=5
    c2=0
    while True:
        print('''1. Proceed to login screen
2. Exit''')
        c2=int(input("Enter your choice: "))
        if c2==1:
            while attempts<max_attempts:
                user_id=int(input("Enter your User ID: "))
                password=input("Enter your password: ")
                cursor.execute("select password from domain where user_id=%s", (user_id,))
                stored_pw=cursor.fetchone()
                if stored_pw is None:
                    attempts+=1
                    print("Invalid User ID! try again")
                    print(max_attempts-attempts, "attempts left.")
                else:
                    stored_pw=stored_pw[0]
                    if stored_pw==password:
                        print("Login Successful!")
                        return
                    else:
                        attempts+=1
                        print("Incorrect Password! Try again")
                        print(max_attempts-attempts, "attempts left")
            if attempts==max_attempts:
                print("Two many unsuccessful attempts, exiting the program.")
                print("Have a great day ahead!")
                exit()
        elif c2==2:
            print("Going too soon! :(  Do you really want to exit")
            ic3=input("Enter choice (y/n): ")
            if ic3=="y":
                print("Exiting the program")
                exit()
            elif ic3=="n":
                continue

# 1. Viewing available products
def view_pdt(con_ob):
    cursor=con_ob.cursor()
    cursor.execute("select * from products")
    prdt=cursor.fetchall()
    for prd in prdt:
        print(prd)

# 2. Adding a product
def add_pdt(con_ob):
    cursor=con_ob.cursor()
    nprd_id=get_next_id("products", "prd_id")
    prd_name=input("Enter the product name: ")
    brand=input("Enter the brand/manufacturer: ")
    category=input("Enter the category: ")
    price=int(input("Enter the price: "))
    quantity=int(input("Enter the quantity: "))
    
    add_sq1="insert into products values(%s, %s, %s, %s, %s, %s)"
    cursor.execute(add_sq1, (nprd_id, prd_name, brand, category, price, quantity))
    con_ob.commit()
    print("Product added successfully with product ID", nprd_id)

# 3. Updating existing product
def upd_pdt(con_ob):
    cursor=con_ob.cursor()
    prd_id=int(input("Enter the product id for the existing product: "))
    cursor.execute("select * from products where prd_id=%s", (prd_id,))
    product=cursor.fetchone()
    print(product)
    if product:
        while True:
            print('''Select the field to be updated
1. Product Name
2. Brand
3. Category
4. Price
5. Quantity
6. Exit''')
            c3=int(input("Enter your choice: "))
            if c3==1:
                n_name=input("Enter new product name: ")
                cursor.execute("update products set prd_name=%s where prd_id=%s", (n_name, prd_id))
                con_ob.commit()
                print("Product", prd_id, "updated successfully.")
            elif c3==2:
                n_brand=input("Enter new brand: ")
                cursor.execute("update products set brand=%s where prd_id=%s", (n_brand, prd_id))
                con_ob.commit()
                print("Product", prd_id, "updated successfully")
            elif c3==3:
                n_cat=input("Enter new category: ")
                cursor.execute("update products set category=%s where prd_id=%s", (n_cat, prd_id))
                con_ob.commit()
                print("Product", prd_id, "updated successfully")
            elif c3==4:
                n_price=input("Enter new price: ")
                cursor.execute("update products set price=%s where prd_id=%s", (n_price, prd_id))
                con_ob.commit()
                print("Product", prd_id, "updated successfully")
            elif c3==5:
                n_qua=int(input("Enter new quantity: "))
                cursor.execute("update products set quantity=%s where prd_id=%s", (n_qua, prd_id))
                con_ob.commit()
                print("Product", prd_id, "updated successfully")
            elif c3==6:
                print("Exiting the menu.")
                break
            else:
                print("Invalid Choice! Enter a number between 1 and 6.")

# 4. Delete existing product
def del_prd(con_ob):
    cursor=con_ob.cursor()
    prd_id=int(input("Enter product ID to be deleted: "))
    cursor.execute("select * from products where prd_id=%s", (prd_id,))
    product=cursor.fetchone()
    if product:
        confirm=input("Are you sure you want to delete this product? (y/n): ")
        if confirm=="y":
            cursor.execute("delete from products where prd_id=%s", (prd_id,))
            con_ob.commit()
            print("Product deleted successfully!")
        elif confirm=="n":
            print("Exiting the menu")
            return
        else:
            print("Invalid Character! Try again")

# 5. Viewing all customers
def view_cust(con_ob):
    cursor=con_ob.cursor()
    cursor.execute("select * from profiles")
    custd=cursor.fetchall()
    for cus in custd:
        print(cus)

# 6. Adding a customer
def add_cust(con_ob):
    cursor=con_ob.cursor()
    ncust_id=get_next_id("profiles", "cust_id")
    name=input("Enter your name: ")
    contact=int(input("Enter your contact: "))
    gender=input("Enter your gender: ")
    email=input("Enter your email: ")
    print("Enter your address in line 1, line 2 and line 3 accordingly. Leave line 3 empty (if not applicable)")
    add_l1=input("Address line 1: ")
    add_l2=input("Address line 2: ")
    add_l3=input("Address line 3: ")
    city_state=input("Enter your city and state (separated by ','): ")

    add_sq2="insert into profiles values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(add_sq2, (ncust_id, name, contact, gender, email, add_l1, add_l2, add_l3, city_state))
    con_ob.commit()
    print("Profile added Successfully")

# 7.1. Processing a sale
def prcs_sale(con_ob):
    from datetime import datetime
    cursor=con_ob.cursor()
    prd_id=int(input("Enter product ID: "))
    cust_id=int(input("Enter customer ID: "))
    sold_qu=int(input("Enter sold quantity: "))
    # Check for sufficient stock of the product id
    cursor.execute("select quantity from products where prd_id=%s", (prd_id,))
    stock=cursor.fetchone()[0]
    if stock>=sold_qu:
        cursor.execute("update products set quantity=quantity-%s where prd_id=%s", (sold_qu, prd_id))
        sale_id=get_next_id("sales", "sale_id")
        saledate=datetime.now()
        add_sq3="insert into sales values(%s, %s, %s, %s, %s)"
        cursor.execute(add_sq3, (sale_id, prd_id, cust_id, sold_qu, saledate))
        con_ob.commit()
        bill_desk(con_ob, sale_id, cust_id, prd_id)
        print("Sale processed successfully with sale ID", sale_id, "for customer ID", cust_id)
    else:
        print("Insufficient Stock, kindly restock first!")

# 7.2. Invoice Creation
def bill_desk(con_ob, sale_id, cust_id, prd_id):
    from datetime import datetime
    cursor=con_ob.cursor()
    inv_no=get_next_id("billdesk", "inv_no")
    saledate=datetime.now()
    cursor.execute("select name from profiles where cust_id=%s", (cust_id,))
    customer=cursor.fetchone()
    if customer:
        cust_name=customer[0]   #  Error here
        cursor.execute("select prd_id, prd_name, price from products where prd_id=%s", (prd_id,))
        product=cursor.fetchone()
    else:
        print("No customer is found with customer ID", cust_id)
        return
    if product:
        prd_id, prd_name, price=product[0], product[1], product[2]
        sold_qu=int(input('Enter Sold Quantity: '))
        dis_am=int(input("Enter discount amount: "))
        def dis(price, dis_am):
            return (dis_am / 100) * price
        discount = dis(price, dis_am)
        final_price = price - discount
        print("Creating invoice with details: inv_no=", inv_no, 'saledate=', saledate, 'sale_id=', sale_id, 'cust_id=', cust_id, 'cust_name=', cust_name, 'prd_id=', prd_id, 'prd_name=', prd_name, 'sold_qu=', sold_qu, 'price=', price, 'dis_am=', dis_am, 'final_price=', final_price)
        add_sq4="insert into billdesk values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(add_sq4, (inv_no, saledate, sale_id, cust_id, cust_name, prd_id, prd_name, sold_qu, price, dis_am, final_price))
        con_ob.commit()
        print("Invoice", inv_no, "created successfully for cust_id", cust_id)
    else:
        print("No Products with Product ID", prd_id)
        return

# 8. View all processed sales
def view_s_rep(con_ob):
    cursor = con_ob.cursor()
    c1 = 0
    while c1!=3:
        print('''\n1. Generate full report
2. Generate for selective members
3. Exit''')
        c1=int(input("Enter your choice: "))
        if c1==1:
            print("Report generated in order- saledate, sale_id, cust_id, cust_name, prd_id, prd_name, sold_qu, final_price")
            cursor.execute("select saledate, sale_id, cust_id, cust_name, prd_id, prd_name, sold_qu, final_price from billdesk")
            rep1=cursor.fetchall()
            for row in rep1:
                print(row)
            con_ob.commit()
        elif c1==2:
            cust_id=int(input("Enter the customer id: "))
            cursor.execute("select saledate, sale_id, cust_id, cust_name, prd_id, prd_name, sold_qu, final_price from billdesk where cust_id={0}".format(cust_id))
            report = cursor.fetchall()
            if report:
                print("Report generated for", cust_id, "generated in order- saledate, sale_id, cust_id, cust_name, prd_id, prd_name, sold_qu, final_price")
                for row in report:
                    print(row)
            else:
                print("No report found")
            con_ob.commit()
        elif c1==3:
            print("Confirm Exit!")
            ui=input("y/n: ")
            if ui=="y":
                print("Exiting report generation")
                break
            elif ui=="n":
                view_s_rep(con_ob)

# 9. Display domain
def display_domain(con_ob):
    try:
        cursor=con_ob.cursor()
        user_id=int(input("Enter your User ID again: "))
        cursor.execute("select user_id, user_name, desig from domain where user_id=%s", (user_id,))
        dom_info=cursor.fetchone()
        u_id=dom_info[0]
        u_n=dom_info[1]
        des=dom_info[2]
        if dom_info:
            print("Domain Information is as followed")
            print("User ID: ", u_id)
            print("Username: ", u_n)
            print("Designation: ", des)
            
    except Exception as e:
        print("No domain available with given User ID.")

# 10. Add a domain
def add_domain(con_ob):
    cursor=con_ob.cursor()
    n_dom_id=get_next_id("domain", "user_id")
    user_name=input("Enter new user name: ")
    desig=input("Enter your designation: ")
    password=input("Enter your password: ")
    
    add_sq5="insert into domain values(%s, %s, %s, %s)"
    cursor.execute(add_sq5, (n_dom_id, user_name, desig, password))
    con_ob.commit()
    print("Domain added successfully with Domain ID", n_dom_id)

# main
print("Welcome to EShop!")
print("This management system is for electronic shop management needs... \n Hope this system fulfils your need today:)")
login_screen(con_ob)
choice=0
while choice!=11:
    print("Select from the menu from 1-11")
    print('''1. View available products
2. Add a Product
3. Update existing product
4. Delete Existing Product
5. View all customers
6. Add a customer
7. Process a sale (followed by invoice creation)
8. View all processed sales
9. Display domain
10. Add a domain
11. Exit''')
    u1=int(input("Enter any value from 1 to 11: "))
    if u1==1:
        view_pdt(con_ob)
    elif u1==2:
        add_pdt(con_ob)
    elif u1==3:
        upd_pdt(con_ob)
    elif u1==4:
        del_prd(con_ob)
    elif u1==5:
        view_cust(con_ob)
    elif u1==6:
        add_cust(con_ob)
    elif u1==7:
        prcs_sale(con_ob)
    elif u1==8:
        view_s_rep(con_ob)
    elif u1==9:
        display_domain(con_ob)  
    elif u1==10:
        add_domain(con_ob)
    elif u1==11:
        print("Hope this helped you today, See you again later.")
        print("Exiting the program")
        exit()
    else:
        print("Invalid choice! Please select from 1 to 11: ")