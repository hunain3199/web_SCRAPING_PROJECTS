
import instaloader

username = 'nadiastrakerbahamas'
password = 'INSTAGRAM02022022'

L = instaloader.Instaloader()
L.post_metadata_txt_pattern = ""
L.download_geotags = False
L.save_metadata = False
L.save_metadata_json = False
L.download_comments = False
# Login or load session

L.login(username, password)#this should be your own username and #password
profile = instaloader.Profile.from_username(L.context, username)
L.download_saved_posts(max_count=1000, fast_update=False, post_filter=None)