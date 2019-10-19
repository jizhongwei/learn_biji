### 1、浮动（float）
1、浮动的框可以向左或向右移动，直到它的外边缘碰到包含框的边框为止。
***由于浮动框不在文档的普通流中，所以文档的普通流中的块框表现得就像浮动框不存在一样***
***一个浮动元素会尽量向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的边框为止***
2、浮动元素之后的元素将围绕它；浮动元素之前的元素将不会受到影响。
***如果图像是右浮动，下面的文本流将环绕在它左边***
```
img {
    float: right;
}
```
3、彼此相邻的浮动元素
> 如果把几个浮动的元素放到一起，如果有空间的话，它们将彼此相邻，直到换行；
***
### 2、HTML\<meta>元素
1、\<meta>标签描述了一些基本的元数据。元数据不会显示在浏览器上，但会被浏览器解析。
2、\<meta>元素可被用于指定网页的描述，关键词，文件的最后修改时间，作者，和其他元数据。元数据可以使用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其它web服务。
```
1、定义搜索引擎的关键词
<meta name="keywords" content="HTML, CSS">
2、定义网页描述内容
<meta name="description" content="免费 web & 编程 教程">
3、定义网页作者
<meta name="author" content="dick">
4、每15秒刷新当前网页
<meta http-equiv="refresh" content="15">
```
***
### 3、阴影box-shadow
1、box-shadow属性可以向盒子添加阴影。
```
属性设置方式：
box-shadow:x-offset y-offset 阴影模糊半径 阴影扩展半径 阴影颜色 投影方式；
1、x-offset：必需。水平阴影的位置，允许负值
2、y-offset：必需。垂直阴影的位置，允许负值
3、阴影模糊半径：可选。模糊距离
4、阴影扩展半径：可选。阴影的尺寸
5、阴影颜色：可选。阴影的颜色。省略默认为黑色
6、投影方式：可选。（设置inset时为内部阴影方式，如果省略为外阴影方式）

实例代码:
(外阴影)
.box-shadow {
    box-shadow: 4px 2px 6px #eee;
}
（内阴影）
.box-shadow {
    box-shadow:4px 2px 6px #eee inset;
}
```
2、阴影模糊半径与阴影扩展半径的区别
> 1、阴影模糊半径：此参数可选，其值只能是正值，如果其值为0时，表示阴影不具有模糊效果，其值越大阴影的边缘就越模糊；
2、阴影扩展半径：此参数可选，其值可以是负值，如果值为正，则整个阴影都延展扩大，反之值为负值时，则缩小；
***
### 4、渐变颜色
1、gradient分为线性渐变（linear）和径向渐变（radial）。
```
linear-gradient(to botton(180deg),#fff,#eee)
```
***
### 5、文字与字体
1、text-overflow与word-wrap
text-overflow用来设置是否使用一个省略标记（...）标示对象内文本的溢出。
```
text-overflow:clip | ellipsis
```
> 但是text-overflow只是用来说明文字溢出时用什么方式显示，要实现溢出时产生省略号的效果，还须定义强制文本在一行内显示（white-space:nowrap）及溢出内容为隐藏（overflow：hidden），只有这样才能实现溢出文本显示省略号的效果
```
{
    text-overflow:ellipsis;
    overflow:hidden;
    white-space:nowrap;
}
```
2、嵌入字体@font-face
@font-face能够加载服务器端的字体文件，让浏览器端可以显示用户电脑里没有安装的字体。
```
语法:
@font-face {
    font-family:字体名称；
    src：字体文件在服务器上的相对路径或绝对路径；
}
```
***
### 6、盒子模型
1、CSS中有一种基础设计模式叫盒模型，盒模型定义了web页面中的元素中如何来解析。CSS中每一个元素都是一个盒模型，包括html和body标签元素。在盒模型中主要包括width、height、border、background、padding和margin这些属性，而且他们之间的层次关系可以相互影响
***
### 7、jQuery
1、**$(document).ready**的作用是等页面的文档（document）中的节点都加载完毕后，在执行后续的代码，因为我们在执行代码的时候，可能会依赖页面的某一个元素，我们要确保这个元素真正的被加载完毕后才能正确的使用
2、jQuery对象与DOM对象
> jQuery对象与DOM对象是不一样的

