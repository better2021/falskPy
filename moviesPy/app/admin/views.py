# 视图处理
# coding:utf8
from . import admin

@admin.route('/')
def index():
  return "<h2 style='color:blue'>admin</h2>"
