### 1、起步
1、浮动属性（float），浮动的元素会脱离文档流，后面的元素会补充上去
> 浮动元素只会对后面的元素产生影响，不会对前面的元素产生影响
，后面的元素会占据原来的浮动元素的位置

2、浮动后的元素可以看成是行级的块，我们可以设置宽高。（而单纯的行级元素是不可以设置宽高的）。
3、行级元素设置浮动属性float后，会变成行级块元素，可以设置宽高。
4、但是我们要强调语义化，尽可能做到顾名思义，不能用span来当div使用。
*** 
### 2、清除浮动
1、通过设置伪元素属性来清除浮动高度坍塌
```
css代码
main{
    border:solid 2px black;
    width:600px;
    padding:20px;
    margin:0 auto;
}
main::after {
    content:" ";
    clear:both;
    display:block;
}
div {
    width:200px;
    height:200px;
    box-sizing:border-box;
}
div:nth-of-type(1){
    border:solid 2px red;
}
div:nth-of-type(2){
    border:solid 2px blue;
}

html代码
<body>
    <main>
        <div></div>
        <div></div>
    </main>
</body>