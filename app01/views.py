from django.shortcuts import render,HttpResponse

# Create your views here.
def show_msg(request):
    MSG =request.GET('test1')
    print(MSG)
    return render(request,'产能报表.html')



def get_msg(request):
    import requests

    # date_time =input("请输入日期 xxxx-xx-xxxx")

    cookies = {
        # 'UM_distinctid': '16b3c18bb7e117-0b45232ceb63d9-36664c08-100200-16b3c18bb7f26b',
        # 'JSESSIONID': '810E90761506E2739A8E76697B2B776F',
        'LtpaToken': 'AAECAzVEMTFDNDYxNUQxMjZEMjFTQzI1NDc5NOrIqF5mgp04UL2ZEnd9VZurWFU=',
    }

    headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    params = (
        ('method', 'data'),
        ('fdId', '16b53fb4f6f5e3b37d039a04b89b8dcd'),
        ('s_ajax', 'true'),
        ('q.docdate', '2019-06-23'),
    )

    response = requests.get('http://oa.sems1991.com:9000/dbcenter/echarts/db_echarts_table/dbEchartsTable.do',
                            headers=headers, params=params, cookies=cookies)

    print(response.text)
    return HttpResponse(response.text)