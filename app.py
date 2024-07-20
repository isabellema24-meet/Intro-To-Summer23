from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return('<html><h1>Welcome to the main page!</h1><a href= "/food1"><h2>food</h2></a></h1><a href= "/outerSpace1"><h2>outer space</h2></a></h1><a href= "/pet1"><h2>pets</h2></a></html>')
@app.route('/outerSpace1')
def outerSpace1():
    return('<html><img src= "https://www.smorescience.com/wp-content/uploads/2023/07/Featured-Images-33.jpg"><a href= "/outerSpace2"><h2>outer space 2</h2></a><a href= "/home"><h2>home page</h2></a></html>')
@app.route('/pet1')
def pet1():
    return('<html><img src= "https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg"><a href= "/pet2"><h2>pet 2</h2></a><a href= "/home"><h2>home page</h2></a></html>')
@app.route('/food1')
def food1():
    return('<html><img src= "https://www.indianhealthyrecipes.com/wp-content/uploads/2015/10/pizza-recipe-1.jpg"><a href= "/food2"><h2>food 2</h2></a><a href= "/home"><h2>home page</h2></a></html>')
@app.route('/food2')
def food2():
    return('<html><img src= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNJYdKbYEXieWoQa2OISBqVSJIAmW0Kcf2pQ&s"><a href= "/food3"><h2>food 3</h2></a><a href= "/home"><h2>home page</h2></a></html>')
@app.route('/food3')
def food3():
    return('<html><img src= "https://www.gutekueche.at/storage/media/recipe/106126/conv/wiener-schnitzel-default.jpg"><a href= "/home"><h2>home page</h2></a></html>')
@app.route('/outerSpace2')
def outerSpace2():
    return('<html><img src= "https://cdn.britannica.com/70/94870-050-2ECAB6AD/Cats-Eye-nebula.jpg"><a href= "/outerSpace3"><h2>outer space 3</h2></a><a href= "/home"><h2>home page</h2></a></html>')
@app.route('/outerSpace3')
def outerSpace3():
    return('<html><img src= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-PuKZcup1JDrFRkCM0mqfISTwf17u_8fy4w&s"><a href= "/home"><h2>home page</h2></a></html>')
@app.route('/pet2')
def pet2():
    return('<html><img src= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0sOA9N5tXNCRWuSoihvRD4F4qPf6_30El1A&s"><a href= "/pet3"><h2>pet 3</h2></a><a href= "/home"><h2>home page</h2></a></html>')
@app.route('/pet3')
def pet3():
    return('<html><img src= "https://ars.els-cdn.com/content/image/3-s2.0-B9780323851251000934-f00093-04-9780323851251.jpg"><a href= "/home"><h2>home page</h2></a></html>')
if __name__ == '__main__':
    app.run(debug=True)
