from flask import *


app = Flask("Shop")
db_name = "Site.db"

clothes = [
    (0, "https://football-world.com.ua/product-images/product/Nike/33466-63a5b23a75727.webp","Куртка Nike",3000,"Тепла і комфортна куртка з флісового матеріалу для осінньо-зимового сезону."),
    (1,"https://ireland.apollo.olxcdn.com/v1/files/hzqmv79gclar1-UA/image;s=1000x921","Куртка Jordan",5500,"Тепла і комфортна куртка з флісового матеріалу для осінньо-зимового сезону." ),
    (2, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmIsqDbwGf8MVnOG3FHoA1MpFk_b8-VRoHDw&s","Куртка Champion",3500,"Тепла і комфортна куртка з флісового матеріалу для осінньо-зимового сезону."),
    (3,"https://sportcity.ua/wa-data/public/shop/products/75/01/20175/images/229083/229083.750.jpg","Куртка Puma",4000,"Тепла і комфортна куртка з флісового матеріалу для осінньо-зимового сезону." ),
]

furniture = [
    (0, "https://images.prom.ua/4668486902_w640_h320_pylesos-philips-kontejnernyj.jpg","PHILIPS",2500,"Сучасний пилосос з високою потужністю і низьким рівнем шуму."),
    (1,"https://files.foxtrot.com.ua/PhotoNew/img_0_105_2919_0.jpg","SAMSUNG",3500,"Сучасний пилосос з високою потужністю і низьким рівнем шуму." ),
    (2, "https://content.rozetka.com.ua/goods/images/big/348717472.jpg","Grunhelm",2000,"Сучасний пилосос з високою потужністю і низьким рівнем шуму."),
    (3,"https://coyot.ua/content/images/11/325x325l50nn0/44281897508070.jpeg","CLATRONIX",2300,"Сучасний пилосос з високою потужністю і низьким рівнем шуму." ),
]

Leptops = [
    (0, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSucTyk6M0oPTikMCVCcyykEZiMVoKZqnZvRw&s","Lenovo Legion Y540",29999,"Потужний ноутбук для роботи та розваг, з довгим часом автономної роботи.."),
    (1,"https://files.foxtrot.com.ua/PhotoNew/img_0_58_26293_0_1_01xywr.jpg","Lenovo Legion 5 Pro",49999,"Потужний ноутбук для роботи та розваг, з довгим часом автономної роботи." ),
    (2, "https://i.eldorado.ua//goods_images/1039096/8571327-1728301419.jpg","ASUS ROG Strix",59999,"Потужний ноутбук для роботи та розваг, з довгим часом автономної роботи."),
    (3,"https://texnomarket.in.ua/thumbs/s600_600__r/aHR0cHM6Ly9jZG4uY29tZnkudWEvbWVkaWEvY2F0YWxvZy9wcm9kdWN0L2NhY2hlLzQvc21hbGxfaW1hZ2UvNjAweC82MmRlZmM3ZjQ2ZjNmYmZjOGFmY2QxMTIyMjdkMTE4MS96L3EvenFuOHZudnkuanBn.webp","lenovo Gaming 3",25000,"Потужний ноутбук для роботи та розваг, з довгим часом автономної роботи." ),]

Gadgets = [
    (0,"https://cdn0.it4profit.com/s3/cms/category/c8/fe/c8fed38a65ca19e427ac4d2bd5ef96ac/group_1211651_11.webp","Apple Watch",10000,"Стильний смарт-годинник з функцією моніторингу здоров'я та трекінгу активності."),
    (1,"https://cdn.tehnoezh.ua/0/0/0/1/1/3/8/0/0/000113800_545_545.jpeg","Galaxy Watch 5",9000,"Стильний смарт-годинник з функцією моніторингу здоров'я та трекінгу активності."),
    (2,"https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQ7l1rTrff60E6y49w4rkPdOqdGPGe8d-S40lYtOo9sVMYHplgPCRY7Uvq-AFYemEmRLnk0ejpHHqsf4adHntjhgStV0x8yOXjweuw-g2jhdlKoPId0Pz_NM8-szG0AJ1rrif8NdPs&usqp=CAc","Forever",5000,"Стильний смарт-годинник з функцією моніторингу здоров'я та трекінгу активності."),
    (3,"https://cdn.tehnoezh.ua/0/0/0/1/1/3/8/0/0/000113800_545_545.jpeg","Galaxy Watch 5",9000,"Стильний смарт-годинник з функцією моніторингу здоров'я та трекінгу активності.")
]

Phones = [
    (0, "https://a.allegroimg.com/s600/035df6/9123c9194e609beea105862d349e/Xiaomi-Mi-9T-Pro-6-128GB-LodowiecNiebieski.webp", "Xiomi mi 9t", 5000, "Смартфон з високою продуктивністю, чудовою камерою та великим екраном."),
    (1, "https://img.mta.ua/image/cache/data/foto/z910/910842/photos/Google-Pixel-8a-8128GB-24-Bay-01-600x600.jpg", "Pixel 9", 15000, "Смартфон з високою продуктивністю, чудовою камерою та великим екраном."),
    (2, "https://scdn.comfy.ua/89fc351a-22e7-41ee-8321-f8a9356ca351/https://cdn.comfy.ua/media/catalog/product/_/a/_apple_iphone_16_512gb_ultramarine_1.jpg/w_600", "Iphone 16", 20000, "Смартфон з високою продуктивністю, чудовою камерою та великим екраном."),
    (3, "https://cdn.samsungshop.com.ua/products/8654/cover/163343/%D0%A124%D0%A3%D0%BB%D1%8C%D1%82%D1%80%D0%B0-%D0%A4%D0%B8%D0%BE%D0%BB%D0%B5%D1%82%D0%BE%D0%B2%D1%8B%D0%B9-%E2%80%94-%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F.webp", "Samsung S24 Ultra", 17000, "Смартфон з високою продуктивністю, чудовою камерою та великим екраном.")
]



@app.route("/")
def base():
    return render_template("main.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/products")
def products():
    return render_template("products.html", clothes=clothes,furniture=furniture,Leptops=Leptops,Gadgets=Gadgets,Phones=Phones)

@app.route("/buy")
def buy():
    return render_template("buy.html")

app.run()