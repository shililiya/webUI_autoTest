import xlrd
from framework.logger import Logger
logger=Logger("logger=Util").getlog()
class Util(object):
    @classmethod
    def read_excel(self,excelPath,sheetName="Sheet1"):
        workbook=xlrd.open_workbook(excelPath)
        sheet=workbook.sheet_by_name(sheetName)
        #以第一行当键值
        keys=sheet.row_values(0)
        #获取总行数
        rowNum=sheet.nrows
        #获取总列数
        cloNum=sheet.ncols
        if rowNum<=1:
            logger.error("表中数据行数少于1行")
        else:
            newSheet=[]
            for i in range(1,rowNum):
                #创建一个空字典
                sheet_data = {}
                values=sheet.row_values(i)
                for j in range(cloNum):
                    sheet_data[keys[j]] = values[j]
                newSheet.append(sheet_data)
        return newSheet
if __name__ == "__main__":
    print(Util.read_excel("D:/Python/DiscuzProject/data/data.xlsx","Sheet1"))
