# 存放数据模型
#coding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from datatime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:709463253@localhost:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

'''
# 会员
class User(db.Model):
  __tablename__ = "user"
  id = db.Column(db.Integer,primary_key = True) # primary_key 主键
  name = db.Column(db.String(100),unique = True) # unique 唯一的
  email = db.Column(db.String(100),unique = True)
  phone = db.Column(db.String(11),unique = True)
  info = db.Column(db.Text) # Text 文本类型
  face = db.Column(db.String(255),unique = True) 
  addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)
  uuid = db.Column(db.String(255),unique = True) #uuid 唯一标志符 
  userlogs = db.relationship('Userlog',backref = 'user') # 会员日志外键关系关联
  comments = db.relationship('Comment',backref = 'user') # 评论外键关系关联
  moviecols = db.relationship('Moviecol',backref = 'user')

  def __repr__(self):
    return "<User %r>" % self.name


# 会员登录日志
class Userlog(db.Model):
  __tablename__ = 'userlog'
  id = db.Column(db.Integer,primary_key = True)
  user_id = db.Column(db.Integer,db.ForeignKet('user_id'))
  ip = db.Column(db.String(100))
  addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)

  def __repr__(self):
    return "<USerlog %r>" % self.id


# 标签
class Tag(db.Model):
  __tablename__ = 'tag'
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(100),unique = True) # unique 唯一的
  addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)
  movies = db.relationship("Movie",backref = 'tag') #电影外键关联

  def __repr__(set):
    return "<Tag %r>" % self.name


# 电影
class Movie(db.Model):
  __tablename__ = 'movie'
  id = db.Column(db.Integer,primary_key = True)
  title = db.Column(db.String(255),unique = True)
  url = db.Column(db.String(255),unique = True)
  info = db.Column(db.Text)
  logo = db.Column(db.SmallInteger)
  star = db.Column(db.SmallInteger) # star 星级
  playnum = db.Column(db.BigInteger) # playnum 播放量
  commentnum = db.Column(db.BigInteger)
  tag_id = db.Column(db.Integer,db.ForeignKey('tag_id'))
  area = db.Column(db.String(255))
  release_time = db.Column(db.Date) # release_time 上映时间
  length = db.Column(db.String(100))
  addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)
  comments = db.relationship("Comment",backref = 'movie') #电影外键关联
  moviecols = db.relationship('Moviecol',backref = 'movie')

  def __repr__(self):
    return "<Movie %r>" % self.title
  

  # 预告
  class Preview(db.Model):
    __tablename__ = 'preview'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),unique = True)
    logo = db.Column(db.SmallInteger) # 预告封面
    addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)

    def __repr__(self):
      return "<Preview %r>" % self.title

 # 评论
  class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer,db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)

    def __repr__(self):
      return "<Comment %r>" % self.id


  # 电影收藏
  class Moviecol(db.Model):
    __tablename__ = 'moviecol'
    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer,db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)

    def __repr__(self):
      return "<Moviecol %r>" % self.id     


  # 权限
  class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),unique = True)
    url = db.Column(db.String(255),unique = True)
    addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)

    def __repr__(self):
      return "<Auth %r>" % self.name     


  # 管理员
  class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),unique = True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger) # 0为超级管理员
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))
    addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)
    adminlogs = db.relationship('Adminlog',backref = 'admin')
    oplogs = db.relationship('Oplog',backref = 'admin')

    def __repr__(self):
      return "<Admin %r>" % self.name    


  # 管理员登录日志
  class Adminlog(db.Model):
    __tablename__ = 'adminlog'
    id = db.Column(db.Integer,primary_key = True)
    ip = db.Column(db.String(100))
    admin_id = db.Column(db.Integer,db.ForeignKey('admin.id'))
    addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)

    def __repr__(self):
      return "<Adminlog %r>" % self.name       


  # 操作日志
  class Oplog(db.Model):
    __tablename__ = 'oplog'
    id = db.Column(db.Integer,primary_key = True)
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(600))
    admin_id = db.Column(db.Integer,db.ForeignKey('admin.id'))
    addTime = db.Column(db.DateTime,index = True ,default = datatime.utcnow)

    def __repr__(self):
      return "<Oplog %r>" % self.name   

'''

# 角色
class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(255),unique = True)
  email = db.Column(db.String(100),unique = True)

  def __repr__(self):
    return "<Role %r>" % self.name  


if __name__=="__main__":

  role = Role(
    name = '管理员',
    email = '12545255@qq.com'
  )
  db.session.add(role)
  db.session.commit()