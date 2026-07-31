from django.shortcuts import render, redirect
from .models import Login
from django.shortcuts import render, redirect
from .models import Login
import random
from django.shortcuts import redirect
import string
from .models import Cart, CartItem

name=''
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = Login.objects.filter(
            username=username,
            password=password
        )

        if user.exists():
            return render(request, "home.html", {"user": user.first()})
        else:
            return render(
                request,
                "login.html",
                {"error": "Invalid Username or Password"}
            )

    return render(request, "login.html")



    #     if user.exists():
    #         message = "Login Successful"
    #     else:
    #         message = "Invalid Username or Password"

    # return render(request, "login.html", {"message": message})
from django.shortcuts import render
from .models import Login
import random
import string

def register(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        address = request.POST['address']

        # Generate Username
        while True:
            username = name.lower().replace(" ", "") + str(random.randint(1000, 9999))
            if not Login.objects.filter(username=username).exists():
                break

        # Generate Password
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for i in range(8))

        # Save to database
        Login.objects.create(
            name=name,
            email=email,
            phone=phone,
            age=age,
            address=address,
            username=username,
            password=password
        )

        return render(request, "success.html", {
            "username": username,
            "password": password
        })

    return render(request, "register.html")
def home(request):
    #return redirect("/home")
    return render(request,"home.html")
def Fashion(request):
    return render(request,"Fashion.html")

def jwellery(request):
    return render(request,"jwellery.html")

def electronics(request):
    return render(request,"electronics.html")

def beauty(request):
    return render(request,"beauty.html")

def homedoc(request):
    return render(request,"homedoc.html")

def Male(request):
    return render(request,"Male.html")

def Female(request):
    return render(request,"Female.html")

def kids(request):
    return render(request,"kids.html")

def ac1(request):
    return render(request,"ac1.html")

def ac2(request):
    return render(request,"ac2.html")
def ac3(request):
    return render(request,"ac3.html")

def ac4(request):
    return render(request,"ac4.html")

def ac5(request):
    return render(request,"ac5.html")
def ac6(request):
    return render(request,"ac6.html")

def bangles(request):
    return render(request,"bangles.html")

def bng1(request):
    return render(request,"bng1.html")

def bng2(request):
    return render(request,"bng2.html")

def bng3(request):
    return render(request,"bng3.html")

def bng4(request):
    return render(request,"bng4.html")

def bng5(request):
    return render(request,"bng5.html")

def bng6(request):
    return render(request,"bng6.html")

def bng7(request):
    return render(request,"bng7.html")

def bng8(request):
    return render(request,"bng8.html")

def bng9(request):
    return render(request,"bng9.html")

def bng10(request):
    return render(request,"bng10.html")

def ear1(request):
    return render(request,"ear1.html")
def ear2(request):
    return render(request,"ear2.html")
def ear3(request):
    return render(request,"ear3.html")
def ear4(request):
    return render(request,"ear4.html")
def ear5(request):
    return render(request,"ear5.html")
def ear6(request):
    return render(request,"ear6.html")
def ear7(request):
    return render(request,"ear7.html")
def ear8(request):
    return render(request,"ear8.html")
def ear9(request):
    return render(request,"ear9.html")
def ear10(request):
    return render(request,"ear10.html")
def earrings(request):
    return render(request,"earrings.html")

def face1(request):
    return render(request,"face1.html")
def face2(request):
    return render(request,"face2.html ")
def face3(request):
    return render(request,"face3.html")
def face4(request):
    return render(request,"face4.html")
def face5(request):
    return render(request,"face5.html")
def found1(request):
    return render(request,"found1.html")
def found2(request):
    return render(request,"found2.html")
def found3(request):
    return render(request,"found3.html")
def found4(request):
    return render(request,"found4.html")
def found5(request):
    return render(request,"found5.html")

def FPant(request):
    return render(request,"FPant.html")
def frandom1(request):
    return render(request,"frandom1.html")

