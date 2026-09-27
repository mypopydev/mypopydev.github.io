<span class="origpage" title="英文原版第 343 页">343</span>

# 注释
## 序言
1. 威廉·罗恩·哈密顿写给 P. G. Tait 的信，发表于 P. G. Tait 的 *An Elementary Treatise on Quaternions*（Cambridge: Cambridge University Press, 1890）第三版序言中。
2. 麦克斯韦并没有使用“向量场”这个术语，但他所创造的正是向量场（几年后，他在 1873 年的 *Treatise on Electricity and Magnetism* 中把这一点说得很清楚）；这意味着什么、它又如何影响了后来的物理学家，我将在后续各章中探讨。
3. *古代表格数学*：参见 Eleanor Robson, "Mathematical Cuneiform Tablets in the Ashmolean Museum, Oxford," *SCIAMVS* 5 (2004): 2–65；Duncan J. Melville, "Computation in Early Mesopotamia," in *Computations and Computing Devices in Mathematics Education before the Advent of Electronic Calculators*, ed. A. Volkov and V. Freiman (Switzerland: Springer Nature, 2018), 25–47。Melville 强调了解读这类古代文献及其预期用途时存在的困难；Robert Middeke-Conlin 则指出，关于部分美索不达米亚数学泥板的用途之争至今仍在继续，见 "The Mathematics of Canal Construction in the Kingdoms of Larsa and Babylon," *Water History* 12 (2020): 105–28。不过，Daniel Mansfield 2021 年的研究为其中的一些解读增添了重要的清晰度；见他的 "Plimpton 322: A Study of Rectangles," *Foundations of Science* 26 (2021): 977–1005。
<span class="origpage" title="英文原版第 344 页">344</span>

4. 关于美索不达米亚的土地使用与测量，以及普林顿 322 号泥板所起的作用，我得益于 Mansfield 的 "Plimpton 322"。Mansfield 发现了 Si427 号泥板的毕达哥拉斯性质，他也为普林顿 322 号泥板提供了新见解，并给出了美索不达米亚乘法表的细节。不过，关于他对美索不达米亚三角学的论断，参见例如 Evelyn Lamb, "Don't Fall for Babylonian Trigonometry Hype," *Scientific American*（博客），2017 年 8 月 29 日。
5. *澳大利亚原住民天文学*：Duane Hamacher, "Stories from the Sky: Astronomy in Indigenous Knowledge," *The Conversation*, 2014 年 12 月 1 日；Ray P. Norris, Cilla Norris, Duane W. Hamacher, and Reg Abrahams, "Wurdi Youang: An Australian Aboriginal Stone Arrangement with Possible Solar Indications," *Rock Art Research* 30, no. 1 (2013): 55–65。
6. 托勒密那些辉煌、但如今大多已散佚的资料来源中，有克尼多斯的欧多克索斯——他或许是开启天文学几何建模进程的第一人，并且开创了我们将在第 2 章遇到的、原始微积分的穷竭法；昔兰尼的埃拉托斯特尼——他显然使用了一种基本的经纬度，并且在仅靠一根影子杆和几根简单量杆的条件下，异常准确地推算出了地球的大小；尼西亚的喜帕恰斯——他似乎是第一个系统地用 360° 圆来精确几何表示行星运动的人，其数学与天文学造诣之高，使他发现了二分点岁差；还有佩尔加的阿波罗尼奥斯——他在对圆锥曲线的数学分析中使用了一种事后建立的坐标系，托勒密的行星运动本轮与偏心圆模型正是直接建立在他的基础之上。
7. 例如，假设你正以 35 mph 的速度朝**东北**方向行进，你的向量会指向与坐标轴成 45° 的方向，但它的分量必须满足：用毕达哥拉斯定理把它们合起来时，模仍是 35。所以，这个向量就是 $\left(\frac{35}{\sqrt{2}},\frac{35}{\sqrt{2}}\right)$。
向量 $\left(\frac{35}{\sqrt{2}},\frac{35}{\sqrt{2}}\right)$ 由<a href="#fig-0-2">图 0.2</a> 得出，依据是：在求分量时需要用到 $\sin 45^{\circ}=\cos 45^{\circ}=\frac{1}{\sqrt{2}}$；如果你对三角学有些生疏，可以预先看一眼<a href="#fig-3-4">图 3.4</a>，就会明白为什么垂直分量和水平分量需要 sin 45° 与 cos 45°。然后，用毕达哥拉斯定理，有 $\left(\frac{35}{\sqrt{2}}\right)^{2}+\left(\frac{35}{\sqrt{2}}\right)^{2}=35^{2}$，于是向量是 $\left(\frac{35}{\sqrt{2}},\frac{35}{\sqrt{2}}\right)$，模为 35。
<span class="origpage" title="英文原版第 345 页">345</span>

8. 四维速度的各分量是仿照普通速度来定义的，即（时空）坐标对（固有）时间的导数。固有时就是可以直接测量的“时钟时间”，也就是相对于观察者静止的那只时钟所记录的时间。
9. *疯帽匠戏仿猜想*指的是哈密顿某种新型乘法的一个后果（即不可交换性，我们将在第 1 章和第 4 章看到）；这一猜想由维多利亚文学研究专家 Melanie Bayley 提出，见 "Alice's Adventures in Algebra: Wonderland Solved," *New Scientist*, 2009 年 12 月 16 日。Michael Brooks 在他的 *The Art of More* (Melbourne: Scribe, 2021), 194–96 中与 Bayley 一起继续讲了这个故事。
Brooks 和 Bayley 把道奇森描绘成一个保守、平庸的数学家（另见例如 Michael Deakin, "Lewis Carroll—Mathematician?," *Function* 18, no. 1 [1994 年 2 月]: 10–18）——一个不可能理解哈密顿工作的人。这很可能是事实。然而，道奇森／卡罗尔今日的数学声望，并不建立在他生前发表的工作上，而是建立在后世发现的晚期手稿上：关于投票方法，以及关于符号逻辑（在其中他用荒诞命题和符号代数来教授逻辑规则）；参见 Francine Abeles, "Logic and Lewis Carroll," *Nature* 527 (2015 年 11 月 19 日): 302–4；Amirouche Moktefi, "Why Make Things Simple When You Can Make Them Complicated? An Appreciation of Lewis Carroll's Symbolic Logic," *Logica Universalis* 15 (2021): 359–79；想领略一下卡罗尔的逻辑谜题，可参见夏威夷大学网站 <http://math.hawaii.edu/~hile/math100/logice.htm>。
不过要注意，在卡罗尔的 *Symbolic Logic* (New York: Dover, 1958；原版出版于 1897 年，即《爱丽丝》问世三十年后) 中，他建立了一套**可交换**的符号逻辑代数（例如第 35、70 页）：卡罗尔的等式关乎逻辑而非代数，但耐人寻味的是，他选择强调“交换性”——或许他确实对哈密顿的不可交换乘法有所不满。又或许，他只是想把自己那些符号化的逻辑命题与向量积区分开来。
## 第 1 章
1. 哈密顿在他的 *Lectures on Quaternions* 序言中说，他之所以被引向四元数，是因为他想把“*计算*”与“*几何*”联系起来，并想把这些计算“从平面推向空间”。后文中他展示了如何做三维旋转；见 *Lectures on Quaternions* (Dublin: Hodges and Smith, London: Whittaker, and Cambridge: Macmillan, 1853), 269 (art. 282)。
<span class="origpage" title="英文原版第 346 页">346</span>

2. Melanie Bayley（"Alice's Adventures in Algebra"）指出了这一点，以及其他一些在她看来表明卡罗尔在戏仿哈密顿的例子。但也有可能，卡罗尔只是想把逻辑的规则与哈密顿代数的规则区分开来。
3. *哈密顿的电学类比*出自他写给儿子 Archibald 的信（转引自 Michael J. Crowe, *A History of Vector Analysis* [Notre Dame, IN: University of Notre Dame Press, 1967], 29–30）。他在 1858 年写给 P. G. Tait 的信中也给出了相似的描述：<https://www.tcd.ie/library/manuscripts/blog/tag/moon-landing/>。那件纪念性艺术装置由 Emma Ray 创作；见皇家爱尔兰学院的网站——该作品由它联合委托创作——尤其是记录准备与安装过程的 YouTube 视频，见 <https://www.google.com/search?client=safari&rls=en&q=Commemorative+art+installation+Hamilton+Broombridge+Luas&ie=UTF-8&oe=UTF-8#fpstate=ive&vld=cid:a9bfbdde,vid:1nQct3p3184>。
4. 在参观都柏林三一学院老图书馆时，阿姆斯特朗在哈密顿的大理石半身像旁驻足，向他的向导解释了四元数如何辅助航天器导航：Estelle Gittins，2019 年 7 月 19 日，<https://www.tcd.ie/library/manuscripts/blog/tag/moon-landing/>。
5. 我改编了一幅据认为可能出自毕达哥拉斯的图示，该图见 T. L. Heath, *Translation of Euclid's Elements* (Cambridge: Cambridge University Press, 1925)，又转载于 John Stillwell, *Mathematics and Its History* (New York: Springer-Verlag, 1989), 7。欧几里得更精妙的证明，见 Carl Boyer, *A History of Mathematics*, rev. Uta Merzbach (New York: John Wiley and Sons, 1991), 108。
6. 有不同版本流传，但可参见例如美国国会图书馆 <https://www.loc.gov/item/2021666184/>。
7. 现代数学家更倾向于把 *i* 定义为 *x*<sup>2</sup> + 1 = 0 的（主）解，而不是把它指定为 $\sqrt{-1}$；换句话说，*i* 通常是通过它的平方 *i*<sup>2</sup> = −1 来定义的，而不是作为某个平方根。这是因为后一种做法会导致如下这样的悖论：
$-1=i\times i=\sqrt{-1}\times\sqrt{-1}\sqrt{\left(-1\right)\left(-1\right)}=\sqrt{1}=\pm 1,$
而如果你取正根，就会得到 −1 = 1，这显然是错误的！
8. *笛卡尔论虚数*：Brian E. Blank, "Book Review: An Imaginary Tale by Paul Nahin," *Notices of the AMS*（1999 年 11 月）: 1233。
<span class="origpage" title="英文原版第 347 页">347</span>

9. 花拉子米的引文见 Boyer, *History of Mathematics*, 229；他用几何方法配方的说明见 231。*Al-jabr* …… 的译文及几何实例：Raymond Flood and Robin Wilson, *The Great Mathematicians* (London: Arcturus, 2011), 46–47。
10. 关于哈里奥特非凡的生平与工作，详见我的 *Thomas Harriot: A Life in Science* (New York: Oxford University Press, 2019) 及其中所引文献。请注意，他身后出版的 *Praxis* 是由他的朋友们整理而成的，但显然这些朋友的数学水平远不及他：他的手稿中包含比他们所出版的更为精深的工作，其中就包括对虚数的使用。
11. 关于代数符号演化的迷人历史，见 Joseph Mazur, *Enlightening Symbols: A Short History of Mathematical Notation and Its Hidden Powers* (Princeton, NJ: Princeton University Press, 2014)。
12. 1905 年，爱因斯坦除了发表狭义相对论和 *E* = *mc***2** 的论文外，还发表了两篇关于布朗运动与分子大小的重要论文，以及一篇关于光的量子理论的开创性论文。入门概述见我的 *Young Einstein and the Story of E = mc<sup>2</sup>* (Sydney: Ligature, 2014)。
13. 这道题出自泥板 CBS 43，译文见 Eleanor Robson, "Mathematical Cuneiform Tablets in Philadelphia, Part I: Problems and Calculations," *SCIAMVS* 1 (2000): 11–48；为了便于说明，我把问题右端的数改成了 21——泥板上（见第 39 页）写的是 41，但正如 Robson 所说（第 42 页），泥板上的符号并不完全清晰，而且按现有释读也得不出当时惯用的那种整数解或两位（六十进制）解。我关于古巴比伦几何配方方法的图示改编自该书第 42 页。
14. *运河等*：Robert Middeke-Conlin, "The Mathematics of Canal Construction in the Kingdoms of Larsa and Babyon," *Water History* 12 (2020): 105–28。
15. 需要注意的是，更早的数学家——包括传说中十二世纪初的波斯诗人欧玛尔·海亚姆，他同时也是一位数学家——已经找到了纯几何的方法来求解某些具有正根的三次方程，方法是求两条曲线的交点：Boyer, *History of Mathematics*, 241；Flood and Wilson, *The Great Mathematicians*, 49。关于图西，见 J. J. O'Connor 和 E. F. Robertson 为他撰写的 MacTutor 条目，<https://mathsh> istory.st-andrews.ac.uk/Biographies/Al-Tusi_Sharaf/。
<span class="origpage" title="英文原版第 348 页">348</span>

16. *卡尔达诺的底层算法*（基于塔尔塔利亚的）用于求解形如 *x*<sup>3</sup> = *cx* + *d* 的方程，具体如下：选取新的变量 *u, v*，令 *x* = *u* + *v, uv* = c/3。把它们代入原方程，你会得到 *u*<sup>3</sup> + *v*<sup>3</sup> = *d*；消去 *v*，这就变成了一个关于 *u*<sup>3</sup> 的二次方程，可用求根公式求解。把这个 *u*<sup>3</sup> 的解代入 *u*<sup>3</sup> + *v*<sup>3</sup> = *d*，解出 *v*<sup>3</sup>。再对 *u*<sup>3</sup> 和 *v*<sup>3</sup> 开立方，求得 *u, v*，从而得到 *x* = *u* + *v*。这一方法极为巧妙，而且是在没有那种让思路更易于追踪的现代符号的情况下创造出来的。我所举的例子 *x*<sup>3</sup> = 6*x* + 40，以及卡尔达诺求解它的算法——连同他对立方的几何补全——见他的 *Ars Magna* 第 12 章，重印于 R. Laubenbacher and D. Pengelley, "Algebra: The Search for an Elusive Formula," in *Mathematical Expeditions*, Undergraduate Texts in Mathematics (New York: Springer, 1999), 230; <https://doi.org/10.1007/978-1-4612-0523-4_5>。
17. 例如，薛定谔方程描述光子、电子及其他亚原子粒子等基本粒子的动力学——而它含有 *i*。电磁波用复数形式处理起来也更方便，所以 *i* 是各种现代技术背后的功臣。
18. *沃利斯论哈里奥特*：转引自 Jacqueline Stedall, "Rob'd of Glories: The Posthumous Misfortunes of Thomas Harriot and His Algebra," *Archive for History of Exact Sciences* 54, no. 6 (2000 年 6 月): 490。*哈里奥特最先以代数（符号）方法解三次方程*：这一看法最早由伟大的数学家拉格朗日提出；见 Seltman, "Harriot's Algebra: Reputation and Reality," in *Thomas Harriot*, vol. 1, *An Elizabethan Man of Science*, ed. Robert Fox (Aldershot: Ashgate, 2000), 185。
19. 类似地，二次方程有两个解，四次方程有四个解，以此类推。德国数学家 Peter Roth 大约在同一时期（在他 1608 年的 *Arithmetica Philosphica* 中）提出了这种次数与解的个数之间的联系，但他既没有用符号书写方程，也没有探讨复根。由哈里奥特的“因式”构造所暗示的“代数基本定理”的严格证明，要到两百年后才出现——哈里奥特本人并未宣称那么多。他用因式和符号求得复数解的一个例子，见例如 British Library Manuscript 6783, fols. 157, 156。
<span class="origpage" title="英文原版第 349 页">349</span>

