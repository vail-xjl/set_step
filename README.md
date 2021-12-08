<h1>介绍</h1>
<h5>这份儿代码是为了在用户有多个小米运动账号的前提下批量自动刷步的代码，本代码通过动态网络爬虫里的selenium包驱动谷歌浏览器核，打开现有的刷步网站，批量提交用户的账号，达到自动化批量刷步的目的。</h5>
<h1>注意：</h1>
<h3>本代码为笔者学习动态网络爬虫时练习的小项目，仅供各位读者学习交流，切勿用于违规违法用途，不得侵犯任何人的任何利益，使用者如开始使用，则默认同意本条款。如果本代码有侵犯任何人的利益，请联系我删除，谢谢。</h3>
<h1>使用说明</h1>
<h5>※说在前面，本代码是Python代码，使用本代码无需任何代码基础（因为笔者都写好了），但是需要读者自己做一小点工作，如果你懒得一点都不想动的话，可以到此为止退出了。</h5>
<h5>※当然如果你是IT界的或者是喜欢敲代码的人，那么你可能很容易就开始使用了（如果你有pycharm编译器并且正好你的运行环境下有selenium这个包的话）</h5>
<ol>
    <li>准备任意一个可以运行Python代码的编译器（笔者推荐pycharm，其他的也完全可以，安装方式可以问度娘）</li>
    <li>在这个网址里【 http://npm.taobao.org/mirrors/chromedriver/ 】找到与你的谷歌浏览器版本相同的核，点击下载下来，命名为【chromedriver】</li>
    <li>在你想要运行这份儿刷步代码的环境下安装selenium包
        <ul>
            <li>按win+R，输入cmd并敲回车</li>
            <li>进入你的虚拟环境（当然如果你不是专业Python开发者，忽略这步，因为你用基础环境就可以了）</li>
            <li>输入这条命令【pip install selenium】，敲回车</li></ul>
    <h5>所有工作准备完毕，开始使用（是不是很简单）</h5>
    </li>
    <li>打开你的编译器，打开run.py这份儿代码
    <ul>
        <li>首先修改第15行代码的驱动核路径，下载的文件放到哪，双引号里面就写到哪，最后加上这个文件的名字（如果你把第2步下载下来的驱动核和【run.py】放到一起的话，忽略这步，推荐你放到一起）</li>
        <li>在第17行代码里添加你要刷步的账号、密码以及步数，格式为【账号#密码#步数】，参照第16行</li>
        <li>大功告成，运行这份儿代码</li>
    </ul>
    </li>
    <li>
        一次设置，永久免费自动批量刷步
    </li>
</ol>
<h1>可能出错的原因</h1>
<ol>
    <li><h5>找不到驱动核或者驱动核版本不对</h5>
        解决：先做第2步，再做第4步的第一个
    </li>
    <li><h5>报错没有selenium这个包</h5>
        解决：直接做第3步，或者百度【怎么安装selenium包】
    </li>
    <li><h5>后台提醒网页改版</h5>
        解决：请给我留言，我看到后会第一时间处理
    </li>
    <li>
        <h5>网页提醒只能提交3次</h5>
        解决：每换一个网络就能多刷3次，运行完一次之后出现弹窗先别点，等换好网之后再点【确定】。（用手机给电脑开热点，然后手机开飞行模式，再关了，你的手机网络就换了，理论上可以无限刷步）
    </li>
    <li><h5>出现其他问题</h5>
        解决：请给我留言，我看到后会第一时间处理
    </li>
</ol>
