$(document).ready(function () {
    $("#file").on("change",function(evt){ // id为file的元素的改变事件
        var formData=new FormData();//新的formData
        formData.append("file",$("#file")[0].files[0]);//加入文件实体
        var file = $("#file").val();
        var arr = file.split("\\");
        file = arr[arr.length-1];//文件名
        formData.append("name",file);
        $.ajax({
            type:"post",
            url:"http://127.0.0.1:8080",//服务器IP+端口号
            cache: false,
            data:formData,
            datatype:"text",//返回值类型为文本
            processData:false,
            contentType:false,
            success:function(result){
            $("#msg").text(result);//将id为msg的元素文本设置为返回值
            },
            error:function(){
        	    alert(1)
        }
        })
})
})
    
