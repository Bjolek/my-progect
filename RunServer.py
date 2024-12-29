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
    return render_template("products.html", clothes=clothes,furniture=furniture)

app.run()