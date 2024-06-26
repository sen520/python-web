// 搜索
function searchUser(){
    $("#dg").datagrid('load', {
        'userName':$("#s_userName").val()
    })
}

// 弹出添加框
function openAddDialog() {
    $("#parentIdDiv").hide();
    $("#dlg").dialog('setTitle', '添加用户').dialog('open')
}

// 弹出修改框
function openModifyDialog() {
    // 获取选中的行
    var rows = $("#dg").datagrid('getSelections');
    if (rows.length != 1) {
        $.messager.alert('提示', '请选择一条记录进行修改！');
        return ;
    }
    var row = rows[0];
    // 给表单赋值
    var url = '../'+ row.id + '/find_user_roles';
    $.get(url, {}, function(resp){
        row.roleIds = resp;
        $("#fm").form('load', row);
        $("#dlg").dialog('setTitle', '修改用户').dialog('open')
    })

}

// 删除
function deleteUser(){
    // 获取选中的行
    var rows = $("#dg").datagrid('getSelections');
    if (rows.length == 0) {
        $.messager.alert('提示', '至少选择一条记录进行删除！');
        return ;
    }
    // 构建主键ids
    var ids = new Array()
    for (var i=0; i < rows.length; i++) {
        ids.push(rows[i].id);
    }
    // 请求后台在回调
    var note = '确定要删除这<font color="red">'+ ids.length +'</font>记录吗？';
    $.messager.confirm('提示', note, function(r){
        if (r){
            $.post('../delete_user/', {ids: ids.join(',')}, function(resp){
                $.messager.alert('提示', resp.message);
                if (resp.code == 1){
                    $("#dg").datagrid('reload');
                }
            })
        }
    })
}


// 点击保存
function saveUser() {
    // 前台参数校验
    if (!$("#fm").form('validate')){
        return;
    }
    // 提交
    var data = $("#fm").serialize();
    var id = $("#id").val();
    var url = '../add_user/';
    if (id != null && id.trim().length > 0) {
        url = '../update_user/';
    }
    $.post(url, data, function(resp){
        $.messager.alert('提示', resp.message);
        if (resp.code == 1){
            closeDialog();
            $("#dg").datagrid('reload');
        }
    });

}

// 关闭
function closeDialog() {
    $("#fm").form('clear');
    $("#dlg").dialog('close')
}