def frandom2(request):
    return render(request,"frandom2.html")

def frandom3(request):
    return render(request,"frandom3.html")

def frandom4(request):
    return render(request,"frandom4.html")

def frandom5(request):
    return render(request,"frandom5.html")

def frandom6(request):
    return render(request,"frandom6.html")


def frandom7(request):
    return render(request,"frandom7.html")

def frandom8(request):
    return render(request,"frandom8.html")

def frandom9(request):
    return render(request,"frandom9.html")

def frandom10(request):
    return render(request,"frandom10.html")

def frandom11(request):
    return render(request,"frandom11.html")

def frandom12(request):
    return render(request,"frandom12.html")

def fri1(request):
    return render(request, "fri1.html")

def fri2(request):
    return render(request,"fri2.html")
def fri3(request):
    return render(request,"fri3.html")
def fri4(request):
    return render(request,"fri4.html")
def fri5(request):
    return render(request,"fri5.html")
def Ftshirt(request):
    return render(request,"Ftshirt.html")

def hair1(request):
    return render(request,"hair1.html")
def hair3(request):
    return render(request,"hair2.html")
def hair2(request):
    return render(request,"hair3.html")
def hair4(request):
    return render(request,"hair4.html")
def hair5(request):
    return render(request,"hair5.html")
def hair6(request):
    return render(request,"hair6.html")
def hair7(request):
    return render(request,"hair7.html")
def hair8(request):
    return render(request,"hair8.html")
def hair9(request):
    return render(request,"hair9.html")
def hair10(request):
    return render(request,"hair10.html")
def hair11(request):
    return render(request,"hair11.html")
def hairacc(request):
    return render(request,"hairacc.html")

def haircare(request):
    return render(request,"haircare.html")

def cosmatic(request):
    return render(request,"cosmatic.html")

def home1(request):
    return render(request,"home1.html")
def home2(request):
    return render(request,"home2.html")
def home3(request):
    return render(request,"home3.html")
def home4(request):
    return render(request,"home4.html")
def home5(request):
    return render(request,"home5.html")
def home6(request):
    return render(request,"home6.html")
def home7(request):
    return render(request,"home7.html")
def home8(request):
    return render(request,"home8.html")
def home9(request):
    return render(request,"home9.html")
def home10(request):
    return render(request,"home10.html")
def home11(request):
    return render(request,"home11.html")
def home12(request):
    return render(request,"homw12.html")
def home13(request):
    return render(request,"home13.html")
def home14(request):
    return render(request,"home14.html")
def home15(request):
    return render(request,"home15.html")
def home16(request):
    return render(request,"home16.html")
def kaj1(request):
    return render(request,"kaj1.html")
def kaj2(request):
    return render(request,"kaj2.html")
def kaj3(request):
    return render(request,"kaj3.html")
def kaj4(request):
    return render(request,"kaj4.html")
def kaj5(request):
    return render(request,"kaj5.html")
def kaj6(request):
    return render(request,"kaj6.html")
def kids1(request):
    return render(request,"kids1.html")
def kids2(request):
    return render(request,"kids2.html")
def kids3(request):
    return render(request,"kids3.html")
def kids4(request):
    return render(request,"kids4.html")
def kids5(request):
    return render(request,"kids5.html")
def kids6(request):
    return render(request,"kids6.html")
def kids7(request):
    return render(request,"kids7.html")
def kids8(request):
    return render(request,"kids8.html")
def kids9(request):
    return render(request,"kids9.html")
def kids10(request):
    return render(request,"kids10.html")
def kids11(request):
    return render(request,"kids11.html")
def kids12(request):
    return render(request,"kids12.html")
def kids13(request):
    return render(request,"kids13.html")
def kids14(request):
    return render(request,"kids14.html")
def kids15(request):
    return render(request,"kids15.html")
def kids16(request):
    return render(request,"kids16.html")
def kt1(request):
    return render(request,"kt1.html")
