# -*- coding: UTF-8 -*-

'''
把根目录下的所有文件，按照 train: test: val == 6: 2: 2的比例分类。
'''
import os
import shutil
import glob


totallyNum = len(glob.glob('*')) - 1    # 总数减去1个py文件
trainNum = int(totallyNum * 0.6)
testNum = int((totallyNum - trainNum)/2)
valNum = totallyNum - trainNum - testNum

localPath = os.getcwd()     # 根目录
basename = os.path.basename(localPath)      # 当前所在文件夹名
upPath = os.path.abspath(os.path.dirname(localPath))    # 上级目录
targetPath = upPath        # 目标目录


def shear_files(filePath, targetPath):

    modelist = ['train','test','val']
    i = 0
    while(i <= 2):
        mode = modelist[i]
        i = i + 1

        if mode == 'train':
            num = trainNum
        elif mode == 'test':
            num = testNum
        elif mode == 'val':
            num = valNum
        else:
            print("Error mode type.")

        count = 0
        for aFile in os.listdir(localPath):
            if aFile == '1.py':
                continue
            elif count < num:
                aFilePath = filePath + '\\' + aFile
                targetDir = targetPath + '\\' + mode + '\\' + basename

                if not os.path.exists(targetDir):
                    os.mkdir(targetDir)

                shutil.move(aFilePath, targetDir)
                count = count + 1



    print("Done!")


shear_files(localPath, targetPath)
