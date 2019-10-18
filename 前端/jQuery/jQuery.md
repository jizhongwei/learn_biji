## jQuery库学习笔记
***
### 1、什么是jQuery？
1、jQuery是一个JavaScript库
>说白了就是对JavaScript的封装，让程序员能更高效的使用JavaScript

2、jQuery极大地简化了JavaScript编程
> jQuery是一个轻量级的“写的少，做的多”的JavaScript库

3、jQuery很容易学习
***
### 2、学习jQuery必备基础知识
1、HTML
> jQuery本身就是用来控制HTML的，不会HTML就不可能能学习jQuery

2、CSS
> jQuery的一部分就是通过改变html元素的css属性，来达到改变页面的目的，所以也要会CSS

3、JavaScript
> 本身jQuery就是用JavaScript编写的，不会JavaScript就更谈不上学习jQuery了
***
### 3、jQuery的功能
1、HTML元素选取
2、HTML元素操作
3、CSS操作
4、HTML事件函数
5、JavaScript特效和动画
6、HTML DOM遍历和修改
7、ajax
8、utilities
***
### 4、jQuery的安装
1、本地安装
> 通过把jQuery源文件下载到本地电脑，然后在HTML文档中引入
```
在HTML文档头部中引入jQuery文件
<head>
    <script src="path/to/jquery.min.js"></script>
</head>
```
2、使用CDN
> 使用服务提供商的CDN服务，但前提是本地电脑可以联手互联网，建议使用国内服务提供商的CDN
```
1、百度CDN
<head>
<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js">
</script>
</head>
2、又拍云CDN
<head>
<script src="https://upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.2.min.js">
</script>
</head>
```
***安装完jQuery后，我们可以在浏览器的调试界面的console下，输入$.fn.jquery来查看jQuery的版本，不过一般我们引入jQuery的时候都知道版本号的***
***
### 5、jQuery语法
1、通过jQuery，您可以选取（查询，query）HTML元素，并对它们执行“操作”（actions）
> jQuery语法通过选取HTML元素，并对选取的元素执行某些操作
基础语法：
\$(selectot).action()
1、美元符号定义jQuery
2、选择符（selector）“查询”和“查找”HTML元素
3、action()执行对元素的操作
例子：
\$(this).hide()隐藏当前元素
\$("p").hide()隐藏所以p元素
\$("p.test").hide()隐藏所有clas=“test”的p元素
\$("#test").hide()隐藏所有id=“test”的元素
***
### 6、jQuery选择器
1、jQuery选择器允许我们对HTML元素组或单个元素进行操作
> jQuery选择器基于元素的id、类、类型、属性、属性值等“查找”（或选择）HTML元素。它基于已经存在的css选择器，除此之外，它还有一些自定义的选择器。
jQuery中所有选择器都以美元符号开头：$()

2、元素选择器
> jQuery元素选择器基于元素名选取元素
比如在选中页面中所有的p标签元素
$("p")
```
用户点击按钮后，所有的p元素都隐藏
$(document).ready(function(){
    $("button").click(function(){
        $("p").hide();
    });
});
```
```
更多实例
$("*") 选取全部元素
$(this) 选取当前HTML元素
$("p.intro") 选取class为intro的p元素
$("p:first") 选取第一个p元素
$("ul li:first") 选取第一个ul元素的第一个li元素
$("ul li:first-chlid")选取每个ul元素的第一个li元素
$("[href]") 选取带有href属性的元素
$("a[target='_blank']") 选取所有target属性值等于"_blank"的a元素
$("a[target!='_blank']") 选取所有target属性值不等于"_blank"的a元素
$(":button") 选取所有type="button"的input元素和button元素
$("tr:even") 选取偶数位置的tr元素
$("tr:odd") 选取奇数位置的tr元素
```
***
### 7、jQuery事件
***什么是事件？***
页面对不同访问者的响应叫做事件
事件处理程序指的是当HTML中发生某些事件时所调用的方法。
1、在元素上移动鼠标
2、选取单选按钮
3、点击元素
|鼠标事件|键盘事件|表单事件|文档/窗口事件|
|:-:|:-:|:-:|:-:|
|click|keypress|submit|load|
|dbclick|keydown|change|resize|
|mouseenter|keyup|focus|scroll|
|mouseleave||blur|unload|
|hover||||
***
### 8、jQuery效果
1、隐藏和显示
1.1、jQuery.hide()隐藏
1.2、jQuery.show()显示
1.3、jQuery.toggle()隐藏和显示来回切换
> 上面三个方法接收三个参数，
如：
jQuery.hide(元素，速度参数，回调函数)
1、元素是要控制的HTML元素
2、速度是动作的时间效果
3、回调函数是效果完成后执行的动作

