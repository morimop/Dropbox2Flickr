# coding=utf-8   

import os
import dropbox
dbx = dropbox.Dropbox(os.environ.get("DROPBOX_API_KEY"))

import flickr_api
auth_handler = flickr_api.auth.AuthHandler(
  os.environ.get("FLICKR_API_KEY"),
  os.environ.get("FLICKR_API_SECRET"),
  access_token_key=os.environ.get("FLICKR_ACCESS_KEY"),
  access_token_secret=os.environ.get("FLICKR_ACCESS_SECRET"))

flickr_api.set_auth_handler(auth_handler)

def get_path_for_camera_upload_jp():
    for entry in dbx.files_list_folder('').entries:
        if(entry.name == u'\u30ab\u30e1\u30e9\u30a2\u30c3\u30d7\u30ed\u30fc\u30c9'):
            return entry.path_lower

def transfer():
    target_folder_path = get_path_for_camera_upload_jp()
    print("target_path:" + target_folder_path)
    entries = dbx.files_list_folder(target_folder_path).entries
    print("entries : {0}".format(len(entries)))
    for entry in entries :
        if isinstance(entry, dropbox.files.FileMetadata):
            print("process :" + entry.name)
            target_filepath_tmp = '/tmp/' + entry.name
            dbx.files_download_to_file(target_filepath_tmp, entry.path_lower)
            flickr_api.upload(photo_file=target_filepath_tmp, title=entry.name)
            dbx.files_move(
                entry.path_lower,
                target_folder_path + "/processed/" + entry.name,
                autorename=True)
            print('done')

transfer()
