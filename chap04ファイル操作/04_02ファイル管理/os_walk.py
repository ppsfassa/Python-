import os

for foldername, subfolders, filenames in os.walk('C:\\test'):
    print('現在のディレクトリは-->' + foldername)

    for subfolder in subfolders:
        print(foldername + 'のサブフォルダー:' + subfolder)

    for filename in filenames:
        print(foldername + 'のファイル:' + filename)

    print('')
