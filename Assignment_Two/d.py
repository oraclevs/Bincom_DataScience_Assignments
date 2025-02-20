images = [
  "https://ng.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/25/8797052/1.jpg?4457",
  'https://www-konga-com-res.cloudinary.com/w_500,f_auto,fl_lossy,dpr_auto,q_auto/media/catalog/product/D/L/163031_1716824314.jpg',
  'https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/82/658597/1.jpg?9713',
  'https://i5.walmartimages.com/seo/Wrangler-Men-s-and-Big-Men-s-Performance-Series-Regular-Fit-Jean_4ce104b8-bdc6-4c68-9ad5-78beef46dd64.a43b99e36dfb3e36aa312b618d61a1f1.jpeg?odnHeight=640&odnWidth=640&odnBg=FFFFFF',
  'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1512868708i/37201160.jpg',
  'https://www.design-your-homeschool.com/images/a-beka-books.jpg',
  'https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/49/3997072/1.jpg?5130',
  'https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/45/4249102/1.jpg?6897',
  'https://images-cdn.ubuy.co.in/63eced25f5e737227e25637c-14-pcs-big-ultimate-superhero-action.jpg',
  'https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/62/6991952/1.jpg?0717',
]
Product = [
  {
    "name": "Hikers 32'' Frameless Android Smart HD LED TV",
    "description": "32-inch Android Smart HD LED TV with frameless design and 1-year warranty",
    "brand": "Hikers",
    "price": 249.99,
    "category": "Electronics",
    "stock_quantity": 50,
    "attributes": {
      "size": ["32 inches"],
      "color": ["Black"],
      "material": ["Plastic", "Metal"]
    }
  },
  {
    "name": "Zealot 80W Super Bass Bluetooth Speaker with 16000mAh Battery S97",
    "description": "80W Bluetooth speaker with super bass and long-lasting 16000mAh battery",
    "brand": "Zealot",
    "price": 129.99,
    "category": "Electronics",
    "stock_quantity": 30,
    "attributes": {
      "size": ["Medium"],
      "color": ["Black"],
      "material": ["Plastic"]
    }
  },
  {
    "name": "VEJARO D01 Female Office Lady Casual Hot Dress Multicolor Printing",
    "description": "Casual office lady dress with multicolor printing",
    "brand": "VEJARO",
    "price": 39.99,
    "category": "Clothing",
    "stock_quantity": 100,
    "attributes": {
      "size": ["Small", "Medium", "Large"],
      "color": ["Multicolor"],
      "material": ["Cotton"]
    }
  },
  {
    "name": "Men's 2 In 1 Stretch Regular Fit Jeans",
    "description": "Regular fit stretch jeans for men, 2-in-1 design",
    "brand": "Generic",
    "price": 49.99,
    "category": "Clothing",
    "stock_quantity": 75,
    "attributes": {
      "size": ["Medium", "Large"],
      "color": ["Blue"],
      "material": ["Denim"]
    }
  },
  {
    "name": "8-Book BabyLit Literary-Classics Board-Book Bundle",
    "description": "A bundle of 8 board books inspired by literary classics for babies",
    "brand": "BabyLit",
    "price": 59.99,
    "category": "Books",
    "stock_quantity": 20,
    "attributes": {
      "size": ["Small"],
      "color": ["Multicolor"],
      "material": ["Paper"]
    }
  },
  {
    "name": "Abeka Homeschool Textbooks Overview",
    "description": "A comprehensive overview of Abeka homeschool textbooks",
    "brand": "Abeka",
    "price": 29.99,
    "category": "Books",
    "stock_quantity": 40,
    "attributes": {
      "size": ["Medium"],
      "color": ["Multicolor"],
      "material": ["Paper"]
    }
  },
  {
    "name": "Shoe Rack Multi-layer Ten Layers And Nine Grids Silver Gray",
    "description": "Multi-layer shoe rack with ten layers and nine grids, silver gray color",
    "brand": "Generic",
    "price": 89.99,
    "category": "Furniture",
    "stock_quantity": 15,
    "attributes": {
      "size": ["Large"],
      "color": ["Silver Gray"],
      "material": ["Metal"]
    }
  },
  {
    "name": "Leather Shoes Black Corporate Classy Lace Shoes",
    "description": "Classy corporate lace shoes made of black leather",
    "brand": "Generic",
    "price": 79.99,
    "category": "Furniture",
    "stock_quantity": 60,
    "attributes": {
      "size": ["Medium", "Large"],
      "color": ["Black"],
      "material": ["Leather"]
    }
  },
  {
    "name": "Action Figure Set",
    "description": "A set of 5 action figures with movable joints",
    "brand": "HeroToys",
    "price": 39.99,
    "category": "Toys",
    "stock_quantity": 30,
    "attributes": {
      "size": ["Small"],
      "color": ["Multicolor"],
      "material": ["Plastic"]
    }
  },
  {
    "name": "Plush Teddy Bear",
    "description": "A soft and cuddly teddy bear for kids",
    "brand": "CuddleBears",
    "price": 19.99,
    "category": "Toys",
    "stock_quantity": 50,
    "attributes": {
      "size": ["Medium"],
      "color": ["Brown"],
      "material": ["Plush", "Cotton"]
    }
  }
]

for i in range(len(Product)):
    Product[i]['images'] = [images[i]]
print(Product)