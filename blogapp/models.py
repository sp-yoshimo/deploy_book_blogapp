from django.db import models

# Create your models here.
class BlogPost(models.Model):

    #カテゴリ➡タプルの第一要素はモデルが使用する値、第二要素は管理サイトの選択メニューに表示する文字列
    CATEGORY=(("science","科学のこと"),("food","食のこと"),("music","音楽のこと"))

    #タイトル用のフィールド
    title=models.CharField(verbose_name="タイトル",max_length=50)

    #本文用のフィールド
    content=models.TextField(verbose_name="本文")

    #投稿日時のフィールド
    posted_at=models.DateTimeField(verbose_name="投稿日時",auto_now_add=True)

    #カテゴリのフィールド
    category=models.CharField(verbose_name="カテゴリ",max_length=10,choices=CATEGORY)

    def __str__(self) -> str:
        return self.title
