def dbCover(value) :
    return "'"+str(value)+"'"

def CreateDB(table_name, col, value) :
    len_col = len(col)
    len_value = len(value)
    if len_col == 0 or len_value == 0 or len_col != len_value :
        return -1
    qs = 'insert into ' + table_name + ' ('
    for item in col :
        qs += item + ', '
    qs = qs[:-2] + ') values ('
    for item in value :
        qs += dbCover(item) + ', '
    qs = qs[:-2] + ')'
    print 'CreateDB Returned : ' + qs
    return qs

def ReadDB(table_name, what, where_col=0, where_value=0, limit=0) :
    if len(what) == 0 :
        return []
    qs = 'select '
    for item in what :
        qs += str(item) + ','
    qs = qs[:-1] + ' from ' + table_name
    if where_col != 0 and where_value != 0 :
        qs += ' where '
        whereLen = len(where_col)
        for i in range(whereLen) :
            qs += where_col[i]+'='+dbCover(where_value[i])+' and '
        qs = qs[:-4]
    if not (limit == 0 or limit == []) :
        if len(limit) == 1 :
            qs += ' limit ' + str(limit[0])
        elif len(limit) == 2 :
            qs += ' limit ' + str(limit[0]) + ', ' + str(limit[1])
    print 'ReadDB Returned : ' + qs
    return qs

def UpdateDB(table_name, set_col, set_value, where_col=0, where_value=0) :
    len_set_col = len(set_col)
    len_set_value = len(set_value)
    len_where_col = len(where_col)
    len_where_value = len(where_value)
    if len_set_col == 0 or len_set_value == 0 or len_set_col != len_set_value :
        return -1
    qs = 'update ' + table_name + ' set '
    for i in range(len_set_col) :
        qs += set_col[i] + '=' + dbCover(set_value[i]) + ', '
    qs = qs[:-2]
    if where_col != 0 and where_value != 0 :
        qs += ' where '
        for i in range(len_where_col) :
            qs += where_col[i] + '=' + dbCover(where_value[i]) + ' and '
        qs = qs[:-5]
    print 'UpdateDB Returned : ' + qs
    return qs

def DeleteDB(table_name, where_col, where_value) :
    len_where_col = len(where_col)
    len_where_value = len(where_value)
    if len_where_col == 0 or len_where_value == 0 or len_where_col != len_where_value :
        return -1
    qs = 'delete from ' + table_name + ' where '
    for i in range(len_where_col) :
        qs += where_col[i] + '=' + dbCover(where_value[i]) + ', '
    qs = qs[:-2]
    print 'DeleteDB Returned : ' + qs
    return qs