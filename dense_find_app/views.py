from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView

from . import forms

#---------定型文----------
import tweepy

CONSUMER_KEY = "x1tSfyIRhTJGckl3wqCnbvPX4"
CONSUMER_SECRET = "moHqyx9HQ0gnKtMiChizYamHYKIZvkCj697w88DtKoqkuBwKGO"
ACCESS_TOKEN = "1151348998239748096-nWAVN3Ju5NKhOPQhPdy0Fa0iSMoVav"
ACCESS_SECERET = "34HfOwpJ0zH27QUrbgN76rWKFc207saZ3Ph4a6hbqLb6Z"

#OAuth認証
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECERET)

#TwitterAPIオブジェクト
api = tweepy.API(auth)
#-----------------------

#-----------------------------


# Create your views here.

class HomeView(FormView):
    template_name = "dense_find_app/index.html"  #dense_find_app/templates/dense_find_app/index.html
    form_class = forms.TextForm
    def form_valid(self, form):
        # form.cleaned_dataにフォームの入力内容が入っています
        tweets_list=[]
        print("pressed")
        data = form.cleaned_data
        coordinates = data["coordinates"]
        # ここで変換
        keyword = ""
        geocode = coordinates + ",1km"
        try:
            tweets = tweepy.Cursor(api.search, q=keyword, tweet_mode="extended", geocode=geocode).items()
            tweets_list  = [tweet._json for tweet in tweets]
        except tweepy.error.TweepError:
            print('Error')
        # テンプレートに渡す
        if tweets_list:
            ctxt = self.get_context_data(tweets_list=tweets_list, form=form)
            return self.render_to_response(ctxt)
        else:
            ctxt = self.get_context_data(tweets_list="error", form=form)
            return self.render_to_response(ctxt)
            
class TokyoView(TemplateView):
    template_name = "dense_find_app/tokyo.html" 
        
class NagoyaView(TemplateView):
    template_name = "dense_find_app/nagoya.html" 
        
class ShibuyaView(TemplateView):
    template_name = "dense_find_app/hideo.html" 


        
    
