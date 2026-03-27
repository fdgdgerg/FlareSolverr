from bs4 import BeautifulSoup

test = """[<span class="tl" id="tl87220">
<!-- / tracklist tools menu -->
<span style="font-size:8pt"><b>Disc 1</b></span>
<br/><br/>
<table border="0" cellpadding="1" cellspacing="0" class="role">
<tbody><tr>
<td></td>
<td colspan="3">
<span class="label" style="font-size:8pt; padding-left:5px; margin-top:18px;">A-Side</span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">01</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

大空を駆ける勇者</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label"> </span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">
<span class="label" style="color:#506070">01</span> 
&lt;主題歌&gt; 燃えろ!仮面ライダー(TV用唄入り)</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time label"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">02</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

ネオショッカーのテーマ</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">03</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

戦え!スカイライダー</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">04</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

宇宙からの侵略</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">05</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

強化ネオショッカー大進撃</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">06</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

8人ライダーヒットメドレー</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">07</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

勝利の8人ライダー!</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr>
<td></td>
<td colspan="3">
<span style="float:right; margin:1px;"><span class="smallfont" style="color: #606978"> </span> <span class="time"></span></span>
</td></tr>
<tr>
<td></td>
<td colspan="3">
<span class="label" style="font-size:8pt; padding-left:5px; margin-top:18px;">B-Side</span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">08</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

惑星開発用改造人間第1号</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label"> </span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">
<span class="label" style="color:#506070">01</span> 
&lt;主題歌&gt; 仮面ライダースーパー1(TV用唄入り)</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time label"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">09</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

技は赤心少林拳</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">10</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

激突!スーパー1対テラーマクロ</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">11</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

ジンドグマのテーマ</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">12</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

大宇宙への旅立ち</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">13</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

時空破断システム</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">14</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

ドラゴン・ロード</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr>
</tbody></table>
<span style="float: right; margin: 1px;">
<span class="smallfont" style="color: #606978"> </span>
<span class="time"></span>
</span>
<br style="clear: both"/>
<h4 style="font-weight: normal; clear:both"><span class="label">

 </span>
</h4></span>, <span class="tl" id="tl143395" style="display: none">
<!-- / tracklist tools menu -->
<span style="font-size:8pt"><b>Disc 1</b></span>
<br/><br/>
<table border="0" cellpadding="1" cellspacing="0" class="role">
<tbody><tr>
<td></td>
<td colspan="3">
<span class="label" style="font-size:8pt; padding-left:5px; margin-top:18px;">A-Side</span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">01</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Oozora o Kakeru Yuusha</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">02</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Neo Shocker no Theme</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">03</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Tatakae! Skyrider</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">04</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Uchuu Kara no Shinryaku</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">05</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Kyouka Neo Shocker Daishingeki</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">06</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

8-nin Rider Hit Medley</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">07</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Shouri no 8-nin Rider!</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr>
<td></td>
<td colspan="3">
<span style="float:right; margin:1px;"><span class="smallfont" style="color: #606978"> </span> <span class="time"></span></span>
</td></tr>
<tr>
<td></td>
<td colspan="3">
<span class="label" style="font-size:8pt; padding-left:5px; margin-top:18px;">B-Side</span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">08</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Wakusei Kaihatsuyou Cyborg Dai-1-gou</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">09</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Waza wa Sekishin Shourinken</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">10</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Gekitotsu! Super 1 Tai Terror Macro</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">11</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Jin Dogma no Theme</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">12</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Daiuchuu e no Tabidachi</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">13</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Jikuu Hadan System</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">14</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Dragon Road</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr>
</tbody></table>
<span style="float: right; margin: 1px;">
<span class="smallfont" style="color: #606978"> </span>
<span class="time"></span>
</span>
<br style="clear: both"/>
<h4 style="font-weight: normal; clear:both"><span class="label">
Transliterated by <b>anisonfan</b><br/>
 </span>
</h4></span>]"""

