import pandas as pd

# 데이터 읽기
df = pd.read_csv(r"C:\Users\Yechan\Desktop\Study\4-1\비즈니스 어낼리틱스\연구\tsmixer\dataset\weather.csv")

# location과 company 컬럼 제거
df = df.drop(['location', 'company'], axis=1)

# 새로운 CSV 파일로 저장
output_path = r'./filtered_dataset.csv'
df.to_csv(output_path, index=False)

# 결과 확인
df.head()
