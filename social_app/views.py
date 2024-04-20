from django.shortcuts import render


def Home(request):
    # Client secrets = a9ed1212f0e426fe211b4b19b63040aa8501a582

    #Client ID =0d78b8cb386aa5cb476e

    # google
   #Client secrets= 667804701841-bn35u3c3g3v0sd53faos9grnio969nbj.apps.googleusercontent.com
   
    #Client ID = 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
    return render(request,"home.html")





