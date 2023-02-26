from apiclient.discovery import build
import json
import pandas as pd


# # jsonファイルからAPIKEYの取得
# with open('JARVIS/Streamlit_app/jarvis-youtube.json') as f:
#     secret = json.load(f)

# DEVELOPER_KEY = secret['KEY']
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"
# # 認証を行っている
# youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
#                 developerKey=DEVELOPER_KEY)


def video_search(youtube, q, max_results=30):
    response = youtube.search().list(
        # 検索クエリを指定している
        q=q,
        part="id,snippet",
        # リソースの並べ替え方法を指定(今回は視聴回数)
        order='viewCount',
        # クエリの対象を特定のタイプのみに制限する
        type='video',
        # 何件取得するか
        maxResults=max_results
        # リクエストを叩く
    ).execute()
    items_id = []
    items = response['items']
    # 動画のIDととのチャンネルIDを辞書で取り出しリストへ格納する
    for item in items:
        item_id = {}
        item_id['video_id'] = item['id']['videoId']
        item_id['channel_id'] = item['snippet']['channelId']
        items_id.append(item_id)
    # リストに格納した動画IDとチャンネルIDの辞書をdfに格納する
    df_video = pd.DataFrame(items_id)
    return df_video


def get_results(youtube, df_video, threshold):
    channel_ids = df_video['channel_id'].unique().tolist()
    # print(channel_ids[:3])

    subscriber_list = youtube.channels().list(
        # チャンネルIDをカンマ区切りで格納、idの条件
        id=','.join(channel_ids),
        part="statistics",
        fields='items(id,statistics(subscriberCount))'
        # リクエストを叩く
    ).execute()

    subscribers = []
    for item in subscriber_list['items']:
        subscriber = {}
        if len(item['statistics']) > 0:
            subscriber['channel_id'] = item['id']
            subscriber['subscriber_count'] = int(
                item['statistics']['subscriberCount'])
        else:
            subscriber['channel_id'] = item['id']
        subscribers.append(subscriber)
    # print(subscribers)

    df_subscribers = pd.DataFrame(subscribers)
    # print('デバック', df_subscribers.head())
    # print('デバック', df_video.head())

    df = pd.merge(left=df_video, right=df_subscribers, on='channel_id')
    # print(df.head())
    df_extracted = df[df['subscriber_count'] < threshold]
    # print('デバック:df_extracted', df_extracted.empty)
    if df_extracted.empty:
        return '検索結果はありません'
    else:
        video_ids = df_extracted['video_id'].tolist()
        # print('デバック:video_ids', video_ids)

        videos_list = youtube.videos().list(
            # チャンネルIDをカンマ区切りで格納、idの条件
            id=','.join(video_ids),
            part="snippet,statistics",
            fields='items(id,snippet(title),statistics(viewCount))'
        ).execute()

    # print('デバック',videos_list['items'][:3])
    videos_info = []
    for item in videos_list['items']:
        video_info = {}
        video_info['video_id'] = item['id']
        video_info['title'] = item['snippet']['title']
        video_info['view_count'] = item['statistics']['viewCount']
        # print('デバック', video_info)
        videos_info.append(video_info)
    # print('デバック', videos_info)

    df_video_info = pd.DataFrame(videos_info)

    results = pd.merge(left=df_extracted, right=df_video_info, on='video_id')
    results = results.loc[:, ['video_id', 'title',
                              'view_count', 'subscriber_count', 'channel_id']]
    return results

# df_video = video_search(youtube, q='コレコレ', max_results=50)
# results = get_results(
#     youtube, df_video, threshold=10000)
# print(results)