20. 仿照欧拉的做法（或第 3 章的<a href="#fig-3-4">图 3.4</a>、<a href="#fig-3-6">图 3.6</a> 及相关讨论），你可以把复数 *a* + *ib* 写成 *r*(cos θ + *i* sin θ) = *re<sup>i</sup>*<sup>θ</sup>，其中 $r=\sqrt{\left(a^{2}+b^{2}\right)}$，θ 则由反余弦和反正弦相应地确定。由棣莫弗定理（或干脆由指数律），这个数的立方根是 $\sqrt[3]{\left(re^{i\theta}\right)}=r^{1/3}e\frac{i\left(\theta+2k\pi\right)}{3}$，其中 *k* = 0, 1, 2 给出三个不同的根。把它应用于 $\sqrt[3]{\left(2+11i\right)}+\sqrt[3]{\left(2-11i\right)}=r^{1/3}e\frac{i\left(\theta+2k\pi\right)}{3}+r^{1/3}e\frac{i\left(-\theta-2k\pi\right)}{3}=2r^{1/3}\cos\frac{\left(\theta+2k\pi\right)}{3}$，你就得到卡尔达诺方程的三个解 $x=4,-2+\sqrt{3},-2-\sqrt{3}$。过程略显烦琐，但所有步骤只用到高中高年级或大学一年级的数学。
21. *哈里奥特的引文*：British Library Additional Manuscript 6783 fol. 186。另见 Jacqueline Stedall, "Notes Made by Thomas Harriot on the Treatises of François Viète," *Archive for Exact Sciences* 62, no. 2 (2008 年 3 月): 179–200。
22. *Seltman 的引文*见她的 "Harriot's Algebra," in *Thomas Harriot*, vol. 1, *An Elizabethan Man of Science*, ed. Robert Fox (Aldershot: Ashgate, 2000), 184，着重标记为我所加。关于哈里奥特对复数解和负数解的使用，Seltman 精辟地分析了哈里奥特的手稿优于其身后出版的 *Artis Analyticae Praxis* 之处——后者由他那几位才具不及的朋友依据他们从他手稿中所理解的内容拼凑而成，其中包括他们对哈里奥特使用虚数和负数的排斥。
## 第 2 章
1. 声波是气压的变化，石子激起的冲击波在池塘的水中传播——但光是从太阳穿过**虚空**而来的。那么光波中究竟有什么在起伏呢？那种神秘而无法探测的“以太”早已被假定存在，而麦克斯韦最终会给出答案（第 6 章）。玛丽·萨默维尔的回忆见她的回忆录 *Personal Recollections from Early Life to Old Age of Mary Somerville*，由其女儿 Martha Charters Somerville 编辑 (London: John Murray, 1873), 132。
2. *光镊*利用激光束的辐射压来移动微小粒子，这是数学预测的又一个例子：正是麦克斯韦在数学上预言了辐射压的存在，三十年后，即 1901 年，它被实验证实。*麦克斯韦论辐射压*：*Treatise on Electricity and Magnetism* (Oxford: Clarendon Press, 1873，第 3 版 [1891] 于 1954 年由 Dover 重印), 2:440–41 (arts. 792–93)。
3. 阿赫摩斯写下的就是如今所称的莱因德纸草书，其名得自 1850 年代在埃及买下它的收藏家；它现在藏于大英博物馆。
4. *论牛顿*：Richard S. Westfall, *Never at Rest: A Biography of Isaac Newton* (Cambridge: Cambridge University Press, 1980)；Westfall 也为《大英百科全书》撰写了牛顿的条目。
5. 对莱布尼茨的描述出自 Philip P. Wiener 编 *Leibniz Selections* (New York: Charles Scribner's Sons, 1951) 导言的第一页。
<span class="origpage" title="英文原版第 350 页">350</span>

6. *定义无穷小与极限的尝试*：莱布尼茨：“一个微分小于任意给定的量”，以及“如果有人宁愿拒斥无穷小量，那么也可以假定它们小到人所判断的必需程度，使之不可比较，从而所产生的误差无关紧要，或小于任何给定的量。”牛顿：“在任何有限时间内持续趋于相等、并在该时间结束之前彼此接近到小于任何给定差量的量与量之比，最终成为相等。”
*现代定义*：在适当的定义域上定义 *f*(*x*)，$\lim_{x\to\alpha}f\left(x\right)=L$ 的意思是：给定任意数 ε > 0，我们都能找到一个数 δ > 0，使得当 *a* − δ < *x* < *a* + δ 时，*f*(*x*) 满足 *L* − ε < *f*(*x*) < *L* + ε。对于 *x* 趋于无穷的极限，我们有 $\lim_{x\to\infty}f\left(x\right)=L$，如果对任意数 ε > 0，我们都能找到一个数 *M*，使得当 *n* > *M* 时有 *L* − ε < *f*(*x*) < *L* + ε。这一定义源自牛顿尝试定义极限两百年之后柯西、魏尔斯特拉斯等人的工作。
7. *沃利斯承认了哈里奥特*（还有奥特雷德和笛卡尔），见他的 *Arithmetica Infinitorum*——转引自 Boyer, *The History of Calculus and Its Conceptual Development* (New York: Dover, 1959), 170；另见 168–69。关于沃利斯对哈里奥特的亏欠及其见解独到的钦佩，详见 Stedall, "Rob'd of Glories," 481–90。*牛顿首次发表他的微积分*是在《原理》第 2 卷。虽然他的大多数证明是几何式的，但他有时也用代数符号给出微积分的算法，例如第 2 卷第 2 节引理 2。当他给出几何图形时，有时也用符号代数来解释算法或作图，如第 2 卷命题 10 问题 3。即便在第 1 卷，微积分概念也常常在相关的几何作图中清晰可见（例如他对命题 39 的证明）。不过，在他最早的微积分手稿中，他用的是代数而不是几何。
<span class="origpage" title="英文原版第 351 页">351</span>

8. *沃利斯对阵费马等人*：Jacqueline Stedall, "John Wallis and the French: His Quarrels with Fermat, Pascal, Dulaurens, and Descartes," *Historia Mathematica* 39 (2012): 265–79。*笛卡尔与哈里奥特*：沃利斯的说法有些夸张，但它们并非他的创见，因为笛卡尔在写出他著名的 *La géometrie* 之前是否见过哈里奥特的 *Praxis*，确实存在不确定之处；当然，各自独立发现并不罕见，而且笛卡尔比哈里奥特走得远得多，但笛卡尔在交代资料来源方面出了名地含糊，连他的同胞、韦达的编者 Jean Beaugrand 都注意到笛卡尔的工作与哈里奥特的工作有相似之处。见 Stedall, "Rob'd of Glories," 488–89，以及 Jacqueline Stedall, "Reconstructing Thomas Harriot's Treatise on Equations," in *Thomas Harriot*, vol. 2, *Mathematics, Exploration, and Natural Philosophy in Early Modern England*, ed. Robert Fox (Farnham, Surrey: Ashgate, 2012), 62，另见 Carl Boyer, *The Rainbow: From Myth to Mathematics* (Princeton, NJ: Princeton University Press, 1987), 203, 211。
9. *沃利斯*：摘自 John Stillwell, *Mathematics and Its History* (New York: Springer-Verlag, 1989), 110–12 中的沃利斯小传。
10. *沃利斯的政治际遇*：见博德利图书馆对 J. Wallis, *A Collection of Letters and Other Papers*, MS e Mus. 203 的描述，<https://archives.bodleian.ox.ac.uk/repositories/2/resources/5805>；以及 J. J. O'Connor and E. F. Robertson, <https://mathshistory.st-andrews.ac.uk/Biographies/Wallis/>。
11. *爱因斯坦对牛顿的评价*出自他的 *Ideas and Opinions* (1954; New York: Three Rivers Press, 1982), 254–55。
12. *胡克关于行星运动的工作*：例如 Michael Nauenberg, "Robert Hooke's Seminal Contributions to Orbital Dynamics," *Physics in Perspective* 7 (2005): 1–31。Nauenberg 详细研究了胡克的工作以及牛顿对它的利用。给予胡克应得的评价是很重要的，尽管我倾向于认为 Nauenberg 高估了胡克的数学能力，因为他的论证只建立在一个作图之上，而该作图完成于 1685 年，那时他很可能已经看过牛顿的初步论文 *De Motu*。无论如何，胡克构造出了由与距离成正比的力所产生的轨道；虽然他的方法新颖，但与《原理》中针对各种力和运动的**数百个**计算相比，这只是**一个**计算。
<span class="origpage" title="英文原版第 352 页">352</span>

13. *牛顿的“干瘪的计算者”*：写给哈雷的信，转引自 Nauenberg, "Robert Hooke," 7。Nauenberg 称之为“一篇激烈的抨击”，这在我看来——考虑到《原理》的广度与胡克贡献的对比（参见上一条注释）——说明他为胡克辩护得过于激烈了。*现代数学：计算还是创造*：Patrick Bangert 发表于澳大利亚数学会 *Gazette* 32, no. 3（2005 年 7 月）的一篇异想天开的报告表明，许多数学家认为自己的学科更多地关乎模式、语言、艺术或逻辑，而不是应用。类似地，2021 年 7 月，Ole Warnaar 在 *Gazette*（第 48 卷第 3 期）上报告了学会成员对澳大利亚数学课程改革草案的反馈：批评包括其过于功利化的取向。当然，把数学用于实际是令人兴奋的，也具有重要的社会意义，Warnaar 也赞同教授这类技能；但他同时感叹，“在传达数学内在的美、以及人们从学习和理解新的数学概念中获得的乐趣方面，所做的努力还不够”。
14. *在蒸发过程中*，热量提高了水分子的动能，使它们得以挣脱把分子束缚成液体的电性键。紫色的布把较冷的紫光反射到我们眼中，而吸收其他较暖的颜色。所以它干得最快，因为它比床单上的其他颜色吸收热量更快。埃米莉·迪沙特莱的结果，见她 1738 年 *Essay on Fire*（*Dissertation sur la nature et la propagation du feu*）的扩充版，出版于 1744 年 (Paris: Chez Prault Fils)。
15. *《原理》中牛顿的几何版微积分*：例如，试着把牛顿对第 1 卷命题 39 的证明翻译成现代符号。他想求物体在向心力作用下的下落速度，并把力定义为与速度的增量（*I*）除以时间的增量成正比，这是 *dv*/*dt* 的几何／微分版本；但他也以近乎现代的方式求出了 *v*<sup>2</sup> 的导数，实际上写成了 [(*v* + *I*)<sup>2</sup> − *v*<sup>2</sup>]/Δ*y*，从而得到 2*vdv*/*dy*。（他之所以用 *v*<sup>2</sup>，是因为他实际上是在证明一个关于动能即力所做功的定理。）
16. 关于埃米莉·迪沙特莱的牛顿式工作的更多内容，见我的 *Seduced by Logic: Émilie du Châtelet, Mary Somerville and the Newtonian Revolution* (New York: Oxford University Press, 2012)。
## 第 3 章
1. *SI 单位*：Système international d'unités——国际单位制——在国际上缩写为 SI。
2. 关于 *Questiones Mechanicae* 及其影响：David Marshall Miller, "The Parallelogram Rule from Pseudo-Aristotle to Newton," *Archive for History of Exact Sciences* 71 (2017): 157–91，尤见 161–66。按现代标准，《力学问题》只包含一种原始的平行四边形法则，但即便如此，也很少有人领会到它的重要性。
3. *塔尔塔利亚*：他那 45° 的计算假定你是从地面发射，而不是从某一高度发射。*“辱骂性的”著作*：转引自 Michael Brooks, *The Art of More* (Melbourne: Scribe, 2021), 94。在此处以及下一段中，我受惠于 Brooks，也受惠于 J. J. O'Connor 和 E. F. Robertson 在圣安德鲁斯大学 MacTutor 上关于塔尔塔利亚的文章，<https://mathshistory.st-andrews.ac.uk/Biographies/Tartaglia/#:~:text=Quick%20Info&text=Tartaglia%20as%20an%20Italian%20mathematician,published%20in%20Cardan%27s%20Ars%20Magna>。
4. Miller, "Parallelogram Rule," 164。
<span class="origpage" title="英文原版第 353 页">353</span>

5. Joseph Jarrett——在 "Algebra and the Art of War: Marlowe's Military Mathematics in Marlowe's 'Tamburlaine I and II,'" *Cahiers Élizabéthain* 95, no. 1 (2018): 19–39 中——提出，马洛之所以能在小小的舞台上表现宏大的战争场面，是因为他运用了某种紧凑的表示法，类似于哈里奥特所开创的代数符号。Jarrett 也让我注意到了阿尔特多费尔的战争画。
6. 伽利略和哈里奥特对下落运动与水平抛射的理解是正确的，但他们把抛射体的斜向运动当作单一的一种减速运动来处理，而不是用相互独立的分量来处理：Matthias Schemmel, "Thomas Harriot as an English Galileo: The Force of Shared Knowledge in Early Modern Mechanics," in *Thomas Harriot*, vol. 2, *Mathematics, Exploration and Natural Philosophy in Early Modern England*, ed. Robert Fox (Farnham, Surrey: Ashgate, 2012), 89–111，尤见 95, 97。
7. *伽利略、斯蒂文、笛卡尔与平行四边形法则*：Miller, "Parallelogram Rule," 166, 167, 170, 183, 186。
8. *哈里奥特的计算（<a href="#fig-3-3">图 3.3</a>）*：在每幅图中，左侧的实心圆 *a* 和 *A* 表示两个球的起点。它们在中间相撞，并反弹到虚线圆所示的位置。图下方的计算考虑了两个球的速度和质量：哈里奥特考察的是在给定时间间隔 *x* 内发生的事情，因此速度是用两球之间连线的方向和长度来表达的，这与我们今天用向量的做法类似。
哈里奥特仔细地解释了他对平行四边形法则的运用。例如，他说，如果没有发生碰撞，那么在第二个时间间隔 *x* 内，球 *a* 本会以同样的速度沿同一条直线 *ab* 继续运动——可见他已经直觉到了运动第一定律。不过，在发生碰撞时，这一运动被“平移”到了平行线 *fc* 上——他强调，这不是物理上的平移，而是为了“合成表观运动”。第二个球同理，运动 *AB* 被平移到了 *FC*。
点 *f* 和 *F* 是由每个球在碰撞前后的运动合成得到的。例如，对于第一个球，*bf* 等于（我们会称之为）两个向量之和：（负的）小球初始运动的垂直分量 *bd*——也就是它仿佛只是从一个等质量的静止球上弹回时的运动——加上由大球的动量（按我们的说法）所传递的额外运动的垂直分量 *df*(=*gb*)。
用动量守恒和动能守恒来做会更容易，但这些概念在哈里奥特的时代还没有。不过，他的图的对称性表明，他假定了“冲力”的守恒；而图下方的计算——其中他的 $\bar{b},\bar{B}$ 表示两个球的速度，*b, B* 表示它们的质量——本质上与我们的动量守恒计算相同。请注意
<span class="origpage" title="英文原版第 354 页">354</span>

<figure id="fig-0-1" markdown="1">

<img src="../../assets/images/vector/p382.jpg" style="width:80%">

图 0.1　
{: .figcap }

</figure>
是他对 $\left(\bar{b}+\bar{B}\right)\left(b+B\right)/B$ 的记法。（他在这一项上犯了一个小错误。）
*哈里奥特的小错误*（以及对他论文的分析）：Johannes Lohne, "Essays on Thomas Harriot," *Archive for History of Exact Sciences* 20, nos. 3/4 (1979): 189–312，以及 Jon V. Pepper, "Harriot's Manuscript on the Theory of Impacts," *Annals of Science* 33, no. 2 (1976): 131–51, DOI: 10.1080/00033797600200191。
9. *“仿佛”*是哈里奥特的原话，正如在 Miller, "Parallelogram Rule," 158 这样的现代记述中一样。哈里奥特的论文首次发表于 1970 年代：拉丁文原稿的英译见 Lohne, "Essays on Thomas Harriot"。
10. *沃利斯与哈里奥特*：Jacqueline Stedall, "Rob'd of Glories: The Posthumous Misfortunes of Thomas Harriot and His Algebra," *Archive for History of Exact Sciences* 54, no. 6 (2000 年 6 月): 483。*沃利斯与费马*：Miller, "Parallelogram Rule," 171–72, 186–87。
11. 沃利斯试图找到一种思考形如 *x*<sup>2</sup> + 2*bx* + *c*<sup>2</sup> = 0 的二次方程复数解的方法——如果你还记得通过配方推出的求根公式，你就知道 $x=-b\pm\sqrt{\left(b^{2}-c^{2}\right)}$。当 *b* ≥ *c* 时，沃利斯找到了把两个解表示为实数直线上点的办法——于是他试着对 *b* < *c* 时得到的复数解做类似的处理。他通过考察 $x=-b\pm\sqrt{\left(c^{2}-b^{2}\right)}$ 来避免直接处理 *i*；而且他用的是三角形的烦琐作图来表示他的解，而不是像我们今天这样把它们表示为复平面上的点。John Stillwell 在<a href="#fig-13-3">图 13.3</a> 中展示了沃利斯的尝试及其缺陷，见 *Mathematics and Its History* (New York: Springer-Verlag, 1989)。
12. 欧拉对 *e* 的定义的现代版本是 $\lim_{x\to\infty}\left(1+\frac{1}{n}\right)^{n}$。这一思想最早出现在雅各布（或雅克）·伯努利（约翰／让的哥哥）对复利的研究中；更早，虽然是隐含地，出现在约翰·纳皮尔的对数以及哈里奥特未发表的关于连续复利和渐长纬度的计算中。但正是欧拉认识到这个数的威力，并使之得到了应有的关注。他还把它写成泰勒级数，这正是计算 *e* 的十进制近似值的方法，比如你计算器上显示的那个（我的是 2.718281828）。
<span class="origpage" title="英文原版第 355 页">355</span>

13. *论欧拉及其恒等式*：Ed Sandifer, "How Euler Did It," *MAA Online*, 2007 年 8 月。另见 Carl Boyer, *History of Mathematics*, rev. Uta Merzbach (New York: John Wiley and Sons, 1991), 443–44（关于欧拉与大学数学，见 441–42）。*棣莫弗与牛顿*：Orlando Merlino, "A Short History of Complex Numbers," University of Rhode Island, 2006 年 1 月。
14. *欧拉与费马大定理*：后来的数学家发现，费马并没有证明他证明中的某一步，但那一步本身是正确的；这一点，以及欧拉在证明中对复数的使用，在 Harold M. Edwards, "Fermat's Last Theorem," *Scientific American* 239, no. 4 (1978 年 10 月): 104–23 中有很好的解释。
15. *欧拉／达朗贝尔*：Stillwell, *Mathematics and Its History*, 202。*索菲·热尔曼*没有发表她关于费马定理的工作，但勒让德在 *n* = 5 的证明中使用了她的一个结果，并把这一结果归功于她。
16. *哈密顿的苹果与橘子*：Karen Hunger Parshall, "The Development of Abstract Algebra," in *The Princeton Companion to Mathematics*, ed. Timothy Gowers et al. (Princeton, NJ: Princeton University Press, 2010), 95–106，尤见 105。
17. 高斯的话转引自 Christian Gérini, "Argand's Geometric Representation of Imaginary Numbers," University of Toulon, 2009 年 1 月，Helen Tomlinson 英译，2017 年 4 月，在线见 <http://www.bibnum.education.fr/sites/default/files/21-argand-analysis.pdf>。阿尔冈的“有向直线”也见此文。*德摩根的话*转引自 Raymond Flood and Robin Wilson, *The Great Mathematicians* (London: Arcturus, 2011), 143。*关于德摩根的更多背景*：Morris Kline, *Mathematics: The Loss of Certainty* (New York: Oxford University Press 1982), 155–56。
18. 巴贝奇的话转引自 Dirk Struik, *A Concise History of Mathematics* (New York: Dover, 1967), 168。
19. 哈密顿的话转引自 Janet Folina, "Newton and Hamilton: In Defense of Truth in Algebra," *Southern Journal of Philosophy* 50, no. 3 (2012): 515。
20. *哈密顿的历程*，从负数／时间的科学到复数二元组再到四元数，Teun Koetsier 在 "Explanation in the Historiography of Mathematics: The Case of Hamilton's Quaternions," *Studies in History and Philosophy of Science Part A* 26, no. 4 (1995): 593–616 中有详细阐述。*哈密顿作为向量的“步”*：见他的 *Lectures on Quaternions* (Dublin: Hodges and Smith; London: Whittaker; and Cambridge: Macmillan, 1853), 3ff。
*哈密顿之于复数的重要性*：Parshall, "Development of Abstract Algebra," 105；Boyer, *History of Mathematics*, 583。*哈密顿援引牛顿*论时间的代数：Folina, "Newton and Hamilton," 513。
21. *德摩根论哈密顿的二元组*：转引自 Diana Willment, "Complex Numbers from 1600 to 1840"（硕士论文，Middlesex University, 1985）, 102。*哈密顿、符号体系、德摩根*：Koetsier, "Explanation," 610。
<span class="origpage" title="英文原版第 356 页">356</span>

22. *文学界的朋友*，包括华兹华斯，对哈密顿的仰慕：Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 22；以及 Daniel Brown, *The Poetry of Victorian Scientists: Style, Science and Nonsense* (Cambridge: Cambridge University Press, 2013), 1。*玛丽亚·埃奇沃思论哈密顿*："Miss Edgeworth Advises," Royal Irish Academy (RIA)（博客），2018 年 6 月 24 日，<https://www.ria.ie/news/library-library-blog/miss-edgeworth-advises>。
23. *玛丽亚·埃奇沃思、皮科克与萨默维尔*：见我的 *Seduced by Logic: Émilie du Châtelet, Mary Somerville and the Newtonian Revolution* (New York: Oxford University Press, 2012), 195, 197–98。
24. *玛丽亚·埃奇沃思与皇家爱尔兰学院*：RIA（博客），"Miss Edgeworth Advises"，以及 Clare O'Halloran, "'Better without the Ladies': The Royal Irish Academy and the Admission of Women Members," *18<sup>th</sup>–19<sup>th</sup> Century Social Perspectives (History Ireland)* 19, no. 6 (2011 年 11 月／12 月): 42–46。
25. *哈密顿论作为有向直线的向量*：例如他的 *Lectures on Quaternions*, 35。
## 第 4 章
1. *爸爸，你能把三元组相乘吗？* 哈密顿 1865 年写给 Archibald 的信，见 Robert P. Graves, *Life of Sir William Rowan Hamilton*, 3 vols. (Dublin: Hodges, Figgis, 1882, 1885, 1889), 2:434–35，被广泛引用，例如 Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 29。*向“我的孩子们”解释*：1852 年写给德摩根的信，Graves, *Life of Hamilton* (1889), 3: #59, 307–8。
2. *代数／算术的定律*：例如，(3 + 2) + 5 = 5 + 5 = 10；但在这个例子中，括号放在哪里并不重要，因为 3 + (2 + 5) = 3 + 7，同样等于 10。这叫作加法的结合律，乘法也有类似的定律。同样，2 × 3 = 3 × 2，2 + 3 = 3 + 2；这就是著名的乘法与加法的交换律。皮科克还引入了分配律，*a*(*b* + *c*) = *ab* + *bc*。
3. *模律*：对于普通的复数 *z* = *x* + *iy*，哈密顿已经证明，你可以通过对
(*x* + *iy*)(*x* − *iy*) = *x*<sup>2</sup> + *y*<sup>2</sup>,
取平方根来定义这个数的“模”（大小或“绝对值”），其中左端的第二个因子是第一个的“共轭”。（这一点可能早在欧拉时代就已为人所知。）而且还有这样的结论：*两个复数之积的模等于这两个模之积*——哈密顿称之为“模律”，今天的教科书用符号写作 |*zw*| = |*z*||*w*|。
例如，令 *z* = *x* + *iy, w* = *a* + *ib*。那么
$\left|zw\right|=|(x+iy)(a+ib)|=|(xa-yb)+i(xb+ya)|=\sqrt{(xa-yb)^{2}+(xb+ya)^{2}}$
而
<span class="origpage" title="英文原版第 357 页">357</span>

$\left|z\right|\left|w\right|=\sqrt{\left(x^{2}+y^{2}\right)\left(a^{2}+b^{2}\right)}=\sqrt{\left(xa-yb\right)^{2}+\left(xb+ya\right)^{2}}.$
所以 |*zw*| = |*z*||*w*|，模律在二维中成立。
然而，如果你拿 *x* + *iy* + *jz* 和 *a* + *ib* + *jc* 来试，那么要让模律成立，你就必须对 *x, y, a, b* 之间的关系作出简化假设——哈密顿试过，但这会破坏模律的一般性——或者对 *i, j, ij* 和 *ji* 之间的关系作出假设。哈密顿接下来做了什么，见正文的叙述。关于哈密顿的这一历程，包括他写给格雷夫斯的信，见 Teun Koetsier, "Explanation in the Historiography of Mathematics: The Case of Hamilton's Quaternions," *Studies in the History and Philosophy of Science Part A* 26, no. 4 (1995): 593–616。
4. 哈密顿在他的 *Lectures on Quaternions* 序言中解释了这一过程。
5. Augustus De Morgan, *Essays on the Life and Work of Newton*, 由 Philip Jourdain 编辑并加注与附录 (Chicago: Open Court, 1914)。*关于德摩根的生平资料*：Leslie Stephen, *Dictionary of National Biography* 14 (1885–1900), s.v. De Morgan；顺便一提，Stephen 是著名小说家弗吉尼亚·伍尔夫的父亲。另见例如 Carl Boyer, *History of Mathematics*, rev. Uta Merzbach (New York: John Wiley and Sons, 1991), 581。
6. *“极为崇敬”*：Alexander MacFarlane, *Lectures on Ten British Mathematicians* (London: Chapman and Hall, 1916), 第 3 章（出自 1901 年的一次演讲）。
7. 近来的研究追溯了关于哈密顿的流言的演变，把它置于女性角色与社会约束的背景之中，并为他和海伦的生活描绘了一幅更为正面的图景：Anne van Weerden and Stephen Wepster, "A Most Gossiped about Genius: Sir William Rowan Hamilton," *BSHM Bulletin* 33, no. 1 (2018): 2–20。对于早先记载所暗示的情形，他们也给出了更为公允的叙述，例如把一段据说哈密顿酩酊大醉的插曲放回到禁酒运动的语境中去理解。
<span class="origpage" title="英文原版第 358 页">358</span>

8. *德摩根与洛芙莱斯*：Christopher Hollings、Ursula Martin 与 Adrian Rice 的两篇论文："The Early Mathematical Education of Ada Lovelace," *BHSM Bulletin* 32, no. 3 (2017): 221–34，以及 "Lovelace-De Morgan Correspondence: A Critical Re-appraisal," *Historia Mathematica* 44 (2017): 202–31。请注意，巴贝奇的“差分机”超越了它的时代，从未投入生产。
9. 德摩根的话转引自 Janet Folina, "Newton and Hamilton: In Defense of Truth in Algebra," *Southern Journal of Philosophy* 50, no. 3 (2012): 511。请注意，哈密顿与德摩根在代数基础问题上取径不同（511–12）。
10. *哈密顿致德摩根，1841 年*，转引自例如 Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 27。
11. *引入 k = ij*：对于三元组 *a* + *ib* + *jc* 和 *x* + *iy* + *jz*，模律说的是
|(*a* + *ib* + *jc*)(*x* + *iy* + *jz*)| = |*a* + *ib* + *jc*||*x* + *iy* + *jz*|.
右端（RHS）就是
(*a*<sup>2</sup> + *b*<sup>2</sup> + *c*<sup>2</sup>)(*x*<sup>2</sup> + *y*<sup>2</sup> + *z*<sup>2</sup>).
现在看左端（LHS）：假定 *ij* = −*ji*，考虑展开括号后的左端：
|*ax* − *by* − *cz* + *i*(*ay* + *bx*) + *j*(*az* + *cx*) + *ij*(*bz* − *cy*)| = (*ax* − *by* − *cz*)<sup>2</sup> + (*ay* + *bx*)<sup>2</sup> + (*az* + *cx*)<sup>2</sup> + (*bz* − *cy*)<sup>2</sup>.
但你只有把 *ij*(*bz* − *cy*) 的共轭纳入模的定义——*就像 ij 也是和 i、j 一样的复数那样*——才能得到最后这一项，而这一项正是你为了与右端配平所需要的。正是这一点让哈密顿想到，要解决他三元组乘法的问题，就必须引入**第三个**虚向量 *k* = *ij*。
*哈密顿的“电路”*：我稍微改动了 "closed" 一词的时态；参见哈密顿 1865 年写给 Archibald 的信，转引自 Crowe, *History of Vectors*, 29。*哈密顿致格雷夫斯*：转引自 B. L. van der Waerden, "Hamilton's Discovery of Quaternions," *Mathematics Magazine* 49, no. 5 (1976 年 11 月): 227–34，尤见 230。
<span class="origpage" title="英文原版第 359 页">359</span>

12. 德摩根的话转引自 Folina, "Newton and Hamilton," 505。*华兹华斯*论哈密顿平庸的诗才：Daniel Brown, *The Poetry of Victorian Scientists: Style, Science and Nonsense* (Cambridge: Cambridge University Press, 2013), 1–2。*薛定谔*：Crowe, *History of Vector Analysis*, 17。薛定谔指的是今天所说的哈密顿动力学，它是运动定律的一种不依赖坐标的替代形式，与牛顿的方法等价但更为灵活。
13. *玩一玩哈密顿的涂鸦*只有在这样的前提下才成立：假定只能在字符串的首尾消去项，并且假定两两相乘是反交换的。于是，要从 *j*<sup>2</sup> = *ijk* 求出 *j*，就改写为 *j*<sup>2</sup> = −*jik*，然后在两边消去 *j*，得到 *j* = −*ik* = *ki*。
14. *标量积*只是把分量相乘，所以 ***p*** ∙ ***q*** = *p*<sub>1</sub>*q*<sub>1</sub> + *p*<sub>2</sub>*q*<sub>2</sub> + *p*<sub>3</sub>*q*<sub>3</sub> 是一个数，即标量，而不是向量。（在哈密顿完整的四元数乘积中，***p*** ∙ ***q*** 前面有一个负号，这一点会引起争议，我们将在第 7 章看到。）
*向量积*给出的是向量；***p*** × ***q*** 的分量形式最容易记忆和计算，可由行列式 $\left|\begin{matrix} \boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\ p_{1} & p_{2} & p_{3} \\ q_{1} & q_{2} & q_{3} \end{matrix}\right|$ 得出
15. *凯莱与四元数*：Crowe, *History of Vector Analysis*, 35。*凯莱的生平*：Tony Crilly, "Arthur Cayley: The Road Not Taken," *Mathematical Intelligencer* 20, no. 4 (1998): 49–53；Crilly 也为《大英百科全书》撰写了凯莱的条目。
16. 高斯消元法的计算机算法，例如见 Erwin Kreyszig, *Advanced Engineering Mathematics* (New York: Wiley, 1993), 976。
17. *西尔维斯特的“不变量”*：Crilly, "Arthur Cayley: The Road Not Taken," 51。
18. *布尔与凯莱*：Tony Crilly, "The Rise of Cayley's Invariant Theory," *Historia Mathematica* 13 (1986): 241–54。
19. Eunice Foote, "Circumstances Affecting the Heat of the Sun's Rays," *American Journal of Science and Arts* (1856): 382–83。几年后，丁达尔显然独立地为 Foote 的实证发现注入了物理学解释：见 Roland Jackson, "John Tyndall: The Forgotten Cofounder of Climate Science," *The Conversation*, 2020 年 7 月 31 日。傅里叶在 1820 年率先研究了大气的加热效应，但他是在计算地球温度的语境下做的。
20. *搜索引擎*：要推出两个向量 a 与 b 之间夹角所需的标量积形式是 ***a*** ∙ ***b*** = |***a***||***b***|cosθ。我的描述参考了 Amy Langville 出色的入门文章 "The Linear Algebra behind Search Engines: Focus on the Vector Space Model," *Convergence*, Mathematical Association of America（2006 年 12 月）；<https://www.maa.org/press/periodicals/loci/joma/the-linear-algebra-behind-search-engines-focus-on-the-vector-space-model>。
<span class="origpage" title="英文原版第 360 页">360</span>

21. *谷歌 PageRank 算法*：我参考了康奈尔大学一篇内容充实的讲义，<http://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html>。
22. *对人工智能、社交媒体与搜索算法的批评*：参见例如 Cathy O'Neill, *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy* (New York: Crown Publishing, 2017)；Safiyah Umoja Noble, *Algorithms of Oppression* (New York: NYU Press, 2018)；Shoshana Zuboff, *The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power* (London: Profile Books, 2019)；以及其他许多著作。
23. 萨拉·弗莱纳里的算法未能通过安全性检验（参见她的 *In Code* [London: Profile Books, 2001]），但研究者仍然相信，不可交换乘法会被证明是一种有价值的密码学工具。
24. *四元数旋转*：哈密顿在他的 *Lectures on Quaternions*, 269 (art. 282) 中简要勾勒了如下方法：
举一个简单的例子，要把向量 ***p*** 绕 *i* 轴旋转，你可以选取单位四元数 *U* = cos θ + *i* sin θ，这与我<a href="#fig-4-3">图 4.3</a> 中的复数相类比。（这就是四元数 *U* = (cosθ, sin θ, 0, 0)，因为在这种情况下，旋转轴的 *j* 与 *k*（即 *y* 与 *z*）分量为零。）然后，利用欧拉定理，你有 *U* = *e<sup>i</sup>***θ**。这种形式使乘法变得更容易——指数律把乘法变成加法——并且清楚地显示了它们与旋转的关系，正如我们在<a href="#fig-3-8">图 3.8</a> 中也看到的。
现在构造一个新的向量，
***a*** = *U**p**U***<sup>−1</sup>** = *e*<sup>*i***θ**</sup>***p*** *e*<sup>**−***i***θ**</sup> = *e<sup>i</sup>*<sup>θ</sup>(*ix* + *jy* + *kz*)*e***−**<sup>*i***θ**</sup>.
哈密顿想出这个组合想必经过了一番试验，因为当你在阿尔冈平面上时，并不需要再乘一个 *U*<sup>−1</sup>（参见<a href="#fig-4-3">图 4.3</a>、3.8）。（顺便说一句，对于单位四元数，其逆就是复共轭，所以我本可以把 ***a*** = *U**p**U*<sup>*****</sup> 写成 ***a*** = *U**p**U*<sup>−1</sup>。）从几何上说，这个 *U*<sup>−1</sup> 因子是用来抵消一个多余的旋转的——它之所以出现，是因为旋转发生在四维超空间中，但这超出了我这里的讨论范围。在代数上，我们说的是矩阵*相似变换*的四元数类比。不过，你并不需要这些技术细节，就能完成由这套“机械装置”导出的简单代数运算：
如果把 *k* 换成哈密顿的定义 *ij*，你就得到
***a*** = *e<sup>i</sup>*<sup>θ</sup>(*ix* + *jy* + *kz*)*e***−**<sup>*i*</sup><sup>θ</sup> = *e<sup>i</sup>*<sup>θ</sup>(*ix* + (*y* + *iz*)*j*)*e***−**<sup>*i*</sup><sup>θ</sup> = *e<sup>i</sup>*<sup>θ</sup>(*ix*)*e***−**<sup>*i*</sup><sup>θ</sup> + *e<sup>i</sup>*<sup>θ</sup>(*y* + *iz*)*je***−**<sup>*i*</sup><sup>θ</sup>.
接下来是巧妙之处：记住 *e***−**<sup>*i*</sup><sup>θ</sup> = cos θ − *i* sin θ，最后一项中的 *je***−**<sup>*i*</sup><sup>θ</sup> 就变成
<span class="origpage" title="英文原版第 361 页">361</span>

*j*(cos θ − *i* sin θ) = *j* cos θ − *ji* sin θ.
但哈密顿定义了 *ij* = *k* = −*ji*，所以我们有
*j* cos θ − *ji* sin θ = *j* cos θ + *ij* sin θ = (cos θ)*j* + (*i* sin θ)*j* = (cos θ + *i* sin θ)*j* = *e<sup>i</sup>*<sup>θ</sup>*j*.
（我之所以写 *j* cos θ = (cos θ)*j*，是因为 cosθ 只是一个实数或标量；只有当两个数都是复数时，乘法才不一定可交换——如 *ij* = *k* = −*ji* 那样。*j* sin θ = (sin θ)*j* 同理。）
最后，利用指数律和哈密顿关于 *i, j, k* 乘积的规则，我们得到向量 ***p*** 旋转后的版本：
***a*** = *xi* + *e<sup>i</sup>*<sup>2θ</sup>( *y* + *zi*)*j* = *xi* + *e<sup>i</sup>*<sup>2θ</sup>(*yj* + *zk*).
这看起来是对的，因为 ***p*** 是绕 *i* 轴旋转的，所以它的 *i* 分量不变，因为它只在 *j*-*k* 平面内移动。而 *e<sup>i</sup>*<sup>2θ</sup> 这个因子表明，***p*** 的 *j* 和 *k* 分量确实在 *j*-*k* 平面内旋转了 2θ 角。（所以如果你想旋转 θ，就要把单位四元数取为 *U* = *e<sup>i</sup>*<sup>θ/2</sup>。）
*要绕任意轴旋转*——该轴的方向由单位向量 ***u*** = *ai* + *bj* + *ck* 给定，而不像上面的计算那样只绕 *i*——就仿照欧拉公式取 *U* = cos θ + ***u*** sin θ = *e***<sup>*u*</sup><sup>θ</sup>**。（你可以通过比较等式两边表达式的级数来证明欧拉公式。）我上面的叙述是哈密顿的概要以及 John Huerta（Fullerton College）的讲义 "Introducing the Quaternions" 中那个例子的展开版。
***另一种做法***，你可以像我在正文中所展示的那样，用源自四元数乘法的*标量积与向量积*来展开 ***a*** = *U**p**U*<sup>−1</sup>，完成上述计算：
*PQ* = *wa* − ***p*** ∙ ***q*** + *w**q*** + *a**p*** + ***p*** × ***q***.
25. 关于矩阵导致万向锁的一个例子，见 Justin Wyss-Gallifent 的 MATH431 课程 "Gimbal Lock"，2021 年 11 月 3 日：<http://www.math.umd.edu/~immortal/MATH431/book/ch_gimballock.pdf>。
<span class="origpage" title="英文原版第 362 页">362</span>

26. *谱线*：如果原子吸收能量，它的电子就会跃迁到更高的能态；当它们回到原来更稳定的状态时，原子会发射一个光子，表现为一条有颜色的谱线。颜色对应于所发射光的波长，而波长又与跃迁的能阶大小和原子的构成有关。这就是为什么先驱女天文学家安妮·詹普·坎农自 1896 年起一直在哈佛学院天文台工作，不辞辛劳地分类恒星的光谱以确定其化学成分。她一直做到 1941 年，也就是她去世的那一年。
27. 实际上，与斯特恩-格拉赫实验的联系是稍后才建立起来的。总之，乌伦贝克与古德斯米特给出的数值是 ±*h*/4π；符号取决于自旋轴是与磁场方向一致还是相反，而其大小是“归一化”普朗克常数 *h*/2π（记作 *ħ*，读作“h 拔”）的**一半**。这就是今天说电子自旋为 ½ 的原因。
28. *埃伦费斯特、洛伦兹*：古德斯米特在 1971 年 4 月为荷兰物理学会金禧纪念宣读的一篇饶有趣味的论文中讲述了电子自旋的发现过程；<https://www.lorentz.leidenuniv.nl/history/spin/goudsmit.html>。
29. *泡利矩阵与四元数*：泡利矩阵与四元数之间的关系还表明，你可以拥有一个由（实际上是矩阵的）向量构成的“向量空间”。要紧的是向量的规则：如果某个东西表现得像向量，那就可以把它当作向量来对待。*泡利论四元数*：W. Pauli, *General Principles of Quantum Mechanics*, Springer-Verlag, Berlin/Heidelberg, 115；他指出，*i* 乘以该矩阵后遵循单位四元数的乘法规则。*狄拉克*：P. A. M. Dirac, "The Quantum Theory of the Electron," *Proceedings of the Royal Society of London*, series A, 117, 778 (1928 年 2 月 1 日): 610–24；以及 Paul A. M. Dirac, "Theory of Electrons and Positrons," 1933 年诺贝尔奖演讲，<https://www.nobelprize.org/uploads/2018/06/dirac-lecture.pdf>。
30. *四元数与自旋旋转*：狄拉克的新理论表明，物质的所有构件——电子、质子和中子——都含有 ½ 的自旋；也就是说，它们是 ½ 的奇数倍，这类粒子被称为费米子。（光子及其他所谓的玻色子则具有整数自旋。）
正是粒子自旋中的 ½ 造成了那种奇特的行为：你需要**两次** 360° 旋转，才能把一个费米子带回原来的状态。这一发现来自旋转量子粒子自旋轴所需的数学——碰巧与四元数旋转的数学相似。考虑到两者给出的是同一类反直觉的旋转，这其实并不奇怪。我在这里做一个简要概述：
正如我在<a href="#fig-4-4">图 4.4</a> 和关于四元数旋转的尾注中所暗示的，要把一个向量绕 *x* 轴旋转 θ 角，单位四元数是 $U=e^{i\frac{\theta}{2}}$。类似地，要把一个自旋为二分之一的角动量向量绕 *x* 轴旋转 θ，你需要一个酉算子 $U=e^{-i\frac{\theta}{2}\sigma x}$，其中单位的选择使得 2π/*h* = 1，σ<sup>*x*</sup> 是泡利自旋矩阵。*请注意两种情形中都有* θ*/2——这就是为什么你需要两次完整的 2π 旋转，才能回到最初未旋转（θ = 0 + 2*n*π）的状态。
相比之下，要把轨道角动量（而非自旋角动量）绕 *x* 轴旋转 θ 角，酉算子是 *U* = *e***–**<sup>*i*</sup><sup>θ</sup> <sup>*Jx*</sup>。旋转 2π，你就**回到**了出发点。还要注意，在四元数旋转和量子旋转中，你都还需要右乘逆或共轭；这叫作“相似变换”。
描述四元数与自旋之间联系的另一种说法是：四元数旋转矩阵与自旋二分之一的旋转矩阵都是群 *SU*(2) 的元素。*群论*处理的是底层结构，因此通过研究各种数学或物理结构的群性质，你有时能发现两件表面上截然不同的事物之间的相似之处。
<span class="origpage" title="英文原版第 363 页">363</span>

31. 克莱因和奥帕特用的是中子而不是电子，因为电子上的电荷会与外部磁场产生过强的干扰。他们用一块铁磁晶体把一束中子（以物质波的形式行进）衍射成两部分，其中一部分与外部磁场发生相互作用。（在量子力学中，“物质波”或“波函数”描述的是在某一时刻、某一地点探测到粒子的概率。）他们的发现是：当其中一束——波的一个部分——被旋转了 360° 或 2π 弧度的奇数倍时（当然，2π 本身也包括在内），它会与另一束未经旋转的部分发生**相消**干涉，产生一种独特的干涉图样。而对于 2π 的偶数倍，这种相消干涉就消失了。所以，在 2π 的奇数倍情形下，你需要再旋转一次自旋，使它总共经过诸如 4π 这样的偶数倍，干涉图样才会恢复正常。A. G. Klein and G. I. Opat, "Observation of 2π Rotations by Fresnel Diffraction of Neutrons," *Physical Review Letters* 37, no. 5 (1976 年 8 月 2 日): 238–40。
32. 另外两个团队由赫尔穆特·劳赫（Helmut Rauch）和萨姆·维尔纳（Sam Werner）领衔，但三支队伍非但没有相互竞争，反而在随后展开了合作，正如克莱因在 "Neutron Interferometry: A Tale of Three Continents" 中所描述的，该文见 <http://www.europhysicsnews.org> 或 <http://dx.doi.org/10.1051/epn/2009802>。
33. 哈密顿的《颂歌》由 Brown 分析，见 *Poetry of Victorian Scientists*, 7–9。
<span class="origpage" title="英文原版第 364 页">364</span>

34. *今日的八元数*：关于当前研究的技术性综述，见 Peter Rowlands and Sydney Rowlands, "Are Octonions Necessary to the Standard Model?," *Journal of Physics: Conference Series* 1251, 012044 (2019), DOI 10.1088/1742-6596/1251/1/012044。这些研究者中有一位是年轻的加拿大女性科尔·富里（Cohl Furey）；另一位是加州大学的数学家约翰·贝兹（John Baez）。2021 年，贝兹在 <https://math.ucr.edu/home/baez/standard/> 上给出了这一领域的最新进展。
## 第 5 章
1. Robert P. Graves, *The Life of Sir William Rowan Hamilton*, 3 vols. (Dublin: Hodges, Figgis, 1882, 1885, 1889), 2:585–86。
2. Graves, *Life of Hamilton*, 2:586。
3. 关于格拉斯曼早年的生活与工作，以及下面大部分内容，我主要受惠于 Michael J. Crowe, *History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 第 3 章（更多细节见 Hans-Joachim Petsche, *Hermann Grassmann* [Basel: Birkhäuser, 2009]）；关于向量的发现历程（包括哈密顿与格拉斯曼）的综述，见 Jean-Luc Dorier, "A General Outline of the Genesis of Vector Space Theory," *Historia Mathematica* 22 (1995): 227–61。
4. *格拉斯曼“惊愕不已”*：1847 年写给 Saint-Venant 的信，转引自 Crowe, *History of Vector Analysis*, 56。
5. Crowe, *History of Vector Analysis*, 70–72。
6. 那些狂热的新当权者曾在意大利出生的拉格朗日身上犹豫过——外国人通常会被剥夺职位和财产——但最终一项特别法令让他留了下来，而且还当上了委员会主席。这在很大程度上要归功于先驱化学家安托万·拉瓦锡为外国科学家所做的努力——他和妻子玛丽被誉为现代化学的“父与母”。拉瓦锡因在一家包税公司中的商业利益而悲剧性地死在断头台上，拉格朗日那句名言说：暴民砍下他的头不过是一瞬间的事，而再出现一个这样的人也许要一个世纪。十八个月后，政府宣布拉瓦锡在包税公司一事上无任何不法行为。
7. 有些资料说有两个孩子活了下来：无论哪种说法，都是何等的悲惨——尤其是对他可怜的母亲而言！难怪拉格朗日本人也没有孩子。
<span class="origpage" title="英文原版第 365 页">365</span>

8. 如果你用*向量积*去乘代表一个平行四边形两条有向直线的向量，你会得到另一个向量。（这使得向量积是“封闭”的。）积向量垂直于原来两个向量所在的平面。但如果你用*格拉斯曼的外积*去乘这个平行四边形的两条边，你得到的不是另一条“直线”——格拉斯曼并没有用“向量”这个术语——而是一个有向的**面积**。所以外积在概念上不同于向量积。（不过它与张量积有关，我们后面会看到。）然而二者是等价的：由两条边的向量积得到的向量，与格拉斯曼的有向面积方向相同、大小相等。
9. *哈密顿的信*写给 Mortimer O'Sullivan，发表于 Graves, *Life of Hamilton*, 2:683。
10. *赫歇尔致哈密顿*，转引自 Graves, *Life of Hamilton*, 3:121。
11. 莫比乌斯、阿佩尔特、巴尔策，转引自 Crowe, *History of Vector Analysis*, 78–80。
12. 莫比乌斯、阿佩尔特、巴尔策，转引自 Crowe, *History of Vector Analysis*, 78–80。
13. 莫比乌斯、阿佩尔特、巴尔策，转引自 Crowe, *History of Vector Analysis*, 78–80。
14. *安培对格拉斯曼*：若要看当时人所作、判断公允的评述，见麦克斯韦的 *Treatise on Electricity and Magnetism*, 1891（1873 年原版的第 3 版，Clarendon Press 或 Dover 重印本）, arts. 482, 509–10（麦克斯韦自己的分析见 511–25）, 526（麦克斯韦偏爱安培，因为格拉斯曼的公式违反了牛顿第三定律），但见 687：麦克斯韦的结论是，不可能通过**实验**在这两个公式之间作出判定。
*近来从实验与概念上作出判定的尝试*：Christine Blondel and Bertrand Wolff, trans. Andrew Butricia, "Ampère's Force Law: An Obsolete Formula?" *Histoire de l'Électricité et du Magnetisme*（2009 年 5 月；英译 2013 年，2021 年修订）, <http://www.ampere.cnrs.fr/histoire/parcours-historique/lois-courants/force-obsolete/eng>。
这篇论文对近期研究给出了简短而不偏不倚的综述。一份详尽、最终倾向于安培的论述：A. K. T. Assis and J. P. M. C. Chaib, *Ampère's Electrodynamics* (Apeiron, 2015), 第 14 章、16.4 节及结论，491；不过，1996 年 Assis 曾（与 Marcelo A. Bueno 一起）证明，在安培所主张的实验设置下，格拉斯曼公式与安培公式是等价的："Equivalence between Ampère and Grassmann's Forces," *IEEE Transactions on Magnetics* 32, no. 2 (1996 年 3 月): 431–36。
请注意，一些现代作者正利用安培对格拉斯曼之争来质疑场论进路（麦克斯韦之后，格拉斯曼的结果被整合进了场论）；参见安培的超距作用。麦克斯韦本人说过，看待事物多一种方式总是好的！
*格拉斯曼的原始论文*：Hermann Grassmann, "Neue Theorie der Elektrodynamik," *Annalen der Physik und Chemie* 1 (1845): 1–18。
<span class="origpage" title="英文原版第 366 页">366</span>

15. *莱布尼茨与格拉斯曼*：Joseph Kouneiher, "Broken Symmetry, Pointless Space and Leibniz's Legacy: The Origin of Physics," *Advanced Studies in Theoretical Physics*（2015 年 9 月），取自 ResearchGate, <https://www.researchgate.net/publication/281526332_Broken_symmetry_Pointless_Space_and_Leibniz%27s_Legacy_the_origin_of_physics>。
16. Graves, *Life of Hamilton*, 3:424。
17. Graves, *Life of Hamilton*, 3:441–42。
18. William Rowan Hamilton, *Lectures on Quaternions* (London: Whittaker, and Cambridge: Macmillan, 1853), 例如第 59 页，关于乘以 *j* 与改变望远镜的朝向。
19. Crowe 令人信服地论证了：向量分析的历史编纂学是从哈密顿及其后继者、而非格拉斯曼这一脉展开的（*History of Vector Analysis*, 77，第 4 章）。很久以后，正如我们将看到的，格拉斯曼会影响嘉当、克利福德**及其**追随者。
## 第 6 章
1. 关于麦克斯韦生平与工作的通俗叙述，见我的 *Einstein's Heroes: Imagining the World through the Language of Mathematics* (St. Lucia: University of Queensland Press, 2003; New York: Oxford University Press, 2005)。
2. *泰特那封激动的信*：Cargill Gilston Knott, *The Life and Scientific Work of P. G. Tait* (London: Cambridge University Press, 1911), 9。*关于荣誉学位考试*：八天十六场考试的数字出自 1854 年（麦克斯韦那一年）：D. O. Forfar, "What Became of the Senior Wranglers?" *Mathematical Spectrum* 29, no. 1 (1996)；可查 www.clerkmaxwellfoundation.org。
3. *麦克斯韦在剑桥*：Lewis Campbell and William Garnett, *The Life of James Clerk Maxwell* (London: Macmillan, 1882), 94–95。（有 1997 年 Sonnet Software 出的数字版。）
4. 这首诗——全名是 "A Vision of a Wrangler, of a University, of Pedantry, and of Philosophy"——发表于 Campbell and Garnett, *Life of Maxwell*, 307。
5. *麦克斯韦任考官*：Campbell and Garnett, *Life of Maxwell*, 175。
6. *泰特论麦克斯韦*：讣告，*Proceedings of the Royal Society of Edinburgh* 10 (1878–80): 331–39。*他父亲写给麦克斯韦的信*：Campbell and Garnett, *Life of Maxwell*, 109。*他的老教师*：David O. Forfar and Chris Pritchard, "The Remarkable Story of Maxwell and Tait," *James Clerk Maxwell Commemorative Booklet* (Edinburgh, 1999), 3。
<span class="origpage" title="英文原版第 367 页">367</span>

7. *论斯托克斯定理*：麦克斯韦在他的 *A Treatise on Electricity and Magnetism* (Oxford: Clarendon Press, 1873), 1:27 中把证明归功于汤姆森和泰特（并提到它最早出现在史密斯奖考试中）。汤姆森很可能是该定理的提出者，因为他在 1850 年写给斯托克斯的信中就已包含它。Victor J. Katz（"The History of Stokes' Theorem," *Mathematics Magazine* [MAA] 52, no. 3 [1979 年 5 月]: 146–56）认为 Hermann Hankel 给出了第一个发表的证明（1861 年），但它不如汤姆森的（1867 年）那样具有一般性。
8. *作为面积分的圆的面积*：设想该圆所围曲面上的一个微小面元 *dS*，思路是对整个曲面积分 *dS* 以求面积。这里 *x* 轴和 *y* 轴表示定义该曲面的两个维度，所以你可以想象每个方向上的小线段 *dx* 和 *dy*，它们围出曲面的一个矩形面积元——因此在面积分中，你是对 *dS* = *dxdy* 积分。（因为这个曲面是平面，这其实只是二重积分而非面积分；在面积分中 *dS* 比 *dxdy* 复杂，因为需要用向量来求曲面的法线。）把它变换到极坐标（如<a href="#fig-2-2">图 2.2</a>a），并且别忘了坐标变换的雅可比因子，你就得到 *dS* = *dx dy* = *rdr d*θ。沿半径为 *R* 的圆积分：
$\text{Area}=\int _{0}^{2\pi}\int _{0}^{R}rdrd\theta=\int _{0}^{2x}\frac{1}{2}R^{2}d\theta=\pi R^{2}$.
如果你不熟悉雅可比行列式，就极坐标而言，可以设想一个角度为 *d*θ、半径为 *r* 的微小扇形：扇形的弧长 *s* 是 *rd*θ（因为按弧度的定义，$\frac{s}{2\pi r}=\frac{d\theta}{2\pi}$），而径向元素长为 *dr*，所以面积元就是 *rdr d*θ。
9. 这片园地连同格伦莱尔宅邸及附属建筑的修复得以保存，主要归功于庄园现任主人邓肯·弗格森（Duncan Ferguson）上尉的努力。我有幸在格伦莱尔见到了邓肯，你可以在 <http://www.glenlair.org.uk> 上看到他和格伦莱尔信托为麦克斯韦与格伦莱尔所做的更多工作。
10. *麦克斯韦在英国科学促进会会议上*，由 William Swan 回忆，见 Campbell and Garnett, *Life of Maxwell*, 236。
11. *静止的引力？*当然，太阳和行星都在运动，但在轨道上任意给定的一点，它们彼此相对静止，并且相距一个给定的距离。牛顿定律只处理由这一距离和两个质量所产生的力。*库仑定律*：麦克斯韦在他的 *Treatise on Electricity and Magnetism*, 1:34, 75 中描述了确立平方反比定律的更精确的实验。
<span class="origpage" title="英文原版第 368 页">368</span>

12. *拉格朗日势的（简化版）数学*：功 = 力 × 距离，所以如果移动的距离是在竖直方向（比如说 *y*），那么 *W* = *f* × *y*。如果力保持不变，这个公式没问题；但对于随距离变化的力，比如引力，你就需要用积分学来把力与增量距离的乘积在物体移动的*每一点上*“累加”起来。
牛顿曾用几何微积分把它定义为力曲线下的面积，但用莱布尼茨的记号则是 $W=\int _{a}^{b}fdy$，得到 *F*(*b*) − *F*(*a*)，其中 *F* 是 *f* 的反导数。（实际上，这只对“保守”力成立，包括引力，它们只依赖于积分的端点；对于摩擦力等其他力，你需要*线积分*，以考虑起点 *a* 与终点 *b* 之间整条路径的特性。）
拉格朗日实际上所证明的是 $f=\frac{dF}{dy}$。这正是微积分入门课上所教的微积分基本定理，但拉格朗日把它推广到了三维，使力和移动的距离可以沿任意方向，而不只是上下——于是他发现力具有分量 $\frac{\partial F}{\partial x},\frac{\partial F}{\partial y},\frac{\partial F}{\partial z}$。（“弯尾巴的 d”这个记号在当时还不是标准的，但我用它，以免让现代数学读者感到困惑。）他沿袭牛顿，把力设想为一个向量性的量，但和哈密顿与格拉斯曼之前的所有人一样，他只处理分量，而不处理整体向量。
借助功与势能之间的关系，*F* 被称为与力 *f* 相关联的“势”。一般来说，力用大写 *F* 表示，所以势常用的符号是 *V*。（乔治·格林在 1828 年最先使用了“势”这个术语。）
13. *偏导数*：在 $\frac{\partial F}{\partial x}$ 这一项中，*F* 只对 *x* 求导，所以这一项告诉我们当 *y* 和 *z* 保持不变时 *F* 如何沿 *x* 方向变化——另外两项同理。
14. *“电学中的牛顿”*：麦克斯韦，*Treatise on Electricity and Magnetism*, 2:175。
15. 这类只依赖于端点、而不依赖于两端之间路径性质的力，被称为“保守”力，因为它们导致能量守恒。例如，对于牛顿引力，运动是径向的，所以平方反比定律可以写成 $m\ddot{r}=-\frac{GmM}{r^{2}};$，写出 $\ddot{r}=\dot{r}d\dot{r}/dr$，积分即可求出该力把物体从点 1 移动到点 2 所做的功：
$m\int _{\dot{r}_{1}}^{\dot{r}_{2}}\dot{r}d\dot{r}=-GMm\int _{r_{1}}^{r_{2}}\frac{1}{r^{2}}dr\Rightarrow\frac{1}{2}m\dot{r}^{2}-\frac{GMm}{r}=\text{constant},$
这意味着动能与势能之和守恒；该常数由定积分的端点确定。
<span class="origpage" title="英文原版第 369 页">369</span>

16. 麦克斯韦，*Lecture on Faraday's Lines of Force*，他于 1873 年发表的一次演讲，见他的文集 *The Scientific Letters and Papers of James Clerk Maxwell*, ed. P. M. Harman, 2 vols. (Cambridge: Cambridge University Press, 1990, 1995), 803。
17. *汤姆森与法拉第论场*：Ernan McMullin, "The Origins of the Field Concept in Physics," *Physics in Perspective* 4 (2002): 13–39（尤见 14）。这篇论文详细概述了场的概念及其演化，直至麦克斯韦给出第一个成熟的场论。
18. *马歇尔学院的教授职位*：Forfar 与 Pritchard（"Remarkable Story," 3–4）指出，学院的记录已不存在，但据信泰特是麦克斯韦所得那个职位的候选人之一——后来阿伯丁大学的 John S. Reid 在 "James Clerk Maxwell's Scottish Chair," *Philosophical Transactions of the Royal Society A* (2008), 366, 1661–84, DOI:10.1098/rsta.2007.2177 中确认泰特确为候选人。倘若如此，正如 Forfar 与 Pritchard 所指出的，麦克斯韦与泰特的通信表明二人之间并无芥蒂——无论是在 1856 年，还是在 1860 年（那一年泰特在爱丁堡的职位竞争中胜过了麦克斯韦）。*凯莱的申请*：Crilly, "Arthur Cayley: The Road Not Taken," 52。
19. *麦克斯韦解释自己的语言选择*：他在 1865 年的论文开头有所暗示（J. Clerk Maxwell, "A Dynamical Theory of the Electromagnetic Field," *Philosophical Transactions of the Royal Society London* 155 [1865]: 459–512），并在他的 *Treatise on Electricity and Magnetism*, 1:98–99 (art. 95) 以及第 2 卷（第 3 版）176–77 (art. 529) 中作了充分解释。他说，普通积分以及在有限空间上的线积分与面积分适合超距作用的进路，而偏微分方程以及遍及整个空间的（体积）积分则是场的自然语言。
20. *麦克斯韦对电流的定义及其与通量的关系*：他列出了两类电流：一类是导体（比如一圈导线）中的常规电流——电流就是电流密度的通量；另一类是电容器中的有效电流，他称之为“位移电流”，它与电容器极板间电通量的变化成正比。
21. *把麦克斯韦场方程中的积分化为导数*：“积分学第一基本定理”把积分与导数联系起来：
$\int _{a}^{b}f\left(x\right)dx=F\left(b\right)-F\left(a\right)$，其中 *F* (*x*) 是 *f* (*x*) 的反导数。
换句话说，$f\left(x\right)=\frac{dF\left(x\right)}{dx}$，前提是相关函数可积／可微！这意味着你可以通过积分从 *f*(*x*) 走到 *F*(*x*)，或通过微分从 *F*(*x*) 走到 *f*(*x*)。*斯托克斯定理*就是这一思想的推广：你可以从（单重）线积分走到（二重）面积分，反之亦然。类似地，你也可以通过如今（在向量之后）称为“散度定理”的东西，从面积分走到体积（三重）积分并再走回来。例如，麦克斯韦就是这样推出静电与静磁的高斯定律的微分形式的（见他的 *Treatise on Electricity and Magnetism*, 1:68, 79, 98–99）：
实验上已知，给定体积内所含的电荷量 *e* 可以写成电荷密度 ρ 的体积积分：
<span class="origpage" title="英文原版第 370 页">370</span>

*e* = ∫∫∫ρ *dx dy dz* ……我把这个方程称为 (1)。
同样已知（由库仑定律）单位试探电荷对电荷 *e* 施加的力 *R* 是 *R* = *e*/*r*<sup>2</sup>，而穿过闭合曲面的电通量为
∫∫ *R* cos ε *dS* = 4π*e*, … (2)
其中 ε 是力的方向角。麦克斯韦借用法拉第的说法，把 *R*cos ε*dS* 称为穿过曲面的“感应”。麦克斯韦把 *R* 的分量标记为 *X, Y, Z*，并把它们与下述定理联系起来（现在称为散度定理，但当时它没有名字，而且只以这里所示的分量形式为人们所知）：
$\iint R\cos\epsilon dS=\iiint\left(\frac{dX}{dx}+\frac{dY}{dy}+\frac{dZ}{dz}\right)dxdydz$ … (3)
于是麦克斯韦把 (1) 乘以 4π，并令其与 (2) 相等，得到
∫∫ *R* cos ε *dS* = 4π ∫∫∫ ρ *dx dy dz*.... (4)
最后，令 (3) 与 (4) 相等，并把 (3) 中的闭合曲面取作 (4) 中体积的一个体元，得到：
$\frac{dX}{dx}+\frac{dY}{dy}+\frac{dZ}{dz}=4\pi\rho$...(5)
如果你已经熟悉向量微积分，你会认出左端就是 *R* 的*散度*，不过我们要等到正文中泰特和麦克斯韦（以及亥维赛）把它写成向量形式时再讲。
同时，正如麦克斯韦接着解释的，如果你能把电力写成势 *V* 的形式，那么 (5) 就变成泊松对拉普拉斯方程的推广。式 (5) 的向量形式，就是库仑定律在今天麦克斯韦方程组中的样子。静磁的结果可类似地推出。
我在这里展示的麦克斯韦的推导，清楚地揭示了通量／面积分与散度之间的联系——它类似于麦克斯韦用斯托克斯定理把安培定律和法拉第定律表达为微分方程的方式（见 *Treatise on Electricity and Magnetism*, 2:29, 45, 147–48, 233, 251, 255）。其中涉及另一个向量微积分运算，不是散度而是*旋度*；这两个向量运算我们在下一章都会遇到。
<span class="origpage" title="英文原版第 371 页">371</span>

22. *爱因斯坦的引文*出自 Albert Einstein, *Ideas and Opinions* (1954; New York: Three Rivers Press, 1982), 327。*麦克斯韦的“重炮”*出自写给 Charles Cay 的信，重印于 Campbell and Garnett, *Life of Maxwell*, 169。
23. 这是因为一般的波动方程是微分方程；但要导出电磁波方程，你还需要麦克斯韦对安培定律所作的理论改动，也就是加上“位移电流”。
24. 引文出自 Anne van Weerden, *A Victorian Marriage: Sir William Rowan Hamilton* (Stedum, Netherlands: J. Fransje van Weerden, 2017), 10, 56, 326。
25. Van Weerden, *A Victorian Marriage*, 326。
26. *论爱丁堡的职位（以及巴里）*：Forfar and Pritchard, "Remarkable Story." *巴里的引文*：Raymond Flood, "Thomson and Tait: The Treatise on Natural Philosophy," in Raymond Flood, Mark McCartney, and Andrew Whitaker, *Kelvin: Life, Labours and Legacy*, Oxford Scholarship Online（2008 年 5 月）: DOI: 10.1093/acprof:oso/9780199231256.001.0001。*吉尔论麦克斯韦的教学*：Reid, "Maxwell's Scottish Chair," 1673。
## 第 7 章
1. *泰特致汤姆森*：见 R. Flood, "Thomson and Tait: The Treatise on Natural Philosophy," in Raymond Flood, Mark McCartney, and Andrew Whitaker, *Kelvin: Life, Labours and Legacy* (Oxford: Oxford University Press, 2008) 与 Scholarship Online (2021), 176. DOI: 10.1093/acprof:oso/9780199231 256.003.0011。
2. *泰特的书房与清单*：Cargill Gilston Knott, *The Life and Scientific Work of P. G. Tait* (London: Cambridge University Press, 1911), 33, 43。
<span class="origpage" title="英文原版第 372 页">372</span>

3. *论麦克斯韦绰号的由来*：该方程出现在泰特 *Sketch of Thermodynamics* (Edinburgh: Edmonston and Douglas, 1868) 的第 162 节。另见 M. J. Klein, "Maxwell, His Demon, and the Second Law of Thermodynamics," in *Maxwell's Demon: Entropy, Information, Computing*, ed. Harvey Leff and Andrew Rex (Princeton, NJ: Princeton University Press, 1990), 85–86。Klein 的文章写于 1970 年；麦克斯韦的“妖”是一个有助于澄清热力学本质的思想实验。
4. *麦克斯韦的评论*：*Scientific Papers of James Clerk Maxwell*, ed. W. D. Niven (Cambridge: Cambridge University Press, 1890), 326–27。*麦克斯韦致泰特*，1871 年 12 月 21 日，Knott, *Life of Tait*, 150。
5. *麦克斯韦致泰特*（着重标记为我所加），1870 年 11 月 14 日，见 Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 132；麦克斯韦致坎贝尔，1872 年 10 月 19 日，见 Lewis Campbell and William Garnett, *The Life of James Clerk Maxwell* (London: Macmillan, 1882), 186。麦克斯韦的“分类”论文发表于 *Proceedings of the London Mathematical Society*（1871 年 3 月 9 日）: 224–33。
6. *麦克斯韦致泰特*谈向量微积分的命名：1870 年 11 月 7 日，转引自 Knott, *Life of Tait*, 167。
7. 麦克斯韦在他的 *Treatise on Electricity and Magnetism* (Oxford: Clarendon Press, 1873), 1:28 (art. 25) 中定义了“收敛”，即散度的负值。正文中那些整体向量方程见麦克斯韦的 *Treatise*，第 2 卷（第 3 版），252, 259。抛开负号不看，当你查看他的分量版本（第 77 条，或我的<a href="#fig-7-1">图 7.1</a>，以及第 612 条）时，你会发现他的版本与我们的相同。麦克斯韦在他对 𝔇 的定义中还有一个额外的比例常数 *K*，但他指出对空气而言 *K* = 1。所以，为了让向量的思想始终居于前台，我在书写他的方程时一般假定单位的选择使得各种电学和磁学常数等于 1。（有些现代教材也把散度 ***E*** 方程中的 4π 约掉了。）𝔇 是电位移；正文中给出的麦克斯韦定义是针对各向同性物质的。请注意，他在第 2 卷的整体向量方程中使用的是 *e* 而不是 ρ，而他在第 1 卷第 77 条中用的是 ρ，今天也用 ρ——所以我在正文中使用了 ρ。
8. *麦克斯韦致泰特*（着重标记为我所加），1871 年 11 月 2 日，见 Crowe, *History of Vectors*, 133。
9. 电磁学与广义相对论中的类似方程包括比安基恒等式，我们在第 13 章会简要遇到。在电磁学中，这些恒等式包括反映不存在磁单极子的散度 ***B*** 方程。托尼和我还没有把我们的部分结果写成论文，但早期的一篇是 R. Arianrhod, A. W.-C. Lun, C. B. G. McIntosh, and Z. Perjés, "Magnetic Curvatures," *Classical and Quantum Gravity* 11 (1994): 2331–34。
<span class="origpage" title="英文原版第 373 页">373</span>

10. 麦克斯韦在他的 *Treatise*, 2:248 (art. 604) 中以分量形式写下了（我们今天所称的）散度 ***B*** 方程，并指出它由第 591 条的方程 (A)（第 233 页）推出。Bruce Hunt（*The Maxwellians* [Ithaca, NY: Cornell University Press, 1991], 245）提到了分量形式（Hunt 把它标为 A′），但说麦克斯韦把它写作 *S*. ∇𝔅 = 0。这当然就是第 248 页那个分量方程在哈密顿记号下的等价形式，尽管我在我所藏的《电磁通论》第三版中找不到它。
11. *向量势*：麦克斯韦，*Treatise*, 第 2 卷，第 405、422–23、592 条：他定义向量势 ***A***，使得 ***A*** 的线积分（通过斯托克斯定理）等于磁场 ***B*** 的面积分（***B*** 是向量势 ***A*** 的旋度）。他还给出了它的物理解释，用磁矩（第 405 条）和电磁动量（第 590、592、618 条）来说明——不过这是通过数学类比，而非直接的物理对应；例如，他之所以选用“电磁动量”这个术语，是因为在数学上它是力对时间的积分（第 590 条）——也就是说，它对时间的导数是一个力，就像普通的牛顿动量一样。
12. *整体向量方程*：*Treatise on Electricity and Magnetism*, 第 2 卷（第 3 版），258（分量形式见 233, 248）。*势*：现代记号不一，但 ***A*** 用得相当普遍，例如 Luciano Maiani and Omar Benhar, *Relativistic Quantum Mechanics* (Boca Raton, FL: CRC Press, 2016), 56；Ray D'Inverno, *Introducing Einstein's Relativity* (Oxford: Clarendon Press, 1992), 160；Walter Strauss, *Partial Differential Equations* (New York: Wiley, 1992), 342；Bernard Schutz, *A First Course in General Relativity* (Cambridge: Cambridge University Press, 1985), 211。
13. *麦克斯韦致坎贝尔*：Campbell and Garnett, *Life of Maxwell*, 186。
14. *麦克斯韦的瓦特讲座*：*The Scientific Letters and Papers of James Clerk Maxwell*, ed. P. M. Harman, 2 vols. (Cambridge: Cambridge University Press, 1990, 1995), 791。
15. 泰特的书 *Introduction to Quaternions* 是与他昔日的老师 Philip Kelland 合著的。*麦克斯韦的评论*（着重标记为我所加）：*Nature* 9 (1873): 137–38；Crowe, *History of Vectors*, 133。*牛顿*：写给哈雷的信，见例如 Nicolae Sfetcu, "Isaac Newton vs Robert Hooke on the Law of Universal Gravitation," SetThings (2019 年 1 月 14 日), MultiMedia Publishing, DOI:10.13140/RG.2.2.19370.26567, Creative Commons。
16. *麦克斯韦、泰特与巴尔福*：Knott, *Life of Tait*, 149–50。*柯瓦列夫斯卡娅*：Sophie Kowalevski, "Sur le problème de la rotation d'un corps solide autour d'un point fixe," *Acta Mathematica* 12 (1889 年 1 月): 177–232。它于 1888 年赢得博尔丹奖。
17. *麦克斯韦的“物理推理”*：*Treatise on Electricity and Magnetism* 1:9 (art. 11)。
<span class="origpage" title="英文原版第 374 页">374</span>

18. *汤姆森致 R. B. Hayward*，1892 年，见 Crowe, *History of Vectors*, 120。
19. *凯莱的肖像／麦克斯韦的诗*：Alexander MacFarlane, *Lectures on Ten British Mathematicians* (1916), 第 5 章。*克利福德单杠上的身手*：Carl Boyer, *A History of Mathematics*, rev. Uta Merzbach (New York: John Wiley and Sons, 1991), 592；另见 Monty Chisholm, "Science and Literature Linked: The Story of William and Lucy Clifford," *Advances in Applied Clifford Algebras* 19 (2009): 657–71。
20. *克利福德的无神论*：Sally Shuttleworth, "Science and Periodicals: Animal Instinct and Whispering Machines," in Juliet John, ed., *The Oxford Handbook of Victorian Literary Culture* (2016), DOI: 10.1093./oxfordhb/9780199593736.013.31。
21. *泰特的书评*：重印于 Knott, *Life of Tait*, 270–72。
22. *四元数 q 的逆*是 *q*<sup>−1</sup> = *q*<sup>*****</sup>/*qq*<sup>*****</sup>，其中 *q*<sup>*****</sup> 是 *q* 的复共轭。如果你把 *qq*<sup>−1</sup> 乘开，就会发现它确实等于 1。
23. 美国数学家戴维·赫斯特内斯（David Hestenes）是第一位在 1960 年代认识到克利福德与格拉斯曼对几何代数之重要性的现代数学家，此后赫斯特内斯等人进一步发展了这一领域。楔积在现代张量分析中很重要（它们是用我们将在第 11 章看到的张量积来定义的）。
24. *泰特致凯莱*：Knott, *Life of Tait*, 155。
25. *自由功利主义者*：David Weinstein, "Herbert Spencer," in Edward Zalta, ed., *Stanford Encyclopedia of Philosophy*（2019 年秋季版）, plato.stanford.edu。*麦克斯韦与泰特*：例如 Knott, *Life of Tait*, 284–88。
26. *今天对刘易斯身心分析的评价*：Elfed Huw Price, "George Henry Lewes (1817–1878): Embodied Cognition, Vitalism, and the Evolution of Symbolic Perception," in *Brain, Mind and Consciousness in the History of Neuroscience*, ed. Chris Smith and Harry Whitaker (New York: Springer, 2014), 105–23。*泰特、刘易斯、布莱克伍德*：Gordon Haight, ed., *The George Eliot Letters* (New Haven, CT: Yale University Press, 1955), 5:401, 417, 以及 9n181。
27. *麦克斯韦的诗*："British Association, 1874" 发表于 1874 年 12 月号的 *Blackwood's*：Campbell and Garnett: *Life of Maxwell*, 8（诗重印于 326）。
28. *泰特与布莱克伍德在高尔夫球场上（以及麦克斯韦的“更好的 ½”）*：Martin Goldman, *The Demon in the Aether* (Edinburgh: Paul Harris Publishing, 1983), 105。
29. 关于麦克斯韦的诗及相关争论的更多内容，见 Raymond Flood, Mark McCartney, and Andrew Whitaker, *James Clerk Maxwell: Perspectives on His Life and Work* (Oxford: Oxford University Press, 2014)。
<span class="origpage" title="英文原版第 375 页">375</span>

30. *麦克斯韦致坎贝尔*：Campbell and Garnett, *Life of Maxwell*, 202。
31. Knott, *Life of Tait*, 261。
32. *萧伯纳致露西*：转引自 Chisholm, "Science and Literature Linked," 668。
## 第 8 章
1. Bruce Hunt 在其 *The Maxwellians*（Ithaca, NY: Cornell University Press, 1991）中首创了“Maxwellians”（麦克斯韦学派）一词。*洛奇抢先一步*：James Rautio, “Twentythree Years: Acceptance of Maxwell’s Theory,” *Applied Computational Electromagnetics Society Journal* 25, no. 12（December 2010）, 998–1006。
2. *关于亥维赛*：本段及以下各段，我参考了 Bruce Hunt, “Oliver Heaviside: A First-Rate Oddity,” *Physics Today* 65, no. 11 (2012): 48–54, DOI: 10.1063/PT.3.1788；Jed Buchwald, “Oliver Heaviside, Maxwell’s Apostle and Maxwellian Apostate,” *Centaurus* 28 (1985): 288–330；I. Yavetz, *From Obscurity to Enigma: The Work of Oliver Heaviside, 1872–1889*（Basel: Springer, 2011）；以及亥维赛本人的论文，下文我一般随引随注。
3. *麦克斯韦提及亥维赛* 被补进他为第 1 卷所列的勘误表（p. 2），涉及第 404 页。*亥维赛论麦克斯韦的*《*Treatise*》：Rautio, “Twentythree Years.”
4. *天赐的麦克斯韦*：Oliver Heaviside, *Electromagnetic Theory*（London, 1893; New York: Chelsea Publishing, 1971）, 1:14。
5. *崇拜四元数*：Heaviside, *Electromagnetic Theory*, 1:136。
6. Heaviside, *Electromagnetic Theory*, 1:137, 139。
7. *亥维赛从向量中消去虚数*：*Electromagnetic Theory*, 1:137, 142, 149。*他的诙谐*：*Electromagnetic Theory*, 1:135。
8. 亥维赛在英国科学促进会（BAAS）上缺席：*Engineering* 46 (1888): 352；转引自 Hunt, “Oliver Heaviside,” 52–53。
9. *锅嫌壶黑*：Heaviside, *Electromagnetic Theory*, 1:203；*谋杀势*：致 FitzGerald 的信，转引自 Rautio, “Twenty-three Years,” 1004。
10. *亥维赛的形式还不完全是“现代”形式*：在多数本科教材里，麦克斯韦方程组是用 ***E*** 和 ***B*** 写出的，但在亥维赛那里被单独挑出来的却是 ***E*** 和 ***H***。麦克斯韦区分了磁感应（即磁场）***B***——它是一个*通量*——与磁*力 **H***。当磁场完全由磁力感生时，就有 ***B*** = μ***H***，其中 μ 是磁导率系数。亥维赛用的正是这个定义，所以看他的方程时，从 ***H*** 换成 ***B*** 是很直接的。他还采用了麦克斯韦关于电位移 ***D*** 的定义，即用“力” ***E*** 表示的一个通量：***D*** = *c**E***/4π。
今天有些作者仍用 ***H***，不过用 ***B*** 能让亥维赛的方程更加对称。也有些作者追随麦克斯韦和亥维赛，在散度方程里用 ***D*** 而不是 ***E***，但正如我说过的，它与 ***E*** 在数值上成正比。
<span class="origpage" title="英文原版第 376 页">376</span>

11. *势是非物理的（对定域能量而言）*：Buchwald, “Oliver Heaviside,” 293 中有详细说明。*麦克斯韦的波动方程*：用势表述见 *Treatise* 2, 434（art. 784）；用磁场表述见 “A Note on the Electromagnetic Theory of Light,” *Philosophical Transactions of the Royal Society* 158 (1868): 643–57, esp. 655。
在 1868 年的这篇论文里，麦克斯韦的四个场方程还不完全是现代的四个方程，但他从中推导出了磁场的波动方程。这正是亥维赛“谋杀”势时想做的事！可惜麦克斯韦没有把这条路走得更远——不过正如亥维赛指出的（*Electromagnetic Theory*, 1:69），麦克斯韦在《*Treatise*》里并没有充分彰显自己的理论：相反，他提供的是对当时电磁学研究中已有全部贡献的精彩综述。他当然说明了自己怎样以及为何从早先已知的工作发展出这套理论，以及它与别人的超距作用模型相比如何，但他确实不是个自我推销的人。
12. 这四个方程在不同教材中样子略有不同，取决于电学常数和磁学常数的单位怎么选。特别是，除了电学常数和磁学常数，光速 *c* 也常被取为 1（我在这里就是这么做的）；而按亥维赛的做法，通过调整常数的单位，因子 4π 常常被有效地取为 1。（此外，有些教材用亥维赛的“div”和“curl”，而不用吉布斯的点和叉。）
13. 亥维赛深深着迷于四个关键麦克斯韦方程中电场与磁场之间的对称性，以至于他给方程 ∇ ∙ ***B*** = 0 添上了一个虚构的磁“荷”（从而假定磁单极子*确实*存在——正如近半个世纪后狄拉克所做的那样），又在 ∇ × ***E*** 方程里添上了一个磁“流”。但这些添加至今没有任何已知的物理依据（人工制造的短寿命量子单极子除外），所以它们一般不被收入现代的电磁方程；这意味着——撇开向量形式体系不论——现代方程确实是*麦克斯韦的*方程，正如我的叙述所表明的。
<span class="origpage" title="英文原版第 377 页">377</span>

14. *从麦克斯韦的整体向量方程求出* ∇ × ***E***，见其 *Treatise on Electricity and Magnetism*, vol. 2（3rd ed., 1891; reprint, Dover, 1954）：例如，在 2:232（art. 590），麦克斯韦（以文字）给出定义 ***A*** = ∫***E** dt*，或等价地（他 1865 年论文的第 29 式）***E*** = −*d**A***/*dt*。对此式两边取旋度，并记住麦克斯韦定义了 ***B*** = ∇ × ***A***，你就有（利用可以交换求导次序这一点）
$\nabla\times\boldsymbol{E}=-\frac{d}{dt}\left(\nabla\times\boldsymbol{A}\right)=-\frac{d\boldsymbol{B}}{dt}.$
另一种做法是从我叙述中给出的麦克斯韦方程（*Treatise* 2:258 [art. 619]）出发，
$\boldsymbol{E}=v\times\boldsymbol{B}-\frac{d\boldsymbol{A}}{dt}-\nabla\phi,$
然后对两边取旋度。利用恒等式 curl grad = 0，最后一项就消掉了。如果没有运动的电荷，因而电场只由随时间变化的磁场感生（参见 *Treatise* 2:240–41 [art. 599], 2:433 [art. 783]），那么 ***v*** = 0。于是同样有 $\nabla\times\boldsymbol{E}=-\frac{d}{dt}\left(\nabla\times\boldsymbol{A}\right)=-\frac{d\boldsymbol{B}}{dt}$
15. *麦克斯韦的五个向量（四元数）方程* 见其 *Treatise* 2:258–59。（这几页上还有七个定义方程——正如亥维赛所用的那样。）亥维赛特意说过，他的方程形式仍应称为麦克斯韦方程组：*Electromagnetic Theory*, vol. 1, 序言（第五页）及第 69 页。赫兹也同意：Rautio, “Twenty-three Years,” 1005。
16. Heaviside, *Electromagnetic Theory*, 1:297。
17. *吉布斯走向向量之路*：他最初受麦克斯韦启发，随后自己另辟蹊径——与格拉斯曼无关，数年后他才发现格拉斯曼。这一点我们是从他写给 Victor Schlegel 的信中得知的，该信很久之后才由吉布斯的学生 Lynde Phelps Wheeler 在其著作 *Josiah Willard Gibbs: The History of a Great Mind*（New Haven, CT: Yale University Press, 1952）中发表。
18. *吉布斯回应泰特的“怪物”*：“On the Role of Quaternions in the Algebra of Vectors,” *Nature* 43（April 2, 1891）: 511–13。*亥维赛*（含“雌雄同体的怪物”一语及引文）：*Electromagnetic Theory*, 1:137–38, 301。
19. Peter Guthrie Tait, “The Role of Quaternions in the Algebra of Vectors,” *Nature* 43（April 30, 1891）: 608。关于我深为倚重的向量之战的详细分析，见 Michael J. Crowe, *A History of Vector Analysis*（Notre Dame, IN: University of Notre Dame Press, 1967）, chap. 6。
20. *汤姆森的“四元数之战”*：Cargill Gilston Knott, *The Life and Scientific Work of P. G. Tait*（London: Cambridge University Press, 1911）, 185。
<span class="origpage" title="英文原版第 378 页">378</span>

21. Knott, *Life of Tait*, 185；Alexander Macfarlane, “Principles of the Algebra of Vectors,” *Proceedings of the American Association for the Advancement of Science* 40（1891, published 1892）: 65–117；Alexander McAulay, “Quaternions as a Practical Instrument of Physical Research,” *Philosophical Magazine*, 5th ser., 33（June 1892）: 477–95；Crowe, *History of Vectors*, 189–97。
22. Martin Rees 在 *If Science Is to Save Us*（Cambridge: Polity Press, 2022）中给出了这些问题的应对之道。
23. McAulay 转引自 Crowe, *History of Vectors*, 195。*Ida McAulay*：Bruce Scott, “McAulay, Alexander,” *Australian Dictionary of Biography*, adb.anu.edu.au。
24. *泰特评 McAulay*：*Nature* 49（December 28, 1893）: 193–94。
25. Heaviside, “Vectors versus Quaternions,” *Nature*（April 6, 1893），转引自 Crowe, *History of Vectors*, 200。*水电*：Scott, “McAulay, Alexander”；Carol Raabus and Leon Compton, “The Engineering Feats of Tasmania’s Hydroelectric System,” ABC Radio, July 29, 2013。
26. Gibbs, “Quaternions and the Algebra of Vectors,” *Nature* 47（March 16, 1893）: 463–64。
## 第 9 章
1. *Grace Chisholm 谈凯莱*：I. Grattan-Guinness, “A Mathematical Union: William Henry and Grace Chisholm Young,” *Annals of Science* 29, no. 2（August 1972）: 117–18。
2. *纽纳姆学院的历史*：<https://newn.cam.ac.uk/about/history/history-of-newnham/>。牛津大学直到 1920 年才最终允许女性取得正式学位，而剑桥大学更是到 1948 年才如此。
3. 凯莱与泰特的通信见 Cargill Gilston Knott, *The Life and Scientific Work of P. G. Tait*（London: Cambridge University Press, 1911）, 154–96。
4. 在本书写作之时，这些机器作出的预测中有许多仍需在实验室里验证，但即便如此，它们仍能为基因组学研究指明方向。
5. *判别式在平移下的不变性*：二次方程 *ax*<sup>2</sup> + *bx* + *c* = 0 的解为 $x=\left[-b\pm\sqrt{b^{2}-4ac}\right]/2a$。若把 *x* 变换为 *x′* = *x* + *h*，相应的二次方程就变成 *ax′*<sup>2</sup> + *bx′* + *c* = 0，其解为 $x'=\left[-b\pm\sqrt{b^{2}-4ac}\right]/2a$。两者的判别式相同，都是 *b*<sup>2</sup> − 4*ac*，但解并不相同：对平移后的方程我们有 $x'=x+h=\left[-b\pm\sqrt{b^{2}-4ac}\right]/2a$，这意味着 $x=\left[-b-2ah\pm\sqrt{b^{2}-4ac}\right]/2a$；而这并不等于原来的解 $x=\left[-b\pm\sqrt{b^{2}-4ac}\right]/2a$。
6. *凯莱与泰特的引语*：Michael J. Crowe, *A History of Vector Analysis*（Notre Dame, IN: University of Notre Dame Press, 1967）, 212, 214。*Grace Chisholm 谈凯莱*：Grattan-Guinness, “A Mathematical Union,” 117。
7. Crowe, *History of Vectors*, 214。
<span class="origpage" title="英文原版第 379 页">379</span>

8. Crowe, *History of Vectors*, 217。
9. 他在 1901 年 3 月 27 日写给米列娃·马里奇的信中，谈到求职时提到了反犹主义：*Collected Papers of Albert Einstein*, vol. 1, ed. John Stachel, David C. Cassidy, and Robert Schulmann（Princeton, NJ: Princeton University Press, 1987; English Supplement translated by Anna Beck）, document 94, <https://einsteinpapers.press.princeton.edu/vol1-trans/182>。
<span class="origpage" title="英文原版第 380 页">380</span>

10. 在上一则尾注提到的 1901 年 3 月 27 日的那封信里（<https://einsteinpapers.press.princeton.edu/vol1-trans/182>），爱因斯坦期盼着“我们俩共同把相对运动的研究带到胜利的结局”的那一天。一些学者引此为爱因斯坦与马里奇合作研究相对论的证据，不过语境以及“胜利的结局”这些字眼也提示，这可能只是他们结婚计划的一个比喻（婚事因亲属反对、米列娃为毕业所做的挣扎，以及爱因斯坦没有工作而一再拖延）。据我所查，在现存写给马里奇的信中，爱因斯坦此前（以及此后）提到相对论，仅有的几次是：1899 年 9 月 10 日的信（*Collected Papers of Albert Einstein*, vol. 1, document 54），他在信中告诉米列娃，自己有了一个想法，关于相对于以太的相对运动如何影响光速，并补充说“这个就说到这儿吧！”（因为她在准备考试）：<https://einsteinpapers.press.princeton.edu/vol1-trans/155>；以及 1899 年 9 月 28 日的第 57 号文件，其中没有出现“我们的”理论这样的说法；1901 年 12 月 17 日的第 128 号文件同样如此。从她的信和爱因斯坦写给她的信来看，她显然从未就此发表过任何评论——她关注的反而是与考试相关的题目。要是我们知道他们在一起、不需要写信时都发生了些什么就好了！爱因斯坦早年确实怀抱着两人共度科学生涯的梦想——在本卷 1900 年 8 月 14 日的第 72 号文件中，他告诉她，不在她身边时他便缺乏自信，也感受不到工作的乐趣。马里奇这一时期的信件存世极少：留存下来的那些聚焦的都是她结婚、通过文凭考试、开始读博士的梦想（而她的文凭论文写的是热与能量，不是相对论）。至于她“替爱因斯坦做数学”，他们 1900 年的考试成绩显示，爱因斯坦数学优秀而她不及格：vol. 1, document 67, <https://einsteinpapers.press.princeton.edu/vol1-trans/163>。考试成绩当然不能说明一切，但这确实终结了所谓爱因斯坦数学无能的说法。在我看来，要更公正地对待马里奇这位女性科学先驱，应当去审视毁掉她前程的偏见，而不是去宣称那些没有明确证据的事情。关于这段关系以及狭义相对论的更多信息，见我的电子短篇 *Young Einstein and the Story of E = mc*<sup>2</sup>（Sydney: Ligature, 2014）及其中的文献。关于“米列娃·马里奇是共同作者”这一说法的证据，有一份很简短的最新综述：Ann Finkbeiner, “The Debated Legacy of Einstein’s First Wife,” *Nature* 567 (2019): 28–29。
11. *麦克斯韦的想法* 表述于他为第 9 版《*Encyclopaedia Britannica*》（1878）所写的“Ether”词条，8:568–72，并在 1879 年 3 月 19 日致 David Peck Todd 的信（他去世前几个月）中有更详细的说明。托德认识到它的重要性，把它寄给斯托克斯，后者转交皇家学会，学会将它发表于会刊：“‘On a possible method of detecting the motion of the solar system through the luminiferous ether’ by the late Professor J. Clerk Maxwell,” *Proceedings of the Royal Society*, January 22, 1880, 108–10。*迈克耳孙研究过这封信*，因为他曾在托德的办公室工作。另见 Robert Shankland, “Michelson and His Interferometer,” *Physics Today* 27, no. 4（1974）: 37, DOI: 10.1063/1.3128534；Shankland 文中附有迈克耳孙干涉仪的照片。*不过，在他们报告结果的论文中*，迈克耳孙与莫雷把卫星法列为鉴于其否定结果而可能进行的未来实验，却没有引用麦克斯韦；想必他们不知道他的信已经发表：Albert A. Michelson and Edward W. Morley, “On the Relative Motion of the Earth and the Luminiferous Ether,” *American Journal of Science*, ser. 3, 34, no. 203（November 1887）: 345。
12. *洛伦兹电子论*：麦克斯韦假定电荷是连续分布的——因此他的方程里有电荷密度项 ρ 和电流密度 ***J***；洛伦兹证明，这些密度是电荷（点）分布的近似或平均，麦克斯韦方程在这些点上奇异，但在其他各处成立。*爱因斯坦论洛伦兹*：Albert Einstein, *Ideas and Opinions*（1954; New York: Three Rivers Press, 1982）, 73–76，以及 Banesh Hoffman（with the collaboration of Helen Dukas）, *Einstein*（Frogmore: Paladin, 1975）, 98。
<span class="origpage" title="英文原版第 381 页">381</span>

13. H. Poincaré, “Sur la dynamique de l’électron,” *Rendiconti del Circolo Matematica di Palermo* 21 (1906): 18–76。他此前已于 1905 年 6 月 5 日向法国科学院提交过此文的初步“Note”，并在几年前就相关的想法写过文章。爱因斯坦 1905 年论文（原载 *Annalen der Physik*）的英译本见：A. Einstein, “On the Electrodynamics of Moving Bodies,” in H. A. Lorentz et al., *The Principle of Relativity*（New York: Dover, 1952）, 37–65。
14. 早在 1910 年，一直在研究洛伦兹群几何（该群在爱因斯坦狭义理论中居于基础地位）的费利克斯·克莱因（Felix Klein）就声称，人们“如果真想的话，完全可以用‘相对于一个变换群的相对性’这一术语来取代‘关于一个变换群的不变量理论’”（转引自 Yvette Kosmann-Schwarzbach [translated by Bertram E. Schwarzbach], *The Noether Theorems: Invariance and Conservation Laws in the Twentieth Century* [New York: Springer, 2011], 70）。2022 年，Martin Rees（在 *If Science Is to Save Us* [Cambridge: Polity, 2022], 93）提出，用“不变性理论”而非“相对性”来命名，本可以避免“与人类语境中相对主义的有误导性的类比”。
15. *Grace Chisholm 与高维*：她的这段回忆转载于 Grattan-Guinness, “A Mathematical Union,” 128–29。
16. 关于这些四维探索及其背景（包括布尔一家，以及超正方形类比）的精彩叙述，见 Nicholas Mee, *Celestial Tapestry: The Warp and Weft of Art and Mathematics*（Oxford: Oxford University Press, 2020）。
17. 关于（双）四元数在狭义相对论中的现代分析，见 Joachim Lambek, “In Praise of Quaternions,” *Comptes Rendues Mathematical Reports*, Academy of Sciences, Canada, 35, no. 4（2013）: 121–36；<https://www.math.mcgill.ca/barr/lambek/pdffiles/Quater2013.pdf>。哈密顿本人讨论过双四元数（其系数为复数）。
18. *“懒狗”*：转引自 Michael White and John Gribbin, *Einstein: A Life in Science*（London: Simon and Schuster, 1993）, 39。*闵可夫斯基论四元数*：Scott Walter, “Breaking in the 4-vectors: The Four-dimensional Movement in Gravitation, 1905–1910,” in *The Genesis of General Relativity*, ed. Jürgen Renn（Dordrecht: Springer, 2007）, 3:212。
19. 闵可夫斯基的引语见 Constance Reid, *Hilbert*（Berlin: Springer-Verlag, 1970）, 105, 112。
20. *时空间隔* 告诉你如何考量发生在两个不同地点和时刻的两个事件之间的“距离”：
$\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}-\left(c\left(t_{2}-t_{1}\right)\right)^{2}}.$
如果你在空间中*同一*点观察先后发生的两个事件，那么间隔给出的就是按你自己的腕表计量的两者之间的时间（因为 *x*<sub>2</sub> − *x*<sub>1</sub>、*y*<sub>2</sub> − *y*<sub>1</sub>、*z*<sub>2</sub> <sub>−</sub> *z*<sub>1</sub> 全为零）。这就是所谓“固有”时间。类似地，如果你在同一时刻测量两个事件，度规给出的就是它们之间的（固有）距离（因为此时 *t*<sub>2</sub> − *t*<sub>1</sub> 为零）。但正如洛伦兹变换所表明的，相对运动的观测者对这些时间和距离并无一致意见——双方唯一认同的是*间隔整体是不变的*。
顺便说一句，为了让这个二次型的间隔度量的“号差”（signature——其名如此）变成 + + + + 而不是 + + + −，闵可夫斯基把时间取为虚数，以契合二次型的原初想法。
<span class="origpage" title="英文原版第 382 页">382</span>

21. H. Minkowski, “Space and Time,” 1908，英译见 H. A. Lorentz et al., *Principle of Relativity*, 75–91。涨红了脸：Reid, *Hilbert*, 92。关于 1907 年的演讲：Walter, “Breaking in the 4-vectors,” 219。
22. *关于闵可夫斯基之死*：Reid, *Hilbert*, 115。
23. *克莱因与尤斯图斯*：Crowe, *History of Vectors*, 92。
24. *不变的时空间隔／常量 c*：速度等于距离／时间，所以在三维空间中，光速可以用关于距离的毕达哥拉斯定理来定义：
*c*<sup>2</sup> = (*x*<sup>2</sup> + *y*<sup>2</sup> + *z*<sup>2</sup>)/*t*<sup>2</sup>；
这个方程的另一种写法当然是
*x*<sup>2</sup> + *y*<sup>2</sup> + *z*<sup>2</sup> − (*ct*)<sup>2</sup> = 0。
左边的表达式在洛伦兹变换下不变，这意味着当坐标 (*x, y, z, t*) 与 (*x′, y′, z′, t′*) 通过洛伦兹变换相联系时，你仍然得到
*x*<sup>2</sup> + *y*<sup>2</sup> + *z*<sup>2</sup> − (*ct*)<sup>2</sup> = *x′*<sup>2</sup> + *y′*<sup>2</sup> + *z′*<sup>2</sup> − (*ct′*)<sup>2</sup>。
这也就意味着 *x′* <sup>2</sup> + *y′* <sup>2</sup> + *z′* <sup>2</sup> − (*ct′*)<sup>2</sup> = 0 同样成立，于是在 (*x′, y′, z′, t′*) 系中光速也必定是 *c*。
25. William Thomson, “Elements of a Mathematical Theory of Elasticity,” *Philosophical Transactions of the Royal Society of London* 146（1856）: 481–98；Augustin Cauchy, “Sur les equations qui experiment les conditions d’équilibre ou les lois du movement intérieur d’un corps solide, élastique ou nonélastique,” *Exercises de Mathématiques* 3（1828）: 160–87。
26. Maxwell, *Treatise on Electricity and Magnetism*（Oxford: Clarendon Press, 1873）, 2:278–81。
<span class="origpage" title="英文原版第 383 页">383</span>

27. 闵可夫斯基把这些特殊的双指标量称为“第二类向量”（vectors of the second kind），索末菲称之为“六向量”（six-vectors）。今天它们被径直称为张量——在这里是反对称的二阶（second-rank 或 second-order）张量，其中“秩”（rank）或“阶”（order）指其分量上指标的数目。（如果这些张量是定义在整个空间上、而不是在一点上的，那么严格说来它们是张量场。）
## 第 10 章
1. *爱因斯坦的博士*：Banesh Hoffmann, *Einstein*（Frogmore: Paladin, 1975）, 55。*格罗斯曼看出爱因斯坦的伟大*：见我的 *Young Einstein* 及其中的文献。
2. Albert Einstein, *Ideas and Opinions*（1954; New York: Three Rivers Press, 1982）, 289。
3. *爱因斯坦致索末菲*：Judith Goodstein, *Einstein’s Italian Mathematicians*（Providence, RI: American Mathematical Society, 2018）, 95。
4. *高斯、测量与最小二乘*：Martin Vermeer and Antti Rasilia, *Map of the World: An Introduction to Mathematical Geodesy*（Milton Park, UK: Taylor and Francis, 2019）, 181；Frank Reid, “The Mathematician on the Bank Note: Carl Friedrich Gauss,” *Parabola* 36, no. 2 (2000)。高斯虽于 1825 年退出野外作业，但一直指导这项测量直到 1844 年完成。
5. 实际上，闵可夫斯基和爱因斯坦写下这个度规时正负号是反过来的：
*ds*<sup>2</sup> = −*dx*<sup>2</sup> − *dy*<sup>2</sup> − *dz*<sup>2</sup> + *c*<sup>2</sup>*t*<sup>2</sup>，或 *ds*<sup>2</sup> = *c*<sup>2</sup>*t*<sup>2</sup> − *dx*<sup>2</sup> − *dy*<sup>2</sup> − *dz*<sup>2</sup>；
符号的选取称为“号差”，就我们的目的而言，关键在于时间微分的符号与空间的各项相反。
6. *高斯论证概要*：这里的页码（以及别处）指高斯 1828 年论文的英译本，*General Investigations of Curved Surfaces of 1827 and 1825*, by Karl Friedrich Gauss, translated by James Morehead and Adam Hiltebeitel, Project Gutenberg, 2011（from the 1902 edition, Princeton: Princeton University Library）；<https://www.gutenberg.org/files/36856/36856-pdf.pdf>。
我说过，对他的二维曲面，高斯把三个 *x, y, z* 坐标变换为两个他称之为 *p*、*q* 的新变量的函数——所以你可以把坐标变换写成（我将其取为线性的）
*x* = *f*(*p, q*), *y* = *g*(*p, q*), *z* = *h*(*p, q*)。
于是链式法则给出
$dx=\frac{\partial f}{\partial p}dp+\frac{\partial f}{\partial p}dq=adp+a'dq$ 用高斯的记号（p. 7）。
（遗憾的是，高斯和黎曼一样，用的是撇号而不是不同的字母。）
同样地，*dy* = *bdp* + *b′dq, dz* = *cdp* + *c′dq*。把这些式子平方相加，你得到（参见高斯 pp. 18, 20）：
<span class="origpage" title="英文原版第 384 页">384</span>

*dx*<sup>2</sup> + *dy*<sup>2</sup> + *dz*<sup>2</sup> = (*a*<sup>2</sup> + *b*<sup>2</sup> + *c*<sup>2</sup>)*dp*<sup>2</sup> + 2(*aa′* + *bb′* + *cc′*)*dpdq* + (*a′*<sup>2</sup> + *b′*<sup>2</sup> + *c′*<sup>2</sup>)*dq*<sup>2</sup> = *Edp*<sup>2</sup> + 2*Fdpdq* + *Gdq*<sup>2</sup>，
其中高斯用 *E, F, G* 来简化表达式。
但事后看来令人着迷的是：从标量积的代数定义可以看出，*E, F, G* 正是我们今天所说的向量
***v*** = *a**i*** + *b**j*** + *c**k, v′*** = *a′**i*** + *b′**j*** + *c′**k***；
的标量积；换句话说，
*E* = ***v*** ∙ ***v**, F* = ***v*** ∙ ***v′**, G* = ***v′*** ∙ ***v′***。
这两个向量是坐标线 *p, q* 的*单位切向量*，正如叙述中的<a href="#fig-10-4">图 10.4</a> 所示。（要看出这一点，考虑无穷小位移向量，用向量的简写括号记法：
*d**r*** = (*dx, dy, dz*) = (*a, b, c*)*dp* + (*a′, b′, c′*)*dq* = ***v**dp* + ***v′**dq*；
*切向量*是通过把它对这两个坐标求导得到的，正如我们对普通函数求导以求其切线的斜率一样：
$\frac{dr}{dp}=v,\frac{dr}{dq}=v'.)$
两个向量标量积的几何定义是 ***a.b*** = |***a***||***b***| cosθ，而正如我们在第 9 章看到的，$|\boldsymbol{a}|=\sqrt{\boldsymbol{a}\cdot\boldsymbol{a}}$。所以这两个切向量之间的夹角是
$\cos\theta=\frac{v\cdot v'}{(\sqrt{v\cdot v)(v\cdot v'})}=\frac{F}{\sqrt{EG}}.$
后来的数学家将其推广到任意的度规和维数，度规的系数写作 *g<sub>ij</sub>*：对于这里的二维情形，我们有
$\cos\theta=\frac{g_{12}}{\sqrt{g_{11}g_{22}}}.$
为了求曲面的曲率，把这些公式应用于边由坐标线围成的三角形，如<a href="#fig-10-4">图 10.4</a>，然后如我在叙述中所解释的，由内角和给出曲率的性质。
顺便说一句，如果你熟悉二重积分，那么我在叙述中提到的面积积分里的表达式 $\sqrt{EG-F^{2}}$ 就是雅可比行列式。它是度规系数矩阵的行列式，用广义相对论中的一般度规来写就是 $\sqrt{-g}$。
*高斯用角度定义曲率*：p. 46（及 44）。
*哈里奥特的工作*：见我的 *Thomas Harriot: A Life in Science*（New York: Oxford University Press, 2019）, 160–61，另见 John Stillwell, *Mathematics and Its History*（New York: Springer-Verlag, 1989）, 249–50。
<span class="origpage" title="英文原版第 385 页">385</span>

7. *霍金论黑洞视界（边界）*：他于 1972 年发表了这一结果；他也在 S. W. Hawking and G. F. R. Ellis, *The Large Scale Structure of Space-time*（Cambridge: Cambridge University Press, 1973）, 335–37 中给出了证明。关于霍金证明的简要勾勒以及一份有用的曲率简史，见 Greg Galloway, “From the Shape of the Earth to the Shape of Black Holes: Aristotle to Hawking and Beyond,” Miami University’s Mathematics Department, Arts and Sciences Cooper Lecture, November 2017。关于黑洞历史的有趣概述，见诺贝尔奖网站上 2020 年物理学奖的综述。注意，有研究者提出，事件视界望远镜（EHT）的首张黑洞直接图像，实际上拍到的可能是引力磁单极子而非黑洞；他们已计算出一些参数，可在未来更精确的 EHT 观测中区分这两种可能：M. Ghasemi-Noedi et al., “Investigating the Existence of Gravitomagnetic Monopole in M87*,” *European Physics Journal C* 81, no. 939 (2021)；<https://doi.org/10.1140/epjc/s10052-021-09696-3>。
8. 仅举一例，关于高斯曲率在材料起皱研究中所起的作用，以及以创新方式利用这些褶皱的可能性，见 Stephen Ornes, “The New Math of Wrinkling,” *Quanta* 杂志（September 22, 2022）；<https://www.quantamagazine.org/the-new-math-of-wrinkling-patterns-20220922/>。
9. Lewis Campbell and William Garnett, *The Life of James Clerk Maxwell*（London: Macmillan, 1882）, 324–25。
10. *爱因斯坦任无薪讲师（Privatdozent）*：Hoffmann, *Einstein*, 86–87。*高斯论黎曼*：Raymond Flood and Robin Wilson, *The Great Mathematicians*（London: Arcturus, 2011）, 160。*七十七岁的高斯*：Goodstein, *Einstein’s Italian Mathematicians*, 31。*高斯深受打击*：Stillwell, *Mathematics and Its History*, 253–54。
11. 关于黎曼工作的一份出色的、更具技术性的叙述——以及该论文的英译——见 Ruth Farwell and Christopher Knee, “The Missing Link: Riemann’s ‘Commentatio,’ Differential Geometry and Tensor Analysis,” *Historia Mathematica* 17 (1990): 223–55。
<span class="origpage" title="英文原版第 386 页">386</span>

12. Maxwell, *Treatise on Electricity and Magnetism*（Oxford: Clarendon, 1873）, 1:333（art. 280）。注意，汤姆森和泰特（在其 *T&T′*, 1:515）用成对的字母表示弹性系数，正如黎曼那样，而不像麦克斯韦那样使用指标。
13. 如果材料是各向异性的（如黎曼所假设的），导热系数就是一个双指标张量。对于各向同性材料，热量向各个方向均匀散开，因此无需顾虑随方向的变化，可以用标量表示。
14. Bernhard Riemann, translated into English by William Kingdon Clifford, “On the Hypotheses Which Lie at the Bases of Geometry,” *Nature* 8, no. 183 (1873): 14–17, and no. 184, 36–37。
15. 关于黎曼 1854 年和 1861 年的论文、以及包括埃尔温·克里斯托费尔在内的后继者工作的详细分析，见 Olivier Darrigol, “The Mystery of Riemann’s Curvature,” *Historia Mathematica* 42 (2015): 47–83。另见 Farwell and Knee, “Missing Link.” 埃尔温·克里斯托费尔 1869 年论文的英译见 Bas Fagginger Auer 的 “Christoffel Revisited”（硕士学位论文，Mathematical Institute, University of Utrecht, 2009）第 8 章。
16. 若选取单位使 *c* = 1，系数就是 1, 1, 1, −1。黎曼证明，如果度规的系数是常数，那么可以缩放坐标，使度规中所有系数都是 1（或如闵可夫斯基后来所证明的，−1）。
## 第 11 章
1. 关于里奇的生平细节，包括政治背景，我在本章中始终参考 Judith Goodstein, *Einstein’s Italian Mathematicians*（Providence, RI: American Mathematical Society, 2018）。
2. Goodstein, *Einstein’s Italian Mathematicians*, 2。
3. *里奇致 Antonio Manzoni*，1872 年 11 月 24 日，转引自 Goodstein, *Einstein’s Italian Mathematicians*, 6。
4. Goodstein, *Einstein’s Italian Mathematicians*, 16。
5. *里奇与奇泽姆谈克莱因*：转引自 Goodstein, *Einstein’s Italian Mathematicians*, 16, 17。注意：柯瓦列夫斯卡娅（Kovalevsky）1874 年的哥廷根博士学位与奇泽姆的剑桥学位一样，是“非正式”的。
6. Goodstein（*Einstein’s Italian Mathematicians*, 27–30）用里奇与比安卡的通信勾勒出他们恋情的温情图景。
7. *里奇为其 1884 年论文所写的引言*：转引自 Goodstein, *Einstein’s Italian Mathematicians*, 32。
8. W. H. and G. Chisholm Young, *Nature* 58, no. 1492（June 2, 1898）: 99–100。
<span class="origpage" title="英文原版第 387 页">387</span>

9. *黎曼张量上的指标*：粗略地说，由于这个张量由双指标度规分量的二阶导数构成，它的四个指标涉及的是哪个度规分量被哪一对坐标所微分。实际情况比这稍复杂一些，因为黎曼张量是度规分量导数的和，但大意如此。
10. 麦克斯韦的方法是“加色法”——把三个滤镜的光叠加，再把图像投射到屏幕上。今天的幻灯片、电视和数字图像用的就是这种方法。印刷图像用的是“减色法”（在麦克斯韦铺路之后才被发现），三种颜色是从纸上的颜料反射出来的，而不是透过滤镜／像素层传到屏幕上。减色法的三原色与麦克斯韦的正好“相反”——它们是青色、品红和黄色。
11. *关于训练 AI 模型时盗用数据*：见，例如，Nick Vincent and Hanlin Li, “ChatGPT Stole Your Work. So What Are You Going to Do?,” *Wired*（January 28, 2023）, <https://www.wired.com/story/chatgpt-generative-artificial-intelligence-regulation/>。关于写作者的反击，见，例如，Vanessa Thorpe, “‘ChatGPT Said I Did Not Exist’: How Writers and Artists Are Fighting Back against AI,” *The Guardian*, March 19, 2023。
<span class="origpage" title="英文原版第 388 页">388</span>

12. *NLP（含大语言模型）的益处与问题*：本书付印之时，情形想必已变了许多，AI 发展就是这么快；不过这里给出一些较新的参考。关于益处的另一个例子，见 Samantha Spengler, “For Some Autistic People, ChatGPT Is a Lifeline,” *Wired*, May 30, 2023；<https://www.wired.com/story/for-some-autistic-people-chatgpt-is-a-lifeline/#>。关于问题，除了训练数据被盗用之外，人们已就 ChatGPT 某些输出的不可靠写过很多——所以尽管益处明显，它在教育中的角色仍无定论：见，例如，Hayden Horner, “ChatGPT: Brilliance or a Bother for Education,” Engineering Institute of Technology 新闻网站, March 13, 2023, <https://www.eit.edu.au/chatgpt-brilliance-or-a-bother-for-education/>。同样地，在远程医疗（以及其他许多领域）中，有利也有弊：见，例如，Som Biswas, “Role of ChatGPT in Public Health,” *Annals of Biomedical Engineering*（March 2023），线上发表于 <https://www.researchgate.net/profile/Som-Biswas-2/publication/369269117>。复杂的 AI 带来明显的社会问题，从助长监控到制造深度伪造和假新闻。我在第 4 章的注释里提过偏见问题，另见，例如，Grace Browne, “AI Is Steeped in Big Tech’s ‘Digital Colonialism,’” *Wired UK*（May 25, 2023）；<https://www.wired.co.uk/article/abeba-birhane-ai-datasets>。围绕相似主题，另见 *MIT Technology Review* 的系列文章 “AI Colonialism”，<https://www.technologyreview.com/supertopic/ai-colonialism-supertopic/>，其中也包含受压迫民族以积极方式使用 AI 进行反击的例子。此外还有环境问题，例如 Maanvi Singh, “As the AI Industry Booms, What Toll Will It Take on the Environment?,” *The Guardian*（June 9, 2003）。关于科学与技术的知情公共讨论，比以往任何时候都更为关键！
13. 当然，NLP 和大语言模型的内容远不止张量积。就我的叙述（以及关于 NLP 的更多内容）而言，我特别受惠于 Qiuyuan Huang, Paul Smolensky, Xiaodong He, Li Deng, Dapeng Wu, “Tensor Product Generation Networks for Deep NLP Modeling,” *Proceedings of NAACL-HLT 2018*（New Orleans）: 1263–73；Lipeng Ahang et al., “A Generalized Language Model in Tensor Space,” 33rd Annual Conference of the AAAI (2019)；以及 Matthew Kramer, “Word Embeddings,” Medium.com, August 31, 2021。
14. “原则上，一台 300 量子比特的量子计算机在一瞬间所能完成的计算，比可见宇宙中的原子还多”：Charles Q. Choi, “How Many Qubits Are Needed for Quantum Supremacy?” *IEEE News*, May 21, 2020；<https://spectrum.ieee.org/qubit-supremacy#:~:text=Superposition%20lets%20one%20qubit%20perform,eight%20calculations%3B%20and%20so%20on>。
15. *Enrico Betti*：*n* 维中的斯托克斯定理：Victor Katz, “The History of Differential Forms from Clairaut to Poincaré,” *Historia Mathematica* 8 (1981): 161–88, esp. 175。*贝蒂当兵、为期刊投稿*：Goodstein, *Einstein’s Italian Mathematicians*, 7。*贝蒂与里奇的论文*：Goodstein, *Einstein’s Italian Mathematicians*, 148。
16. 里奇的信，转引自 Goodstein, *Einstein’s Italian Mathematicians*, 9–10。
17. *里奇为晋升的长期奋斗*：Goodstein, *Einstein’s Italian Mathematicians*, 35–43, 59–61。
18. G. Ricci and T. Levi-Civita, “Méthodes de calcul différential absolu et leurs applications,” *Mathematische Annalen* 54 (1900): 125–201；关于学习新技能所需付出的努力与回报，见 128（我的译文）。
19. 例如，若按<a href="#fig-11-1">图 11.1</a> 由两个*逆变*向量 ***a*** 和 ***b*** 的张量积（外积）构成一个二阶张量 *T*，你就有变换法则
$T^{\mu'v'}\equiv a^{\mu'}b^{v'}=\left(A_{\sigma}^{\mu'}a^{\sigma}\right)\left(A_{\lambda}^{v'}a^{\lambda}\right)=A_{\sigma}^{\mu'}A_{\lambda}^{v'}a^{\sigma}a^{\lambda}\equiv A_{\sigma}^{\mu'}A_{\lambda}^{v'}T^{\sigma\lambda}.$
别忘了，这里用于张量、变换矩阵系数和指标的字母都是任意的，就像代数里的 *x*。但它们提供了多么奇妙的灵活性——你可以如此轻易地挪动变换符号，从而给出你想要的任何种类张量的法则！
<span class="origpage" title="英文原版第 389 页">389</span>

20. *昂鲁效应*：1976 年，加拿大物理学家威廉·昂鲁（William Unruh）借助量子理论发现，广义相对论预言温度并不完全像我在<a href="#fig-11-1">图 11.1</a> 中所说的那样是与坐标无关的标量。相反，加速运动的观测者所测得的时空温度，会与静止观测者测得的略有不同。这种“昂鲁效应”尚未被探测到——要测出一度的温度变化，你得接近光速旅行才行。但在 2022 年，由 James Quach 领导的阿德莱德大学团队发明了一种“量子温度计”，也许很快就能证明昂鲁、以及广义相对论是对的。
21. 不过请注意，这里我们谈的是单一参照系中的向量——与上面的旋转例子不同，这种求和与参照系之间的变换无关。
22. *证明 *n* 维中标量积在坐标变换下的不变性*：用变换方程中矩阵系数的微分形式最容易看清。例如，二维旋转变换方程的第一个是 *x′* = *x* cosθ + *y* sin θ。用偏导数，这个方程的微分形式是
$dx'=\frac{\partial x'}{\partial x}dx+\frac{\partial x'}{\partial y}dy,$
你可以看出 $\frac{\partial x'}{\partial x}=\cos\theta$，其余导数依此类推——所以这些导数正是我在叙述中标为 $A_{\sigma}^{\mu'}$ 的那些分量。对于列向量与行向量的数量（内）积，你会有（最后一项用链式法则得到）：
$u^{\mu'}v_{\mu'}=A_{\sigma}^{\mu'}A_{\mu'}^{\lambda}u^{\sigma}v_{\lambda}\equiv\frac{\partial x^{\mu'}}{\partial x^{\sigma}}\frac{\partial x^{\lambda}}{\partial x^{\mu'}}u^{\sigma}v_{\lambda}=\frac{\partial x^{\lambda}}{\partial x^{\sigma}}u^{\sigma}v_{\lambda}.$
重复指标意味着右端是
$\frac{\partial x^{\lambda}}{\partial x^{1}}u^{1}v_{\lambda}+\frac{\partial x^{\lambda}}{\partial x^{2}}u^{2}v_{\lambda}+\dots+\frac{\partial x^{\lambda}}{\partial x^{n}}u^{n}v_{\lambda}.$
这些导数是对*独立*坐标求的，所以唯一有意义的导数是 $\frac{\partial x^{\lambda}}{\partial x^{\lambda}}=1$。这类似于中学微积分：通常只有一个自变量，比如 *x*，于是 $\frac{dx}{dx}=1.$。所以上面那个右端表达式里 σ 唯一可能的取值是 λ。也就是说，我们有
<span class="origpage" title="英文原版第 390 页">390</span>

*u*<sup>μ´</sup> *v*<sub>μ´</sub> = *u*<sup>λ</sup>*v*<sub>λ</sub>。
这个表达式在变换后的坐标系（带撇的）中与在原来的坐标中形式相同。（重复指标用什么字母无关紧要，因为它们只是告诉你要求和的占位符。所以我可以把 μ 换成 λ。）
换句话说，标量积在这种坐标变换下是不变的。
23. *ds<sup>2</sup> 的不变性*：我们前面看到，逆变张量与协变张量的坐标变换矩阵互为逆矩阵，$A_{\sigma}^{\mu'}\to A_{\mu'}^{\sigma}$（或用导数记号表示矩阵分量，$\frac{\partial x^{\mu'}}{\partial x^{\sigma}}\to\frac{\partial x^{\sigma}}{\partial x^{\mu'}}).$所以互逆的一对会“抵消”，于是我们有
$ds^{2}=g_{\mu'v'}dx^{\mu'}dx^{v'}=A_{\mu'}^{\sigma}A_{v'}^{\lambda}A_{\sigma}^{\mu'}A_{\lambda}^{v'}g_{\sigma\lambda}dx^{\sigma}dx^{\lambda}=g_{\sigma\lambda}dx^{\sigma}dx^{\lambda}.$
距离测度 *ds*<sup>2</sup> 在每个参照系中具有相同的形式和相同的数值。（记住，重要的是指标的模式，而不是字母的选择。）
24. *欧金尼奥·贝尔特拉米论里奇的张量*：Goodstein, *Einstein’s Italian Mathematicians*, 49。
25. Ricci and Levi-Civita, “Méthodes de calcul différential absolu,” 128（我的译文）。
## 第 12 章
1. G. Ricci and T. Levi-Civita, “Méthodes de calcul différential absolu et leurs applications,” *Mathematische Annalen* 54 (1900): 125–201。
2. R. H. Dicke（“The Eötvös Experiment,” *Scientific American* 205, no. 6（December 1961）: 84–95）提出，爱因斯坦早期思考引力时是否知道厄特沃什（Eötvös）的结果并不清楚，但如果实验表明伽利略定律是错的，爱因斯坦肯定会听说。关于 2022 年的检验：Pierre Touboul et al., “MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle,” *Physical Review Letters* 129 (2022): 121102.1–121102.8。
3. Urbain LeVerrier 是第一个算出这一差异的人；用更新后的测量数据，他的方法给出约 43 角秒。
4. 转引自 Abraham Pais, *Subtle Is the Lord*（Oxford: Oxford University Press, 1982）, 178。有人把“happiest”译为“最幸运的”。
5. 由于下落观测者越接近地心，地球引力就越强，下落观测者与匀加速观测者之间存在可测量的差异。同样，海洋潮汐之所以产生，是因为地球朝向月亮的一面离月亮更近、感受到的拉力更强。
<span class="origpage" title="英文原版第 391 页">391</span>

6. *爱因斯坦在布拉格的职位*：Banesh Hoffmann, *Einstein*（Frogmore: Paladin, 1975）, 94。1882 年，在捷克民族主义与民族纠纷之后，布拉格大学（即查理大学）分裂为捷克部分和德国部分：<https://cuni.cz/UKEN-298.html>。
7. *牛顿引力的势形式，由牛顿定律导出* $F=ma=\frac{GmM}{r^{2}}\Rightarrow a=\frac{GM}{r^{2}}$。在笛卡儿坐标中，把引力加速度 *a* 的分量记作 *X, Y, Z*，并注意向量 ***a*** 与两个质量之间的距离 *r* 同方向。把一个质量 *m* 放在原点，那么 ***r*** 就是第二个质量 *M* 的位置向量，*M* 位于点 (*x, y, z*)。***a*** 的水平分量由 $\boldsymbol{a}\cdot\boldsymbol{i}=a\cos\theta=\frac{ax}{r}=\frac{GMx}{r^{3}},$ 给出，其余分量同理。对这些分量求导（用 $r=\sqrt{x^{2}+y^{2}+z^{2}}$ 和链式法则）并相加，得到 $\frac{\partial V}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}=0.$ 由于加速度与（保守）力成正比，我们可以用一个势 $V:X=\frac{\partial V}{\partial x},Y=\frac{\partial V}{\partial y},Z=\frac{\partial V}{\partial z},$ 来写出它的分量，于是上式变成拉普拉斯方程 $\frac{\partial^{2}V}{\partial x^{2}}+\frac{\partial^{2}V}{\partial y^{2}}+\frac{\partial^{2}V}{\partial z^{2}}=0.$ 如果存在密度为 ρ 的连续物质分布，那么成立的则是泊松方程，右端为 4π*G*ρ。
8. *电荷与质量密度的注意事项*：在电磁学中，需要区分电荷密度与点电荷。就引力而言，无论是牛顿的还是爱因斯坦的，区别在于物质的平均分布（遍布太阳系，或在星云、星系中）与点源（如单颗恒星或行星）。（牛顿证明了球体作用起来如同其全部质量集中在一点，即球心。）这意味着方程在一点上是奇异的——也就是说，它们在那里失效——但在这个点源之外它们没问题，在那里它们被称为“真空方程”。对于密度为 ρ 的物质平均分布，它们同样没问题。更多内容见 Peter Gabriel Bergmann, *Introduction to the Theory of Relativity*（New York: Dover, 1976）, 175–77。
9. 爱因斯坦致贝索，转引自 Hanoch Gutfreund and Jürgen Renn, *The Road to Relativity: The History and Meaning of Einstein’s “The Foundation of General Relativity”*（Princeton, NJ: Princeton University Press, 2015）, 9。*“严重的错误”* 转引自 Judith Goodstein, *Einstein’s Italian Mathematicians*（Providence, RI: American Mathematical Society, 2018）, 102–3。
10. 转引自 Goodstein, *Einstein’s Italian Mathematicians*, 104。我对亚伯拉罕与爱因斯坦关系的概述也要归功于 Goodstein。
<span class="origpage" title="英文原版第 392 页">392</span>

11. 爱因斯坦的恳求由他在 ETH 的同学、后来的教授 Louis Kollros 回忆；转引自 N. Straumann, “Einstein’s ‘Zürich Notebook’ and His Journey to General Relativity,” *Annals of Physics*（Berlin）523, no. 6（2011）: 488–500, esp. 490。
12. 爱因斯坦在他 1916 年的论文（*The Foundation of the General Theory of Relativity*, 1916，英译见 H. A. Lorentz et al., *The Principle of Relativity* [New York: Dover, 1952], 113）中这样定义广义相对性原理：“物理学定律必须具有这样的性质：它们适用于作任何种类运动的参照系。”换句话说，这些定律必须对所有观测者（所有参照系）保持相同的形式，而这意味着它们必须用张量形式来表述。
13. Albert Einstein, *Ideas and Opinions*（1954; New York: Three Rivers Press, 1982）, 309。
14. *任何坐标变换都可以吗？* 有许多令人困惑之处是爱因斯坦不得不设法理清的。例如，那些不改变点的位置的变换，比如从笛卡儿坐标到极坐标，该怎么看？爱因斯坦意识到了这个问题，这正是他为广义协变性的想法而苦苦挣扎的原因，我们将会看到。见 John D. Norton, “General Covariance and the Foundations of General Relativity: Eight Decades of Dispute,” *Reports on Progress in Physics* 56 (1993): 791–858, esp. 833–34。此外，在流形上，这些变换是针对点求出的，而不是针对整个空间。关于这一微妙之处的分析，见 Norton, “General Covariance,” 804；以及 John Earman and Clark Glymour, “Lost in the Tensors: Einstein’s Struggle with Covariance Principles 1912–1916,” *Studies in History and Philosophy of Science* 9 (1978): 4, 251–78, esp. 254。
15. Einstein, *Ideas and Opinions*, 288。
16. 我用了“极小化”一词，但严格来说我的意思是把这个积分“取极值”，因为路径在类时测地线（time-like geodesic）上是最长的（由于时间膨胀，而不是空间收缩）；不过这里我们无需为此操心。
17. *“燃起来了”*：爱因斯坦的回忆，转引自 Straumann, “Einstein’s ‘Zürich Notebook,’” 490。
18. *F<sup>μν</sup> 是张量吗*：是的，因为（参见第 11 章）它这样变换：
$F^{\mu'v'}=A_{\sigma}^{\mu'}A_{\lambda}^{v'}F^{\sigma\lambda},$
其中在闵可夫斯基时空中，变换矩阵 *A* 表示洛伦兹变换（LT）。但在洛伦兹变换下，由于时间与空间坐标交织在一起，那些分量是空间和时间的函数的向量（例如速度，或电场向量与磁场向量），其变换并不像我们在第 11 章看到的那么简单。
<span class="origpage" title="英文原版第 393 页">393</span>

19. 不同作者偏爱其中一个名字，不过公道还是有的，因为在微分几何中有一个对偶张量，如方框中那样用星号表示，所以两个名字都用得上。
20. 这种对称性在物理上由考虑物质的一个元素来保证，在数学上则由考虑降指标时的情形来保证：$g_{\mu\nu}T_{\sigma}^{\mu}=T_{v\sigma}$，而 $g_{\mu\nu}T_{\sigma}^{\mu}=T_{\sigma v}$。但这两个方程的左端相同，因为 *g*<sub>μν</sub> = *g*<sub>νμ</sub>，这意味着 *T*<sub>νσ</sub> = *T*<sub>σν</sub>。
21. *局域定律*：爱因斯坦的质能守恒定律是 *T* <sup>μν</sup><sub>;ν</sub> = 0，但这是一条局域守恒定律。整体引力能量守恒的概念至今仍格外棘手，而即便是引力场能量密度这样的局域概念，也难以在物理上定义。这是因为 *T* <sup>μν</sup><sub>;ν</sub> = 0 是一个数学类比；我们将在下一章看到更多。
在地球上，“局域”区域必须小到测不出表面的曲率——否则引力的平方反比定律表明引力处处不同，我在<a href="#fig-12-1">图 12.1</a> 中使用的伽利略常量重力加速度 32 英尺/秒/秒就不再适用。在太阳系中，“局域”区域可以很大，只要来自太阳和行星的引力场大致恒定。在更远的地方，“局域”可以覆盖广袤的区域——也许是两颗恒星之间距离的一半。（这些估计我要归功于伯特兰·罗素精彩的 *The ABC of Relativity*，初版于 1925 年，节录于 *The World Treasury of Physics and Mathematics*, ed. Timothy Ferris [Boston: Little, Brown, 1991], 194–202。）
关于爱因斯坦在能量守恒与协变性上的挣扎的详细讨论，见 Straumann, “Einstein’s ‘Zürich Notebook’”；Earman and Glymour, “Lost in the Tensors”；以及 Galina Weinstein, “Why Did Einstein Reject the November Tensor in 1912–1913, Only to Come Back to It in November 1915?,” *Studies in History and Philosophy of Modern Physics* 62 (2018): 98–122。“十一月张量”就是里奇张量。
关于爱因斯坦试图解释《纲要》（*Entwurf*）缺乏广义协变性、以及这一问题直至今日的哲学意义的详细讨论，见 John D. Norton, “The Hole Argument,” *Stanford Encyclopedia of Philosophy*, online, updated 2019；<https://plato.stanford.edu/entries/spacetime-holearg/>。
22. *格罗斯曼谈张量带来的麻烦*：转引自 Earman and Glymour, “Lost in the Tensors,” 258–59。*爱因斯坦的“沉重心情”*：转引自 Straumann, “Einstein’s ‘Zürich Notebook,’” 489。
<span class="origpage" title="英文原版第 394 页">394</span>

23. *爱因斯坦致埃伦费斯特*，document 173, in *Collected Papers of Albert Einstein*, vol. 8, ed. Robert Schulman, A, J. Knox, Michel Janssen, and Jósef Illy；English translation by Ann M. Hentschel（Princeton, NJ: Princeton University Press, 1998）；承蒙该出版社与爱因斯坦文献项目提供在线版本，<https://einsteinpapers.press.princeton.edu/vol8-trans/195>。爱因斯坦致贝索，转引自 Goodstein, *Einstein’s Italian Mathematicians*, 105–6。关于爱因斯坦的同事为何否定《纲要》（*Entwurf*），另见 Earman and Glymour, “Lost in the Tensors,” 264ff.。
24. 转引自 Earman and Glymour, “Lost in the Tensors,” 260。
25. 斯特恩转引自 Hanoch Gutfreund, “Otto Stern—with Einstein in Prague and in Zürich,” Springer Link, June 20, 2021, open access, <https://link.springer.com/chapter/10.1007/978-3-030-63963-1_6?error=cookies_not_supported&code=bb7fb68a-a41c-4c71-ace0-33a64d5f7756>。
26. *米列娃的伤心信*：转引自 Roger Highfield and Paul Carter, *The Private Lives of Albert Einstein*（London: Faber and Faber, 1993）, 128。爱因斯坦对米列娃尖刻的要求，在 1914 年 7 月的信件中有令人痛心的罗列，例如 document 22, *Collected Papers of Albert Einstein*, vol. 8, <https://einstein> papers.press.princeton.edu/vol8-trans/60。
27. *告文明世界书*：Constance Reid, *Hilbert*（Berlin: Springer-Verlag, 1970）, 137–38。
28. 爱因斯坦致列维-奇维塔，document 60, *Collected Papers of Albert Einstein*, vol. 8, <https://einsteinpapers.press.princeton.edu/vol8-trans/99>。
29. David E. Rowe, “Einstein Meets Hilbert: At the Crossroads of Physics and Mathematics,” *Physics in Perspective* 3 (2001): 379–424, esp. 393–96。
30. 正如我们在第 11 章看到的，齐次坐标变换使诸如 ***a*** ∙ ***b*** = 0 这样的方程保持不变。同样地，爱因斯坦在他 1916 年的综述中说（*The Foundation of the General Theory of Relativity*, 1916，英译见 H. A. Lorentz et al., *The Principle of Relativity* [New York: Dover, 1952], 121）：“如果一条自然定律是把一个张量的全部分量都等于零来表达的，那么它就是广义协变的。”相关讨论见 Norton, “General Covariance,” 833–34。Norton 指出（834），度规的协变性比张量分析的通常变换更具限制性。
<span class="origpage" title="英文原版第 395 页">395</span>

31. 爱因斯坦 1915 年 11 月写给家人的信见 *Collected Papers of Albert Einstein*, vol. 8（周围都是写给希尔伯特的信！），例如 documents 142–43, <https://einsteinpapers.press.princeton.edu/vol8-trans/174,> document 150, <https://einsteinpapers.press.princeton.edu/vol8-trans/177>。1915 年 11 月 5 日，马里奇表示她本人愿意让爱因斯坦多见见他们的孩子们，document 135, <https://einsteinpapers.press.princeton.edu/vol8-trans/169>。爱因斯坦始终未能与小儿子爱德华建立良好的关系，爱德华才华横溢却极为敏感，后来患上精神分裂症。爱因斯坦负担了他的照料费用，但情感上的重担落在马里奇身上。
32. *爱因斯坦致友人埃伦费斯特*，转引自 Banesh Hoffmann, *Einstein*（Frogmore: Paladin, 1975）, 125；*爱因斯坦致希尔伯特*，1915 年 11 月 18 日，*Collected Papers of Albert Einstein*, vol. 8, document 148, <https://einsteinpapers.press.princeton.edu/vol8-trans/176>；*爱因斯坦致贝索*，1915 年 11 月 17 日，in *Collected Papers of Albert Einstein*, vol. 8, document 147, <https://einsteinpapers.press.princeton.edu/vol8-trans/176>。注意，爱因斯坦此时还没有完整的场方程，但他已经有了正确的真空方程，而那正是他计算水星测地线路径所需要的；结果与牛顿椭圆有偏离，这给了他近日点运动的差异。推导见广义相对论教材，如 Ray d’Inverno, *Introducing Einstein’s Relativity*（Oxford: Clarendon Press, 1992）, 195–98（其中 198 页比较了近日点进动的观测值与用广义相对论算出的值）。
<span class="origpage" title="英文原版第 396 页">396</span>

33. *11 月 20 日论文中没有显式方程*：Leo Corry 及其同事 Jürgen Renn（Max Planck Institute for the History of Science）和 John Stachel（Center for Einstein Studies, Boston University）在 “Belated Decision in the Hilbert-Einstein Priority Dispute,” *Science* 278 (1997): 1270–73 中比对了校样与发表的版本。更多文献列在下面。*希尔伯特 11 月 20 日校样并非广义协变*：见，例如，Vladimir P. Vizgin, “On the Discovery of the Gravitational Field Equations by Einstein and Hilbert: New Materials,” *Physics-Uspekhi* 44, no. 12 (2001): 1289；Gutfreund and Renn, *Road to Relativity*, 33；Jürgen Renn and John Stachel, “Hilbert’s Foundation of Physics: From a Theory of Everything to a Constituent of General Relativity,” in *The Genesis of General Relativity*, ed. Jürgen Renn（Dordrecht: Springer, 2007）, 4:858–59。
34. 沿袭米的做法，希尔伯特采用了一条与爱因斯坦截然不同的路径——一种优雅的拉格朗日（变分）方法。但爱因斯坦此前也已尝试过这种方法，见他 1914 年的论文，希尔伯特读过该文。爱因斯坦在他 1916 年的综述论文中也列入了他用于讨论守恒律的变分方法，用的是哈密顿量而非拉格朗日量。关于这两种方法的讨论见 Rowe, “Einstein Meets Hilbert,” 414–15。
35. *爱因斯坦与希尔伯特的优先权之争，以及两人不同的路径*：Tilman Sauer, “Einstein Equations and Hilbert Action: What Is Missing on Page 8 of the Proofs for Hilbert’s First Communication on the Foundations of Physics?,” *Archives for History of Exact Sciences* 59 (2005): 577–90。Vizgin, “On the Discovery of the Gravitational Field Equations,” 1283–98。Leo Corry, Jürgen Renn, and John Stachel, “Belated Decision,” 1270–73。F. Winterberg, “On ‘Belated Decision in the Hilbert-Einstein Priority Dispute,’ Published by L. Corry, J. Renn and J. Stachel,” *Z. Naturforsch* 59a (2004): 715–19。John Earman and Clark Glymour, “Einstein and Hilbert: Two Months in the History of General Relativity,” *Archives for History of Exact Sciences* 19 (1978): 291–308。Renn and Stachel, “Hilbert’s Foundation of Physics,” 4:857–973（关于爱因斯坦对自己推导的说明，见，例如，他写给索末菲（document 153）和埃伦费斯特（document 185）的信，in *Collected Papers of Albert Einstein*, vol. 8）。David E. Rowe, “Einstein Meets Hilbert,” 379–424。Ivan T. Todorov, “Einstein and Hilbert: The Creation of General Relativity,” 预印本线上见 arXiv:physics/0504179v1, April 25, 2005。Galina Weinstein, “Did Einstein ‘Nostrify’ Hilbert’s Final Form of the Field Equations?,” 线上见 *Physics ArXiv:1412.1816*, December 11, 2014。还有更多！注意，网上关于优先权问题有大量错误信息。例如，V. A. Petrov（“Einstein, Hilbert and Equations of Gravitation,” 博客，<https://arxiv.org/pdf/gr-qc/0507136.pdf>）声称，爱因斯坦不可能在他说过的那个时间点导出正确的水星近日点进动，因为他当时还没有最终的方程；他暗示爱因斯坦必定看过希尔伯特的工作（关于迹项），但近日点方程只需要真空解，那里没有迹项；Petrov 还暗示希尔伯特导出了比安基恒等式，而这掩盖了一个事实：希尔伯特并未充分理解这些恒等式在能量守恒中所起的作用（我将在下一章讨论）。Petrov 引用了 Winterberg（上文），后者又引用了 C. J. Bjerknes（Petrov 也引用了此人），但 Bjerknes 并不是一位可信的学者：见，例如，John Stachel, “Anti-Einstein Sentiment Surfaces Again,” *Physics World* 16, no. 4 (2003): 40。
36. Rowe 在 “Einstein Meets Hilbert,” 408 中对此有很好的讨论；他确实指出（418），希尔伯特本应更改发表论文的投稿日期，尽管这在当时是标准做法。我要补充的是，今天的论文发表时会同时标注原始投稿日期*和*修订日期。
37. Renn and Stachel, “Hilbert’s Foundation of Physics” 详细展示了希尔伯特在读过爱因斯坦的论文后对自己已发表的论文作了哪些修改，并指出他起初曾试图把爱因斯坦的一些关键贡献说成是自己的（见，例如，920–21）。
<span class="origpage" title="英文原版第 397 页">397</span>

38. 希尔伯特转引自 Reid, *Hilbert*, 142。爱因斯坦那封令人唏嘘的和解信见，例如，Vizgin, “On the Discovery of the Gravitational Field Equations,” 1289。
39. 我们前面看到，在闵可夫斯基时空中，标量积（从而散度之和）对 *t* 分量有一个符号变化。但这里的要点在于，这些都是*定义*，所以只消盯住散度各项中指标的模式。
40. 这是因为在一点上总可以找到一个局域惯性（“自由下落”）参照系，在其中狭义相对论成立（且协变导数中用到的埃尔温·克里斯托费尔符号为零）。按照张量分析的规则，张量方程的形式在任何参照系中都是不变的——只要你用（无挠的）协变导数而不是偏导数，以顾及时空的曲率。这条规则还假定我们把平直的闵可夫斯基度规换成了一般的弯曲度规。
41. 不过，在“非相对论”单位下，*k* = 8π*G*/*c*<sup>4</sup>，其中 *G* 是牛顿引力定律中的比例常数；这凸显了一个事实：爱因斯坦是通过与牛顿理论类比而导出他的方程的，并确保了它们在地球这样的弱引力场中退化为牛顿理论。
42. 这两个方程等价，因为对爱因斯坦原来的方程缩并指标，并注意到 $g_{\mu}^{\mu}=4$（由 *g*<sub>**μν**</sub> 与 *g*<sup>μν</sup> 互为逆矩阵的定义，正如我们在第 11 章所见），你会发现 $R_{\mu}^{\mu}=-kT_{\mu}^{\mu}\equiv R=-kT.$（注意，爱因斯坦在原来的方程中系数其实是 −*k*，但既然这是常数，我就把负号吸收进我对 *k* 的定义之中，以符合今天通常的写法。另外，爱因斯坦在最终方程里把左端（里奇张量）用埃尔温·克里斯托费尔符号完整写了出来，但他此前已把这个表达式定义为 *R*μν。）
43. 爱因斯坦早先的方程 *R*μν = *kT*μν 与这两个最终形式之间的差别，关键在于标量 *T* 或希尔伯特等价的标量 *R*。（这些标量称为“迹”。）究竟是爱因斯坦还是希尔伯特先认识到这一点，正是“优先权之争”的核心，因为它在希尔伯特 11 月 20 日的拉格朗日表述中只是隐含的。由于爱因斯坦与希尔伯特交换过论文，他们肯定相互影响过，但很可能各自独立地迈出了这最后一步，因为他们走的是不同的路。今天，希尔伯特的方法被广泛使用，与拉格朗日量相关的所谓爱因斯坦–希尔伯特作用量就是为了纪念他。
<span class="origpage" title="英文原版第 398 页">398</span>

44. *近期对爱因斯坦理论的检验*：见，例如，Pierre Touboul et al., “MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle,” *Physical Review Letters* 129, no. 21102（September 14, 2022）；Ignazio Ciufolini et al., “An Improved Test of the General Relativistic Effect of Frame-Dragging Using the LARES and LAGEOS Satellites,” *European Physical Journal C* 79, article no. 872 (2019)；Gemma Conroy, “Albert Einstein Was Right (Again): Astronomers Have Detected Light from Behind a Supermassive Black Hole,” ABC News, July 29, 2021, <https://www.abc.net.au/news/science/2021-07-29/albert-einstein-astronomers-detect-light-behind-black-hole/100333436>；Geraint Lewis, “Astronomers See Ancient Galaxies Flickering in Slow Motion Due to Expanding Space”（检验爱因斯坦关于时间变慢的预言）, *The Conversation*, July 4, 2023；Jet Propulsion Laboratory blog（August 24, 2022）, “NASA Scientists Help Probe Dark Energy by Testing Gravity”——他们发现爱因斯坦的方程依然站得住。（波恩大学的 Pavel Kroupa 不以为然，见 “Dark Matter Doesn’t Exist,” *IAE News*, July 12, 2022。但一项新研究用广义相对论对引力透镜的预言来绘制暗物质图：Robert Lea, “New Dark Matter Map Created with ‘Cosmic Fossil’ Shows Einstein Was Right (Again),” *Space* [April 18, 2023]。）*关于黑洞的进动*：Brandon Specktor, “One of the Most Extreme Black Hole Collisions in the Universe Just Proved Einstein Right,” *LiveScience*, October 13, 2022。*关于参考系拖曳*：见，例如，Charles Q. Choi, “Spacetime Is Swirling around a Dead Star, Proving Einstein Right Again,” *Space.com*, January 31, 2020。还有很多很多！
关于日食考察（以及光在黑洞附近弯曲）的通俗概述，见我的文章 “A ‘Revolution in Science’ 100 Years Later,” *Cosmos Magazine* 83 (2019): 29–35。注意，早先用牛顿理论预言光线弯曲的是 Johann Soldner，他得到的结果只有广义相对论的一半。还要注意，1980 年曾出现对考察队领队有偏见的指控，但这些指控已被推翻，1919 年的结果得到了确认。
关于引力磁性的简短概述，见我的文章 “The Amazing Concept of Gravito-electromagnetism,” *Cosmos Magazine* 84（September 2019）: 61–63。删节版见 <https://cosmosmagazine.com/science/introducing-the-amazing-concept-of-gravito-electromagnetism/>。
我自己的研究针对的是正文中提到的第二个类比。见，例如，C. B. G. McIntosh, R. Arianrhod, S. T. Wade, and C. Hoenselaers, “Electric and Magnetic Weyl Tensors: Classification and Analysis,” *Classical and Quantum Gravity* 11 (1994): 1555–64；以及 R. Arianrhod, A. W-C. Lun, C. B. G. McIntosh, and Z. Perjés, “Magnetic Curvatures,” *Classical and Quantum Gravity* 11 (1994): 2331–35。在某些应用中，特别是暗能量，会在方程中加上爱因斯坦的引力常数。
<span class="origpage" title="英文原版第 399 页">399</span>

45. Einstein, *Ideas and Opinions*, 289–90。
46. 爱因斯坦那页封面在英译本中缺失，但最近被 Alicia Dickenstein 找到，她在 “About the Cover: A Hidden Praise of Mathematics,” *Bulletin of the American Mathematical Society*, n.s., 46, no. 1（January 2009）: 125–29 中给出了爱因斯坦完整的致谢。
47. 列维-奇维塔转引自 Goodstein, *Einstein’s Italian Mathematicians*, 151, 155。
## 第 13 章
1. *克莱因与希尔伯特谈诺特小姐*：转引自 Yvette Kosmann-Schwarzbach, translated by Bertram E. Schwarzbach, *The Noether Theorems: Invariance and Conservation Laws in the Twentieth Century*（New York: Springer, 2011）, 45, 66。
2. John Norton 在他 1993 年的论文 “General Covariance and the Foundations of General Relativity” 中，不仅精彩地讲述了爱因斯坦的挣扎，还讲述了其他人如何回应或重新解释他的协变性原理、相对性原理和等效原理。他用二十世纪教科书叙述的演变来说明这一点，并指出至今仍有争议或混乱。当然，正如我在上一章末尾所表明的，迄今的物理观测已经证实这些方程非常出色，无论其基础如何！
3. 诺特论文的英译见 Kosmann-Schwarzbach, *Noether Theorems*, 3–22。
4. 在像地球上这样弱的引力场中，“动量”的时间分量确实等于粒子的静止质量、引力势能和动能之和。见，例如，Bernard Schutz, *A First Course in General Relativity*（Cambridge: Cambridge University Press, 1985）, 190。
<span class="origpage" title="英文原版第 400 页">400</span>

5. 要看出诺特结果的精髓（她在 1918 年的定理中作了全面推广），让我们回到前面谈过的那些平移。取 *a* 的所有值，从 *x* 到 *x* + *a* 的这些平移构成一个群（就像<a href="#fig-9-3">图 9.3</a> 中的洛伦兹变换）。与不变性相关的群称为“对称群”。这里的“对称性”就是由 *V* 与 *x* 无关这一事实所表达的不变性。如果同样的对称性在每个方向上都成立，那么 ***p*** 的所有分量都守恒，我们就有了熟悉的动量守恒定律。诺特所证明的是：经典力学*和*狭义相对论的对称群是有限的，而广义相对论中的对称群是无限的，因为广义相对论允许一切可能的坐标，从而允许一切可能的点变换。这意味着引力场的能量–动量守恒定律确实不同于力学和狭义相对论中通常的守恒定律。技术细节见 Kosmann-Schwarzbach, *Noether Theorems*, 56–64。
6. *关于把物理定律写成散度*：Peter Gabriel Bergmann, *Introduction to the Theory of Relativity*（New York: Dover, 1976）, 194–97。*关于诺特定理中的散度*：Kosmann-Schwarzbach, *Noether Theorems*, 例如 6–10。
7. *关于在广义相对论中定义能量*：Robert M. Wald, *General Relativity*（Chicago: University of Chicago Press, 1984）, 84, 286，关于诺特定理见 457；S. W. Hawking and G. F. R. Ellis, *The Large-Scale Structure of Space-time*（1973; Cambridge: Cambridge University Press, 1991）, 61–62, 73–74, 88–96。*关于诺特定理*：Kosmann-Schwarzbach, *Noether Theorems*；更简单的概述见 David E. Rowe, “On Emmy Noether’s Role in the Relativity Revolution,” *Mathematical Intelligencer* 41, no. 2 (2019): 65–72。
8. 爱因斯坦坚持认为，真正广义的相对论应当允许任何坐标——这就是他的协变性原理——但我们看到，这允许了代表同一点的坐标。这意味着我们可以得到实际上表示同一时空的不同形式的度规——正如我们看到的圆的方程用笛卡儿坐标和极坐标写出的情形。为缓解这一局面，四个能量守恒方程（或我们下一节将遇到的缩并的比安基恒等式）对坐标的选择施加了额外约束（见尾注 10）。
9. 在第 12 章中，*T***μν** 和 *T*μν 具有相同的内容，因为指标是用闵可夫斯基度规提升的。在广义相对论中，张量在提升指标时会从度规中多出一些项，但由于这在张量方程两边都发生，方程的实质内容不变。
10. 这四个缩并的比安基恒等式给出了关于里奇张量的额外信息，这意味着十个爱因斯坦方程中只有六个是独立的。这带来了任意选择四个坐标（参照系）的自由，确保每个观测者都推出相同的物理学定律。
<span class="origpage" title="英文原版第 401 页">401</span>

11. T. Levi-Civita (1917), translated by S. Antoci and A. Loinger, “On the Analystic Expression That Must Be Given to the Gravitational Tensor in Einstein’s Theory,” <https://arxiv.org/pdf/physics/9906004.pdf>。*关于希尔伯特经由变分方法所作的曲折推导*，见 David E. Rowe, “Einstein’s Gravitational Field Equations and the Bianchi Identities,” *Mathematical Intelligencer* 24, no. 4 (2002): 57–66 的 p. 59；Ivan T. Todorov, “Einstein and Hilbert: The Creation of General Relativity,” arXiv:physics/0504179v1；David E. Rowe, “Emmy Noether on Energy Conservation in General Relativity,” December 4, 2019, 预印本线上见 <https://arxiv.org/pdf/1912.03269.pdf,> 21n32；Carlo Cattani and Michelangelo De Maria, “Conservation Laws and Gravitational Waves,” in *The Attraction of Gravitation: New Studies in the History of General Relativity*, ed. John Earman, Michel Janssen, and John D. Norton（Boston: Birkhäuser, 1993）, 67。
12. 那将意味着标量 *R* 和 *T* 在整个宇宙中都是常数。这些标量反映的是曲率和质能，所以 *T* 在真空中应当与在物质中不同。
13. *比安基恒等式*：David E. Rowe, “Einstein’s Gravitational Field Equations and the Bianchi Identities,” *Mathematical Intelligencer* 24, no. 4 (2002): 57–66；*斯特勒伊克与斯豪滕*：Rowe, “Einstein’s Gravitational Field Equations,” 66；Kosmann-Schwarzbach, *Noether Theorems*, 43。
14. *关于斯特勒伊克*：本段及以下各段，我受惠于 David E. Rowe, “Interview with Dirk Jan Struik,” *Mathematical Intelligencer* 11, no. 1 (1989): 14–26。这篇访谈也讨论了斯特勒伊克的马克思主义思想如何使他在麦卡锡主义下遭受苦难。斯特勒伊克显然非同寻常，而同样非同寻常的是，他活到了 106 岁（他于 2000 年去世）。
15. 斯特勒伊克转引自 Rowe, “Interview with Struik,” 19。爱因斯坦的引语见 Constance Reid, *Hilbert*（Berlin: Springer-Verlag, 1970）, 142。
16. 转引自 Reid, *Hilbert*, 143。
17. *爱因斯坦支持诺特*：转引自 Kosmann-Schwarzbach, *Noether Theorems*, 72。*魏玛*：Rowe, “Noether’s Role in Relativity,” 66。
18. *现代代数之母*：Norbert Schappacher and Cordula Tollmien, “Emmy Noether, Hermann Weyl, and the Göttingen Academy: A Marginal Note,” *Historia Mathematica* 43 (2016): 194–97。
19. 斯特勒伊克转引自 Rowe, “Interview with Struik,” 16。
20. *斯特勒伊克*：Rowe, “Interview with Struik,” 17。*霍奇*：转引自 Judith Goodstein, *Einstein’s Italian Mathematicians*（Providence, RI: American Mathematical Society, 2018）, 165。
<span class="origpage" title="英文原版第 402 页">402</span>

21. *1928 年大会与希尔伯特激动人心的演讲*：Reid, *Hilbert*, 188。
22. 见，例如，澳大利亚数学会的 *Gazette* 49，第 1 期（Ole Warnaar 的主席专栏）和第 2 期（Letters，来自 Aerwm Pulemotov）。
23. 爱因斯坦与嘉当的引语分别出自 1929 年 12 月 8 日和 1930 年 2 月 17 日的通信，见 *Elie Cartan–Albert Einstein: Letters on Absolute Parallelism 1929–1930*, ed. Robert Debever（Princeton, NJ: Princeton University Press, 1979）。
24. *爱因斯坦致嘉当*：in *Elie Cartan-Albert Einstein*, ed. Debever, 203；*爱因斯坦致格罗斯曼夫人*：in Banesh Hoffmann, *Einstein*（Frogmore: Paladin, 1975, 36。
## 结语
1. 粒子对撞机让物理学家得以建立描述物质及其与各种力相互作用的标准模型，CERN 指出，它除了科学收益之外还带来了社会效益：<https://home.cern/news/news/cern/society-benefits-investing-particle-physics>。不过，前粒子物理学家 Sabine Hossenfelder 是对科学收益持怀疑态度者之一；见，例如，她的博客文章 <https://backreaction.blogspot.com/2022/04/did-w-boson-just-break-standard-model.html>。同样，*Quora* 上的这篇帖子提出，大型强子对撞机的阴性结果（即未发现新粒子的结果）对科学至关重要，但这是在排除流行理论的意义上：<https://www.quora.com/Was-building-the-Large-Hadron-Collider-worth-it-Did-they-discover-anything-from-it>。另见，例如，Nick Scott, “CERN’s Grand Ambitions: Are Particle Accelerators Worth It?” *Varsity*（January 26, 2021）, <https://www.varsity.co.uk/science/20486>；Tom Hartsfield, “Please, Don’t Build Another Large Hadron Collider,” *Big Think*（June 6, 2022）, <https://bigthink.com/hard-science/large-hadron-collider-economics/>。
2. 实际上，狄拉克用的是 *E* = *mc*<sup>2</sup> 的*平方*，它给出正解和负解：正解是爱因斯坦关于普通物质的方程；负解 *E* = −*mc*<sup>2</sup> 则指反物质。简要介绍见狄拉克 1933 年诺贝尔奖致辞的节录，in *The World Treasury of Physics, Astronomy and Mathematics*, ed. Timothy Ferris（Boston: Little, Brown, 1993）, 80–85。现代分析见 Luciano Maiani and Omar Benhar, *Relativistic Quantum Mechanics*（Boca Raton, FL: CRC Press, 2016）, 113–16。
3. 见 Bertha Swirles, “The Relativistic Interaction of Two Electrons in the Self-Consistent Field Method,” *Proceedings of the Royal Society A* 157, no. 892（December 2, 1936）: 680–96。
<span class="origpage" title="英文原版第 403 页">403</span>

4. *计算数学（尤其是数值线性代数 NLA）中的张量*：见，例如，Lek-Heng Lim, “Tensors in Computation,” *Acta Numerica* (2021): 555–764, DOI:10.1017/S09622 492921000076。
5. 爱因斯坦致 Heinrich Zangger，document 152, *Collected Papers of Albert Einstein*, <https://einsteinpapers.press.princeton.edu/vol8-trans/179>。这封信也显示出爱因斯坦对前妻的怨恨，认为她似乎阻碍了他与儿子汉斯·阿尔伯特修复关系。
