from django import forms

class ContactForm(forms.Form):
    #formのフィールドをクラス変数として定義
    name=forms.CharField(label="お名前")
    email=forms.EmailField(label="メールアドレス")
    title=forms.CharField(label="件名")
    message=forms.CharField(label="メッセージ",widget=forms.Textarea)

    def __init__(self,*args, **kwargs):
        #ContactFormのコンストラクタ
        super().__init__(*args, **kwargs)

        #nameフィールドのplaceholderメッセージを登録
        self.fields["name"].widget.attrs["placeholder"]=\
            "お名前を入力してください"
        #nameフィールドを出力する<input>タグのclass属性を指定
        self.fields["name"].widget.attrs["class"]="form-control"

        #emailフィールドのplaceholderメッセージを登録
        self.fields["email"].widget.attrs["placeholder"]=\
            "メールアドレスを入力してください"
        #nameフィールドを出力する<input>タグのclass属性を指定
        self.fields["email"].widget.attrs["class"]="form-control"

        #titleフィールドのplaceholderメッセージを登録
        self.fields["title"].widget.attrs["placeholder"]=\
            "タイトルを入力してください"
        #nameフィールドを出力する<input>タグのclass属性を指定
        self.fields["title"].widget.attrs["class"]="form-control"

        #messageフィールドのplaceholderメッセージを登録
        self.fields["message"].widget.attrs["placeholder"]=\
            "メッセージを入力してください"
        #nameフィールドを出力する<input>タグのclass属性を指定
        self.fields["message"].widget.attrs["class"]="form-control"

