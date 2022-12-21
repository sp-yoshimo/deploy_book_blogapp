from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import BlogPost
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.
class IndexView(ListView):

    #テンプレートレンダリングに特化したTemplateViewを継承

    #index.htmlをレンダリングする
    template_name="index.html"

    #object_listキーの別名を設定
    context_object_name="orderby_records"
    #モデルBlogPostのオブジェクトにordeer_by()を適用して投稿日時の降順に並び変える
    queryset=BlogPost.objects.order_by("-posted_at")

    #1ページに表示するレコードの件数を設定
    paginate_by=4


class BlogDetail(DetailView):
    #詳細ページのビュー

    template_name="post.html"

    #クラス変数modelにモデルBlogPostを設定
    model=BlogPost

class ScienceView(ListView):
    #Scienceカテゴリのビュー

    template_name="science_list.html"

    model=BlogPost

    context_object_name="science_records"
    queryset=BlogPost.objects.filter(category="science").order_by("-posted_at")

    paginate_by=2


class FoodView(ListView):
    #foodカテゴリのビュー

    template_name="food_list.html"

    model=BlogPost

    context_object_name="food_records"
    queryset=BlogPost.objects.filter(category="food").order_by("-posted_at")

    paginate_by=2


class MusicView(ListView):
    #Musicカテゴリのビュー

    template_name="music_list.html"

    model=BlogPost

    context_object_name="music_records"
    queryset=BlogPost.objects.filter(category="music").order_by("-posted_at")

    paginate_by=2

class ContactView(FormView):
    #問い合わせページのビュー
    template_name="contact.html"

    form_class=ContactForm

    #送信完了時にリダイレクトするページ
    success_url=reverse_lazy("blogapp:contact")

    def form_valid(self, form):

        #フォームに入力されたデータをフィールド名を指定して取得
        name=form.cleaned_data["name"]
        email=form.cleaned_data["email"]
        title=form.cleaned_data["title"]
        message=form.cleaned_data["message"]

        subject="お問い合わせ:{}".format(title)
        #フォームの入力データの書式を設定
        message=\
            "送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:{3}\n"\
            .format(name,email,title,message)
        #送信先のアドレス
        to_list=["yoshi.syun8@gmail.com"]
        #EmailMessageオブジェクトを生成
        message=EmailMessage(subject=subject,body=message,to=to_list)
        #send()でメールを送信
        message.send()

        #送信完了後に表示するメッセージ
        messages.success(self.request,"お問い合わせは正常に送信されました。")
        return super().form_valid(form)