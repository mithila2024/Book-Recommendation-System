from flask import Flask,render_template,request
import pickle
import numpy as np
# Below pickle command was not working because pandas version from jupyter nootbook and vs was different.
#  I use update version in vs using pip install --upgrade pandas==1.5.3
popular_df=pickle.load(open('popular.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
similarity_score=pickle.load(open('similarity_score.pkl','rb'))

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           ratings=list(np.round(popular_df['avg_ratings'].values,2)),
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input=request.form.get('user_input')
    index=np.where(pt.index==user_input)[0][0]## finding the index of a book from pivot table pt

    ## Now we found the index we need to go to similarity_score and find that index
## taking the enumarate, so that find index and similarity score at the same ime
### Now we need to sort it in the base of value(in ascending order) not index
### Now the first score will be similiarity with it self so we will not take that
### we will take top 5 score from 1:6
    similar_items=sorted(list(enumerate(similarity_score[index])), key=lambda x:x[1],reverse=True)[1:6]
    
    data=[]
    for i in similar_items:## take the similar item 1 by 1
       ## print(pt.index[i[0]])  ### take the index value for each item
        item=[]
        tmp_df=books[books['Book-Title']==pt.index[i[0]]]
        item.extend(list(tmp_df.drop_duplicates('Book-Title')['Book-Title'].values))## droping duplicates as one book-title can have multiple isbn
        item.extend(list(tmp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(tmp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    print(data)

    return render_template('recommend.html', data=data)

if __name__== '__main__':
    app.run(debug=True)