$(document).ready(function () {
    // grade选择改变值时要触发
    $("#grade").combobox({
        onChange: function(newValue, oldValue){
            if (newValue == 0) {
                // 清除父级菜单的combobox的内容
                $("#parentId").combobox('clear');
                $("#parentIdDiv").hide();
            } else {
                $("#parentIdDiv").show();
                // 获取上一级的菜单
                $("#parentId").combobox({
                    valueField: 'id',
                    textField: 'moduleName',
                    url: '../findByGrade?grade=' + (newValue-1),
                    method: 'GET',
                    editable: false
                })
            }
        }
    })
});

// 格式化等级
function formatGrade(value, row){
    if (value == 0) {
        return '根级'
    } else if(value == 1) {
        return '第一级'
    } else if(value == 2) {
        return '第二级'
    }
}

// 弹出添加框
function openAddDialog() {
    $("#parentIdDiv").hide();
    $("#dlg").dialog('setTitle', '添加模块').dialog('open')
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
    $("#fm").form('load', row);

    if (row.grade == 0) {
        $("#parentId").combobox('clear');
        $("#parentIdDiv").hide();
    } else {
        $("#parentIdDiv").show();
        $("#parentId").combobox({
            valueField: 'id',
            textField: 'moduleName',
            url: '../findByGrade?grade=' + (row.grade - 1),
            method: 'GET',
            editable: false,
            value: row.parent // 默认值
        })

    }
    $("#dlg").dialog('setTitle', '修改模块').dialog('open')
}

// 删除
function deleteModule(){
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
            $.post('../delete_module/', {ids: ids.join(',')}, function(resp){
                $.messager.alert('提示', resp.message);
                if (resp.code == 1){
                    $("#dg").datagrid('reload');
                }
            })
        }
    })
}


// 点击保存
function saveModule() {
    // 前台参数校验
    if (!$("#fm").form('validate')){
        return;
    }
    // 层级
    var grade = $("#grade").combobox('getValue')
    if (grade != 0) {
        var parentId = $("#parentId").combobox('getValue')
        if (parentId == null || parentId.trim().length == 0){
            $.messager.alert('提示', '请选择父级菜单！');
            return;
        }
    }
    // 提交
    var data = $("#fm").serialize();
    var id = $("#id").val();
    var url = '../add_module/';
    if (id != null && id.trim().length > 0) {
        url = '../update_module/';
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
