# -*-coding:utf-8-*-
# 字段位置一一对应

Index2ColName = {  # 按照表(对象)分类
    
    'note': {
        0:'note_id', 1:'title', 2:'detail', 3:'pub_date', 4:'is_valid'
    },

    'user': {
        0:'user_id', 1:'grade', 2:'_class', 3:'user_type', 4:'tel,email'
    },

    
}

'''
select GROUP_CONCAT(COLUMN_NAME) from information_schema.COLUMNS where table_name = 'user_info';
查询字段名称
'''