# Importing all Modules
from flask import Flask, render_template, Markup, request, redirect
import text_extract
import summary
import name_recog
import os
import transcript

# Defining App
app = Flask(__name__)

#Calling functions from other Python files to use in Flasjk Deployment
text = text_extract.text_extract_func()
summarize = summary.summary_func()
name_finder = name_recog.name_recog_func()
my_str = ("")
count = 1
for i in name_finder :
    my_str += Markup(str(count) +". " + str(i) + "<br>")
    count += 1

# The login Page
@app.route('/')
def home_page(): # Form
    return render_template('details.html')

# The output webpage
@app.route('/output', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      username = request.form['uname']
      the_path = request.form['path']
      data = request.form['inp']
      os.environ['username'] = username
      os.environ['the_path'] = the_path
      os.environ['data'] = data

      print(os.environ['data'])
      print(os.environ['the_path'])
      print(os.environ['username'])

      return redirect("/output", code=302)
   else:
      username = request.args.get('uname')
      text = text_extract.text_extract_func()
      summarize = summary.summary_func()
      name_finder = name_recog.name_recog_func()
      my_str = ("")
      count = 1
      for i in name_finder:
          my_str += Markup(str(count) + ". " + str(i) + "<br>")
          count += 1

      return render_template('index.html', output = text, sum_output = summarize, name_find = my_str)



if __name__ == '__main__':
    app.run(debug=True)
