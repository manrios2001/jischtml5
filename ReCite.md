#Javascript code/bookmarklet to reform ciations in HTML5 pages

# Introduction #

ReCite is a tool to enable readers to reformat the citation and references in HTML5 pages.

NOTE: This is an early version with limited features. More will be added to this tool over the coming weeks. Currently the only supported citation format is that used by Zotero 3, but as part of the jiscHTML5 project we hope to bring interop with other reference managers and online sources of citation data.

NOTE: The Citeproc.js library does not work properly in Chrome - so this currently runs only in Firefox.

TODO: Add issue tickets for the features below.
| Feature | Done? |
|:--------|:------|
| Embedding citations using JISCHTML5 conventions for HTML5 microdata | Done |
| Embedding data in-page using Zotero JSON format and dataURIs, via the WordDown conversion tool | Done |
| Embedding data in-page using jiscHTML5 conventions for full-citation microdata | TODO (need to agree on format) |
| Simple reformatting using a few demo styles | DONE |
| Show summary of citation data in tabular form on hover over in text citation | TODO |
| Allow user to choose any CSL stylesheet from the standard otero library | TODO |
| Allow user to use custom stylesheet | TODO |
| Fetch data from the web from a variety of sources rather than using inline data - building on this work: http://hublog.hubmed.org/archives/001946.html | TODO |


# Getting ReCite #
To get ReCITE, drag this bookmarklet to your browser links bar:
http://hublog.hubmed.org/archives/001946.html

> <a href="javascript:(function(){var head=document.getElementsByTagName('head')[0],script=document.createElement('script');script.type='text/javascript';script.src='http://jischtml5.googlecode.com/git/tools/bookmarklets/recite/recite-bookmarklet.js';head.appendChild(script);})(); void 0">ReCite</a>