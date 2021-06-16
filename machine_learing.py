from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

dt_clf_iris = DecisionTreeClassifier(random_state=156)

iris_data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_data.data,

dt_clf_iris.fit(X_train, y_train)

from sklearn.tree import export_graphviz
export_graphviz(dt_clf_iris.......)

import graphviz 

# 시각화를 통해서 우선적으로 의사결정나무를 훑어본다!                   
# 왜 이렇게 나왔는데 물어보면, 의사결정나무로 설명해주면 된다. 분류든,,, 회귀분류 해 본다!!!
# 반드시 이해하기 위해서는 기본모델로 사용해야 한다. 
# 딥러닝은 중간과정을 알 수가 없다. 입력은 알고, 히든 레이어는 합쳐서 들어오니, 의미를 알 수가 없다. 그래서,
# 결과는 나오는 데, 과정을 알 수가 없다.
# 조금만 돌리고, 그 결과값을 의사결정의 입력으로 돌려서 시각적으로 확인가능하다.
# 한편, 일반화하는 조건인가? 노이즈데이터를 보지 않기 위해서는 가지치기를 제한하라!
# 오븐 온도를 150도로 할 것인지, 152도로 할 것인지? 이게 뭐가 중요한가와 비슷한 개념이다.

                                                
with open('tree.dot') as f:
    dot_grpah = f.read()
graphviz.Source(dot_graph)





                                                   
                                                    
                       
