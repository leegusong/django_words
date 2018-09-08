from django.shortcuts import render
import pandas as pd
import random


# Create your views here.
def post_list(request):
    df = pd.read_csv('words.csv', encoding='cp949')
    words = df['word']
    word = random.choice(words)

    meaning = df[words == word]['meaning']

    # 다른 보기 만들기
    choices = random.sample(set(df[df['meaning'] != meaning]['meaning']), 3)
    choices.append(meaning)
    random.shuffle(choices)

    return render(request, 'blog/post_list.html', {'word': word, 'definition': meaning, 'choices': choices})
