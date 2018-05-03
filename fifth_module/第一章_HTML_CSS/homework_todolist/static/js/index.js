/*
1.本例子是用localStorage 进行存储的
*/

// 存储数据
function saveData(data){
    //localStorage.setItem(key,value)：将value存储到key字段
    //JSON.stringify() 方法用于将 JavaScript 值转换为 JSON 字符串。
	localStorage.setItem("todo",JSON.stringify(data));
}

// 获取本地存储并返回
function loadData(){
	var collection=localStorage.getItem("todo");
	if(collection != null){
	    //JSON.parse() 方法用于将一个 JSON 字符串转换为对象。
		return JSON.parse(collection);
	}
	else return [];
}


// 清空本地存储
function clear(){
	localStorage.clear();
	load();
}

function postaction(){
    //获取到 input标签
	var title = document.getElementById("title");
	if(title.value === "") {
		alert("内容不能为空");
	}else{
		var data=loadData();
		var todo={"title":title.value,"done":false};
		// push() 方法可向数组的末尾添加一个或多个元素，并返回新的长度。
        // 往data数组的末尾添加一个字典。
		data.push(todo);
		//保存到本地数据
		saveData(data);
		var form=document.getElementById("form");
		// reset() 方法可把表单中的元素重置为它们的默认值。
		form.reset();
		load();
	}
}

function saveSort(){
	var todolist=document.getElementById("todolist");
	var donelist=document.getElementById("donelist");
	var ts=todolist.getElementsByTagName("p");
	var ds=donelist.getElementsByTagName("p");
	var data=[];
	for(i=0;i<ts.length; i++){
		var todo={"title":ts[i].innerHTML,"done":false};
		data.unshift(todo);
	}
	for(i=0;i<ds.length; i++){
		var todo={"title":ds[i].innerHTML,"done":true};
		data.unshift(todo);
	}
	saveData(data);
}

function remove(i){
	var data=loadData();
	var todo=data.splice(i,1)[0];
	saveData(data);
	load();
}

function update(i,field,value){
	var data = loadData();
	var todo = data.splice(i,1)[0];
	todo[field] = value;
	data.splice(i,0,todo);
	saveData(data);
	load();
}

function edit(i) {
	load();
	var p = document.getElementById("p-"+i);
	title = p.innerHTML;
	p.innerHTML="<input id='input-"+i+"' value='"+title+"' />";
	var input = document.getElementById("input-"+i);
	input.setSelectionRange(0,input.value.length);
	input.focus();
	//onblur 事件会在对象失去焦点时发生。
	input.onblur =function(){
		if(input.value.length === 0){
			p.innerHTML = title;
			alert("内容不能为空");
		}
		else{
			update(i,"title",input.value);
		}
	};
}

function load(){
	var todolist=document.getElementById("todolist");
	var donelist=document.getElementById("donelist");
	var collection=localStorage.getItem("todo");

	//获取localStorage的值，首先判断是否存在值，存在则继续判断是todolist里面的值，还是donelist的值
	if(collection!=null){
		var data=JSON.parse(collection);
		var todoCount=0;
		var doneCount=0;
		var todoString="";
		var doneString="";
		for (var i = data.length - 1; i >= 0; i--) {
			if(data[i].done){
				doneString+="<li draggable='true'><input type='checkbox' onchange='update("+i+",\"done\",false)' checked='checked' />"
				+"<p id='p-"+i+"' onclick='edit("+i+")'>"+data[i].title+"</p>"
				+"<a href='javascript:remove("+i+")'>-</a></li>";
				doneCount++;
			}
			else{
				todoString+="<li draggable='true'><input type='checkbox' onchange='update("+i+",\"done\",true)' />"
				+"<p id='p-"+i+"' onclick='edit("+i+")'>"+data[i].title+"</p>"
				+"<a href='javascript:remove("+i+")'>-</a></li>";
				todoCount++;
			}
		}
		todocount.innerHTML=todoCount;
		todolist.innerHTML=todoString;
		donecount.innerHTML=doneCount;
		donelist.innerHTML=doneString;
	}
	else{
		todocount.innerHTML=0;
		todolist.innerHTML="";
		donecount.innerHTML=0;
		donelist.innerHTML="";
	}
    //querySelector() 方法返回文档中匹配指定 CSS 选择器的一个元素。

	var lis=todolist.querySelectorAll('ol li');
	//因为document.querySelectorAll()返回的并不是我们想当然的数组，而是NodeList，对NodeList，它里面没有.forEach方法，我们使用了这样的方法进行循环：
	[].forEach.call(lis, function(li) {
	    //addEventListener() 方法用于向指定元素添加事件句柄。
		li.addEventListener('dragstart', handleDragStart, false);
		li.addEventListener('dragover', handleDragOver, false);
		li.addEventListener('drop', handleDrop, false);

		onmouseout =function(){
			saveSort();
		};
	});
}

//window.onload是一个事件，当文档加载完成之后就会触发该事件
window.onload=load;

window.addEventListener("storage",load,false);

var dragSrcEl = null;
function handleDragStart(e) {
  dragSrcEl = this;
  //DataTransfer.effectAllowed 属性指定拖放操作所允许的一个效果。move操作用于指定被拖动的数据将被移动。
  e.dataTransfer.effectAllowed = 'move';
  //DataTransfer.setData() 方法用来设置拖放操作的drag data到指定的数据和类型。
  e.dataTransfer.setData('text/html', this.innerHTML);
}
function handleDragOver(e) {
    //preventDefault() 该方法将通知 Web 浏览器不要执行与事件关联的默认动作（如果存在这样的动作）。
  if (e.preventDefault) {
    e.preventDefault();
  }
  e.dataTransfer.dropEffect = 'move';
  return false;
}
function handleDrop(e) {
    //stopPropagation():终止事件在传播过程的捕获、目标处理或起泡阶段进一步传播。调用该方法后，该节点上处理该事件的处理程序将被调用，事件不再被分派到其他节点。
  if (e.stopPropagation) {
    e.stopPropagation();
  }
  if (dragSrcEl !== this) {
    dragSrcEl.innerHTML = this.innerHTML;
    this.innerHTML = e.dataTransfer.getData('text/html');
  }
  return false;
}