可能一时半会分不清楚哪些是jQuery对象，哪些是DOM对象
下面利用代码区别：
```
JavaScript：
var p = document.getElmentById("imooc");
p.innerHTML = 'xxxxxx';
p.style.color = 'red';
jQuery：
var $p = $('$imooc');
$p.html("xxxxx").css('color', 'red');
```
3、jQuery库本质上还是JavaScript代码，它只是对JavaScript语言进行包装处理，为的是提供更好更方便快捷的DOM处理与开发中经常使用的功能。我们使用jQuery的同时也能混合JavaScript原生代码一起使用。在很多场景中，我们需要jQuery与DOM能够相互的转换，它们都是可以操作的DOM元素，jQuery是一个类数组对象，而DOM对象就是一个单独的DOM元素。
4、this是JavaScript中的关键字，指的是当前的上下文对象，简单的说就是方法/属性的所有者。
```
var imooc = {
    name: "xxxx",
    getName: function (){
        return this.name;
    }
}
imooc.getName();
```
5、同样，在DOM中this就是指向了这个html元素对象，因为this就是DOM元素本身的一个引用
```
JavaScript：
p.addEventListener('click', function(){
    this.style.color = 'red';
    p.style.color = 'red';
}, false);
通过addEventListener绑定时间回调中，
jQuery：
$('p').click(function(){
    var $this = $(this);
    $this.css("color", "red");
})
通过$()方法传入当前的元素对象的引用this，把这个this加工成jQuery对象，我们就可以用jQuery提供的快捷方法直接处理样式了
```
**总体：**
> this，表示当前的上下文对象是一个html对象，可以调用html对象所拥有的属性和方法。
$(this)，代表的上下文对象是一个jQuery的上下文对象，可以调用jQuery的方法和属性值。

6、操作特性的DOM方法主要有3个
>JavaScript： 
getAttribute、setAttribute、removeAttribute
jQuery：
attr()、removeAttr()
***
### 8、定位（position）
1、绝对定位：
**1、绝对布局默认的宽度为内容宽度**
**2、脱离文档流**
**3、参照物为第一个定义祖先或者根元素**
> 绝对定位的盒子脱离了标准文档流，所以所有的标准文档流的性质，绝对定位之后都不遵守了。绝对定位之后，标签就不区分所谓的行内元素、块级元素了，不需要display:block就可以设置宽、高了。
（1）如果用top描述，那么参考点就是页面的左上角，而不是浏览器的左上角，
（2）如果用bottom描述，那么参考点就是浏览器首屏窗口尺寸，对应的页面的左下角。
一个绝对定位的元素，如果父元素中也出现了已定位（无论是绝对定位、相对定位、还是固定定位）的元素，那么将以父辈这个元素为参考点。（有可能是祖先元素，比如爷爷元素）总之是离绝对定位元素最近的父辈元素。
（子绝父相）：这样可以保证父辈元素没有脱离标准文档流，儿子元素即使脱离标准文档流也只能在父辈元素里面移动

2、绝对定位的元素怎么居中
> 我们知道，如果想让一个标准流中的盒子居中，可以设置margin:0 auto属性。
```
绝对定位元素
{
    width:600px;
    height:60px;
    position: absolute;
    left:50%;
    top:0;
    margin-left:-300px;
}
公式：
left:50%;
margin-left:负的宽度的一半;
```
3、一旦一个元素浮动了，那么将能够并排了，并且能够设置宽高了。无论它原来是div还是span。
4、相对定位（relative）
**1、元素仍在文档流中**
**2、参照物为元素本身**
> 因为相对定位元素仍处于文档中，所以relative一般用作改变层级和作为绝对定位的参照物
*** 
### 9、浮动元素引发的问题
问题1、设置了浮动的元素的父元素的高度会变为0，也就是常说的高度崩塌。
**原因：**
> 浮动元素脱离了文档流，脱离了父级元素中子元素的正常渲染逻辑，从而造成父级元素的高度坍塌

问题2、浮动元素后面的元素跑到了浮动元素的下面，被挡住了。
**原因：**
这是因为一个元素浮动的时候，如果没有关闭浮动，其父元素也就不会再包含这个浮动元素，因为此时浮动元素已经脱离了文档流；
**解决方法**
(1)在设置了浮动元素的父元素上添加一下属性
```
overflow:hidden;
或者overflow:auto;
```
(2)使用伪元素的方式（推荐）
```
.clearfix:before
.clearfix:after {
    display:table;
    content:"";
}
.clearfix:after {
    clear:both;
}
.clearfix {
    zoom:1;
}
然后在父元素上添加clas=“clearfix’即可
```
***为什么会出现环绕浮动元素的效果呢***
**原因是元素设置了float属性，元素脱离了文档流之后，相当于就是从正常的元素排列过程移除出去。元素移除走后，必然会留下空位，则会有后续的非float元素进行补位。
但是float并不会使元素脱离文本流，也就是说，文本内容在渲染的时候还是会计算浮动元素的空间，所以，就会呈现出来环绕的效果**
***
### 10、自适应内容宽度或高度
1、width属性设置成fill-content，块的宽度会变为内容的宽度
2、height属性设置成-webkit-fill-available，子块的高度会等于父级块元素的高度