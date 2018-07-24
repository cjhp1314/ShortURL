#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from libs import short_url


class DB(object):
    def __init__(self, db_kwargs):
        self.db = web.database(**db_kwargs)

    def exist_expand(self, url_md5):
        """检查数据库中是否已有相关记录，有则返回短 URL
        """
        result = self.db.where(table='url', what='shorten',
                               url_md5=url_md5)
        if result:
            return result[0]

    def add_url(self, long_url, url_md5):
        """添加 URL，返回短 URL
        """
        id_ = self.db.insert(tablename='url', seqname='id', shorten='',
                             expand=long_url)
   
        shorten = short_url.encode_url(id_)
        self.db.update(tables='url', shorten=shorten, url_md5=url_md5,
                       where='id=$id_', vars=locals())
        return web.storage(shorten=shorten)

    def get_expand(self, shorten):
        """根据短 URL 返回原始 URL
        """
        result = self.db.where(table='url', what='expand',
                               shorten=shorten)
        if result:
            return result[0]

    def get_last_data(self):
        result = self.db.select('url', order='id desc', limit=100)
        return result
