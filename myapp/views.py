from django.shortcuts import render, HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
nextId = 4


topics = [
{'id': 1, 'title': 'routing', 'body': 'routing is ..'},
{'id': 2, 'title': 'view', 'body': 'View is ..'},
{'id': 3, 'title': 'model', 'body': 'Model is ..'},

]


def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
        <html>
    <body>
        <h1><a href = "/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href ="/create/">create</a></li>
            <li>
                <form>
                    <input type="submit" value="delete">
                </form>
            </li>
        </ul>
    </body>
    </html>
    '''


def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form action ="/create/" method ="post">
                <p><input type ="text" name ="title" placeholder ="title"></p>
                <p><textarea name ="body" placeholder ="body"></textarea></P>
                <p><input type ="submit"></P>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))

    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "body": body}
        topics.append(newTopic)

        url = 'read/'+str(nextId)
        nextId = nextId + 1

        return redirect(url)


def read(request, id):
    global topics

    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
