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