import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pandas as pd

# Use a service account.
cred = credentials.Certificate('./JARVIS/jarvis_database.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# データの読み込み
users_ref = db.collection('users')
docs = users_ref.stream()

users = []
indexes = []

for doc in docs:
    indexes.append(doc.id)
    users.append(doc.to_dict())
    # print(f'{doc.id} => {doc.to_dict()}')

df = pd.DataFrame(data=users, index=indexes, columns=[
                  'first_name', 'last_name', 'nick_name', 'age'])
# print(df)


def add_data(first_name, last_name, age, nick_name):
    """
    データの追加
    """
    db.collection('users').add({
        'first_name': first_name,
        'last_name': last_name,
        'nick_name': nick_name,
        'age': age
    })


def update_data():
    """
    データの更新
    """
    index_id = df.loc[df['nick_name'] == 'pandamegane'].index[0]
    first_name = 'masachika'
    last_name = 'togashi'
    nick_name = 'zz'
    age = 100
    users_ref = db.collection('users').document(index_id)
    users_ref.update({
        'first_name': first_name,
        'last_name': last_name,
        'nick_name': nick_name,
        'age': age
    })


# update_data()


# フィールドの削除
# user_ref = db.collection('users').document('suzuki')
# user_ref.update({
#     'nick_name': firestore.DELETE_FIELD
# })

# ドキュメントの削除
# db.collection('users').document('suzuki').delete()