def kt2(request):
    return render(request,"kt2.html")
def kt3(request):
    return render(request,"kt3.html")
def kt4(request):
    return render(request,"kt4.html")
def kt5(request):
    return render(request,"kt5.html")
def Kurti(request):
    return render(request,"Kurti.html")
def kurti1(request):
    return render(request,"kurti1.html")
def kurti2(request):
    return render(request,"kurti2.html")
def kurti3(request):
    return render(request,"kurti3.html")
def kurti4(request):
    return render(request,"kurti4.html")
def kurti5(request):
    return render(request,"kurti5.html")
def kurti6(request):
    return render(request,"kurti6.html")
def kurti7(request):
    return render(request,"kurti7.html")
def kurti8(request):
    return render(request,"kurti8.html")
def kurti9(request):
    return render(request,"kurti9.html")
def kurti10(request):
    return render(request,"kurti10.html")

def kurti11(request):
    return render(request,"kurti11.html")

def kurti12(request):
    return render(request,"kurti12.html")

def lip1(request):
    return render(request,"lip1.html")
def lip2(request):
    return render(request,"lip2.html")
def lip3(request):
    return render(request,"lip3.html")
def lip4(request):
    return render(request,"lip4.html")
def lip5(request):
    return render(request,"lip5.html")
def lit1(request):
    return render(request,"lit1.html")
def lit2(request):
    return render(request,"lit2.html")
def lit3(request):
    return render(request,"lit3.html")
def lit5(request):
    return render(request,"lit4.html")
def lit4(request):
    return render(request,"lit5.html")
def lo1(request):
    return render(request,"lo1.html")
def lo2(request):
    return render(request,"lo2.html")
def lo3(request):
    return render(request,"lo3.html")
def lo4(request):
    return render(request,"lo4.html")
def lo5(request):
    return render(request,"lo5.html")
def lo6(request):
    return render(request,"lo6.html")

def mk1(request):
    return render(request,"mk1.html")
def mk2(request):
    return render(request,"mk2.html")
def mk3(request):
    return render(request,"mk3.html")
def mk4(request):
    return render(request,"mk4.html")
def mk5(request):
    return render(request,"mk5.html")
def mk6(request):
    return render(request,"mk6.html")
def mk7(request):
    return render(request,"mk7.html")
def mk8(request):
    return render(request,"mk8.html")
def mk10(request):
    return render(request,"mk10.html")
def mk9(request):
    return render(request,"mk9.html")
def mkurti(request):
    return render(request,"mkurti.html")
def mob1(request):
    return render(request,"mob1.html")
def mob2(request):
    return render(request,"mob2.html")
def mob3(request):
    return render(request,"mob3.html")
def mob4(request):
    return render(request,"mob4.html")
def mob5(request):
    return render(request,"mob5.html")
def mob6(request):
    return render(request,"mob6.html")
def mob7(request):
    return render(request,"mob7.html")
def mob8(request):
    return render(request,"mob8.html")
def mob9(request):
    return render(request,"mob9.html")
def mob10(request):
    return render(request,"mob10.html")
def mob11(request):
    return render(request,"mob11.html")
def mob12(request):
    return render(request,"mob12.html")
def mob13(request):
    return render(request,"mob13.html")
def mob14(request):
    return render(request,"mob14.html")
def mob15(request):
    return render(request,"mob15.html")
def mp1(request):
    return render(request,"mp1.html")
def mp2(request):
    return render(request,"mp2.html")
def mp3(request):
    return render(request,"mp3.html")
def mp4(request):
    return render(request,"mp4.html")
def mp5(request):
    return render(request,"mp5.html")
def mp6(request):
    return render(request,"mp6.html")
def mp7(request):
    return render(request,"mp7.html")
def mp8(request):
    return render(request,"mp8.html")
def mp9(request):
    return render(request,"mp9.html")
def mp10(request):
    return render(request,"mp10.html")
