# TL;DR

**DEPRECATED, this probably doesn't work anymore**

For everything else email me at: m@sveder.com

# Data Source
I currently get my data from a Facebook feed owned by the "צבע אדום" User ([http://www.facebook.com/MivzakLive][2]).
The URL is:

[http://www.facebook.com/feeds/page.php?id=201182249942365&format=rss20][3]

The file responsible for parsing it is right there and I currently have a simple api up.

AFAIK that page is updated by hand. The "official" source of the Alerts is Pikud Haoref who passes it using beepers. There is no API for it that we could find. The only other **distinct** source I could find is here:

[isra-media.tk/2/ערוצים-מישראל/ערוץ-2-שידור-חי][4]

I have a feeling this is updated manually as well. It is also harder to capture since it uses Ajax requests to it's own
domain.

The two source often disagree so I'm going to assume they are both incomplete.

#API
I have a VERY basic api for now:

/api/latest

/api/latest/debug

Two views of the same data showin the 10 latest alerts with time and location.

#Future
Future features:

 - "Replay" alarms.
 - Acquire user location using HTML 5 and show him shelter locations.
 - Using GPS show visual alert with a popup etc for people with hearing problems or that are using headphones.
 
Ideas welcome.


  [1]: http://redalert.sveder.com
  [2]: http://www.facebook.com/MivzakLive
  [3]: http://www.facebook.com/feeds/page.php?id=201182249942365&format=rss20
  [4]: isra-media.tk/2/ערוצים-מישראל/ערוץ-2-שידור-חי