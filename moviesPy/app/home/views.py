# 视图处理
# coding:utf8
from . import home

@home.route('/')
def index():
  return "<h2 style='color:green'>flask</h2>"
