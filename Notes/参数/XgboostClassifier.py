# XgboostClassifier 的相关参数总结
# 官方API：https://xgboost.readthedocs.io/en/latest/python/python_api.html

paramaters_dict = {
	'max_depth':3,                      #树的深度
	'learning_rate':0.1,                #学习率
	'n_estimators':100,                 #弱学习器的个数
	'objective':'binary:logistic',      #目标损失函数
	'booster':'gbtree'                  #booster的类型 
	'verbosity':1,                      #运行时是否有信息，0为silent
	'silent':None,                      #与verbosity差不多
	'n_jobs':1,                         #并行的线程数
	'nthread':None,                     #与n_jobs差不多
	'gamma':0,                          #将叶节点分裂成中间节点的最小值
	'min_child_weight':1,               #
	'max_delta_step':0,                 #
	'subsample':1,                      #随机选择多少样本来建树
	'colsample_bytree':1,               #随机选择多少特征来建树
	'colsample_bylevel':1,              #
	'colsample_bynode':1,               #
	'reg_alpha':0,                      #L1正则化
	'reg_lambda':1,                     #L2正则化
	'scale_pos_weight':1,               #平衡正负样本
	'base_score':0.5,                   #初始预测的分，全局偏置
	'random_state':0,                   #随机数种子，为复现模型
	'seed':None,                        #与seed一样
	'missing':None                      #缺失值的处理
}

#可以利用GridSearchCV配合cv_params来挑选合适的参数，控制变量法。

#XGBoost有两种调用方式：
import XGBoost as xgb
# 这种调用方法是sklearn的方法，不需要对X_train和y_train做处理
model = xgb.XgboostClassifier(**paramaters_dict)
model.fit(X_train,y_train)

# 另一种是train的方法，利用param列表的方式来设置参数，该方法中n_estimators是无效的，转而利用num_round来设置次数
X_train = xgb.DMatrix(X_train,label=y_train,missing=np.nan)
model = xgb.train(paramaters_dict,X_train,num_round=100)


#http://xgboost.readthedocs.io/en/latest/python/python_api.html#xgboost.train
#http://xgboost.readthedocs.io/en/latest/python/python_api.html#xgboost.XGBRegressor
#两种调用方式并无太大差别