#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【跳转到登录页面】:
# (1): -> 移动模拟器一上来应该是在移动端的 TPshop 的首页面。所以应该获取这个包名和启动名。在 base_driver 里面去加,然后
#         就启动首页成功了。
#
#      -> 点击【我的】按钮
#
#      -> 点击【登录/注册】按钮跳转到输入【用户名】和输入【密码】页面即可。
#
#
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
# (2): -> 创建 Page 统一入口页面。
#
#      -> 创建 IndexPage 首页页面。
#
#      -> 然后只要是被 git 管理的项目那么有可能都会弹出一个小的窗口,意思就是说是否要交给 git 去进行管理。然后前面勾选按
#         钮然后在选 yes 即可,然后你的文件就会变颜色了,这个文件变颜色一会在说,那么还有一个主动添加的方法就是进入 ---->↓
#         ctrl + alt + s 页面 -> Version Control 的选项 -> 然后对应右边的页面里面会有灰色路径的显示我们选中这 ---->↓
#         个路径然后点击 add 添加然后在点下面的 ok 也能被 git 进行一个管理,然后文件也变色了。
#         解答颜色: 黑色/白色的字: 说明是提交过的。
#                  蓝色字: 说明我这个没提交过的版本[修改了文件]。
#                  绿色: 说明我这个没提交过的版本[新加的文件]。
#
#      -> 然后我们去 IndexPage 页面。
#
#      -> 然后我们在去 MyPage 页面。
#
#      -> 然后我们在去 Page 页面添加统一入口。
#
#      -> 然后我们在去 test_login 执行脚本测试用例。
#
#      -> 然后提交一次,用命令或者图形界面都可以提交。
#
#      -> 扩展: 关于怎么下载和更新别人的代码,在 sourceTree 中我们只需要把你要的代码项目的一个 github 的项目的地址给
#               放入到 sourceTree 里面的 clone 里面的 原路径/URL 里面即可将你需要的代码项目给弄到你的本地电脑了, 然
#               后如果对方修改了代码那么我们直接点击【拉取】按钮即可。 然后比如说项目已经 clone 到你的本地了如果你想在
#               这个 sourceTree 里面看你当前项目的提交版本的话,  那么就双击点 master 里面的分支点即可然后会弹出一个框
#               为【确认更改工作副本】然后选中某一个点确定,然后在看真实的文件的内容。 就能看到对应提交版本的代码了。那么
#               就是说如果我想看第一个版本的代码那么就双击这个第一个版本的分支然后弹出这个【确认更改工作副本】 框, 然后点
#               击确定即可查看了。
#
#
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
# (3): 获取弹框(toast):
#      -> 去大纲 toast 里面去查看。
#      -> 可以写一个针对查看 toast 的小 demo 看 demo 文件夹。
#      -> 然后去 demo 页面查看。
#
#
#
#
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