soup_sections = """ [<div><h3 style="float: left">Tracklist <a class="collapsible_section" href="#" rel="tracklist"><img src="/db/img/collapse_close.png"/></a></h3>
<ul class="tabnav" id="tlnav" style="margin-left: 10px"><li class="active"><a class="smallfont" href="#" rel="tl87220">Japanese</a></li><li><a class="smallfont" href="#" rel="tl143395">Romaji</a></li></ul>
</div>, <div style="background-color: #2F364F; clear: both">
<b class="rtop"><b></b></b>
<div id="tracklist" style="padding: 6px 10px 10px 10px"><span class="tl" id="tl87220">
<!-- / tracklist tools menu -->
<span style="font-size:8pt"><b>Disc 1</b></span>
<br/><br/>
<table border="0" cellpadding="1" cellspacing="0" class="role">
<tbody><tr>
<td></td>
<td colspan="3">
<span class="label" style="font-size:8pt; padding-left:5px; margin-top:18px;">A-Side</span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">01</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

大空を駆ける勇者</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label"> </span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">
<span class="label" style="color:#506070">01</span> 
&lt;主題歌&gt; 燃えろ!仮面ライダー(TV用唄入り)</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time label"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">02</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

ネオショッカーのテーマ</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">03</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

戦え!スカイライダー</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">04</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

宇宙からの侵略</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">05</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

強化ネオショッカー大進撃</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">06</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

8人ライダーヒットメドレー</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">07</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

勝利の8人ライダー!</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr>
<td></td>
<td colspan="3">
<span style="float:right; margin:1px;"><span class="smallfont" style="color: #606978"> </span> <span class="time"></span></span>
</td></tr>
<tr>
<td></td>
<td colspan="3">
<span class="label" style="font-size:8pt; padding-left:5px; margin-top:18px;">B-Side</span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">08</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

惑星開発用改造人間第1号</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label"> </span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">
<span class="label" style="color:#506070">01</span> 
&lt;主題歌&gt; 仮面ライダースーパー1(TV用唄入り)</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time label"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">09</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

技は赤心少林拳</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">10</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

激突!スーパー1対テラーマクロ</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">11</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

ジンドグマのテーマ</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">12</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

大宇宙への旅立ち</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">13</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

時空破断システム</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">14</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

ドラゴン・ロード</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr>
</tbody></table>
<span style="float: right; margin: 1px;">
<span class="smallfont" style="color: #606978"> </span>
<span class="time"></span>
</span>
<br style="clear: both"/>
<h4 style="font-weight: normal; clear:both"><span class="label">

 </span>
</h4></span>
<span class="tl" id="tl143395" style="display: none">
<!-- / tracklist tools menu -->
<span style="font-size:8pt"><b>Disc 1</b></span>
<br/><br/>
<table border="0" cellpadding="1" cellspacing="0" class="role">
<tbody><tr>
<td></td>
<td colspan="3">
<span class="label" style="font-size:8pt; padding-left:5px; margin-top:18px;">A-Side</span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">01</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Oozora o Kakeru Yuusha</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">02</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Neo Shocker no Theme</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">03</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Tatakae! Skyrider</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">04</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Uchuu Kara no Shinryaku</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">05</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Kyouka Neo Shocker Daishingeki</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">06</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

8-nin Rider Hit Medley</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">07</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Shouri no 8-nin Rider!</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr>
<td></td>
<td colspan="3">
<span style="float:right; margin:1px;"><span class="smallfont" style="color: #606978"> </span> <span class="time"></span></span>
</td></tr>
<tr>
<td></td>
<td colspan="3">
<span class="label" style="font-size:8pt; padding-left:5px; margin-top:18px;">B-Side</span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">08</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Wakusei Kaihatsuyou Cyborg Dai-1-gou</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">09</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Waza wa Sekishin Shourinken</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">10</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Gekitotsu! Super 1 Tai Terror Macro</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">11</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Jin Dogma no Theme</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">12</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Daiuchuu e no Tabidachi</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">13</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Jikuu Hadan System</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr><tr class="rolebit">
<td class="smallfont" style="border-bottom: 1px solid #3C405C"><span class="label">14</span></td>
<td class="smallfont" colspan="2" style="border-bottom: 1px solid #3C405C; padding-left: 6px" width="100%">

Dragon Road</td>
<td align="right" class="smallfont" nowrap="nowrap" style="border-bottom: 1px solid #3C405C; padding-left: 6px"><span class="time"></span>
</td>
</tr>
</tbody></table>
<span style="float: right; margin: 1px;">
<span class="smallfont" style="color: #606978"> </span>
<span class="time"></span>
</span>
<br style="clear: both"/>
<h4 style="font-weight: normal; clear:both"><span class="label">
Transliterated by <b>anisonfan</b><br/>
 </span>
</h4></span>
</div>
<b class="rbot"><b></b></b>
</div>]"""


