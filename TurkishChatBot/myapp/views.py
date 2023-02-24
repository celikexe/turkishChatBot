from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from myproject.chatbot import get_bot_response


# Türkçe stopwords listesi
stop_words = set(stopwords.words('turkish'))

# Snowball Stemmer'ı oluşturun
stemmer = SnowballStemmer('turkish')

# Veritabanı yerine örnek veriler kullanacağız
# Burada, kullanıcının mesajları ve botun vereceği yanıtlar örnek olarak verilmiştir.
data = {
    "merhaba": "Merhaba, nasıl yardımcı olabilirim?",
    "sipariş vermek istiyorum": "Lütfen sipariş vermek için web sitemizi ziyaret edin.",
    "ürünleriniz hakkında bilgi almak istiyorum": "Elbette, web sitemizdeki ürünlerimizi inceleyebilirsiniz.",
    "ürünlerinizdeki fiyatları öğrenmek istiyorum": "Fiyatlarımızı web sitemizde bulabilirsiniz."
}

def chatbot(request):
    if request.method == 'GET':
        message = request.GET.get('msg', '')
        response = get_bot_response(message)
        return JsonResponse({'response': response})
    # kullanıcının mesajını alın
    user_message = request.GET.get('msg')

    # mesajı küçük harfe dönüştürün ve kelimelere ayırın
    words = word_tokenize(user_message.lower())

    # stopwords ve stemmer kullanarak kelimeleri filtreleyin
    filtered_words = [stemmer.stem(w) for w in words if w not in stop_words]

    # veritabanında örnek yanıtları arayın ve en uygun yanıtı seçin
    response = ''
    for word in filtered_words:
        if word in data:
            response = data[word]
            break

    # yanıtı JSON olarak gönderin
    return JsonResponse({'response': response})


@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        message = request.POST['message']
        bot_response = get_bot_response(message)
        return JsonResponse({'response': bot_response})
    return render(request, 'index.html')