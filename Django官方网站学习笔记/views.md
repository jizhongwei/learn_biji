### 视图部分（views）
***这部分的学习笔记是本人看官方网站提供的文档学习的，纯属记录文档要点***
#### 1、URL分发器（dispatcher）
搭建网页站点的一个重要细节就是设计简洁（clean）、优美（elegant）的url模式，恰好Django允许我们定义好看的、容易记忆的url
> 一般情况下，请求会根据settings文件的ROOT_URLCONF（指向一个python模块）来进行路由分发，但是如果HttpRequest对象本身有urlconf属性（通过中间件设置）的话，urlconf属性会被使用来替代ROOT_URLCONF

***
#### 2、自定义路由转换器（custom path converters）
***为了实现更复杂的匹配需求，我们可以自定义自己的路由转换器***
> 一个路由转换器就是一个python类（class），由一下部分组成
1、一个regex类属性，是一个字符串
2、一个to_python(self, value)方法，它处理转换匹配到的字符串为相应的类型，并传递到视图函数。如果转换失败会引发ValueError错误，并返回一个404响应给用户。
3、一个to_url(self, value)方法，处理转换python类型为一个字符串，以便在url中使用。

```
1、定义转换器
class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
2、注册转换器，并使用
from django.urls import path, register_converter
from . import converter, views

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('article/2003/', views.special_case_2003),
    path('aticle/<yyyy:year>/', views.year_achive),
    ...
]
```
***
#### 3、指定视图参数默认值
```
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.page),
    path('blog/page<int:num>/', views.page),
]

def page(request, num = 1):
    pass
```
上面的例子中，有两个url同时指向同一个视图函数（views.page），但是第一个url模式没有捕捉任何东西，如果是第一个url先匹配，视图函数会使用num的默认值；如果是第二个url匹配，视图函数会使用url捕捉的num。
***
#### 4、错误处理
1、Django提供一系列错误匹配处理视图函数
```
handler400 – See django.conf.urls.handler400.
handler403 – See django.conf.urls.handler403.
handler404 – See django.conf.urls.handler404.
handler500 – See django.conf.urls.handler500.
```
它们只能在root urlconf中设置，在任何其他urlconf中设置将不会起作用。
***
#### 5、shortcut function
1、redirect(to, *args, permanent = False, **kwargs)
> 1、to可以是一个model实例，但是要定义get_absolute_url()方法，
2、也可以是一个url名称，redirect函数会调用reverse()方法来反转成url
3、传递一个绝对或者相对url路径，比如http://www.baidu.com或者"/some/url/"。

默认情况下，redirect()函数返回一个临时的重定向，我们可以设置permanent参数为True来返回一个永久重定向。

#### 6、视图错误处理
1、404错误。如果DEBUG为True，404 view将不会被使用，网页会呈现一些调试信息。
2、403错误。
```
from django.core.exceptions import PermissionDenied

def edit(request, pk):
    if not request.user.is_statff:
        raise PermissionDenied
```