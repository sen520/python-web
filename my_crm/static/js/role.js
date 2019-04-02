// 弹出添加
function openAddDialog() {
    $("#dlg").dialog('setTitle', '添加角色').dialog('open')
}

// 弹出修改
function openModifyDialog() {
    // 获取选中的行
    var rows = $("#dg").datagrid('getSelections');
    if (rows.length != 1) {
        $.messager.alert('提示', '请选择一条记录进行修改！');
        return ;
    }
    var row = rows[0];
    // 给表单赋值
    $("#fm").form('load', row);
    $("#dlg").dialog('setTitle', '修改角色').dialog('open')
}

// 删除
function deleteRoles() {
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
            $.post('../delete_role/', {ids: ids.join(',')}, function(resp){
                $.messager.alert('提示', resp.message);
                if (resp.code == 1){
                    $("#dg").datagrid('reload');
                }
            })
        }
    })
}

// 关联模块
function relatePermissions() {

    // 获取选中的行
    var rows = $("#dg").datagrid('getSelections');
    if (rows.length != 1) {
        $.messager.alert('提示', '请选择一条记录进行关联！');
        return ;
    }
    var row = rows[0];
    // 获取角色id
    var roleId = row.id;
    window.parent.openTab('角色关联权限', '/system/'+ roleId +'/relate_modules_index/', 'icon-user')
}

// 保存角色
function saveRole() {
    // 参数校验
    if (!$("#fm").form('validate')){
        return
    }

    var id = $("#id").val();
    var url = '../add_role/';
    var data = {roleName:$("#roleName").val(), roleRemark: $("#roleRemark").val()};
    if (id != null && id.trim().length > 0) {
        url = '../update_role/';
        data.id = id
    }
    $.post(url, data, function(resp){
        $.messager.alert('提示', resp.message);
        if (resp.code == 1) {
            $("#dg").datagrid('reload');
            closeRoleDialog()
        }
    })

}

// 关闭窗体
function closeRoleDialog() {
    $("#fm").form('clear');
    $("#dlg").dialog('close')
}


