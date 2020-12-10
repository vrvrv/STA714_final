# 결측자료분석 기말 과제
STA 714 : Missing data analysis / Final project ( Fall 2020 )

## 결측 자료 생성  
```bash
python generate_missing.py
```
* [data](data) 에 원본 데이터 및 결측 포함 데이터 있음 
  - [boston.csv](data/boston.csv) : 원본 데이터
  - [boston_transform.csv](data/boston_transform.csv) : 정규성을 위해 변환시킨 데이터
  - [boston_nan.csv](data/boston_nan.csv) : 변환된 데이터에 결측을 발생시킨 데이터
* [데이터 EDA 및 MAR 확인](EDA.ipynb)