def _parse_tracklist(soup_tracklist):
    discs = []
    soup_sections = soup_tracklist.find_all("div", recursive=False)
    languages = [
        str(li.a.string) for li in soup_sections[0].ul.find_all("li", recursive=False)
    ]
    soup_tabs = soup_sections[1].div.find_all("span", recursive=False)
    tab_index = -1
    print("overall", soup_tabs)
    for soup_tab in soup_tabs:
        tab_index += 1
        tab_language = languages[tab_index]
        index = 0
        print("test")
        print(index, soup_tab)
        soup_cur = soup_tab.span
        while soup_cur:
            # in logged in mode, skip Edit span
            if soup_cur.b == None:
                soup_cur = soup_cur.find_next_sibling("span")
            disc_name = str(soup_cur.b.string)
            soup_tracklist = soup_cur.find_next_sibling("table")
            soup_cur = soup_tracklist.find_next_sibling("span")
            maybe_disc_length = soup_cur.find_all("span")[-1].string
            if maybe_disc_length:
                disc_length = str(maybe_disc_length)
            else:
                disc_length = "Unknown"
            if len(discs) < index + 1:
                discs.append({})
            discs[index]["name"] = disc_name
            discs[index]["disc_length"] = disc_length
            if "tracks" not in discs[index]:
                discs[index]["tracks"] = []
            track_no = -1
            for soup_track in soup_tracklist.find_all("tr", recursive=False):
                soup_cells = soup_track.find_all("td")
                if len(soup_cells) != 3:
                    continue
                track_no += 1
                track_name = str(soup_cells[1].string).strip()
                maybe_track_length = soup_cells[2].span.string
                if maybe_track_length:
                    track_length = str(maybe_track_length)
                else:
                    track_length = "Unknown"
                if len(discs[index]["tracks"]) < track_no + 1:
                    discs[index]["tracks"].append(
                        {"names": {}, "track_length": track_length}
                    )
                discs[index]["tracks"][track_no]["names"][tab_language] = track_name
            soup_cur = soup_cur.find_next_sibling("span")
            index += 1
    return discs


# soup = BeautifulSoup(test[1:-1], "html.parser")
# soup_tabs = soup.find_all("span", recursive=False)
# print(soup_tabs[0])
# print(soup_tabs[1])
discs = []
soup = BeautifulSoup(soup_sections, "html.parser")
soup_sections = soup.find_all("div", recursive=False)
languages = [
    str(li.a.string) for li in soup_sections[0].ul.find_all("li", recursive=False)
]
soup_tabs = soup_sections[1].div.find_all("span", recursive=False)
tab_index = -1
for soup_tab in soup_tabs:
    tab_index += 1
    tab_language = languages[tab_index]
    index = 0
    soup_cur = soup_tab.span
    while soup_cur:
        print(soup_cur)
        if soup_cur.b == None:
            soup_cur = soup_cur.find_next_sibling("span")
        else:
            print("b", soup_cur.b)
        disc_name = str(soup_cur.b.string)
        soup_tracklist = soup_cur.find_next_sibling("table")
        soup_cur = soup_tracklist.find_next_sibling("span")
        maybe_disc_length = soup_cur.find_all("span")[-1].string
        if maybe_disc_length:
            disc_length = str(maybe_disc_length)
        else:
            disc_length = "Unknown"
        if len(discs) < index + 1:
            discs.append({})
        discs[index]["name"] = disc_name
        discs[index]["disc_length"] = disc_length
        if "tracks" not in discs[index]:
            print("test")
            discs[index]["tracks"] = []
        track_no = -1
        print("soup_tracklist", soup_tracklist)
        print("soup_tracks", soup_tracklist.tbody.find_all("tr", recursive=False))
        for soup_track in soup_tracklist.tbody.find_all("tr", recursive=False):
            print("soup_track", soup_track)
            soup_cells = soup_track.find_all("td")
            if len(soup_cells) != 3:
                continue
            track_no += 1
            track_name = str(soup_cells[1].string).strip()
            maybe_track_length = soup_cells[2].span.string
            if maybe_track_length:
                track_length = str(maybe_track_length)
            else:
                track_length = "Unknown"
            if len(discs[index]["tracks"]) < track_no + 1:
                discs[index]["tracks"].append(
                    {"names": {}, "track_length": track_length}
                )
            discs[index]["tracks"][track_no]["names"][tab_language] = track_name
        soup_cur = soup_cur.find_next_sibling("span")
        index += 1
print("discs", discs)
# break
