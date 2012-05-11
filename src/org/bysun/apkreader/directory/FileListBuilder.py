# -*- coding: UTF-8 -*-
'''
Created on 2012-5-10

@author: bysun
'''
import os

class FileListBuilder(object):
    '''
    文件列表读取
    '''
    def __init__(self,basePath,filterStr):
        '''
        Constructor
        '''
        self.fileList = []
        self.basePath = basePath
        self.filter = filterStr
        self.buildListFile()
        
    def validBasePath(self):
        '''
        判断是否是已存在目录
        '''
        if os.path.exists(self.basePath) & os.path.isdir(self.basePath):
            return True
        else:
            return False
        
    def buildListFile(self):
        '''创建文件列表'''
        if self.validBasePath():
            for fs in os.walk(self.basePath):
                for f in fs[2]:
                    extName = os.path.splitext(f)[1][1:];
                    if extName in self.filter:
                        self.fileList.append(os.path.join(fs[0],f))
                        
    def listFile(self):
        '''返回文件列表'''
        return self.fileList
    def getBasePath(self):
        '''返回基础目录路径'''
        return self.basePath
    


builder = FileListBuilder("D:\\apk_back",["apk"]);
print builder.listFile()
print builder.getBasePath()
