import pandas as pd
file_path = 'data/data_after_2.csv' #파일 경로
pd.set_option('mode.chained_assignment',  None) # 입출력을 제어하기 위한 코드입니다.
########################################코드##########################################

df = pd.read_csv(file_path)

#10점 더한다
for i in range(len(df)):
	if df.iloc[i, 1] + 10 <= 100:
		df.iloc[i,1] += 10
	#10점 더했을때 100을 초과할때 점수를 100으로 바꿔준다
	else:
		df.iloc[i,1] = 100

#교수님 코드 
#df['국어'] += 10
#df.loc[df['국어'] > 100, '국어'] = 100


#####################################################################################

print(df)



