<h1>Logic used in book-recommender-system.ipynb:</h1>
<h2> Here I have applied 2 recommendation Logic. </h2>
<h3> 1>Popularity Based Recommendation </h3>
<p>i)I meged Books dataframe and Rating DataFrame using ISBN<br>
 ii> Then I have taken those Books averge rating from the Books where rating given is >= 250, Here for averaging and counting I have grouped by 'Books-Title' , not 'ISBN' , as for same Books-Title there are mutiple 'ISBN' </p>

 <h3> 1>Collaborating Filter Based Recommendation </h3>
 <p>
  i>Here our strategy is that we will<br>
     a)Take the users who has given more than 200 ratings<br>
     b) after that take the books where ratings given is atleast 50<br>
Here we will work with books , ratings and we will form a table where index will be books and columns will be users and in the cell rating will be there<br>
  Now after that we will create a function where if we give a book name it will recommend us 5 other Books<br>
  also I have taken the dump of pickel file , so that I can use it to make a web app
 </p>

 <h3>Now I have created a web page using html,css(app.py) </h3>
  <p>where first page we will show all he 50 popular books based on popularity based recommendation system(index.html)<br>
  also we have a recommend page , where if we give a book name it will show similar 5 books and their name and author(recommend.html)</p>
