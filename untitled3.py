#Hello
import xlrd
import json


def main():
    workbook = xlrd.open_workbook('C:\\Users\\Anshul Sharma\\Desktop\\ipl2019 url.xlsx')
    worksheet = workbook.sheet_by_index(0)    
    
    video_url = []
    video_title = []
    final_url = {}
    #get all urls
    f = open("D:\\final_url.cmd","a")
    for i in range(1,worksheet.nrows):
        video_url=(worksheet.cell(i,0).value)
        video_title=(worksheet.cell(i,1).value)
        final_url = 'ffmpeg -i "'+video_url+'" -c copy -bsf:a aac_adtstoasc "E:\Cricket\IPL 2018\\'+video_title+'.mp4"'
        f.write(final_url)
        f.write("\n")
        f.write("\n")
    f.close()
    
    
    
    
    #with open('E:\\Cricket\\IPL 2018'+str(main_index)+'.json','w') as outfile:
        #json.dump(final_url,outfile)
        
if __name__ == '__main__':
    main()