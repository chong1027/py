def lo1(n):
    if(n!=None):
     if n=="台北"or n=="臺北":
        re=63
     elif n=="基隆":
        re=10017
     elif n=="新北":
        re=10001
     elif n=="宜蘭":
        re=10002
     elif n=="桃園":
        re=10003
     elif n=="新竹":
        re=10004
     elif n=="苗栗":
        re=10005
     elif n=="台中"or n=="臺中":
        re=10019
     elif n=="彰化":
        re=10007
     elif n=="南投":
        re=10008
     elif n=="雲林":
        re=10009
     elif n=="嘉義市":
        re=10010
     elif n=="嘉義縣":
        re=10020
     elif n=="台南"or n=="臺南":
        re=10021
     elif n=="高雄":
        re=64
     elif n=="屏東":
        re=10013
     elif n=="花蓮":
        re=10015
     elif n=="台東"or n=="臺東":
        re=10014
     elif n=="澎湖":
        re=10016
     elif n=="金門":
        re="09020"
     elif n=="連江":
        re="09007"
     else : print("請重新輸入")
     return re
    else: re=""

def MR(g):
    if(g!=None):
     if g=="MR":
        re="01"
     elif g=="MFR":
        re="02"
     elif g=="MFT":
        re="03"
     elif g=="HK":
        re="04"
     elif g=="AH":
        re="06"
     elif g=="HCI":
        re="07"
     elif g=="MFHRS":
        re="10"
     elif g=="MFE":
        re="08"
     elif g=="HR":
        re="13"
     elif g=="MFA":
        re=16
     else: print("請重新輸入")
     return re
    else: re=""