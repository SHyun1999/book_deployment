from flask import Flask,request,jsonify
import pandas as pd
import numpy as np
import joblib

class Api:

    app = Flask(__name__)

    @app.route('/RecommendBooks', methods=['POST'])
    def preds():

        feat_data = request.json

        df = pd.read_csv('books.csv',  error_bad_lines=False)
        idlist = joblib.load('idlist.pkl')

        book_list = []
        book_id = df[df['title'] == feat_data[0]].index
        book_id = book_id[0]

        for newid in idlist[book_id]:
            book_list.append(df.loc[newid].title)           

        return jsonify(book_list)


    @app.route('/RecommendAuthors', methods=['POST'])
    def preds_books():

        feat_data = request.json

        df = pd.read_csv('books.csv',  error_bad_lines=False)
        idlist = joblib.load('idlist.pkl')

        auth_list = []
        books=[]
        auth_id = df[df['authors'] == feat_data[0]].index
        auth_id = auth_id[0]

        for newid in idlist[auth_id]:
            auth_list.append(df.loc[newid].authors)
            books.append(df.loc[newid].title)
        
        res = dict(zip(books, auth_list))    

        return jsonify(res)    

    if __name__ == '__main__':

        app.run(debug = True)


    