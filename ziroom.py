# -*- coding: utf-8 -*-
import load

url = 'http://vendor.ziroom.com/configuration/supplierDispatchOrderCheckOnline!list.action'
header = {
    'Accept': '*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'gr_user_id=0d9d9712-1993-404b-b9c8-d57beee25869; JSESSIONID=5CDDD5FE3DFA26D85EC5C71FC0F2DE22',
    'Host': 'vendor.ziroom.com',
    'Origin': 'http://vendor.ziroom.com',
    'Referer': 'http://vendor.ziroom.com/login.jsp',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
}
r = load.Ziroom(header)
### login
loginDict = {
    'j_username': 'V20150309013006',
    'j_password': 'V201503090',
}
r.access('http://vendor.ziroom.com/security/security!login.action', loginDict)

### choose city
cityDict = {
    'territoryId': '50',
    'username': 'V20150309013006',
}
r.access('http://vendor.ziroom.com/security/security!selectCity.action?territoryId=50&username=V20150309013006', cityDict)

### getUrllist
def getpage(_page):
    pageDict = {
        'filter_and_firstSendDate_GE_T': '2017-12-13',
        'filter_and_firstSendDate_LE_T': '2017-12-14',
        'filter_and_suspensionState_EQ_I': 1,
        '_pageNum': _page-1,
        '_pageSize': 12,
        'isDefault': 0,
        'pageNum': _page,
        'pageSize': 12,
    }
    return pageDict
for x in range(1,11):
    print(x)
    r.DownloadFiles('http://vendor.ziroom.com/configuration/supplierDispatchOrderCheckOnline!list.action', getpage(x),'z:/download/')
