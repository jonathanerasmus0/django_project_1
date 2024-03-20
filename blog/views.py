from django.shortcuts import render
posts =[{
    'author': 'Jonathan Davies',
    'title': 'This is a sample blog post.',
    'content': 'This is a sample blog post',
    'date_posted': 'March 2024',
},
        {'author': 'Jonathan Erasmus Davies',
    'title': 'This is a sample blog post 2.',
    'content': 'This is a sample blog post 2',
    'date_posted': 'April 2024'}
        ]

def home(request):
    context ={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
 return render(request, 'blog/about.html',{title: 'About'})

