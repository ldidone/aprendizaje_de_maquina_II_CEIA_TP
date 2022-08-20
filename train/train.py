# Importamos las librerías necesarias
import numpy as np
import pandas as pd
import mlflow

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import accuracy_score,plot_confusion_matrix,roc_auc_score, classification_report, confusion_matrix, precision_recall_curve, auc
from sklearn.tree import DecisionTreeClassifier

from sqlalchemy import create_engine

# Obtenemos los datos desde la base de datos
engine = create_engine('postgresql://your_db_user:your_db_password@host:port/your_database')
df = pd.read_sql_query('select * from "acoustic_extinguisher_fire_dataset"',con=engine)

# Formateamos los datos
columns = {
    'SIZE': 'size',
    'FUEL': 'fuel',
    'DISTANCE': 'distance',
    'DESIBEL': 'desibel',
    'AIRFLOW': 'airflow',
    'FREQUENCY': 'frequency',
    'STATUS': 'status',
}

df.rename(columns=columns, inplace=True)


# Definición de X e Y
X = df[['size', 'fuel', 'distance', 'desibel', 'airflow', 'frequency']]
y = df[['status']]

# Pipeline de pre-procesamiento
numeric_features = ['size', 'distance', 'desibel', 'airflow', 'frequency']
categorical_features = ['fuel']

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])

categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])


# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# decision tree model
decision_tree_model = Pipeline(steps=[('preprocessor', preprocessor),
                       ('classifier', DecisionTreeClassifier(criterion='gini', max_depth=30))])

# metric report
def metric_report(y_test, y_pred, y_proba):
    print(classification_report(y_test, y_pred))
    print('Area bajo la curva ROC:',np.round(roc_auc_score(y_test, y_proba[:,1]), 4))
    precision, recall,threshold=precision_recall_curve(y_test, y_proba[:,1]);
    print('Area bajo la curva Precision-Recall:',np.round(auc(recall, precision), 4))

# entrenamiento del modelo
mlflow.start_run()
decision_tree_model.fit(X_train, y_train)

# logueo del modelo
mlflow.sklearn.log_model(decision_tree_model, "decision_tree_model")


# testeo del modelo
y_pred = decision_tree_model.predict(X_test)
y_proba = decision_tree_model.predict_proba(X_test)
metric_report(y_test, y_pred, y_proba)
