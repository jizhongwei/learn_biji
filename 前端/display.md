### 1、display属性
1、block 块级元素
> 常用块级元素有div、p、ul、ol、h1~h6等
块级元素会默认占满父元素的宽度且独占一行
\<div>
    \<p>xxxx\<p>
\<div>

2、inline-block 行内块级元素
3、inline 行内元素
>常见的行内元素有span、img、a、input、button、textarea、select等，它的宽度完全由内容撑开，不能为其设置宽高
***除非父元素一行放满了，行内元素不然不会换行***
行内元素受父元素的text-align的影响，父元素设置text-align：center，行内元素会居中显示
行内元素受父元素的white-space的影响，父元素设置white-space：nowrap，行内元素将不会换行

**实际应用**
在轮播图中，最外层的容器宽度是固定的，且overflow:hidden

第二层容器ul的宽度则是它子元素的宽度之和，因为子元素的个数不确定，所以不能在css中设定确定的宽度值，通常我们都是利用js计算出它子元素的宽度之和再赋予ul元素，今天这个例子我们不用js，利用inline-block宽度由子元素撑开的特性,让ul的宽度由子元素撑开

设置ul的样式display:inline-block,同时为了让所有的li标签不换行，设置white-space: nowrap

为了能让ul的white-space: nowrap生效，li标签需要设置display:inline-block，要消除代码换行造成的间隔，可以让父元素的字体大小设置为0，,然后子元素里面再设置字体大小即可

```
<div>
<ul>
    <li>inline-block</li>
    <li>inline-block</li>
    <li>inline-block</li>
    <li>inline-block</li>
</ul>
</div>
```

4、none 隐藏元素，不占据空间

