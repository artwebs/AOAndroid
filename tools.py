# -*- coding:utf-8 -*-
__author__ = 'artwebs'
import os
import time
import shutil



import sys
import getopt

proName=""
package=""
sDirs=[]
oDirs=['cn','artwebs']
template="artwebsandroid"

def usage():
    print 'tools.py usage:'
    print '-h,--help: print help message.'
    print '-v, --version: print script version'
    print '-o, --output: input an output verb'
    print '--foo: Test option '
    print '--fre: another test option'

def version(args):
    print 'tools.py 1.0.0.0.1'

def output(args):
    print 'Hello, %s'%args

def new(opts):
    source=os.path.abspath(template)
    target=os.path.abspath('./')
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit(1)
        elif o in ('-p'):
            package=a
            print package

        sDirs.extend(package.split('.'))
        proName=sDirs[1]
        sDirs[1]=sDirs[1].lower()
        target+="/"+proName


    if os.path.exists(target):
        print u"项目已经存在,不需要进行创建"
        exit(0)
    copyFiles(source, target,proName,template)
    # shutil.copytree(source, target)
    # copyFiles(source, target)
    shutil.rmtree(target+"/.git")
    #shutil.rmtree(target+"/gen")
    # shutil.copytree(target+"/src/net/zcline/zctechdemo", target+"/src/net/zcline/"+proName.lower())
    # shutil.rmtree(target+"/src/net/zcline/zctechdemo")
    print 'create '+proName +" sucessed!"

def main(argv):
    try:
        action=argv[1]
        opts, args = getopt.getopt(argv[2:], 'hvop:', ['source=', 'target='])
        obj= globals()[action](opts)

    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

copyFileCounts = 0
def copyFiles(sourceDir, targetDir,keyword,template):
    global copyFileCounts
    # print sourceDir
    for f in os.listdir(sourceDir):
        sourceF = os.path.join(sourceDir, f)
        targetF=None
        for index,val in enumerate(oDirs):
            if f==val:
                #print sDirs
                #print index
                targetF=os.path.join(targetDir,sDirs[index])
        if targetF is None:
            targetF = os.path.join(targetDir, f.replace(template,keyword).replace(template.lower(),keyword.lower()))
        #targetF = os.path.join(targetDir, f.replace(template,keyword).replace(template.lower(),keyword.lower()))

        if os.path.isfile(sourceF):
            #创建目录
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            copyFileCounts += 1

            #文件不存在，或者存在但是大小不同，覆盖
            if not os.path.exists(targetF) or (os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                ffrom=open(sourceF, "rb")
                lines   = ffrom.readlines()
                ffrom.close()
                fto=open(targetF, "wb")
                for line in lines:
                    fto.write(line.replace('.'.join(oDirs),'.'.join(sDirs)).replace(template,keyword).replace(template.lower(),keyword.lower()))
                fto.close()
                # print u"%s %s 初始化完成" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF)
            else:   # ~# k1 b! N) [% u
                print u"%s %s 已存在，初始化完成" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF)

        if os.path.isdir(sourceF):
            copyFiles(sourceF, targetF,keyword,template)

if __name__ == '__main__':
    main(sys.argv)