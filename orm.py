#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Simple ORM using metaclass '

class Field(object):

    def __init__(self, name, column_type):                       #定义Field类，它负责保存数据库表的字段名和字段类型：
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        #Parent.fun(self)
        super(StringField, self).__init__(name, 'varchar(100)')    #功能相当于上面引用父类的init函数，super（Class，self）.__init__(name,'')
                                                                   #,varchar(100)是数据库属性，代表100字节
class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')         #bigint是数据库属性，当超出int的范围时使用

class ModelMetaclass(type):                                        #元类，type，type是道，元类是一，类是二，实例是三

    def __new__(cls, name, bases, attrs):                        #元类的操作都在__new__中完成，(cls,name,base,attrs)cls是将创建的类，name 
        if name=='Model':                                        #（名）base（父类通常是object），attrs（类属性）分别代表我是谁，我从哪里来，我将到哪里去。
            return type.__new__(cls, name, bases, attrs)         #如果类名是Model那么就创建元类
        print('Found model: %s' % name)                          #
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