2、淡入淡出
1.1、jQuery.fadeIn()
1.2、jQuery.fadeOut()
1.3、jQuery.fadeToggle()
1.4、jQuery.fadeTo()

3、滑动
1.1、jQuery.slideDown()
1.2、jQuery.fadeUp()
1.3、jQuery.fadeToggle()

4、动画
jQuery.animate()
> jQuery.animate({params}, speed, callback)
1、params参数定义形成动画的css属性
2、speed参数规定效果的时长，它可以取以下值：“slow”、“fast“或者毫秒
3、callback参数动画完成后所执行的函数名称

```
$("button").click(function(){
    $("div").animate({left:'250px'});
});
```
***可以用 animate() 方法来操作所有 CSS 属性吗？***
是的，几乎可以！不过，需要记住一件重要的事情：当使用 animate() 时，必须使用 Camel 标记法书写所有的属性名，比如，必须使用 paddingLeft 而不是 padding-left，使用 marginRight 而不是 margin-right，等等。
***
### 9、停止动画
1、jQuery.stop()方法用于在动画或效果完成前对它们进行停止
> 默认地，stop()会清除在被选元素上指定的当前动画
***
### 10、callback方法
1、callback函数在当前动画100%完成之后执行
***
### 11、添加元素
1、通过jQuery，可以很容易地添加新的元素、内容
> append()在被选元素的结尾插入内容
preappend()在被选元素的开头插入内容
after()在被选元素之后插入内容
before()在被选元素之前插入内容
***
### 12、删除元素
1、通过jQuery，可以很容易地删除已有的HTML元素
> 1、remove()删除被选中元素（及其子元素）
2、empty()从被选元素中删除子元素

2、过滤被删除的元素
> jQuery remove() 方法也可接受一个参数，允许您对被删元素进行过滤。
比如：
$("p").remove(".italic")删除class="italic"的所有p元素
***
### 13、获取并设置CSS类
1、通过jQuery，可以很容易地对css元素进行操作。
> addClass()向被选元素添加一个或多个类
removeClase() 从被选元素删除一个或者多个类
toggleClass()对被选元素进行添加/删除类的切换操作
css()设置或返回样式属性

2、css()方法设置或返回被选元素的一个或多个样式属性
> 1、返回css属性
\$("p").css("background-color");
2、设置css属性
\$("p").css("background-color", 'yellow');
3、设置多个css属性
$("p").css({"background-color":"yellow","font-size":"200%"});
***
### 14、获取元素尺寸
1、通过jQuery，很容易处理元素和浏览器窗口的尺寸
***方法***
> 1、width()方法设置或返回元素的宽度（不包括内边距、边框或外边距）
2、height()方法设置或返回元素的高度（不包括内边距、边框或外边距）
3、innerWidth()方法返回元素的宽度（包括内边距）
4、innerHeight()方法返回元素的高度（包括内边距）
5、outerWidth()方法返回元素的宽度（包括内边距和边框）
6、outerHeight()方法返回元素的高度（包括内边距和边框）
***
### 15、jQuery遍历元素
1、祖先
> 祖先是父、祖父或曾祖父等等
通过jQuery，您能够向上遍历DOM树，以查找元素的祖先

1.1、向上遍历DOM树
> 1、parent()返回被选元素的直接父元素
2、parents()返回被选元素的所有祖先元素，它一路向上直到文档的根元素（<html></html>）。
3、parentUntil()返回介于两个给定元素之间的所有祖先元素（不包括最后的祖先元素）

```
$(document).ready(function(){
    $("span").parents("ul");
});
返回被选元素的祖先元素，并且该祖先元素为ul
$(document).ready(function(){
    $("span").parentsUntil("div");
});
```
2、后代
2.1、children()返回被选元素的所有直接子元素
该方法只会向下一级对DOM树进行遍历
```
返回每个div元素的所有直接子元素
$(document).ready(function(){
    $("div").children();
});
返回类名为 "1" 的所有 <p> 元素，并且它们是 <div> 的直接子元素
$(document).ready(function(){
  $("div").children("p.1");
});
```
2.2、find()方法返回被选元素的后代元素，一路向下直到最后一个后代
```
返回属于 <div> 后代的所有 <span> 元素
$(document).ready(function(){
  $("div").find("span");
});
返回 <div> 的所有后代
$(document).ready(function(){
  $("div").find("*");
});