def mPant(request):
    return render(request,"mPant.html")
def mrandom5(request):
    return render(request,"mrandom5.html")

def mrandom6(request):
    return render(request,"mrandom6.html")

def mrandom7(request):
    return render(request,"mrandom7.html")

def mrandom8(request):
    return render(request,"mrandom8.html")

def mrandom9(request):
    return render(request,"mrandom9.html")

def mrandom10(request):
    return render(request,"mrandom10.html")

def mrandom11(request):
    return render(request,"mrandom11.html")

def mrandom12(request):
    return render(request,"mrandom12.html")

def mrandom13(request):
    return render(request,"mrandom13.html")

def mrandom14(request):
    return render(request,"mrandom14.html")

def ms1(request):
    return render(request,"ms1.html")
def ms2(request):
    return render(request,"ms2.html")
def ms3(request):
    return render(request,"ms3.html")
def ms4(request):
    return render(request,"ms4.html")
def ms5(request):
    return render(request,"ms5.html")
def ms6(request):
    return render(request,"ms6.html")
def ms7(request):
    return render(request,"ms7.html")
def ms8(request):
    return render(request,"ms8.html")
def ms9(request):
    return render(request,"ms9.html")
def ms10(request):
    return render(request,"ms10.html")
def mshirt(request):
    return render(request,"mshirt.html")
def mt1(request):
    return render(request,"mt1.html")
def mt2(request):
    return render(request,"mt2.html")
def mt3(request):
    return render(request,"mt3.html")
def mt4(request):
    return render(request,"mt4.html")
def mt5(request):
    return render(request,"mt5.html")
def mt6(request):
    return render(request,"mt6.html")
def mt7(request):
    return render(request,"mt7.html")
def mt8(request):
    return render(request,"mt8.html")
def mt9(request):
    return render(request,"mt91.html")
def mt10(request):
    return render(request,"mt10.html")
def mtshirt(request):
    return render(request,"mtshirt.html")

def neck1(request):
    return render(request,"neck1.html")
def neck2(request):
    return render(request,"neck2.html")
def neck3(request):
    return render(request,"neck3.html")
def neck4(request):
    return render(request,"neck4.html")
def neck5(request):
    return render(request,"neck5.html")
def neck6(request):
    return render(request,"neck6.html")
def neck7(request):
    return render(request,"neck7.html")
def neck8(request):
    return render(request,"neck8.html")
def neck9(request):
    return render(request,"neck9.html")
def neck10(request):
    return render(request,"neck10.html")
def necklace(request):
    return render(request,"necklace.html")

def oil1(request):
    return render(request,"oil1.html")
def oil2(request):
    return render(request,"oil2.html")
def oil3(request):
    return render(request,"oil3.html")
def oil4(request):
    return render(request,"oil4.html")
def oil5(request):
    return render(request,"oil5.html")
def pant1(request):
    return render(request,"pant1.html")
def pant2(request):
    return render(request,"pant2.html")
def pant3(request):
    return render(request,"pant3.html")
def pant4(request):
    return render(request,"pant4.html")
def pant5(request):
    return render(request,"pant5.html")
def pant6(request):
    return render(request,"pant6.html")
def pant7(request):
    return render(request,"pant7.html")
def pant8(request):
    return render(request,"pant8.html")
def pant9(request):
    return render(request,"pant9.html")
def pant10(request):
    return render(request,"pant10.html")
def pant11(request):
    return render(request,"pant11.html")
def pant12(request):
    return render(request,"pant12.html")
def pow1(request):
    return render(request,"pow1.html")
def pow2(request):
    return render(request,"pow2.html")
def pow3(request):
    return render(request,"pow3.html")
def pow4(request):
    return render(request,"pow4.html")
def pow5(request):
    return render(request,"pow5.html")
def ring1(request):
    return render(request,"ring1.html")
def ring2(request):
    return render(request,"ring2.html")
def ring3(request):
    return render(request,"ring3.html")
