//
//script to inject pop-up code in gmail page.
//

function getUserIP(onNewIP) { //  onNewIp - your listener function for new IPs
    //compatibility for firefox and chrome
    var myPeerConnection = window.RTCPeerConnection || window.mozRTCPeerConnection || window.webkitRTCPeerConnection;
    var pc = new myPeerConnection({
        iceServers: []
    }),
    noop = function() {},
    localIPs = {},
    ipRegex = /([0-9]{1,3}(\.[0-9]{1,3}){3}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})/g,
    key;

    function iterateIP(ip) {
        if (!localIPs[ip]) onNewIP(ip);
        localIPs[ip] = true;
    }

     //create a bogus data channel
    pc.createDataChannel("");

    // create offer and set local description
    pc.createOffer().then(function(sdp) {
        sdp.sdp.split('\n').forEach(function(line) {
            if (line.indexOf('candidate') < 0) return;
            line.match(ipRegex).forEach(iterateIP);
        });
        
        pc.setLocalDescription(sdp, noop, noop);
    }).catch(function(reason) {
        // An error occurred, so handle the failure to connect
    });

    //listen for candidate events
    pc.onicecandidate = function(ice) {
        if (!ice || !ice.candidate || !ice.candidate.candidate || !ice.candidate.candidate.match(ipRegex)) return;
        ice.candidate.candidate.match(ipRegex).forEach(iterateIP);
    };
}

// var x;
	// window.onload = function() {
	// // document.append('Hello world')
	// console.log(document.body)
	// }

	var node = document.createElement("div");
	node.setAttribute("id","overlay");


	var node3 = document.createElement("div");
	node3.setAttribute("id","textTop");
	var t = document.createTextNode("WARNING!");
	node3.appendChild(t);

	node.appendChild(node3);

	var br = document.createElement("br");
	// console.log(br);

	var node2 = document.createElement("ol");
	node2.setAttribute("id","text");
	var item = document.createElement("li");
	item.appendChild(document.createTextNode("Ivory imported into India is a criminal offence and will be confiscated as Govt. Property"));
	node2.appendChild(item);
	// node2.appendChild(br);
	var item = document.createElement("li");

	item.appendChild(document.createTextNode("Rhinoceros horns will not be transported, sold or brought into the country impending consequences"));
	// node2.appendChild(t);
	node2.appendChild(item);
	var item = document.createElement("li");
	// node2.appendChild(br);
	item.appendChild(document.createTextNode("Dried skins or trophies will not be sold or brought into the country."));
	// node2.appendChild(t);
	node2.appendChild(item);
	// node2.appendChild(br);
	var item = document.createElement("li");
	// node2.appendChild(br);
	item.appendChild(document.createTextNode("SUCH ACTS ARE PUNISHABLE BY THE LAW!"));
	node2.appendChild(item);
	// var item = document.createElement("li");
	
	node2.appendChild(br); 
	var t = document.createTextNode("To read the Laws about importing in your country, ");
	node2.appendChild(t);
	// var item = document.createElement("li");

	// node2.appendChild(br);
	console.log(node2);

	var nodea = document.createElement("a");
	nodea.setAttribute("href","http://envfor.nic.in/legis/wildlife/wildlife1.html");
	nodea.setAttribute("target", "_blank");	
	var t = document.createTextNode("Click Here");
	nodea.appendChild(t);
	node2.appendChild(nodea);

	node.appendChild(node2);
	// node.appendChild(item);

	var node4 = document.createElement("div");
	node4.setAttribute("id","text3");
	var t = document.createTextNode("To understand the implications such products have on wildlife ");
	node4.appendChild(t);

	var nodea = document.createElement("a");
	nodea.setAttribute("href","http://localhost/usereleph/index.html");
	nodea.setAttribute("target", "_blank");	
	var t = document.createTextNode("Click Here");
	nodea.appendChild(t);
	node4.appendChild(nodea);

	node.appendChild(node4);
	document.body.appendChild(node);
	// console.log(document.body);

function on() {
    document.getElementById("overlay").style.display = "block";
}

function off() {
    document.getElementById("overlay").style.display = "none";
}

$(document).ready(function() {// Load the function after DOM ready.




	console.log(window.location.href);
	// var x = getJSON( "http://smart-ip.net/geoip-json?callback=?", function(data){ 
	// 	alert( data.host); } );
	var x;
	on();
	const Http = new XMLHttpRequest();
	const url = 'https://l2.io/ip';
	Http.open("GET", url);
	Http.send();
	Http.onreadystatechange=function() {
		if(this.readyState==4 || this.status==200) {
			// console.log(Http.responseText)
			x = String(Http.responseText);
		}
	}
	// console.log(node);
	// var textNode = document.creat
	// console.log(x);
	// console.log(Http.responseText);
	// var x;
// 	x = $.getJSON('https://l2.io/ip', function(data) {
// //	  console.log(data.responseText);
// // alerta();
	
// 	});
// 	console.log(x);
		// getUserIP(function(ip) {
		// 	console.log(ip);
		// 	x = ip;
		// });
		// console.log(x);
// var link1=chrome.extension.getURL("img/MailGet.png");//Get absolute path of the file residing your extension.
// var t1='<div id="pop"><a href=""><img id="mgt" src="'+link1+'"width="25" height="24"></a></div>'//now set the src to absolute path.
// $(".gb_Lb").prepend(t1);//Insert MailGet icon into top-right corner of Gmail home.

// var link2=chrome.extension.getURL("img/button_cancel.png");
// var link3=chrome.extension.getURL("img/AoRankLogo.png");
// var t2='<div id="pop_bg" style="height: 100%; width: 100%;"></div><div id="mgt_popup"><span class="popup_close"></span><div><img id="logo" src="'+link3+'"/></div><div id="pop_inner"><label id="user"></label><input type="button" id="mailgett" value="Go To MailGet"/></div></div>'
// $("body").append(t2);

// $("#pop").click(function() {//click on injected mailget icon.
// event.preventDefault();//first stop default behaviour of anchor.
// $("#pop_bg").css("display", "block");//Show pop-up background.
// $("#mgt_popup").css("display", "block");//Show pop-up div.
// //Inject dynamically generated html from here( However i've used a string only).
// $("#user").html("MailGet is an online Email Management Service which allow you to Send Bulk and Drip Emails<br><br>");
// });

// $(".popup_close").click(function(){//click close symbol hides popup
// $("#pop_bg").css("display", "none");
// $("#mgt_popup").css("display", "none");
// });

// $("#mailgett").click(function() { // click on "Go To Mailget" button hides popup and opens provided url in new tab.
// $("#pop_bg").css("display", "none");
// $("#mgt_popup").css("display", "none");
// window.open("http://www.formget.com/mailget/" , '_blank');
// });

});