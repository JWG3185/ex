import pandas as pd

url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire?serviceKey=Zv%2FutM8zPV4Cpby0tQi%2FtiDmHPhc19Zr67HNB4XUKyLt89VHIxcmVtAdRSWES5ve3JQGe4P3OL6dyL6vChTt8Q%3D%3D&STAGE1=%EB%B6%80%EC%82%B0%EA%B4%91%EC%97%AD%EC%8B%9C&pageNo=1&numOfRows=100'
df1 = pd.read_xml(url, xpath='.//item')
df1_c = df1.copy()
df2 = df1_c[['dutyName','hpid','hvec','hvoc', 'dutyTel3']]
df2_c = df2.rename(columns={'dutyName':'병원명', 'hpid':'병원코드', 'hvoc':'수술실수', 'dutyTel3':'응급실연락처','hvec':'응급실수'})

df2_c
