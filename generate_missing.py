import pandas as pd
import numpy as np

import copy

from scipy.stats import bernoulli

from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from scipy.stats import boxcox


def read_and_transform(path):
	pt = preprocessing.PowerTransformer(copy=True)
	data = pd.read_csv('./data/boston.csv')

	# 변환 (정규성) - Boxcox transformation
	data['LSTAT'], _ = boxcox(data['LSTAT'])

	# 변환 (정규성) - Yeo-Johnson transformation
	data['CRIM'] = np.log(data['CRIM']/(100-data['CRIM']))
	pt.fit(np.array(data['CRIM']).reshape(-1,1))
	data['CRIM']=pt.transform(np.array(data['CRIM']).reshape(-1,1))

	data['PTRATIO'] = np.log(data['PTRATIO']/(100-data['PTRATIO']))
	pt.fit(np.array(data['PTRATIO']).reshape(-1,1))
	data['PTRATIO']=pt.transform(np.array(data['PTRATIO']).reshape(-1,1))
	data.to_csv(path + '/boston_transform.csv', index_label = 'original_idx')

	return data

def ampute(data, i, path):
	data = data.copy()

	# 결측 변수 및 결측 비율 선정
	miss_cov = ['RM', 'LSTAT', 'RAD', 'CRIM', 'PTRATIO']

	# 결측 생성 

	scaler = preprocessing.StandardScaler()

	# 결측변수 RM : 주택 1가구당 평균 방의 개수

	## Latent variable 을 만든데 사용할 변수 설정
	selected_cov = ['ZN', 'NOX', 'CHAS', 'B', 'LSTAT']

	## Latent variable 설정
	z = scaler.fit_transform(data[selected_cov])
	z = pd.DataFrame(z, columns = selected_cov)
	z = -z['ZN']+1.2*z['NOX']+0.3*z['CHAS']+0.1*z['B']-0.6*z['LSTAT']
	z = 1/(1+np.exp(-z))
	# missing_indicator
	m_rm = bernoulli(z).rvs()

	# 결측변수 LSTAT : 모집단의 하위계층의 비율(%)
	data_ = data.iloc[m_rm==1]
	selected_cov = ['CRIM', 'ZN', 'AGE', 'DIS', 'B']
	z = scaler.fit_transform(data_[selected_cov])
	z = pd.DataFrame(z, columns = selected_cov)
	z = -0.5*z['CRIM']-0.6*z['ZN']-0.25*z['AGE']-0.6*z['DIS']-1.2*z['B']+2.5

	# 결측 발생 확률
	z = (1/(1+np.exp(-z)))

	# missing indicator
	m_lstat = bernoulli(z).rvs()

	# 결측변수 RAD : 1000(Bk-0.63)^2, 여기서 Bk는 자치시별 흑인의 비율을 말함
	data_ = data_.iloc[m_lstat==1]
	selected_cov = ['TAX', 'AGE', 'ZN', 'DIS', 'PTRATIO']
	z = scaler.fit_transform(data_[selected_cov])
	z = pd.DataFrame(z, columns = selected_cov)
	z = -0.5*z['TAX']-0.6*z['AGE']-0.6*z['ZN']-0.5*z['DIS']-1.2*z['PTRATIO']+1.5

	# 결측 발생 확률
	z = (1/(1+np.exp(-z)))

	# missing indicator
	m_rad = bernoulli(z).rvs()

	# 결측변수 CRIM : 자치시(town) 별 1인당 범죄율
	data_ = data_.iloc[m_rad==1]
	selected_cov = ['PTRATIO', 'NOX', 'TAX', 'AGE']
	z = scaler.fit_transform(data_[selected_cov])
	z = pd.DataFrame(z, columns = selected_cov)
	z = -0.5*z['PTRATIO']-0.6*z['NOX']-0.6*z['TAX']-0.5*z['AGE']+1.1

	# 결측 발생 확률
	z = (1/(1+np.exp(-z)))

	# missing indicator
	m_crim = bernoulli(z).rvs()

	# 결측변수 PTRATIO : 자치시(town)별 학생/교사 비율
	data_ = data_.iloc[m_crim==1]
	selected_cov = ['DIS', 'ZN', 'CHAS', 'TAX']
	z = scaler.fit_transform(data_[selected_cov])
	z = pd.DataFrame(z, columns = selected_cov)
	z = -0.5*z['DIS']-0.6*z['ZN']-0.6*z['CHAS']-0.5*z['TAX']+0.8

	# 결측 발생 확률
	z = (1/(1+np.exp(-z)))

	# missing indicator
	m_ptratio = bernoulli(z).rvs()

	m_rm_ = [i for i, m in zip(data.index, m_rm) if m==1]
	m_lstat_ = [i for i, m in zip(m_rm_, m_lstat) if m==1]
	m_rad_ = [i for i, m in zip(m_lstat_, m_rad) if m==1]
	m_crim_ = [i for i, m in zip(m_rad_, m_crim) if m==1]
	m_ptratio_ = [i for i, m in zip(m_crim_, m_ptratio) if m==1]

	data.loc[m_rm_, 'RM'] = np.nan
	data.loc[m_lstat_, 'LSTAT'] = np.nan
	data.loc[m_rad_, 'RAD'] = np.nan
	data.loc[m_crim_, 'CRIM'] = np.nan
	data.loc[m_ptratio_, 'PTRATIO'] = np.nan

	data = data[['RM', 'LSTAT', 'RAD', 'CRIM', 'PTRATIO', 'DIS', 'ZN',
				 'NOX', 'CHAS', 'B', 'TAX','INDUS', 'AGE', 'MEDV']]


	data.sort_values(by=['RM', 'LSTAT', 'RAD', 'CRIM', 'PTRATIO'],
                     na_position='first',
                     inplace=True)

	data.to_csv(path + '/nan/boston_nan_'+str(i)+'.csv', index_label = 'original_idx')

if __name__ == '__main__':
	path = './data'
	data = read_and_transform()
	for i in range(1, 1+100):
		ampute(data, i, path)



