import pymysql
import src.ir_test.KeywordExtract as keyword

def get_db_data():
    """
    获取数据库信息
    :return:
    """
    db = pymysql.connect("localhost", "root", "123456", "ir_db")
    sql="SELECT * FROM source_tb"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        # for result in results:
        #     print(result)
    except:
        print("数据库连接失败")
    else:
        return results
        pass
    finally:
        db.close()


def keyword_match(db_source, key_list):
    # print(db_source,key_list)
    max=0
    address=None
    sum=0
    for item in db_source:
        i=1
        while i<len(item)-1:
            if item[i] in key_list:
                sum+=1/i
            i+=1
        if max<sum:
            max=sum
            address=item[-1]
        sum=0
    return address


def display_info(file_address):
    for line in open(file_address, 'r', encoding='UTF-8'):
        print(line)
    pass


if __name__ == '__main__':
    search_str=input("输入关键字查询")
    seg_text=keyword.seg_to_list(search_str,True)
    filter_list = keyword.word_filter(seg_text, True)
    db_source=get_db_data()
    if db_source is None:
        exit()
    else:
        file_address=keyword_match(db_source,filter_list)
        display_info(file_address)