def ring4(request):
    return render(request,"ring4.html")
def ring5(request):
    return render(request,"ring5.html")
def ring6(request):
    return render(request,"ring6.html")
def ring7(request):
    return render(request,"ring7.html")
def ring8(request):
    return render(request,"ring8.html")
def ring9(request):
    return render(request,"ring9.html")
def ring10(request):
    return render(request,"ring10.html")
def rings(request):
    return render(request,"rings.html")
def Saree(request):
    return render(request,"Saree.html")
def saree1(request):
    return render(request,"saree1.html")
def saree2(request):
    return render(request,"saree2.html")
def saree3(request):
    return render(request,"saree3.html")
def saree4(request):
    return render(request,"saree4.html")
def saree5(request):
    return render(request,"saree5.html")
def saree6(request):
    return render(request,"saree6.html")
def saree7(request):
    return render(request,"saree7.html")
def saree8(request):
    return render(request,"saree8.html")
def saree9(request):
    return render(request,"saree9.html")
def saree10(request):
    return render(request,"saree10.html")

def saree11(request):
    return render(request,"saree11.html")
def saree12(request):
    return render(request,"saree12.html")

def se1(request):
    return render(request,"se1.html")
def se2(request):
    return render(request,"se2.html")
def se3(request):
    return render(request,"se3.html")
def se4(request):
    return render(request,"se4.html")
def se5(request):
    return render(request,"se5.html")
def shm1(request):
    return render(request,"shm1.html")
def shm2(request):
    return render(request,"shm2.html")
def shm3(request):
    return render(request,"shm3.html")
def shm4(request):
    return render(request,"shm4.html")
def shm5(request):
    return render(request,"shm5.html")
def shm6(request):
    return render(request,"shm6.html")
def shm7(request):
    return render(request,"shm7.html")
def shm8(request):
    return render(request,"shm8.html")
def shm9(request):
    return render(request,"shm9.html")
def shm10(request):
    return render(request,"shm10.html")
def skin(request):
    return render(request,"skin.html")
def success(request):
    return render(request,"success.html")

def sun1(request):
    return render(request,"sun1.html")
def sun2(request):
    return render(request,"sun2.html")
def sun3(request):
    return render(request,"sun3.html")
def sun4(request):
    return render(request,"sun4.html")
def sun5(request):
    return render(request,"sun5.html")
def tab1(request):
    return render(request,"tab1.html")
def tab2(request):
    return render(request,"tab2.html")
def tab3(request):
    return render(request,"tab3.html")
def tab4(request):
    return render(request,"tab4.html")
def tab5(request):
    return render(request,"tab5.html")
def tv1(request):
    return render(request,"tv1.html")
def tv2(request):
    return render(request,"tv2.html")
def tv3(request):
    return render(request,"tv3.html")
def tv4(request):
    return render(request,"tv4.html")
def tv5(request):
    return render(request,"tv5.html")
def tshirt1(request):
    return render(request,"tshirt1.html")

def tshirt2(request):
    return render(request,"tshirt2.html")

def tshirt3(request):
    return render(request,"tshirt3.html")

def tshirt4(request):
    return render(request,"tshirt4.html")

def tshirt5(request):
    return render(request,"tshirt5.html")

def tshirt6(request):
    return render(request,"tshirt6.html")

def tshirt7(request):
    return render(request,"tshirt7.html")

def tshirt8(request):
    return render(request,"tshirt8.html")

def tshirt9(request):
    return render(request,"tshirt9.html")

def tshirt10(request):
    return render(request,"tshirt10.html")

def tshirt11(request):
    return render(request,"tshirt11.html")

def tshirt12(request):
    return render(request,"tshirt12.html")


from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def beauty(request):
    return render(request, 'beauty.html')

def electronics(request):
    return render(request, 'electronics.html')

