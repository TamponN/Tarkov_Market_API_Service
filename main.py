from application import app, api
from Controllers.itemConroller import ItemController
from Controllers.pageController import PageConroller

if __name__ == "__main__":
    api.add_resource(ItemController)
    api.add_resource(PageConroller)

    app.run(debug=True, port=3000, host='127.0.0.1')