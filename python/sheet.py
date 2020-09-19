#-*- coding : utf-8-*-

import xlrd
import xlwt
import os
import easygui
  
def file_name(file_dir):   
    L=[]   
    K=[]
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.xlsx':  
                L.append(os.path.join(root, file))
                K.append(os.path.splitext(file)[0])
    return L,K

filepath=easygui.diropenbox(title='选择需要合并的excel文件')
#filepath='C:\\Users\\xr chen\\Desktop\\test\\'

if __name__=='__main__':
    [allxls,allname]=file_name(filepath)
    wb1=xlwt.Workbook()
    for i in range(len(allxls)):
        df1=xlrd.open_workbook(allxls[i])
        sheet1 = df1.sheet_by_index(0)
        sheet=wb1.add_sheet(allname[i])
        for i in range(sheet1.nrows):
            for j in range(sheet1.ncols):
                sheet.write(i,j,sheet1.cell_value(i,j))
    outputpath=easygui.diropenbox(title='保存到')
    wb1.save(filepath+'output.xls')
    easygui.msgbox(msg='按完成键结束', title='合并完成', ok_button='完成', image=None, root=None)