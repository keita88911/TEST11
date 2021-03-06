# -*- coding: UTF-8 -*-
import datetime
import MySQLdb
import sys

import time

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class sql():
    @classmethod
    def openDB(self):
        self.db = MySQLdb.connect("119.23.12.94", "root", "tm123456tm", "testData", charset='utf8')
        return self.db

    # 登录
    @classmethod
    def getsqldata(self, name, password):
        tt = time.time()
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        id = []
        taskId = []

        sql = "SELECT * FROM user where username='%s' and  password='%s'" % (name, password)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        for cow in results:
            # print(cow)
            if cow:
                db.close()
                print('SQL Time used: {} sec'.format(time.time() - tt))
                return cow
            else:
                db.close()
                return False

    # 周报查询
    @classmethod
    def SearchData(self, userid, roleid, person=None, start=None, end=None):
        db = self.openDB()

        cursor = db.cursor()
        id = []
        text = []
        startdata = "2000-11-21"

        enddata = "2060-11-01"
        order = " ORDER BY createData DESC"
        if int(roleid) != 1:
            sql = "SELECT * from `week-report`where id like '%'"
            # print("enter 22")
            if userid:
                sql = sql + "and userid =" + "'" + str(userid) + "'"

            if person:
                sql = sql + "and username like" + "'" + str(person) + "%'"
            if start:
                startdata = start
            if end:
                '''
                 时间加1天
                '''
                enddata = str(datetime.datetime.strptime(end, "%Y-%m-%d") + datetime.timedelta(days=1))

            if start or end:
                sql = sql + "and (createData >'" + startdata + "'" + "  AND createData <'" + enddata + "')"
            # if end:
            #     enddata=end
            #     sql = sql + "and (createData >'" + startdata + "'" + "  and createData <'" + enddata + "')"
            sql = sql + order
        else:
            sql = "SELECT * from `week-report`where id like '%'"
            if person:
                sql = sql + "and username like" + "'" + str(person) + "%'"
            if start:
                startdata = start
            if end:
                '''
                 时间加1天
                '''
                enddata = str(datetime.datetime.strptime(end, "%Y-%m-%d") + datetime.timedelta(days=1))

            if start or end:
                sql = sql + "and (createData >'" + startdata + "'" + "  AND createData <'" + enddata + "')"

            sql = sql + order

        print(sql)
        # sql="sql1"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        for cow in results:
            # print(cow)
            if cow:
                text.append(cow)

            else:
                db.close()
                return False
        # print(text)
        db.close()
        return text

    # 周报新增
    @classmethod
    def Add(self, title, username, userid, text):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        title = MySQLdb.escape_string(title)
        text = MySQLdb.escape_string(text)
        sql = "INSERT INTO `week-report`(`title`, `username`, `userid`, `text`, `createData`, `updata`) VALUES ( '%s', '%s','%s', '%s', NOW(), NOW()) " % (
            title, username, userid, text)
        # sql= "insert into `week-report` (`title`, `username`, `userid`, `text`, `createData`, `updata`) values('xljipo3','admin','2','this is test',NULL,NULL)"
        cursor.execute(sql)
        cursor.connection.commit()

        db.close()
        return True

    # 周报详情
    @classmethod
    def Detail(self, reportid):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        id = []
        taskId = []

        sql = "SELECT * from `week-report` WHERE id ='%s'" % (reportid)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        for cow in results:
            # print(cow)
            if cow:
                db.close()
                # print(cow)
                return cow
            else:
                db.close()
                return False

    # 用户详情
    @classmethod
    def Detail_Person(self, userid):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        id = []
        taskId = []

        sql = "SELECT * from `user` WHERE id ='%s'" % (userid)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(sql)
        for cow in results:
            # print(cow)
            if cow:
                db.close()
                # print(cow)
                return cow
            else:
                db.close()
                return False

    # 更新周报信息
    @classmethod
    def Updata(self, reportid, title=None, text=None):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据

        cursor = db.cursor()
        title = MySQLdb.escape_string(title)
        text = MySQLdb.escape_string(text)
        sql = "UPDATE `week-report` SET title = '%s' ,text='%s' WHERE id ='%s'" % (title, text, reportid,)

        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        cursor.execute(sql)
        cursor.connection.commit()
        db.close()

    # 更新用户信息
    @classmethod
    def Updata_PerSon(self, userid_person, username, password, roledid):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据

        cursor = db.cursor()
        username = MySQLdb.escape_string(username)
        password = MySQLdb.escape_string(password)
        sql = "UPDATE `user` SET  `username` = '%s' ,password='%s' ,roleid='%s' WHERE id ='%s'" % (
        username, password, roledid, userid_person)

        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        cursor.execute(sql)
        cursor.connection.commit()
        db.close()
        return True

    # 删除用户
    @classmethod
    def Delete_Person(self, id):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        if type(id).__name__ == 'list':
            for i in id:
                print(i)
                sql = " DELETE FROM `user` WHERE id = '%s'" % (i)
                cursor = db.cursor()
                cursor.execute(sql)
                cursor.connection.commit()
            db.close()
            return True
        cursor = db.cursor()

        sql = " DELETE FROM `user` WHERE id = '%s'" % (id)

        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        cursor.connection.commit()
        db.close()
        return True

    # 用户查询
    @classmethod
    def PerSonNal(self, roleid=None, username=None):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        id = []
        text = []
        startdata = "2000-11-21"

        enddata = "2060-11-01"
        if username:
            username = MySQLdb.escape_string(username)
        sql = "SELECT * from `user`where id like '%'"
        # print("enter 22")
        if username:
            sql = sql + "and username =" + "'" + str(username) + "'"

        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)

        for cow in results:
            # print(cow)
            if cow:

                text.append(cow)
            else:
                db.close()
                return False
        db.close()
        # print(text)
        return text

    # 新增用户
    @classmethod
    def Add_Person(self, username, password, roleid):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        username = MySQLdb.escape_string(username)
        password = MySQLdb.escape_string(password)
        sql = "SELECT * from `user`where username = '%s'" % username
        cursor.execute(sql)
        if cursor.fetchall():
            msg = "用户名已存在"
            print(msg)
            db.close()
            return False, msg
        else:
            sql = "INSERT INTO `user`( `username`,  `password`, `roleid`) VALUES ( '%s', '%s','%s') " % (
                username, password, roleid)
            # sql= "insert into `week-report` (`title`, `username`, `userid`, `text`, `createData`, `updata`) values('xljipo3','admin','2','this is test',NULL,NULL)"
            cursor.execute(sql)
            cursor.connection.commit()
            msg = "创建成功"
            # print(msg)
            db.close()
            return True, msg

    # 周报姓名查询
    @classmethod
    def SearchPerSon(self, username):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        id = []
        text = []

        sql = "SELECT * from `user`where id like '%'"
        if username:
            sql = sql + "and username like" + "'" + str(username) + "%'"
        print(sql)
        # sql="sql1"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        for cow in results:
            # print(cow)
            if cow:
                text.append(cow)

            else:

                return False
        # print(text)
        db.close()
        return text

    # 用户导出
    @classmethod
    def PerSonNal_export(self, roleid=None, username=None):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        id = []
        text = []
        startdata = "2000-11-21"

        enddata = "2060-11-01"

        sql = "SELECT * from `user`where id like '%'"
        # print("enter 22")
        if username:
            sql = sql + "and username =" + "'" + str(username) + "'"

        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results

    # 用户导入
    @classmethod
    def PerSonNal_import(self, username, password, roleid):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        cursor.execute("select * from `user` where  username='%s'" % username)
        results = cursor.fetchall()
        if results:
            msg = username + ":  用户已存在"
            print(msg)
            return False, msg
        try:
            sql = "INSERT INTO `user` (`username`,`password`,`roleId`)VALUES('%s','%s','%s')" % (
            username, password, roleid)
            # print("enter 22")
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.connection.commit()
            db.close()
            msg = username + ':  导入成功'
            # print(msg)
            return True, msg
        except:
            db.close()
            msg = username + ':  导入失败'
            # print(msg)
            return False, msg

    # 手机list
    @classmethod
    def Borrow_Phone(self):
        db = self.openDB()
        cursor = db.cursor()
        sql = " SELECT * from borrow_phone"
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results

    # 归还
    @classmethod
    def Return_Phone(self, returnname, phontid, remark):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        # state='1'
        # borrowname=''
        # datatime='NULL'
        # phonemark=''
        cursor = db.cursor()

        sql = "UPDATE `borrow_phone` SET  `state` = '1' ,borrowname='--' ,returnname='%s',datatime= NOW(),phonemark='%s' WHERE id ='%s'" % (
        returnname, remark, phontid)

        print(sql)
        cursor.execute("SELECT * from borrow_phone where id ='%s'" % phontid)
        results = cursor.fetchall()
        if results:
            # print(results)
            cursor.execute(sql)
            cursor.connection.commit()
            db.close()
            cursor.close()
            # print(u"成功")
            return True
        else:
            db.close()
            cursor.close()
            # print(u"失败")
            return False

    # 借出
    @classmethod
    def Borrow(self, borrowname, phontid, remark):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        # state='1'
        cursor = db.cursor()
        sql = "UPDATE `borrow_phone` SET  `state` = '2' ,borrowname='%s' ,returnname='--',datatime= NOW(),phonemark='%s' WHERE id ='%s'" % (
        borrowname, remark, phontid)

        print(sql)
        cursor.execute("SELECT * from borrow_phone where id ='%s'" % phontid)

        results = cursor.fetchone()

        # print(type(results))
        if results:
            # print(results)
            cursor.execute(sql)
            cursor.connection.commit()
            db.close()
            cursor.close()
            # print(u"成功")
            return True
        else:
            db.close()
            cursor.close()
            # print(u"失败")
            return False

    # 借阅查询
    @classmethod
    def Searchphone(self, phonename=None, start=None, end=None, borrow_state=None):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()

        text = []
        startdata = "2000-11-21"

        enddata = "2060-11-01"

        sql = "SELECT * from `borrow_phone`where id like '%'"

        # print("enter 22")

        if phonename:
            sql = sql + "and phonename like" + "'" + str(phonename) + "%'"
        if start:
            startdata = start
        if end:
            '''
             时间加1天
            '''
            enddata = str(datetime.datetime.strptime(end, "%Y-%m-%d") + datetime.timedelta(days=1))

        if start or end:
            sql = sql + "and (datatime >'" + startdata + "'" + "  AND datatime <'" + enddata + "')"
        if borrow_state:
            sql = sql + "and state='" + borrow_state + "'"

        cursor.execute(sql)
        results = cursor.fetchall()
        print(sql)
        for cow in results:
            # print(cow)
            if cow:
                text.append(cow)

            else:

                return False
        # print(text)
        db.close()
        return text

    # 新增用户
    @classmethod
    def Add_Phone(self, phonename, phonecode):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        phonename = MySQLdb.escape_string(phonename)
        phonecode = MySQLdb.escape_string(phonecode)
        sql = "SELECT * from `borrow_phone`where phonecode = '%s'" % phonecode
        cursor.execute(sql)
        if cursor.fetchall():
            msg = "该物品编码已存在"
            print(msg)
            db.close()
            return False, msg
        else:
            sql = "INSERT INTO `borrow_phone`( `phonename`,  `phonecode`,`state`,`borrowname`,`returnname`,`datatime`,`phonemark`) VALUES ( '%s', '%s','1','--','--',NOW(),'--') " % (
                phonename, phonecode)
            # sql= "insert into `week-report` (`title`, `username`, `userid`, `text`, `createData`, `updata`) values('xljipo3','admin','2','this is test',NULL,NULL)"
            cursor.execute(sql)
            cursor.connection.commit()
            msg = "创建成功"
            # print(msg)
            db.close()
            return True, msg
    #获取指定的手机
    @classmethod
    def Delete_Phone(self, id):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        if type(id).__name__ == 'list':
            for i in id:
                # print(i)
                sql = " DELETE FROM `borrow_phone` WHERE id = '%s'" % (i)
                print(sql)
                cursor = db.cursor()
                cursor.execute(sql)
                cursor.connection.commit()
            db.close()
            return True
        else:
            return False

    # 读取所需项目接口
    @classmethod
    def get_api(self, porjectid=None):
        tt = time.time()
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        text = []
        # sql = "SELECT * FROM api_work where projectsID= '%s' " % (porjectid)
        sql = "SELECT * FROM api_work  "
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        # print("22222")
        print(sql)
        for cow in results:
            # print(cow)
            if cow:
                text.append(cow)
            else:
                return False
        # print(text)
        db.close()
        return text

    # 执行所需项目接口参数
    @classmethod
    def execute_api(self, id):
        tt = time.time()
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        text = []
        sql = "SELECT * FROM api_work where id='%s' " % (id)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        print(sql)
        for cow in results:
            # print(cow)
            if cow:
                cow
            else:
                return False
        db.close()
        return cow

    # 执行接口结果
    @classmethod
    def result_api(self, result, id):
        tt = time.time()
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        text = []
        sql = "UPDATE `api_work` SET result = '%s' WHERE id ='%s'" % (result, id,)
        print(sql)
        # print(results)
        cursor.execute(sql)
        cursor.connection.commit()
        db.close()
        return True

    # 接口查询
    @classmethod
    def SearchApi(self, mark=None, start=None, end=None, level=None, type=None, porject_total_id=None):
        db = self.openDB()

        cursor = db.cursor()
        id = []
        text = []

        startdata = "2000-11-21"

        enddata = "2060-11-01"
        order = " ORDER BY updatatime DESC"

        sql = "SELECT * from `api_work`where id like '%'"
        # print("enter 22")

        if mark:
            sql = sql + "and mark like" + "'" + str(mark) + "%'"
        if type:
            sql = sql + "and type like" + "'" + str(type) + "%'"
        if start:
            startdata = start
        if end:
            '''
             时间加1天
            '''
            enddata = str(datetime.datetime.strptime(end, "%Y-%m-%d") + datetime.timedelta(days=1))

        if start or end:
            sql = sql + "and (updatatime >'" + startdata + "'" + "  AND updatatime <'" + enddata + "')"
        if level:
            sql = sql + "and level like" + "'" + str(level) + "%'"
        if porject_total_id:
            # for i in range(0, len(porject_total_id)):
            #     if i == 0:
            #         sql = sql + "and projectsID ='" + str(porject_total_id[i]) + "'"
            #     elif i > 0:
            #         sql = sql + "or projectsID ='" + str(porject_total_id[i]) + "'"
            total=[]
            for i in range(0,len(porject_total_id)):

                if i!=(len(porject_total_id)-1):
                    total.append("'"+str(porject_total_id[i])+"',")
                else:
                    total.append("'" + str(porject_total_id[i]) + "'")
            if len(porject_total_id)==1:

                sql = sql + "and projectsID ='" + str(porject_total_id[0]) + "'"
            elif len(porject_total_id)>1:
                print(total)
                sql = sql + "and projectsID in(%s)"%" ".join(total)


        print(sql)
        # print("SearchApi")
        # sql="sql1"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        for cow in results:
            # print(cow)
            if cow:
                text.append(cow)

            else:
                db.close()
                return False
        # print(text)
        db.close()
        return text

    # 项目关联子模块查询
    @classmethod
    def Search_project_total(self, projectid=None):
        db = self.openDB()
        search_project_total = []
        cursor = db.cursor()
        sql = "select a.id,a.parentid,a.level from api_project a where a.parentid='%s'" % projectid
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(type(results))
        search_project_total.append(projectid)
        # print(results)
        # print(len(results))
        for i in range(0, len(results)):
            parentid = results[i][1]
            # print(parentid)
            sql = "select a.id,a.parentid,a.level from api_project a where a.parentid='%s'" % parentid
            # print(sql)
            cursor.execute(sql)
            results1 = cursor.fetchall()

            if results1:
                search_project_total.append(results1[i][0])
                # print(results1[i][0])
        # print search_project_total
        db.close()
        return search_project_total

    # 读取所有项目分类排序
    @classmethod
    def Search_project(self):
        tt = time.time()
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        text = []
        sql = "SELECT * FROM api_project "
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(str(results).replace('u\'','\'') .decode("unicode-escape"))
        # print()
        data = {}
        num = 0
        new_results=[]
        results=list(results)
        for i in range(0, len(results)):
            project = []
            # print(results[i])
            if results[i][2] == '0':
                father_id = results[i][0]
                num = num + 1
                project.append(results[i])
                # print father_id
                for cow in results:
                    # print(cow)
                    if str(father_id) == str(cow[2]):
                        # print(cow)
                        project.append(cow)
                    data[num] = project


        db.close()
        # print(str(data).replace('u\'','\'') .decode("unicode-escape"))
        return data
    # 接口页面读取sql
    @classmethod
    def Api_sql(self,sql):
        tt = time.time()
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        text = []
        sql =sql
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        data = {}
        db.close()
        return data

    # 新增接口
    @classmethod
    def Add_api(self, api_project,api_type,api_mark,api_header,api_url,api_data,api_updataname,api_level,api_belong,api_sql=None):

        db = self.openDB()

        cursor = db.cursor()
        api_project = MySQLdb.escape_string(api_project)
        api_type = MySQLdb.escape_string(api_type)
        api_mark = MySQLdb.escape_string(api_mark)
        api_header = MySQLdb.escape_string(api_header)
        api_url = MySQLdb.escape_string(api_url)
        api_data = MySQLdb.escape_string(api_data)
        api_updataname=MySQLdb.escape_string(api_updataname)
        api_level=MySQLdb.escape_string(api_level)
        api_belong= MySQLdb.escape_string(api_belong)
        # sql = "SELECT * from `api_work`where url = '%s'" % api_url
        # cursor.execute(sql)
        # if cursor.fetchall():
        #     msg = u"该接口URL已存在"
        #     print(msg)
        #     db.close()
        #     return False, msg
        # else:
        sql = "INSERT INTO `api_work`( `projectsID`,  `type`,`mark`,`header`,`url`,`data`,`updataname`,`level`,`updatatime`,`belong_id`) VALUES ( '%s', '%s', '%s', '%s', '%s', '%s','%s','%s',NOW(),'%s') " % (
            api_project, api_type, api_mark, api_header, api_url, api_data,api_updataname,api_level,api_belong)
        # sql= "insert into `week-report` (`title`, `username`, `userid`, `text`, `createData`, `updata`) values('xljipo3','admin','2','this is test',NULL,NULL)"
        cursor.execute(sql)
        cursor.connection.commit()
        msg = u"创建成功"
        print(sql)
        db.close()
        return True, msg

    # 新增接口-获取全局变量
    @classmethod
    def Get_api_global(self, user_id,belong_id):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        sql = "SELECT * from `global_variable`where user_id = '%s'  and belong_id='%s'"  % ( user_id,belong_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(sql)
        db.close()
        return results

    # 获取parentid
    @classmethod
    def Get_parentid(self, id):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        sql = sql = "SELECT * FROM api_project where id ='%s'"%id
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        db.close()
        for result in results:
            return result[2]

    # 读取所有项目名称
    @classmethod
    def Search_project_name(self,projectid):
        tt = time.time()
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        text = []
        sql = "SELECT name  FROM api_project  where  id  ='%s'"%projectid
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        return results
  # 读取所有项目&子模块
    @classmethod
    def Search_all_project(self):
        tt = time.time()
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        text = []
        sql = "SELECT * FROM api_project "
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    # 读取所有项目的最高级
    @classmethod
    def Search_main_project(self):
        tt = time.time()
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        text = []
        sql = "SELECT * FROM api_project where parentid='0'"

        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        return results

    # 根据子模块获取项目名称
    @classmethod
    def Get_project_name(self, api_belong_two):
        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        sql = "SELECT * from `api_project`where id = '%s'  "  % (api_belong_two)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(sql)
        # print(results[0][1])
        db.close()
        return results

    # 新增全局变量
    @classmethod
    def Add_global_variable(self, key, value,user_id,belong_id):

        db = self.openDB()
        # print("即将打开数据库")
        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        # 使用 fetchone() 方法获取一条数据
        cursor = db.cursor()
        key = MySQLdb.escape_string(key)
        value = MySQLdb.escape_string(value)
        sql = "INSERT INTO `global_variable`(`key`, `values`, `user_id`, `belong_id`) VALUES ( '%s', '%s','%s', '%s') " % (key, value, user_id, belong_id)
        # sql= "insert into `week-report` (`title`, `username`, `userid`, `text`, `createData`, `updata`) values('xljipo3','admin','2','this is test',NULL,NULL)"
        print(sql)
        cursor.execute(sql)
        cursor.connection.commit()

        db.close()
        return True

    #日报查询
    @classmethod
    def Search_day_data(self, userid, roleid, person=None, start=None, end=None,projectid=None):
        db = self.openDB()
        cursor = db.cursor()
        id = []
        text = []
        startdata = "2000-11-21"

        enddata = "2060-11-01"
        order = " ORDER BY a.creat_time DESC"

        if int(roleid) != 1:

            sql = "SELECT a.id,a.userid,a.username,a.day_bug,a.day_bug_off,a.creat_time,a.updata_time,b.`name`  from `day_report` a,api_project b where a.id like '%' and a.project_id=b.id "
            if userid:
                sql = sql + " and  a.userid =" + "'" + str(userid) + "'"
            if person:
                sql = sql + " and a.username like" + "'" + str(person) + "%'"
            if start:
                startdata = start
            if end:

                enddata = end

            if start or end:
                sql = sql + " and (a.creat_time >='" + startdata + "'" + "  AND a.creat_time <='" + enddata + "')"
            if projectid:
                sql = sql + " and  a.project_id =" + "'" + str(projectid) + "'"
            # if end:
            #     enddata=end
            #     sql = sql + "and (createData >'" + startdata + "'" + "  and createData <'" + enddata + "')"
            sql = sql + order
        else:
            sql = "SELECT a.id,a.userid,a.username,a.day_bug,a.day_bug_off,a.creat_time,a.updata_time,b.`name`  from `day_report` a,api_project b where a.id like '%' and a.project_id=b.id"
            if person:
                sql = sql + " and a.username like" + "'" + str(person) + "%'"
            if start:
                startdata = start
            if end:

                enddata = end

            if start or end:
                sql = sql + " and (a.creat_time >='" + startdata + "'" + "  AND a.creat_time <='" + enddata + "')"
            if projectid:
                sql = sql + " and  a.project_id =" + "'" + str(projectid) + "'"
            sql = sql + order

        print(sql)
        # sql="sql1"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        for cow in results:
            # print(cow)
            if cow:
                text.append(cow)

            else:
                db.close()
                return False
        # print(text)
        db.close()
        return text

    #日报新增
    @classmethod
    def add_day_report(self,userid,username, day_bug, day_bug_off, creat_time,projectid):
        db = self.openDB()
        cursor = db.cursor()

        cursor = db.cursor()

        sql = "INSERT INTO `day_report`( `userid`,  `username`,`day_bug`,`day_bug_off`,`creat_time`,`updata_time`,`project_id`) VALUES ( '%s', '%s', '%s', '%s', '%s',NOW(),'%s') " % (
            userid, username, day_bug, day_bug_off, creat_time, projectid)
        print(sql)
        # sql= "insert into `week-report` (`title`, `username`, `userid`, `text`, `createData`, `updata`) values('xljipo3','admin','2','this is test',NULL,NULL)"
        cursor.execute(sql)
        cursor.connection.commit()
        msg = u"创建成功"

        db.close()
        return True, msg
    #日报新增 判断是否存在
    @classmethod
    def add_day_report_is_new(self, username,creat_time,projectid):
        db = self.openDB()
        cursor = db.cursor()
        sql = "SELECT *  from `day_report` a,api_project b where a.creat_time='%s'and a.username='%s' and project_id='%s'"%(creat_time,username,projectid)
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        if results:
            # print('is true')
            db.close()
            return True
        else:
            # print('is false')
            db.close()
            return False
    # 日报详情
    @classmethod
    def detail_day_report(self, day_reportid):
        db = self.openDB()
        cursor = db.cursor()
        sql = "SELECT a.id,a.userid,a.username,a.day_bug,a.day_bug_off,a.creat_time,a.updata_time,a.project_id,b.`name` from `day_report` a,api_project b where a.id='%s' and a.project_id=b.id" % (day_reportid)
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        db.close()
        return results
    # 日报更新
    @classmethod
    def updata_day_report(self, day_reportid,day_bug, day_bug_off):
        db = self.openDB()
        cursor = db.cursor()
        sql = "UPDATE `day_report` SET day_bug = '%s' ,day_bug_off='%s' WHERE id ='%s'" % (day_bug, day_bug_off,day_reportid)
        print(sql)
        cursor.execute(sql)
        cursor.connection.commit()
        db.close()
        return True
    # 报表查询
    @classmethod
    def report_form(self, start=None, end=None,project_id=None):
        db = self.openDB()
        cursor = db.cursor()
        startdata = "2000-11-21"

        enddata = "2060-11-01"
        order = " ORDER BY a.creat_time ASC"
        group=" GROUP  BY a.creat_time ,b.name "
        # sql = "SELECT SUM(a.day_bug)  , SUM(a.day_bug_off)  , a.creat_time ,b.name   from  day_report a,  api_project b where a.project_id=b.id  and a.project_id ='%s'" \
        #       "and ( a.creat_time>'2019-01-03' and a.creat_time <='2019-01-10' ) " \
        #       "GROUP  BY a.creat_time ,b.name  ORDER  BY b.name ;"%project_id

        sql = "SELECT SUM(a.day_bug)  , SUM(a.day_bug_off)  , a.creat_time ,b.name   from  day_report a,  api_project b where a.project_id=b.id "
        if start:
            startdata = start
        if end:

            enddata = end

        if start or end:
            sql = sql + " and (a.creat_time >='" + startdata + "'" + "  AND a.creat_time <='" + enddata + "')"
        if project_id:
            sql = sql + " and  a.project_id =" + "'" + str(project_id) + "'"
        # if end:
        #     enddata=end
        #     sql = sql + "and (createData >'" + startdata + "'" + "  and createData <'" + enddata + "')"
        sql = sql +group +" "+order
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()

        db.close()
        return results
    # 报表总数查询
    @classmethod
    def report_form_total(self, start=None, end=None, project_id=None):
        db = self.openDB()
        cursor = db.cursor()
        startdata = "2000-11-21"

        enddata = "2060-11-01"
        order = " ORDER BY b.name DESC"
        group = " GROUP  BY b.name "
        # sql = "SELECT SUM(a.day_bug)  , SUM(a.day_bug_off)  , a.creat_time ,b.name   from  day_report a,  api_project b where a.project_id=b.id  and a.project_id ='%s'" \
        #       "and ( a.creat_time>'2019-01-03' and a.creat_time <='2019-01-10' ) " \
        #       "GROUP  BY a.creat_time ,b.name  ORDER  BY b.name ;"%project_id

        sql = "SELECT SUM(a.day_bug) AS '当前时间段所有BUG' , SUM(a.day_bug_off) as '当前时间段所有修复BUG',c.`待修复BUG总数`,c.`总BUG数`,b.name as '项目名称',a.project_id " \
              "from    api_project b  ,day_report a " \
              "LEFT JOIN (SELECT (SUM(a.day_bug)-SUM(a.day_bug_off)) as '待修复BUG总数',SUM(a.day_bug)  AS '总BUG数' ,a.project_id from day_report a GROUP BY a.project_id )c ON a.project_id = c.project_id " \
              "where a.project_id=b.id "
        if start:
            startdata = start
        if end:

            enddata = end

        if start or end:
            sql = sql + " and (a.creat_time >='" + startdata + "'" + "  AND a.creat_time <='" + enddata + "')"
        if project_id:
            sql = sql + " and  a.project_id =" + "'" + str(project_id) + "'"
        sql = sql + group + " " + order
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        db.close()
        return results

    # 报表查询
    @classmethod
    def graph_report_form(self, project_id,start=None, end=None,):
        db = self.openDB()
        cursor = db.cursor()

        startdata = "2000-11-21"

        enddata = "2060-11-01"
        order = " ORDER  BY creat_time ASC"
        group = " GROUP  BY creat_time  "
        # sql = "SELECT SUM(a.day_bug)  , SUM(a.day_bug_off)  , a.creat_time ,b.name   from  day_report a,  api_project b where a.project_id=b.id  and a.project_id ='%s'" \
        #       "and ( a.creat_time>'2019-01-03' and a.creat_time <='2019-01-10' ) " \
        #       "GROUP  BY a.creat_time ,b.name  ORDER  BY b.name ;"%project_id

        sql = "SELECT SUM(day_bug),SUM(day_bug_off),creat_time FROM day_report  where id like '%'  "
        if start:
            startdata = start
        if end:

            enddata =end

        if start or end:
            sql = sql + " and (creat_time >='" + startdata + "'" + "  AND creat_time <='" + enddata + "')"
        if project_id:
            sql = sql + " and project_id =" + "'" + str(project_id) + "'"
        sql = sql + group + " " + order
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        db.close()
        return results
# a=sql.Search_project_name(2)
# print(a[0][0])
