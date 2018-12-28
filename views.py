from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.secret_key = '%we?jus7ine32|]we2DerFAsdw'
@app.route('/')
def index():
    from .forms import WikiForm
    form = WikiForm()
    return render_template('index.html', form=form)

@app.route('/wiki', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        from .wiki_engine import WikiEngine
        query = request.form('search')
        search_query = WikiEngine(query)
        return search_query.get_result()
    return redirect(url_for('index'))