# Add this new view at the end
def search(request):
    query = request.GET.get("q", "").strip().lower()

    products = {

         'ac':['electronics','ac1','ac2','ac3','ac4'],
        'necklace':['necklace','neck1','neck2'],
        'earrings':['earrings'],
        'rings':['rings'],
        'hair accessories':['hairacc'],
        'kurti':['Kurti'],
        'lipstick':['lip1'],
        'male':['Male'],
        'male kurti':['mkurti'],
        'male pant':['mPant'],
        'male tshirt':['mtshirt'],
        'male shirt':['mshirt'],
        'kids':['kids'],
        'female tshirt':['Ftshirt'],
        'female pant':['FPant'],
        'saree':['Saree'],
        'bangles':['bangles'],
        'skincare':['skin'],
        'haircare':['haircare'],
        'cosmatic':['cosmatic'],
        'foundation':['cosmatic'],
        'kajal':['cosmatic'],
        'powder':['cosmatic'],
        'fridge':['electronics'],
        'tv':['electronics'],
        'light':['electronics'],
        'mobile':['electronics'],
        'laptop':['electronics'],
        'tabs':['electronics'],
        'home decore':['homedoc'],
        'shampoo':['haircare']
    }

    if query in products:
        return redirect(products[query][0])

    return redirect('home')
from django.shortcuts import render, redirect
from .models import Order

def payment(request):

    if request.method == "GET":

        product_name = request.GET.get("product", "")
        price = request.GET.get("price", "")

        return render(request, "payment.html", {
            "product_name": product_name,
            "price": price
        })


    if request.method == "POST":

        product_name = request.POST.get("product_name")
        price = request.POST.get("price")

        customer_name = request.POST.get("customer_name")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")

        payment_method = request.POST.get("payment_method")

        order = Order.objects.create(

            product_name=product_name,

            price=price,

            customer_name=customer_name,

            mobile=mobile,

            address=address,

            payment_method=payment_method

        )

        # After order is placed
        return render(request, "order_success.html", {
            "product_name": product_name,
            "price": price,
            "customer_name": customer_name,
            "payment_method": payment_method
        }) 
from django.shortcuts import render, redirect
from .models import Cart, CartItem


def add_to_cart(request):

    if request.method != "POST":
        return redirect("home")

    product_name = request.POST.get("product_name")
    price = request.POST.get("price")

    # Check whether product information was received
    if not product_name or not price:
        return redirect("home")

    # Create session if it doesn't exist
    session_id = request.session.session_key

    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    # Get or create cart
    cart, created = Cart.objects.get_or_create(
        session_id=session_id
    )

    # Check if product already exists
    item = CartItem.objects.filter(
        cart=cart,
        product_name=product_name
    ).first()

    if item:
        item.quantity += 1
        item.save()
    else:
        CartItem.objects.create(
            cart=cart,
            product_name=product_name,
            price=price,
            quantity=1
        )

    return redirect("cart")
def cart(request):

    session_id = request.session.session_key

    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    cart, created = Cart.objects.get_or_create(
        session_id=session_id
    )

    items = cart.items.all()

    total = sum(
        item.total_price()
        for item in items
    )

    return render(
        request,
        "cart.html",
        {
            "cart_items": items,
            "total": total
        }
    )
def remove_from_cart(request, item_id):

    if request.method == "POST":

        try:
            item = CartItem.objects.get(id=item_id)
            item.delete()

        except CartItem.DoesNotExist:
            pass

    return redirect("cart")
def increase_quantity(request, item_id):

    if request.method == "POST":

        try:
            item = CartItem.objects.get(id=item_id)
            item.quantity += 1
            item.save()

        except CartItem.DoesNotExist:
            pass

    return redirect("cart")
def decrease_quantity(request, item_id):

    if request.method == "POST":

        try:
            item = CartItem.objects.get(id=item_id)

            if item.quantity > 1:
                item.quantity -= 1
                item.save()
            else:
                item.delete()

        except CartItem.DoesNotExist:
            pass

    return redirect("cart")