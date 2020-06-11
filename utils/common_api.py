#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: common_api.py
# @time:2020/6/9 11:50 

import requests
from utils.config_util import cfg

def get_access_token_api(grant_type,appid,secret):
    api_url = cfg.hosts+'/cgi-bin/token'
    get_param_data = {
        'grant_type': grant_type,
        'appid': appid,
        'secret': secret}
    response =requests.get(url=api_url,
                           params=get_param_data)
    return response

def get_access_token_value():
    response = get_access_token_api('client_credential',
                                 'aaa',
                                 'bbb')
    # print(response.json()['access_token'])
    return response.json()['access_token']

def create_user_tag_api(token,tag_name):
    api_url = cfg.hosts + '/cgi-bin/tags/create'
    get_param_data = {
        'access_token': token}
    header_info = {
        'Content-Type': 'application/json'}
    post_param_data ={   "tag" : {     "name" : tag_name  } }

    response = requests.post(url=api_url,
                            params=get_param_data,
                            headers=header_info,
                            json=post_param_data)
    return response

def get_uesr_tag_api(token):
    api_url = cfg.hosts + '/cgi-bin/tags/get'
    get_param_data = {
        'access_token': token}
    response = requests.post(url=api_url,
                             params=get_param_data)
    return response

def update_user_tag_api(token,tag_id,tag_name):
    api_url = cfg.hosts + '/cgi-bin/tags/update'
    get_param_data = {
        'access_token': token}
    header_info = {
        'Content-Type': 'application/json'}
    post_param_data = {   "tag" : {     "id" : tag_id,     "name" : tag_name   } }
    response = requests.post(url=api_url,
                             params=get_param_data,
                             headers=header_info,
                             json=post_param_data)
    return response

def delete_user_tag_api(token,tag_id):
    api_url = cfg.hosts + '/cgi-bin/tags/delete'
    get_param_data = {
        'access_token': token}
    header_info = {
        'Content-Type': 'application/json'}
    post_param_data = {   "tag":{        "id" : tag_id   } }
    response = requests.post(url=api_url,
                             params=get_param_data,
                             headers=header_info,
                             json=post_param_data)
    return response

def get_user_fans_list_api(token,tag_id):
    api_url = cfg.hosts + '/cgi-bin/user/tag/get'
    get_param_data = {
        'access_token': token}
    header_info = {
        'Content-Type': 'application/json'}
    post_param_data = {   "tagid" : tag_id,   "next_openid":""}
    response = requests.post(url=api_url,
                             params=get_param_data,
                             headers=header_info,
                             json=post_param_data)
    return response

if __name__ == '__main__':
    get_uesr_tag_api(get_access_token_value())
