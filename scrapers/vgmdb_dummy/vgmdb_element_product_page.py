from bs4 import BeautifulSoup

test = """<html dir="ltr" lang="en" xmlns="http://www.w3.org/1999/xhtml"><head>
<title>Hunter x Hunter - VGMdb</title>





<link href="https://vgmdb.net/product/3167" rel="canonical">


<meta name="keywords" content="Product, Release, VGM, Video Game Music, Game Music, Anime, Animation, OST, Soundtrack, Doujin, database, composer, arranger, discography">
<meta name="description" content="Animation  released on October 02, 2011.">
<meta property="og:title" content="Hunter x Hunter - VGMdb">
<meta property="og:type" content="website">
<meta property="og:image" content="https://media.vgm.io/products/76/3167/3167-1415483428.png">
<meta property="og:url" content="https://vgmdb.net/product/3167">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@vgmdb">
<meta name="twitter:title" content="Hunter x Hunter - VGMdb">
<meta name="twitter:description" content="Animation  released on October 02, 2011.">
<meta name="twitter:image" content="https://media.vgm.io/products/76/3167/3167-1415483428.png">


<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="generator" content="VGMdb">


<!-- CSS Stylesheet -->
<style type="text/css" id="vbulletin_css">
/**
* vBulletin 3.8.11 CSS
* Style: 'Default Style'; Style ID: 1
*/
@import url("/forums/clientscript/vbulletin_css/style-5593b98d-00001.css");
</style>
<link rel="stylesheet" type="text/css" href="/forums/clientscript/vbulletin_important.css?v=3811">


<link rel="stylesheet" type="text/css" href="/db/vgmdb.css?20220131">
<link rel="stylesheet" type="text/css" href="/db/css/vgmdb-colorcode-title.css?20190227" id="colorcode">
<link rel="stylesheet" type="text/css" href="/db/jquery.autocomplete.css?20091023">
<link rel="stylesheet" type="text/css" href="/db/jquery.jcarousel.css?20091124">
<link rel="stylesheet" type="text/css" href="/db/highslide.css?080623">
<!-- / CSS Stylesheet -->

<script type="text/javascript" src="/db/clientscript/yahoo-dom-event.js"></script><style type="text/css" id="operaUserStyle"></style>
<script type="text/javascript" src="/db/clientscript/connection-min.js"></script>
<script type="text/javascript">
<!--
var SESSIONURL = "";
var SECURITYTOKEN = "guest";
var IMGDIR_MISC = "/db/images/misc";
var vb_disable_ajax = parseInt("1", 10);
// -->
</script>
<script type="text/javascript" src="/forums/clientscript/vbulletin_global.js?v=3811"></script>
<script type="text/javascript" src="/forums/clientscript/vbulletin_menu.js?v=3811"></script>
<link rel="alternate" type="application/rss+xml" title="VGMdb Forums RSS Feed" href="/forums/external.php?type=RSS2">

<script type="text/javascript" src="/db/clientscript/jquery-1.4.min.js"></script>
<script type="text/javascript" src="/db/clientscript/jquery.compressed.js"></script>
<script type="text/javascript" src="/db/clientscript/jquery.tristate.js?20100420"></script>
<script type="text/javascript" src="/db/clientscript/highslide.packed.js?080620"></script>
<script type="text/javascript" src="/db/clientscript/vgmdb_global.js?220525"></script>
<link rel="search" type="application/opensearchdescription+xml" title="Search VGMdb" href="/db/search.xml">
<link rel="icon" href="/favicon.ico" type="image/vnd.microsoft.icon">
<link rel="shortcut icon" href="/favicon.ico" type="image/vnd.microsoft.icon">
<script language="javascript" type="text/javascript">
$(document).ready(function() {
	var ItemType = new Array;
	ItemType["0"] = "Album";
	ItemType["1"] = "Artist";
	ItemType["2"] = "Organization";
	hs.showCredits = false;
	hs.allowMultipleInstances = false;
	hs.graphicsDir = '/db/highslide/graphics/';
	function formatItem(row) {
		return "<span style='float: right; margin-left: 10px' class='tinyfont label'>" + ItemType[row[3]] + " #" + row[1] + "</span>" + row[0];
	}
	$('#navoptions a').click(function() {
		if (!$('#pref_content form').length) {
			$.ajax({
				url: '/db/user.php?do=preferences',
				beforeSend: function() {
					$('#navoptions').css('visibility', 'hidden').parent('li').css('background', 'transparent url(/db/img/ajax_loader_small.gif) center center no-repeat');
				},
				success: function(data) { 
					$('#navoptions').css('visibility', 'visible').parent('li').css('background', 'transparent url(/db/img/vgmdbsubnav2010.gif) -593px 0 no-repeat');
					$('#pref_content').html(data.html);
					$('#pref_content form label.tristate').tristate();
					$('#pref_content form').ajaxForm({
						beforeSubmit: function() {
							$('#pref_content form input[type=submit]').css('visibility', 'hidden').parent('div').css('background', 'transparent url(/db/img/ajax_loader_small.gif) center center no-repeat');
						},
						success: function() {
							$('#pref').slideUp('fast');
							$('#pref_content form input[type=submit]').css('visibility', 'visible').parent('div').css('background', 'none');
							$('#navoptions a').blur();
						}
					});
					$('#pref').slideDown('fast');
				},
				dataType: 'json'
			});
		}
		else {
			if ($('#pref').is(':visible')) {
				$('#pref').slideUp('fast');
				$('#navoptions a').blur();
			}
			else $('#pref').slideDown('fast');
		}
		return false;
	});
	$("#simplesearch").autocomplete('/db/ajax-autocomplete.php', {
		minChars: 3,
		delay: 1000,
		max: 150,
		width: 500,
		scrollHeight: 600,
		selectFirst: false,
		formatItem: formatItem
	}).result(function(event, item) {
		location.href = item[2];
	});
	$('label.tristate').tristate(); // 'sup IRA
	
});</script>
<meta name="google-site-verification" content="3hoyGArPHzn4HMMeNfYCjhqM5Ci_675U7M7NxbiLJ1A">
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-6WE0F947BF"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-6WE0F947BF');
</script>
<style>
.alt1_dark {
    background: #151F30;
    color: #FFFFFF;
}

.alt2_dark {
    background: #252B3F;
    color: #FFFFFF;
}
span.link_doc { display: block; background: transparent url('/db/icons/album-cover.gif') 0 2px no-repeat; padding-left: 14px; margin-bottom: 4px; }
</style>
<!---->


<style>tr.extracred { display: none; }</style>

<script language="javascript" type="text/javascript">
$(document).ready(function() {
	$("input.button").click(function() { window.clickedButton = $(this); });
	$("form").submit(function (e) { if (window.clickedButton != null && !window.clickedButton.hasClass("warnbutton")) { $("input.button:not(.warnbutton)").click(function() { return false; }); } });
	$(".auto-collapse").each(function() {
		if ($(this).height() >= 42) {
			$(this).css('cursor', 'pointer').css('overflow', 'hidden');
			if (!$(this).hasClass("auto-collapse-yellow")) {
				$(this).children(":first").css('mask-image', 'linear-gradient(to bottom, black 20px, transparent 50px)');
				$(this).children(":first").css('-webkit-mask-image', 'linear-gradient(to bottom, black 20px, transparent 50px)');
			}
			$(this).click(function(e) {
				$(this).css('max-height', 'none').css('cursor', 'auto');
				if (!$(this).hasClass("auto-collapse-yellow")) {
					$(this).children(":first").css('mask-image', '').css('-webkit-mask-image', '');
				}
			});
		}
	});
	$('textarea.resizable:not(.processed), select.resizable:not(.processed), div.resizable:not(.processed)').TextAreaResizer();
	
	
	
	
	
	
	
	
	
	$(document).ready(function() {
		$('.collapsible_section').click(function() {
			var src = $(this).find('img').attr('src');
			if (src.indexOf('close') > 0) {
				$(this).find('img').attr('src', src.replace('close', 'open'));
				$('#' + $(this).attr('rel')).hide('fast');
			} else {
				$(this).find('img').attr('src', src.replace('open', 'close'));
				$('#' + $(this).attr('rel')).show('fast');
			}
			return false;
		});
	});
	
	
	function dfilter(tablename, filtername, showtype="") {
		$("#" + tablename + " tbody, #" + tablename + " tr").hide();
		var elements = $("#" + tablename + " tr").not("[rel='year']");
		var checked = new Array();
		var unchecked1 = false;
		var unchecked2 = false;
		var unchecked3 = false;
		$("#" + filtername + "filter_menu :checkbox" + showtype).each(function() {
			checked[this.value] = this.checked;
			if (!this.checked) {
				if (this.value.substr(0,1) == 'd') unchecked1 = true;
				if (this.value.substr(0,1) == 'r') unchecked2 = true;
				if (this.value.substr(0,1) == 'c') unchecked3 = true;
			}
		});
		if (unchecked1 || unchecked2 || unchecked3) {
			elements = elements.filter(function(index) {
				var attribs = $(this).attr("rel").split("|");
				if (unchecked1 && !checked[attribs[0]]) return false;
				if (unchecked2 || unchecked3) {
					for (i = 1; i < attribs.length; i++) {
						if (!checked[attribs[i]] && attribs[i][0] == 'c') return false;
					}
					for (i = 1; i < attribs.length; i++) {
						if (checked[attribs[i]] && attribs[i][0] == 'r') return true;
					}
					return false;
				}
				return true;
			});
			elements = elements.siblings("[rel='year']").andSelf().parents("tbody").andSelf();
			elements.show();
		} else {
			$("#" + tablename + " tbody, #" + tablename + " tr").show();
		}
	}
	$("#discotablefilter_menu :checkbox").click(function() { dfilter("discotable", "discotable", ".albumshow"); dfilter("producttable", "discotable", ".productshow"); });
	$("#thankedtablefilter_menu :checkbox").click(function() { dfilter("thankedtable", "thankedtable", ".albumshow"); });
	$("#thankedproducttablefilter_menu :checkbox").click(function() { dfilter("thankedproducttable", "thankedproducttable", ".productshow"); });
	$("#featuredtablefilter_menu :checkbox").click(function() { dfilter("featuredtable", "featuredtable", ".albumshow"); });
	$("#featuredproducttablefilter_menu :checkbox").click(function() { dfilter("featuredproducttable", "featuredproducttable", ".productshow"); });
	
	
	
	
	
	
	
	
	
	
	// shamelessly ripped from Digg
	var cheatCode = '';
	var maxCode = 40;
	$(document).keydown(function(key) {
		if (cheatCode.length < maxCode) {
			var k = (key.keyCode == 0) ? key.charCode : key.keyCode;
			cheatCode = cheatCode + String(k) + ' ';
			switch (cheatCode) {
				case '38 40 37 39 65 13 ':
				window.location='/album/2072';
				break;
				case '38 38 40 40 37 39 37 39 66 65 13 ':
				window.location='/album/3778';
				break;
				case '73 68 68 81 68 ':
				window.location='/album/2950';
				break;
			}
		}
	});
});
</script>
<style type="text/css">:root img[width="728"][height="90"], :root [href="https://adstub.net/cina777/"], :root [href="https://adstub.net/arab777/"], :root [href="https://adstub.net/ratu89/"], :root [href="https://adstub.net/judi89/"], :root [href^="//mage98rquewz.com/"], :root [href^="//x4pollyxxpush.com/"], :root div.content-showcase-itru-sufficient-2d:not(.q7d5z1l):not(.x9a7b3k), :root div[class*="publift-widget-"]:has(.fuse-slot-sticky), :root span[id^="ezoic-pub-ad-placeholder-"], :root ins.adsbygoogle[data-ad-slot], :root ins.adsbygoogle[data-ad-client], :root img[src^="https://s-img.adskeeper.com/"], :root guj-ad, :root gpt-ad, :root div[ow-ad-unit-wrapper], :root div[id^="zergnet-widget"], :root div[id^="vuukle-ad-"], :root div[id^="taboola-stream-"], :root div[id^="sticky_ad_"], :root div[id^="st"][style^="z-index: 999999999;"], :root div[id^="rc-widget-"], :root div[id^="mrec-leaderboard-"], :root div[id^="gpt_ad_"], :root div[id^="ezoic-pub-ad-"], :root div[id^="dfp-ad-"], :root div[id^="crt-"][style], :root div[id^="apn_native_ad_slot_"], :root div[id^="adspot-"], :root div[id^="adrotate_widgets-"], :root ps-connatix-module, :root div[id^="ad_position_"], :root div[id^="ad-div-"], :root div[id*="ScriptRoot"], :root div[id*="MarketGid"], :root [href="https://adstub.net/rusia777/"], :root div[data-id-advertdfpconf], :root div[data-dfp-id], :root hl-adsense, :root div[data-contentexchange-widget], :root div[data-alias="300x250 Ad 2"], :root div[data-adunit-path], :root div[data-adname], :root div[data-ad-placeholder], :root a[href^="https://osfultrbriolenai.info/"], :root div[class^="Adstyled__AdWrapper-"], :root a[href^="https://go.xlviiirdr.com"], :root div[class$="-adlabel"], :root display-ads, :root a[href^="https://go.grinsbest.com/"], :root citrus-ad-wrapper, :root a[href^="https://s.zlinkd.com/"], :root bottomadblock, :root amp-fx-flying-carpet, :root amp-embed[type="taboola"], :root amp-connatix-player, :root div[id^="google_dfp_"], :root ad-slot, :root a[href^="https://www.purevpn.com/"][href*="&utm_source=aff-"], :root a[href^="https://www.privateinternetaccess.com/"] > img, :root a[href^="https://www.onlineusershielder.com/"], :root a[href^="https://financeads.net/tc.php?"], :root a[href^="https://www.mrskin.com/tour"], :root a[href^="https://www.infowarsstore.com/"] > img, :root a[href^="https://ak.psaltauw.net/"], :root broadstreet-zone-container, :root a[href^="https://www.highperformancecpmgate.com/"], :root amp-ad, :root a[href^="https://www.highcpmrevenuenetwork.com/"], :root a[href^="https://www.get-express-vpn.com/offer/"], :root a[href^="https://lnkxt.bannerator.com/"], :root a[href^="https://www.geekbuying.com/dynamic-ads/"], :root [href^="https://groorsoa.net/"], :root a[href^="https://www.financeads.net/tc.php?"], :root a[href^="https://www.effectiveratecpm.com/"], :root [href^="https://www.herbanomic.com/"] > img, :root a[href^="https://www.dql2clk.com/"], :root a[href^="https://www.nutaku.net/signup/landing/"], :root a[href^="https://www.dating-finder.com/signup/?ai_d="], :root a[href^="https://explore-site.com/"], :root a[href^="https://www.brazzersnetwork.com/landing/"], :root [data-template-type="nativead"], :root a[href^="https://www.adultempire.com/"][href*="?partner_id="], :root a[href^="https://voluum.prom-xcams.com/"], :root a[href^="https://twinrdsyte.com/"], :root div[data-type="_mgwidget"]:not(.eyeo), :root a[href^="https://twinrdsrv.com/"], :root a[href^="https://syndicate.contentsserved.com/"], :root div[data-alias="300x250 Ad 1"], :root a[href^="https://trk.nfl-online-streams.club/"], :root a[href^="https://tracking.avapartner.com/"], :root a[href^="https://track.wg-aff.com"], :root a[href^="https://track.ultravpn.com/"], :root a[href^="https://track.afcpatrk.com/"], :root a[href^="https://track.adform.net/"], :root a[href^="https://torguard.net/aff.php"] > img, :root [data-identity="adhesive-ad"], :root a[href^="https://tc.tradetracker.net/"] > img, :root a[href^="https://tatrck.com/"], :root [href^="https://zstacklife.com/"] img, :root a[href^="https://click.candyoffers.com/"], :root a[href^="https://t.aslnk.link/"], :root a[onmousedown^="this.href='https://paid.outbrain.com/network/redir?"], :root a[href^="https://t.ajump1.com/"], :root a[href^="https://t.adating.link/"], :root a[href^="https://go.trackitalltheway.com/"], :root [href^="https://track.fiverr.com/visit/"] > img, :root a[href^="https://syndication.exoclick.com/"], :root a[href^="https://syndication.dynsrvtbg.com/"], :root .gnt_em_vp_c[data-g-s="vp_dk"], :root div[data-ad-wrapper], :root a[href^="https://svb-analytics.trackerrr.com/"], :root a[onmousedown^="this.href='https://paid.outbrain.com/network/redir?"] + .ob_source, :root a[href^="http://www.iyalc.com/"], :root a[href^="https://claring-loccelkin.com/"], :root a[href^="https://stardomcoit.com/"], :root a[href^="https://track.aftrk5.com/"], :root a[href^="https://slkmis.com/"], :root a[href^="https://myclick-2.com/"], :root a[href^="https://sexynearme.com/"], :root [data-ad-manager-id], :root a[href^="https://s.zlinkr.com/"], :root [href="https://adstub.net/gaza88/"], :root a[href^="https://ad.doubleclick.net/"], :root a[href^="https://static.fleshlight.com/images/banners/"], :root a[href^="https://s.zlink7.com/"], :root a[href^="https://s.ma3ion.com/"], :root a[href^="https://s.eunow4u.com/"], :root a[href^="https://random-affiliate.atimaze.com/"], :root #kt_player > div[style$="display: block;"][style*="inset: 0px;"], :root [href$="/sexdating.php"], :root a[href^="https://quotationfirearmrevision.com/"], :root a[href^="https://pubads.g.doubleclick.net/"], :root a[href^="https://prf.hn/click/"][href*="/camref:"] > img, :root a[href^="https://serve.awmdelivery.com/"], :root a[href^="https://www.dating-finder.com/?ai_d="], :root a[href^="https://prf.hn/click/"][href*="/adref:"] > img, :root [href^="https://ap.octopuspop.com/click/"] > img, :root app-ad, :root a[href^="https://postback1win.com/"], :root a[href^="https://a.adtng.com/"], :root a[href^="https://playnano.online/offerwalls/?ref="], :root a[href^="https://mmwebhandler.aff-online.com/"], :root a[href^="https://www.bet365.com/"][href*="affiliate="], :root a[href^="https://pb-track.com/"], :root a[href^="https://pb-front.com/"], :root a[href^="https://paid.outbrain.com/network/redir?"], :root a[href^="https://streamate.com/landing/click/"], :root a[href^="https://upsups.click/"], :root a[href^="https://ndt5.net/"], :root a[href^="https://natour.naughtyamerica.com/track/"], :root a[href^="https://mediaserver.entainpartners.com/renderBanner.do?"], :root [data-ad-name], :root a[href^="https://loboclick.com/"], :root a[href^="https://lead1.pl/"], :root a[href^="https://landing.brazzersnetwork.com/"], :root a[href^="https://juicyads.in/"], :root a[href^="https://snowdayonline.xyz/"], :root a[href^="https://join.dreamsexworld.com/"], :root a[href^="https://join.bannedsextapes.com/track/"], :root a[href^="https://jaxofuna.com/"], :root a[href^="https://italarizege.xyz/"], :root a[href^="https://identicaldrench.com/"], :root ad-shield-ads, :root a[href^="https://hot-growngames.life/"], :root a[href^="https://helmethomicidal.com/"], :root display-ad-component, :root a[href^="https://golinks.work/"], :root a[href^="https://s.zlinkn.com/"], :root a[href^="https://go.xxxvjmp.com/"], :root a[href^="https://go.xxxjmp.com"], :root a[href^="https://zirdough.net/"], :root [class^="tile-picker__CitrusBannerContainer-sc-"], :root a[href^="https://go.xxxiijmp.com"], :root a[href^="https://go.xtbaffiliates.com/"], :root [data-role="tile-ads-module"], :root a[href^="https://go.xlviirdr.com"], :root a[href^="https://go.xlivrdr.com"], :root a[href^="https://ismlks.com/"], :root [href^="https://www.mypillow.com/"] > img, :root a[href^="https://go.xlirdr.com"], :root [data-css-class="dfp-inarticle"], :root a[href^="https://go.tmrjmp.com"], :root a[href^="https://go.markets.com/visit/?bta="], :root a[href^="https://billing.purevpn.com/aff.php"] > img, :root a[href^="https://go.hpyrdr.com/"], :root a[href^="https://lijavaxa.com/"], :root a[href^="https://go.goaserv.com/"], :root app-large-ad, :root [href^="https://turtlebids.irauctions.com/"] img, :root div[data-adunit], :root a[href^="https://go.etoro.com/"] > img, :root a[href^="https://go.dmzjmp.com"], :root a[href^="https://www.bang.com/?aff="], :root #mgb-container > #mgb, :root a[href^="https://go.admjmp.com"], :root a[href^="https://get.surfshark.net/aff_c?"][href*="&aff_id="] > img, :root a[href^="https://datewhisper.life/"], :root a[href^="https://click.linksynergy.com/fs-bin/"] > img, :root a[href^="https://get-link.xyz/"], :root a[href^="https://www.mrskin.com/account/"], :root a[href^="https://www.adskeeper.com"], :root a[data-redirect^="https://paid.outbrain.com/network/redir?"], :root [href^="https://clicks.affstrack.com/"] > img, :root a[href^="https://engine.phn.doublepimp.com/"], :root a[href^="https://dl-protect.net/"], :root a[href*=".foxqck.com/"], :root a[href^="https://ctosrd.com/"], :root a[href^="https://go.bushheel.com/"], :root a[href^="https://ctjdwm.com/"], :root [href="//sexcams.plus/"], :root a[href^="https://camfapr.com/landing/click/"], :root a[href^="https://prf.hn/click/"][href*="/creativeref:"] > img, :root a[href*="&maxads="], :root a[href^="http://www.adultempire.com/unlimited/promo?"][href*="&partner_id="], :root a[href^="https://1betandgonow.com/"], :root a[href^="https://chaturbate.com/in/?"], :root a[href^="https://t.ajrkm1.com/"], :root a[href^="https://bongacams10.com/track?"], :root a[href*=".g2afse.com/"], :root a[href^="https://bodelen.com/"], :root a[href^="//hoodingluster.com/"], :root a[href^="https://black77854.com/"], :root a[href^="https://getmatchedlocally.com/"], :root app-advertisement, :root a[href^="https://rixofa.com/"], :root a[href^="https://best-experience-cool.com/"], :root [data-taboola-options], :root a[href^="https://believessway.com/"], :root a[href^="https://Click.ggpickaff.com/"], :root a[href^="https://banners.livepartners.com/"], :root a[href^="http://revolvemockerycopper.com/"], :root a[href^="https://awptjmp.com/"], :root a[href^="https://join.sexworld3d.com/track/"], :root a[href^="https://aweptjmp.com/"], :root a[href^="https://ausoafab.net/"], :root a[href^="https://clicks.pipaffiliates.com/"], :root a[href^="https://aj1070.online/"], :root a[href^="https://a.bestcontentoperation.top/"], :root a[href^="https://adultfriendfinder.com/go/"], :root a[href^="https://ads.planetwin365affiliate.com/"], :root a[href^="https://ads.leovegas.com/"], :root a[href^="https://go.xlvirdr.com"], :root img[src^="https://images.purevpnaffiliates.com"], :root a[href^="https://porntubemate.com/"], :root a[href^="https://click.dtiserv2.com/"], :root a[href^="https://clickadilla.com/"], :root a[href^="https://a.medfoodhome.com/"], :root a[href^="https://cam4com.go2cloud.org/"], :root .nya-slot[style], :root a[href^="https://a.bestcontentweb.top/"], :root atf-ad-slot, :root a[href^="https://a2.adform.net/"], :root a[href^="https://a.candyai.love/"], :root .banner-img > .pbl, :root [data-m-ad-id], :root a[href^="https://a-ads.com/"], :root a[href^="https://1winpb.com/"], :root div[id^="optidigital-adslot"], :root [href^="https://wsup.ai/"], :root a[href^="https://123-stream.org/"], :root a[href^="https://in.rabbtrk.com/"], :root a[href^="http://www.h4trck.com/"], :root [href^="https://a.acebet.com/api/click?"], :root a[href^="http://www.friendlyduck.com/AF_"], :root a[href^="http://partners.etoro.com/"], :root [href="https://chaturbate.jjgirls.com/"] > img, :root a[href^="http://cam4com.go2cloud.org/aff_c?"], :root a[href^="https://ads.betfair.com/redirect.aspx?"], :root amp-ad-custom, :root a[href^="http://trk.globwo.online/"], :root a[onclick^="window.location.replace('https://random-affiliate.atimaze.com/"], :root a[href^="https://bongacams2.com/track?"], :root a-ad, :root a[href^="https://offhandpump.com/"], :root a[href^="http://stickingrepute.com/"], :root #slashboxes > .deals-rail, :root div[aria-label="Ads"], :root [href^="http://mypillow.com/"] > img, :root a[href^="http://bongacams.com/track?"], :root a[href^="//startgaming.net/tienda/" i], :root a[href^="https://a.medfoodsafety.com/"], :root a[href^="//go.eabids.com/"], :root a[href^=" https://www.friendlyduck.com/AF_"], :root [data-cl-spot-id], :root a[href*="/jump/next.php?r="], :root a[href^="https://go.nordvpn.net/aff"] > img, :root .\[\&_\.gdprAdTransparencyCogWheelButton\]\:\!pjra-z-\[5\], :root [href^="http://clicks.totemcash.com/"], :root a[href^="https://ad.zanox.com/ppc/"] > img, :root [data-d-ad-id], :root a[href*=".engine.adglare.net/"], :root div[id^="lazyad-"], :root a[href^="http://com-1.pro/"], :root [href^="https://www.profitablegatecpm.com/"], :root a[href*=".cfm?domain="][href*="&fp="], :root a[href^="https://ab.advertiserurl.com/aff/"], :root a[data-oburl^="https://paid.outbrain.com/network/redir?"], :root [id^="section-ad-banner"], :root [id^="ad_slider"], :root a[href^="https://www.goldenfrog.com/vyprvpn?offer_id="][href*="&aff_id="], :root a[href^="https://wmctjd.com/"], :root a[href*="//jjgirls.com/sex/Chaturbate"], :root [id^="ad-wrap-"], :root [href^="https://zone.gotrackier.com/"], :root a[href^="http://sarcasmadvisor.com/"], :root [href^="https://www.restoro.com/"], :root a[href^="https://track.totalav.com/"], :root a[href^="https://ctrdwm.com/"], :root [href^="https://www.targetingpartner.com/"], :root a[href^="https://join.virtuallust3d.com/"], :root .section-subheader > .section-hotel-prices-header, :root [href^="https://www.hostg.xyz/"] > img, :root a[href^="https://bngpt.com/"], :root a[href^="https://www.sheetmusicplus.com/"][href*="?aff_id="], :root a[href^="http://adultfriendfinder.com/go/"], :root a[href^="https://fastestvpn.com/lifetime-special-deal?a_aid="], :root a[href^="https://tour.mrskin.com/"], :root div[id^="ad-position-"], :root a[href^="https://www.toprevenuegate.com/"], :root a[href^="https://bc.game/"], :root a[href^="http://join.brokestraightboys.com/track/"], :root div[id^="div-ads-"], :root [href^="https://rapidgator.net/article/premium/ref/"], :root [href^="https://join.girlsoutwest.com/"], :root a[href^="https://activate-game.com/"], :root .scroll-fixable.rail-right > .deals-rail, :root [data-wpas-zoneid], :root a[href^="https://track.aftrk3.com/"], :root [href^="https://join3.bannedsextapes.com"], :root div[data-adzone], :root div[id^="adngin-"], :root [data-rc-widget], :root span[data-ez-ph-id], :root [href^="https://track.aftrk1.com/"], :root [href^="https://join.playboyplus.com/track/"], :root a[href^="https://go.xxxijmp.com"], :root [href^="https://istlnkcl.com/"], :root a[href^="https://trk.softonixs.xyz/"], :root a[href^="https://iqbroker.com/"][href*="?aff="], :root [href^="https://rpwmct.com/"], :root [href^="https://wct.link/click?"], :root a[href^="https://t.acam.link/"], :root a[href^="https://go.strpjmp.com/"], :root [href^="https://url.totaladblock.com/"], :root a[href^="https://go.rmishe.com/"], :root [href^="https://ilovemyfreedoms.com/landing-"], :root [href="https://adstub.net/indo666/"], :root [href^="https://glersakr.com/"], :root a[href^="https://tm-offers.gamingadult.com/"], :root [href^="https://charmingdatings.life/"], :root [data-id^="div-gpt-ad"], :root a[href^="https://tracker.loropartners.com/"], :root [href^="https://awbbjmp.com/"], :root a[href^="https://www.friendlyduck.com/AF_"], :root [href^="https://ad1.adfarm1.adition.com/"], :root a[href^="https://t.ajrkm3.com/"], :root [href^="https://aads.com/campaigns/"], :root a[href^="https://fc.lc/ref/"], :root a[href^="https://go.bbrdbr.com"], :root a[href^="http://tc.tradetracker.net/"] > img, :root a[href^="https://s.zlink3.com/"], :root a[href^="http://sneakyadministration.com/"], :root [href^="https://www.brighteonstore.com/products/"] img, :root a[href^="https://bngprm.com/"], :root [href^="https://shiftnetwork.infusionsoft.com/go/"] > img, :root [href^="http://www.mypillow.com/"] > img, :root .ob_container .item-container-obpd, :root [id^="div-gpt-ad"], :root [href="https://jdrucker.com/gold"] > img, :root a[href^="https://join.virtualtaboo.com/track/"], :root [id^="ad_sky"], :root [name^="google_ads_iframe"], :root aside[id^="adrotate_widgets-"], :root a[href^="https://www.liquidfire.mobi/"], :root DFP-AD, :root .grid > .container > #aside-promotion, :root [data-type="ad-vertical"], :root [href^="https://go.xlrdr.com"], :root a[href^="https://s.cant3am.com/"], :root [data-testid^="taboola-"], :root [data-testid^="section-AdRowBillboard"], :root a[href^="https://track.1234sd123.com/"], :root zeus-ad, :root [data-testid="prism-ad-wrapper"], :root [href^="https://ad.admitad.com/"], :root [href^="https://mypillow.com/"] > img, :root [data-testid="ad_testID"], :root [data-mobile-ad-id], :root [data-dynamic-ads], :root a[href^="https://gamingadlt.com/?offer="], :root [data-desktop-ad-id], :root a[href^="https://go.rmhfrtnd.com"], :root a[href^="https://pb-imc.com/"], :root a[href^="https://www8.smartadserver.com/"], :root topadblock, :root a[href^="//s.zlinkd.com/"], :root [href^="https://mypatriotsupply.com/"] > img, :root [data-testid="adBanner-wrapper"], :root [href^="https://mylead.global/stl/"] > img, :root a[href*=".adsrv.eacdn.com/"], :root [href^="https://antiagingbed.com/discount/"] > img, :root #teaser1[style^="width:autopx;"], :root [href^="https://www.cloudways.com/en/?id"], :root [data-asg-ins], :root [data-block-type="ad"], :root [data-ad-width], :root a[href^="https://clickins.slixa.com/"], :root [onclick*="content.ad/"], :root a[href^="https://go.cmtaffiliates.com/"], :root [href^="https://optimizedelite.com/"] > img, :root div[data-ad-region], :root AMP-AD, :root [data-ad-cls], :root a[href^="https://www.adxsrve.com/"], :root a[href^="https://click.Ggpickaff.com/"], :root [data-ez-name], :root a[href^="https://go.mnaspm.com/"], :root a[href^="https://service.bv-aff-trx.com/"], :root a[href^="https://6-partner.com/"], :root [class^="s2nPlayer"], :root [href^="https://affiliate.fastcomet.com/"] > img, :root [class^="adDisplay-module"], :root a[href^="https://adclick.g.doubleclick.net/"], :root [data-freestar-ad][id], :root AD-SLOT, :root a[href^="https://combodef.com/"], :root a[href^="https://click.hoolig.app/"], :root a[href^="https://www.googleadservices.com/pagead/aclk?"] > img, :root [data-ad-module], :root a[href^="https://a.bestcontentfood.top/"], :root #kt_player > a[target="_blank"], :root a[href^="https://go.skinstrip.net"][href*="?campaignId="], :root #teaser2[style^="width:autopx;"], :root [data-revive-zoneid], :root a[href^="https://losingoldfry.com/"], :root div[id^="div-gpt-"], :root a[href^="https://gml-grp.com/"], :root .ob_dual_right > .ob_ads_header ~ .odb_div, :root div[data-ad-targeting], :root a[style="width:100%;height:100%;z-index:10000000000000000;position:absolute;top:0;left:0;"], :root [href^="https://www.avantlink.com/click.php"] img, :root [data-testid="commercial-label-taboola"], :root [class^="div-gpt-ad"], :root a[href^="https://traffdaq.com/"], :root #teaser3[style^="width:autopx;"], :root a[href^="https://go.hpyjmp.com"], :root iframe[scrolling="no"][sandbox*="allow-popups allow-modals"][style^="width: 100%; height: 100%; border: none;"], :root [href^="https://mystore.com/"] > img, :root [class^="amp-ad-"], :root div[id*="ScriptRoot"]:not(.eyeo), :root a[href^="https://clixtrac.com/"], :root a[href^="https://wittered-mainging.com/"], :root #teaser3[style="width: 100%;text-align: center;display: scroll;position:fixed;bottom: 0;margin: 0 auto;z-index: 103;"] { display: none !important; }</style><style type="text/css">.highslide img {cursor: url(/db/highslide/graphics/zoomin.cur), pointer !important;}</style></head>
<body style="padding: 0; margin: 0">
<a name="top"></a>
<div class="page" style="background-color: #1B273D; height: 100px; width: 100%;">
<div style="float: right; margin-top: 10px; margin-right: 10px;">
	<ul class="pipelist tinyfont">
	
	<li class="smallfont first-child"><span id="navlogin" style="cursor: pointer;"><a href="#">Login</a><script type="text/javascript"> vBmenu.register('navlogin'); </script> <img src="/db/images/misc/menu_open.gif" border="0" title="" alt=""></span></li>
	<li class="smallfont"><a title="Register a new account" href="/forums/register.php">Register</a></li>
	
	</ul>
</div>
<div style="white-space: nowrap;">
<!-- logo -->
<div style="height: 100px; float: left;"><a href="/"><img src="/db/img/vgmdblogo.png" alt="VGMdb" style="padding: 10px; width: 250px; height: 80px; border: 0" title="VGMdb"></a></div>
<!-- /logo -->
<!-- top nav -->
<div style="height: 100px; float: left; position: relative; margin-left: 1px;">
<ul id="topnav">
	<li id="nav_album"><a title="Official Albums, Enclosures, Doujins" href="/db/albums.php">Albums</a><a class="buttonSubmit" href="/album/new" title="Submit a new album"><img src="/db/img/button-add-big.png" alt=""></a></li>
	<li id="nav_artist"><a title="Composers, Arrangers, Lyricists, Performers" href="/db/artists.php">Artists</a><a class="buttonSubmit" href="/db/artists-submit.php" title="Submit a new artist"><img src="/db/img/button-add-big.png" alt=""></a></li>
	<!-- <li id="nav_track"><a title="Instrumentals, Vocals, Sound Effects, Voice Dramas" href="#">Tracks</a></li> -->
	<li id="nav_label"><a title="Music Labels, Publishers, Organizations and Groups" href="/db/org.php">Organizations</a><a class="buttonSubmit" href="/db/org-submit.php" title="Submit a new publisher"><img src="/db/img/button-add-big.png" alt=""></a></li>
	<li id="nav_product"><a title="Games, Video, Radio/Drama Programs, Print Publications" href="/db/product.php">Products</a><a class="buttonSubmit" href="/db/product-submit.php" title="Submit a new product"><img src="/db/img/button-add-big.png" alt=""></a></li>
	<li id="nav_event"><a title="Conventions, Gatherings and Shows" href="/db/events.php">Events</a><a class="buttonSubmit" href="/db/event-submit.php" title="Submit a new event"><img src="/db/img/button-add-big.png" alt=""></a></li>
	
	<!--li id="nav_podcast"><a title="VGM Decibel, our bi-monthly podcast" href="/cast">Podcast</a></li-->
</ul>
</div>
<!-- / top nav -->
</div>
</div>
<div class="label" style="clear: both; width: 100%; background-color: #2F364F; font-family: Arial">
<ul id="subnav">
	<li id="nav_search" style="width: 250px">
		<form name="navsearch" action="/search" method="get">
			<div>
                 <input type="text" class="bginput smallfont ac_input ac_default" name="q" id="simplesearch" maxlength="150" style="width: 160px;" enterkeyhint="go" autocomplete="off">
                 <select name="type" style="width: 70px;">
                    <option value="">all</option>
                    <option value="album">albums</option>
                    <option value="artist">artists</option>
                    <option value="org">organizations</option>
                    <option value="product">products</option>
                </select>
            </div>
		</form>
	</li>
	<li id="nav_advsearch"><a title="More search options" href="/search">Advanced Search</a></li>
	<li id="nav_update"><a title="Latest submissions and edits" href="/db/recent.php">Updates</a></li>
	<li id="nav_calendar"><a title="Release schedules" href="/db/calendar.php?year=2026&amp;month=3">Calendar</a></li>
	<li id="nav_forum"><a title="Community discussions" href="/forums/">Forums</a></li>
	<li id="nav_market"><a title="Trade with other members" href="/db/marketplace.php?do=view">Marketplace</a></li>
	<!--li id="nav_users"><a title="User collections" href="/db/collection.php">Users</a></li-->
	<li id="nav_chat"><a title="Real-time chat" rel="nofollow" href="https://discord.gg/VXgKQUa" target="vgmdbchat">Discord</a></li>
	
	<li id="nav_submit"><a title="Submit an album" href="/album/new">Submit Album</a></li>
	<li id="nav_customize"><span id="navoptions"><a title="Edit your preferences" href="#">Customize</a></span></li>
</ul>
</div>


	<!-- login form -->
	<div class="vbmenu_popup" id="navlogin_menu" style="display:none;">
	<table cellpadding="4" cellspacing="1" border="0"><tbody><tr><td style="background: #BBC7CE;">
	<form action="/forums/login.php?do=login" method="post" onsubmit="md5hash(vb_login_password, vb_login_md5password, vb_login_md5password_utf, 0)">
	<script type="text/javascript" src="/forums/clientscript/vbulletin_md5.js?v=3811"></script>
	<table cellpadding="0" cellspacing="3" border="0">
	<tbody><tr>
		<td class="smallfont"><label for="navbar_username">User Name</label></td>
		<td><input type="text" class="bginput" style="font-size: 11px" name="vb_login_username" id="navbar_username" size="10" accesskey="u" tabindex="101" value="User Name" onfocus="if (this.value == 'User Name') this.value = '';"></td>
		<td class="smallfont" colspan="2" nowrap="nowrap"><label for="cb_cookieuser_navbar"><input type="checkbox" name="cookieuser" value="1" tabindex="103" id="cb_cookieuser_navbar" accesskey="c">Remember</label></td>
	</tr><tr>
		<td class="smallfont"><label for="navbar_password">Password</label></td>
		<td><input type="password" class="bginput" style="font-size: 11px" name="vb_login_password" id="navbar_password" size="10" tabindex="102"></td>
		<td><input type="submit" class="button" value="Log in" tabindex="104" title="Enter your username and password in the boxes provided to login, or click the 'register' button to create a profile for yourself." accesskey="s"></td>
	</tr>
	</tbody></table>
	<input type="hidden" name="s" value="">
	<input type="hidden" name="securitytoken" value="guest">
	<input type="hidden" name="do" value="login">		
	<input type="hidden" name="vb_login_md5password">
	<input type="hidden" name="vb_login_md5password_utf">
	</form>
	</td></tr></tbody></table>
	</div>
	<!-- / login form -->


<!-- content table -->
<div class="page" style="padding:20px 20px 0 20px">

<div id="pref" style="width: 100%; background-color:#1B273D; margin-bottom: 20px; display: none">
	<b class="rtop"><b></b></b>
	<div id="pref_content"></div>
	<b class="rbot"><b></b></b>
</div>



<!-- main page contents -->



<table width="100%" cellpadding="0" cellspacing="0" border="0" align="left">
<tbody><tr><td width="100%" style="background-color: #1B273D;" valign="top">
	<b class="rtop"><b></b></b>
	<div id="innermain" style="padding: 6px 10px 10px 10px">

	<span style="float:right;" class="label smallfont"><a href="/db/product-discuss.php?id=3167">Discuss</a>
</span>

	

	<h1 id="maintitle" style="display: inline"><span class="albumtitle" lang="en" style="display:inline">Hunter x Hunter</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>HUNTERxHUNTER</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>Hunter x Hunter</span></h1> <span class="smallfont time">(Animation)</span>
	<div id="subtitle" class="label" style="padding: 0px 10px 0px 10px"><span class="albumtitle" lang="en" style="display:inline">HUNTERxHUNTER<br>Hunter x Hunter (2011)<br></span><span class="albumtitle" lang="ja" style="display:none">Hunter x Hunter<br>Hunter x Hunter (2011)<br></span><span class="albumtitle" lang="ja-Latn" style="display:none">Hunter x Hunter<br>HUNTERxHUNTER<br>Hunter x Hunter (2011)<br></span></div>

	<div id="innercontent" style="padding: 10px 10px 0px 10px">
	<style>dl {margin: 0; padding: 0} dt {margin-bottom: 6px; float: left; clear: both} dd {margin-bottom: 6px; margin-left: 11em}</style>

	
	<div id="innermain" style="margin: 6px 10px 6px 10px">
	<style>dl {margin: 0; padding: 0} dt {margin-bottom: 6px; float: left; clear: both} dd {margin-bottom: 6px; margin-left: 11em}</style>
	<div style="float: left; text-align:center;  width: 200px; margin: 10px 10px 0 10px;"><a id="thumb_" href="https://media.vgm.io/products/76/3167/3167-1415483428.png" class="highslide" rel="highslide"><img src="https://thumb-media.vgm.io/products/76/3167/3167-1415483428.png" alt="" border="0" style="max-height: 250px;"></a><div class="highslide-caption"><span class="smallfont">Submitted by <b>Illidan</b> on Nov 8, 2014 <span class="time">01:50 PM</span></span></div></div>

	<div style="margin-left: 230px; background-color: #2F364F">
	<b class="rtop"><b></b></b>
	<div style="padding: 6px 10px 6px 10px" class="smallfont">

		<div style="float: left"><dl width="100%">
		<dt class="label" style="padding-bottom: 3px"><b>Franchises</b></dt>
		<dd style="padding-bottom: 3px"><div><a class="smallfont" href="/product/3163"><span class="productname" lang="en" style="display:inline">Hunter x Hunter</span><span style="display:none"><em> / </em></span><span class="productname" lang="ja" style="display:none">ハンター×ハンター</span><span style="display:none"><em> / </em></span><span class="productname" lang="ja-Latn" style="display:none">Hunter x Hunter</span></a></div>
</dd>
		<dt class="label" style="padding-bottom: 3px"><b>Release Date</b></dt>
		<dd style="padding-bottom: 3px">October 02, 2011</dd>
		<dt class="label" style="padding-bottom: 3px"><b>Organizations</b></dt><dd style="padding-bottom: 3px">Madhouse</dd>
		
		</dl></div>
		<div style="clear: both; height: 1px; font-size: 1px; overflow: hidden"></div>
	</div>
	<b class="rbot"><b></b></b>
	</div>


<div style="margin-top:10px;"><h3 class="label">Releases <a href="#" class="collapsible_section" rel="collapse_sub"><img src="/db/img/collapse_close.png"></a></h3>
<div style="background-color: #2F364F;" id="collapse_sub">
<b class="rtop"><b></b></b>
<div style="padding: 6px 10px 6px 10px" class="smallfont"><table cellspacing="0" cellpadding="0" border="0">
<tbody><tr>
<td align="left" style="padding-left: 8px;"><h4>DATE</h4></td>
<td align="left" style="padding-left: 8px;"><h4>RELEASE</h4></td>
<td align="left" style="padding-left: 8px;"><h4>REGION</h4></td>
<td align="left" style="padding-left: 8px;"><h4>PLATFORM</h4></td>
</tr>
<tr style="height:17px">
<td align="left" style="padding-left: 8px;" nowrap="nowrap">
<span class="smallfont label">2011-10-02</span>
</td>
<td align="left" style="padding-left: 8px;">

<a class="smallfont" href="/release/4261"><span class="productname" lang="en" style="display:inline">HUNTERxHUNTER</span><span style="display:none"><em> / </em></span><span class="productname" lang="ja" style="display:none">HUNTERxHUNTER</span><span style="display:none"><em> / </em></span><span class="productname" lang="ja-Latn" style="display:none">HUNTERxHUNTER</span></a>
</td>
<td align="left" style="padding-left: 8px;" nowrap="nowrap">
<span class="smallfont label">Japan</span>
</td>
<td align="left" style="padding-left: 8px;" nowrap="nowrap">
<span class="smallfont label">Series</span>
</td>
</tr>
</tbody></table>

<div style="clear: both; height: 1px; font-size: 1px; overflow: hidden"></div>
</div>
<b class="rbot"><b></b></b>
</div></div>











	<span style="float: right; margin-top: 10px; font-size: 8pt; font-weight: bold; cursor: pointer;" id="discotablefilter">Filter <script type="text/javascript"> vBmenu.register('discotablefilter'); </script> <img src="/db/images/misc/menu_open.gif" border="0" title="" alt=""></span>

	<!-- discography filter menu -->
	<div class="vbmenu_popup" id="discotablefilter_menu" style="display:none">
	<form action="" name="formdiscotablefilter">
	<table cellpadding="4" cellspacing="1" border="0" style="color: white">
	<tbody><tr><td class="thead">Classification</td></tr>
<tr><td style="background-color: #1B273D"><div class="smallfont" style="white-space: nowrap"><label for="r2"><input type="checkbox" class="inlineimg albumshow" name="r2" id="r2" value="r2" checked="checked">Arrangement</label></div>
<div class="smallfont" style="white-space: nowrap"><label for="r6"><input type="checkbox" class="inlineimg albumshow" name="r6" id="r6" value="r6" checked="checked">Vocal</label></div>
<div class="smallfont" style="white-space: nowrap"><label for="r7"><input type="checkbox" class="inlineimg albumshow" name="r7" id="r7" value="r7" checked="checked">OP/ED/Insert</label></div>
<div class="smallfont" style="white-space: nowrap"><label for="r1"><input type="checkbox" class="inlineimg albumshow" name="r1" id="r1" value="r1" checked="checked">Soundtrack</label></div>
<div class="smallfont" style="white-space: nowrap"><label for="r8"><input type="checkbox" class="inlineimg albumshow" name="r8" id="r8" value="r8" checked="checked">Drama</label></div>
</td></tr>

	</tbody></table>
	</form>
	</div>
	<!-- / discography filter menu -->

<h3 style="margin-top: 10px;" class="label">Albums <a href="#" class="collapsible_section" rel="collapse_albums"><img src="/db/img/collapse_close.png"></a></h3>
<div style="background-color: #2F364F;" id="collapse_albums">
<b class="rtop"><b></b></b>
<div id="discotable" style="padding: 6px 10px 10px 10px">
<table cellpadding="4" cellspacing="0" border="0" width="100%">
<tbody class="">
<tr rel="year"><td align="left" style="padding-top: 10px" colspan="3"><h3 class="time">2022</h3></td></tr>
<tr rel="|r2|r6">
   <td align="left" valign="top" style="width: 10%" class="label">04.27</td>
   <td align="left" valign="top"> <a class="albumtitle album-game" href="http://vgmdb.net/album/117173" title="CORUSCATE -DNA- / RAISE A SUILEN [A ver./Limited Edition]"><span class="albumtitle" lang="en" style="display:inline">CORUSCATE -DNA- / RAISE A SUILEN [A ver./Limited Edition]</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>CORUSCATE -DNA- / RAISE A SUILEN [A ver./Blu-ray付生産限定盤]</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>CORUSCATE -DNA- / RAISE A SUILEN [A ver./Limited Edition]</span></a> <span class="catalog album-game">BRMM-10519</span> <span class="smallfont label">Arrangement, Vocal</span></td>
</tr>

</tbody>
<tbody class="">
<tr rel="year"><td align="left" style="padding-top: 10px" colspan="3"><h3 class="time">2018</h3></td></tr>
<tr rel="|r2|r6">
   <td align="left" valign="top" style="width: 10%" class="label">10.04</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/155517" title="DEPARTURE / Ricardo Cruz"><span class="albumtitle" lang="en" style="display:inline">DEPARTURE / Ricardo Cruz</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>DEPARTURE / ヒカルド・クルーズ</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>DEPARTURE / Ricardo Cruz</span></a> <span class="catalog album-anime">N/A</span> <span class="smallfont label">Arrangement, Vocal</span></td>
</tr>

</tbody>
<tbody class="">
<tr rel="year"><td align="left" style="padding-top: 10px" colspan="3"><h3 class="time">2013</h3></td></tr>
<tr rel="|r6|r7">
   <td align="left" valign="top" style="width: 10%" class="label">12.25</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/42543" title="Hyouri Ittai / YUZU"><span class="albumtitle" lang="en" style="display:inline">Hyouri Ittai / YUZU</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>表裏一体 / ゆず</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>Hyouri Ittai / YUZU</span></a> <span class="catalog album-anime">SNCC-89930</span> <span class="smallfont label">Vocal, OP/ED/Insert</span></td>
</tr>
<tr rel="|r6|r7">
   <td align="left" valign="top" style="width: 10%" class="label">12.25</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/42544" title="Hyouri Ittai / YUZU [HUNTER×HUNTER Ver.]"><span class="albumtitle" lang="en" style="display:inline">Hyouri Ittai / YUZU [HUNTER×HUNTER Ver.]</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>表裏一体 / ゆず [HUNTER×HUNTER Ver.]</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>Hyouri Ittai / YUZU [HUNTER×HUNTER Ver.]</span></a> <span class="catalog album-anime">SNCC-89931</span> <span class="smallfont label">Vocal, OP/ED/Insert</span></td>
</tr>
<tr rel="|r1|r6">
   <td align="left" valign="top" style="width: 10%" class="label">09.18</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/40558" title="HUNTER×HUNTER Select×Best×α"><span class="albumtitle" lang="en" style="display:inline">HUNTER×HUNTER Select×Best×α</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>TVアニメ「HUNTER×HUNTER」 セレクト×ベスト×α</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTER×HUNTER Select×Best×α</span></a> <span class="catalog album-anime">VPCG-84946</span> <span class="smallfont label">Soundtrack, Vocal</span></td>
</tr>
<tr rel="|r1|r6">
   <td align="left" valign="top" style="width: 10%" class="label">07.24</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/39426" title="HUNTER×HUNTER Original Soundtrack 3"><span class="albumtitle" lang="en" style="display:inline">HUNTER×HUNTER Original Soundtrack 3</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>TVアニメ「HUNTER×HUNTER」オリジナル・サウンドトラック3</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTER×HUNTER Original Soundtrack 3</span></a> <span class="catalog album-anime">VPCG-84941</span> <span class="smallfont label">Soundtrack, Vocal</span></td>
</tr>
<tr rel="|r6|r7">
   <td align="left" valign="top" style="width: 10%" class="label">01.09</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/36116" title="REASON / YUZU [Limited Edition]"><span class="albumtitle" lang="en" style="display:inline">REASON / YUZU [Limited Edition]</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>REASON / ゆず</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>REASON / YUZU [Limited Edition]</span></a> <span class="catalog album-anime">SNCC-89925</span> <span class="smallfont label">Vocal, OP/ED/Insert</span></td>
</tr>
<tr rel="|r6|r7">
   <td align="left" valign="top" style="width: 10%" class="label">01.09</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/36117" title="REASON / YUZU"><span class="albumtitle" lang="en" style="display:inline">REASON / YUZU</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>REASON / ゆず</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>REASON / YUZU</span></a> <span class="catalog album-anime">SNCC-89926</span> <span class="smallfont label">Vocal, OP/ED/Insert</span></td>
</tr>
<tr rel="|r6|r7">
   <td align="left" valign="top" style="width: 10%" class="label">01.09</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/36118" title="REASON / YUZU [Limited Edition]"><span class="albumtitle" lang="en" style="display:inline">REASON / YUZU [Limited Edition]</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>REASON / ゆず</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>REASON / YUZU [Limited Edition]</span></a> <span class="catalog album-anime">SNCC-89927</span> <span class="smallfont label">Vocal, OP/ED/Insert</span></td>
</tr>

</tbody>
<tbody class="">
<tr rel="year"><td align="left" style="padding-top: 10px" colspan="3"><h3 class="time">2012</h3></td></tr>
<tr rel="|r6|r8">
   <td align="left" valign="top" style="width: 10%" class="label">09.26</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/38537" title="HUNTER x HUNTER Character Song Collection - Genei Ryodanhen -"><span class="albumtitle" lang="en" style="display:inline">HUNTER x HUNTER Character Song Collection - Genei Ryodanhen -</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>「HUNTER×HUNTER」キャラクターソング集 ~幻影旅団編~</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTER x HUNTER Character Song Collection - Genei Ryodanhen -</span></a> <span class="catalog album-anime">VPCG-84930</span> <span class="smallfont label">Vocal, Drama</span></td>
</tr>
<tr rel="|r6">
   <td align="left" valign="top" style="width: 10%" class="label">08.22</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/70151" title="HUNTER×HUNTER DIGITAL LIMITED SINGLE"><span class="albumtitle" lang="en" style="display:inline">HUNTER×HUNTER DIGITAL LIMITED SINGLE</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>HUNTER×HUNTER DIGITAL LIMITED SINGLE</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTER×HUNTER DIGITAL LIMITED SINGLE</span></a> <span class="catalog album-anime">N/A</span> <span class="smallfont label">Vocal</span></td>
</tr>
<tr rel="|r6|r7">
   <td align="left" valign="top" style="width: 10%" class="label">07.18</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/33601" title="HUNTING FOR YOUR DREAM / GALNERYUS [TYPE A]"><span class="albumtitle" lang="en" style="display:inline">HUNTING FOR YOUR DREAM / GALNERYUS [TYPE A]</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>HUNTING FOR YOUR DREAM / GALNERYUS [TYPE A]</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTING FOR YOUR DREAM / GALNERYUS [TYPE A]</span></a> <span class="catalog album-anime">VPCC-82306</span> <span class="smallfont label">Vocal, OP/ED/Insert</span></td>
</tr>
<tr rel="|r6|r7">
   <td align="left" valign="top" style="width: 10%" class="label">07.18</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/33602" title="HUNTING FOR YOUR DREAM / GALNERYUS [TYPE B]"><span class="albumtitle" lang="en" style="display:inline">HUNTING FOR YOUR DREAM / GALNERYUS [TYPE B]</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>HUNTING FOR YOUR DREAM / GALNERYUS [TYPE B]</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTING FOR YOUR DREAM / GALNERYUS [TYPE B]</span></a> <span class="catalog album-anime">VPCC-82307</span> <span class="smallfont label">Vocal, OP/ED/Insert</span></td>
</tr>
<tr rel="|r1">
   <td align="left" valign="top" style="width: 10%" class="label">05.23</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/32123" title="HUNTER×HUNTER Original Soundtrack 2"><span class="albumtitle" lang="en" style="display:inline">HUNTER×HUNTER Original Soundtrack 2</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>TVアニメ「HUNTER×HUNTER」オリジナル・サウンドトラック2</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTER×HUNTER Original Soundtrack 2</span></a> <span class="catalog album-anime">VPCG-84925</span> <span class="smallfont label">Soundtrack</span></td>
</tr>
<tr rel="|r6">
   <td align="left" valign="top" style="width: 10%" class="label">03.21</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/89875" title="HUNTER x HUNTER Character Song Collection 2"><span class="albumtitle" lang="en" style="display:inline">HUNTER x HUNTER Character Song Collection 2</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>TVアニメ「HUNTER×HUNTER」キャラクター･ソング集2</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTER x HUNTER Character Song Collection 2</span></a> <span class="catalog album-anime">VPCG-84922</span> <span class="smallfont label">Vocal</span></td>
</tr>
<tr rel="|r6">
   <td align="left" valign="top" style="width: 10%" class="label">03.07</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/66726" title="HUNTER x HUNTER Character Song Collection 1"><span class="albumtitle" lang="en" style="display:inline">HUNTER x HUNTER Character Song Collection 1</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>TVアニメ「HUNTER×HUNTER」キャラクター･ソング集１</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTER x HUNTER Character Song Collection 1</span></a> <span class="catalog album-anime">VPCG-84920</span> <span class="smallfont label">Vocal</span></td>
</tr>
<tr rel="|r1|r6">
   <td align="left" valign="top" style="width: 10%" class="label">01.25</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/30315" title="HUNTER×HUNTER Original Soundtrack"><span class="albumtitle" lang="en" style="display:inline">HUNTER×HUNTER Original Soundtrack</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>TVアニメ「HUNTER×HUNTER」オリジナル・サウンドトラック</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTER×HUNTER Original Soundtrack</span></a> <span class="catalog album-anime">VPCG-84915</span> <span class="smallfont label">Soundtrack, Vocal</span></td>
</tr>
<tr rel="|r6">
   <td align="left" valign="top" style="width: 10%" class="label">01.25</td>
   <td align="left" valign="top"> <a class="albumtitle album-game" href="http://vgmdb.net/album/30435" title="Kizuna / GALNERYUS"><span class="albumtitle" lang="en" style="display:inline">Kizuna / GALNERYUS</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>Kizuna / GALNERYUS</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>Kizuna / GALNERYUS</span></a> <span class="catalog album-game">VPCC-81723</span> <span class="smallfont label">Vocal</span></td>
</tr>
<tr rel="|r6|r7">
   <td align="left" valign="top" style="width: 10%" class="label">01.11</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/29875" title="Just Awake / Fear, and Loathing in Las Vegas"><span class="albumtitle" lang="en" style="display:inline">Just Awake / Fear, and Loathing in Las Vegas</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>Just Awake / Fear, and Loathing in Las Vegas</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>Just Awake / Fear, and Loathing in Las Vegas</span></a> <span class="catalog album-anime">VPCC-82303</span> <span class="smallfont label">Vocal, OP/ED/Insert</span></td>
</tr>

</tbody>
<tbody class="">
<tr rel="year"><td align="left" style="padding-top: 10px" colspan="3"><h3 class="time">2011</h3></td></tr>
<tr rel="|r6|r7">
   <td align="left" valign="top" style="width: 10%" class="label">12.21</td>
   <td align="left" valign="top"> <a class="albumtitle album-anime" href="http://vgmdb.net/album/29878" title="departure! / Masatoshi Ono"><span class="albumtitle" lang="en" style="display:inline">departure! / Masatoshi Ono</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>departure! / 小野正利</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>departure! / Masatoshi Ono</span></a> <span class="catalog album-anime">VPCG-82643</span> <span class="smallfont label">Vocal, OP/ED/Insert</span></td>
</tr>

</tbody>

</table>

</div>
<b class="rbot"><b></b></b>
</div>

</div></div>
</div></td>
<td id="rightcolumn" rowspan="2" style="width: 270px; padding-left: 20px" valign="top">





<div style="width: 250px; background-color: #1B273D">
<b class="rtop"><b></b></b>
<div style="padding: 6px 10px 0px 10px"><h3>Recent Releases</h3></div>
</div>
<div style="width: 250px; background-color: #2F364F;">


<span class="smallfont"><div class="album_infobit_small smallfont label">
<div class="album_infobit_thumb"><div style="background-image: url('https://thumb-media.vgm.io/albums/37/117173/117173-cd6177464367.jpg')">
<a href="http://vgmdb.net/album/117173" title="CORUSCATE -DNA- / RAISE A SUILEN [A ver./Limited Edition]"></a>
</div></div>
<ul class="album_infobit_detail">
<li><a class="albumtitle smallfont album-game" href="http://vgmdb.net/album/117173" title="CORUSCATE -DNA- / RAISE A SUILEN [A ver./Limited Edition]"><span class="albumtitle" lang="en" style="display:inline">CORUSCATE -DNA- / RAISE A SUILEN [A ver./Limite...</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>CORUSCATE -DNA- / RAISE A SUILEN [A ver./Blu-ra...</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>CORUSCATE -DNA- / RAISE A SUILEN [A ver./Limite...</span></a></li>
<li><span class="catalog smallfont album-game">BRMM-10519</span></li>
<li>Apr 27, 2022</li>
</ul>
</div><div class="album_infobit_small smallfont label">
<div class="album_infobit_thumb"><div style="background-image: url('https://thumb-media.vgm.io/albums/71/155517/155517-c77e80b1501f.jpg')">
<a href="http://vgmdb.net/album/155517" title="DEPARTURE / Ricardo Cruz"></a>
</div></div>
<ul class="album_infobit_detail">
<li><a class="albumtitle smallfont album-anime" href="http://vgmdb.net/album/155517" title="DEPARTURE / Ricardo Cruz"><span class="albumtitle" lang="en" style="display:inline">DEPARTURE / Ricardo Cruz</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>DEPARTURE / ヒカルド・クルーズ</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>DEPARTURE / Ricardo Cruz</span></a></li>
<li><span class="catalog smallfont album-anime">N/A</span></li>
<li>Oct 04, 2018</li>
</ul>
</div><div class="album_infobit_small smallfont label">
<div class="album_infobit_thumb"><div style="background-image: url('https://thumb-media.vgm.io/albums/44/42544/42544-eb33aeb608ab.jpg')">
<a href="http://vgmdb.net/album/42544" title="Hyouri Ittai / YUZU [HUNTER×HUNTER Ver.]"></a>
</div></div>
<ul class="album_infobit_detail">
<li><a class="albumtitle smallfont album-anime" href="http://vgmdb.net/album/42544" title="Hyouri Ittai / YUZU [HUNTER×HUNTER Ver.]"><span class="albumtitle" lang="en" style="display:inline">Hyouri Ittai / YUZU [HUNTER×HUNTER Ver.]</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>表裏一体 / ゆず [HUNTER×HUNTER Ver.]</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>Hyouri Ittai / YUZU [HUNTER×HUNTER Ver.]</span></a></li>
<li><span class="catalog smallfont album-anime">SNCC-89931</span></li>
<li>Dec 25, 2013</li>
</ul>
</div><div class="album_infobit_small smallfont label">
<div class="album_infobit_thumb"><div style="background-image: url('https://thumb-media.vgm.io/albums/34/42543/42543-1386329171.png')">
<a href="http://vgmdb.net/album/42543" title="Hyouri Ittai / YUZU"></a>
</div></div>
<ul class="album_infobit_detail">
<li><a class="albumtitle smallfont album-anime" href="http://vgmdb.net/album/42543" title="Hyouri Ittai / YUZU"><span class="albumtitle" lang="en" style="display:inline">Hyouri Ittai / YUZU</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>表裏一体 / ゆず</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>Hyouri Ittai / YUZU</span></a></li>
<li><span class="catalog smallfont album-anime">SNCC-89930</span></li>
<li>Dec 25, 2013</li>
</ul>
</div><div class="album_infobit_small smallfont label">
<div class="album_infobit_thumb"><div style="background-image: url('https://thumb-media.vgm.io/albums/85/40558/40558-1377894133.png')">
<a href="http://vgmdb.net/album/40558" title="HUNTER×HUNTER Select×Best×α"></a>
</div></div>
<ul class="album_infobit_detail">
<li><a class="albumtitle smallfont album-anime" href="http://vgmdb.net/album/40558" title="HUNTER×HUNTER Select×Best×α"><span class="albumtitle" lang="en" style="display:inline">HUNTER×HUNTER Select×Best×α</span><span class="albumtitle" lang="ja" style="display:none"><em> / </em>TVアニメ「HUNTER×HUNTER」 セレクト×ベスト×α</span><span class="albumtitle" lang="ja-Latn" style="display:none"><em> / </em>HUNTER×HUNTER Select×Best×α</span></a></li>
<li><span class="catalog smallfont album-anime">VPCG-84946</span></li>
<li>Sep 18, 2013</li>
</ul>
</div></span>

<br>
<b class="rbot"><b></b></b>
</div>



<br style="clear: left">

<div class="smallfont" style="width: 250px; background-color: #2F364F;">
<b class="rtop"><b></b></b>
<div style="padding: 6px 10px 6px 10px">

<div style="margin-bottom: 10px;"><img src="/db/img/arrowbit.gif" alt=""> <b class="label">Added</b><br>
Nov 8, 2014 <span class="time">01:20 PM</span></div>

<div style="margin-bottom: 10px;"><img src="/db/img/arrowbit.gif" alt="" border="0"> <b class="label">Edited</b><br>
Jun 18, 2021 <span class="time">05:24 PM</span></div>

<div style="margin-bottom: 10px;"><img src="/db/img/arrowbit.gif" alt=""> <b style="color: #788990">Page traffic</b><br>
<span class="time">4156</span> visitors</div>

<div><img src="/db/img/arrowbit.gif" alt=""> <b style="color: #788990">Page built in</b><br>
<span class="time">0.78</span> seconds</div>

</div>
<b class="rbot"><b></b></b>
</div>

</td></tr><tr><td valign="bottom" style="background-color: #1B273D;">

<!--div style="padding: 10px 10px 0px 10px">
<h3>Notes</h3>
</div-->
<div style="background-color: #2F364F;">
<div style="padding-left: 14px; padding-top:10px; padding-bottom: 6px;" class="smallfont">Source Category: <span style="color: #CEFFFF">Game</span>, <span style="color: yellowgreen">Animation</span>, <span style="color: white">Publication</span>, <span style="color: silver">Radio/Audio Drama</span>, <span style="color: #0FFFFF">Live Action</span>, <span style="color: pink">Tokusatsu/Puppetry</span>, <span style="color: #D2B48C">Multimedia Franchise</span>, <span style="color: violet">Game-adjacent</span>, <span style="color: cadetblue">Event</span>, <span style="color: #00BFFF">Artist Works</span><br>Extra Classification: <span style="color: yellow">Enclosure/Promo</span>, <span style="color: orange">Doujin/Indie</span>, <span style="color: seagreen">Delayed/Cancelled</span>, <span style="color: tomato">Bootleg</span></div>

<b class="rbot"><b></b></b>
</div>

</td></tr>
</tbody></table>



<script language="javascript" type="text/javascript">
$(document).ready(function() {
	$('#relnav li a').click(function() {
		$('#relnav li').removeClass('active');
		$(this).parent('li').addClass('active');
		$('.rel').hide();
		$('.' + $(this).attr('rel')).show();
		return false;
	});
});
</script>
<!-- / main page contents -->

</div>
<!-- /content area table -->
<div style="clear: both; height: 20px"></div>

<div class="alt1" style="width: 100%">
<div id="footer">
<div style="padding: 20px 10px 0 200px">



	<div style="float: right; text-align: right; font-family: Arial;" class="label">
		<a href="/about">About Us</a> •
		<a href="/faq">F.A.Q.</a> •
		<a href="/forums/sendmessage.php" rel="nofollow" accesskey="9">Contact Us</a> •
		<a href="/db/statistics.php" rel="nofollow">Statistics</a> •
		<a href="/album/random" rel="nofollow">Random Album</a> •
		<a href="https://vgmdb.net">Home</a>

		<div class="smallfont" style="font-family: Arial; margin-top: 10px">
		
		
		
		<a href="/forums/archive/index.php">Archive</a> •
		
		<a href="/privacy">Privacy Statement</a> •
		
		<a href="#top" onclick="self.scrollTo(0, 0); return false;">Top</a>
		</div>

	<div style="margin-top: 10px"><form action="index.php" method="get">
	
	
	

	</form></div>
	</div>

	<div class="label">
		<h3>VGMdb 1.4</h3>
		<div class="smallfont"><!-- Do not remove this copyright notice -->
		
		<!-- Do not remove this copyright notice --></div>
		<div class="smallfont">Site code and design copyright VGMdb.net</div>
		<div class="smallfont">Site material is property of their respective owners.</div>
		<div class="smallfont">All times are GMT -8. The time now is <span class="time">12:47 PM</span>.</div>
	</div>





</div></div></div>


<script type="text/javascript">
<!--
	// Main vBulletin Javascript Initialization
	vBulletin_init();
//-->
</script>
<script defer="" src="https://static.cloudflareinsights.com/beacon.min.js/v8c78df7c7c0f484497ecbca7046644da1771523124516" integrity="sha512-8DS7rgIrAmghBFwoOTujcf6D9rXvH8xm8JQ1Ja01h9QX8EzXldiszufYa4IFfKdLUKTTrnSFXLDkUEOTrZQ8Qg==" data-cf-beacon="{&quot;version&quot;:&quot;2024.11.0&quot;,&quot;token&quot;:&quot;ec81bd420a544cb0bdd98c8fb33e0228&quot;,&quot;r&quot;:1,&quot;server_timing&quot;:{&quot;name&quot;:{&quot;cfCacheStatus&quot;:true,&quot;cfEdge&quot;:true,&quot;cfExtPri&quot;:true,&quot;cfL4&quot;:true,&quot;cfOrigin&quot;:true,&quot;cfSpeedBrain&quot;:true},&quot;location_startswith&quot;:null}}" crossorigin="anonymous" style="display: none !important;"></script>

</body></html>"""
# soup = BeautifulSoup(test, "html.parser")
# print(soup.prettify())
