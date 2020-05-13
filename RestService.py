from flask import Flask
from flask_restful import Resource, reqparse ,Api
import json,os,glob

TGS = Flask(__name__)
api = Api(TGS)

os.chdir(os.curdir)
os.listdir
articles = []


class Article(Resource):
    def get_files(self):
        articles.clear()
        for file in glob.glob("*.json"):
            print(file)
            with open(file) as json_data:
                data = json.load(json_data)
                json_data.flush()
                articles.append(data)
                #print(data)
        print(articles)
        return articles

    def get(self, Product):
        suitelist = []
        articles = self.get_files()
        for article in articles:
            if(Product == article["Product"]):
                suitelist.append(article["TestSuiteName"])
            else:
                continue
        return suitelist, 200
        #return "category not found", 404


    def post(self, category):
        parser = reqparse.RequestParser()
        parser.add_argument("views")
        parser.add_argument("title")
        args = parser.parse_args()

        for article in articles:
            if(category == article["category"]):
                return "category  {} already exists".format(category), 400

        article = {
            "category": category,
            "views": args["views"],
            "title": args["title"]
        }
        articles.append(article)
        return article, 201

    def put(self, category):
        parser = reqparse.RequestParser()
        parser.add_argument("views")
        parser.add_argument("title")
        args = parser.parse_args()

        for article in articles:
            if(category == article["category"]):
                article["views"] = args["views"]
                article["title"] = args["title"]
                return article, 200

        article = {
            "category": category,
            "views": args["views"],
            "title": args["title"]
        }
        articles.append(article)
        return article, 201

    def delete(self, category):
        global articles
        articles = [article for article in articles if article["category"] != category]
        return "{} is deleted.".format(category), 200

api.add_resource(Article, "/Product/<string:Product>")
#/<string:TestSuiteName>

TGS.run(host='0.0.0.0',debug=True,port=9095)

