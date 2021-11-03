from flask import Flask,request,jsonify
import pandas as pd
import numpy as np
import joblib



app = Flask(__name__)

@app.route('/RecommendBooks', methods=['GET', 'POST'])
def preds():


    if request.method == 'POST':
        feat_data = request.json

        df = pd.read_csv('books.csv',  error_bad_lines=False)
        idlist = joblib.load('idlist.pkl')

        book_list = []
        rating_list = []
        book_id = df[df['title'] == feat_data[0]].index
        book_id = book_id[0]

        for newid in idlist[book_id]:
            book_list.append(df.loc[newid].title)
            rating_list.append(df.loc[newid].average_rating)
            

        res = [book_list,rating_list]          

        return jsonify(res)

    return        


@app.route('/RecommendAuthors', methods=['GET','POST'])
def preds_books():

    if request.method == 'POST':

        feat_data = request.json

        df = pd.read_csv('books.csv',  error_bad_lines=False)
        idlist = joblib.load('idlist.pkl')

        books=[]
        rating_list = []
        auth_id = df[df['authors'] == feat_data[0]].index
        auth_id = auth_id[0]

        for newid in idlist[auth_id]:
            books.append(df.loc[newid].title)
            rating_list.append(df.loc[newid].average_rating)
            
        res = [books,rating_list]   

        return jsonify(res)

    return        

if __name__ == '__main__':

    app.run()


    