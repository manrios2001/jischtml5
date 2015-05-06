#WordDown is a tool for creating HTML5 from Microsoft Word  documents, using the Save as HTML... feature and then cleaning up the output.

# Introduction #

WordDown is an experimental tool for creating HTML from Microsoft Word and OpenOffice documents based on the same kind of ideas as lightweight wiki markup, but instead of using plain text cues it used the Word's WYSIWYG formatting.

It's called WordDown because it is intended to be used in the same kind of way as MarkDown to create clean high quality HTML only using the Word processor rather than plain text.


# How to run WordDown #

The simplest way to install WordDown is to drag this bookmarklet to your bookmarks toolbar in Chrome or Firefox. It should work in other browsers but current development is done in Chrome and Firefox, with irregular testing in Internet Explorer 8.

The code for the bookmarklet is here:
```
javascript:(function(){var head=document.getElementsByTagName('head')[0],script=document.createElement('script');script.type='text/javascript';script.src='http://tools.scholarlyhtml.org/bookmarklets/w2html5/w2html5-bookmarklet.js?' + Math.floor(Math.random()*99999);head.appendChild(script);})(); void 0
```

Once you have the bookmarklet:
  * Save a Word document as HTML using Word on Windows (any version from Word 2000 on). **Note:** Do not use the 'Filtered' HTML option.
  * Open the Word document in Crome (or whatever browser you like, but note that this is developed and tested on Chrome at the moment).
  * Hit the bookmarklet. The Word document should turn into a pure HTML5 page.
  * Save the document with a new name. (Chrome saves the new HTML5, not the original source TODO: test this behaviour in other browsers)


# Formatting and structure #

WordDown uses a mixture of direct formatting and styles. The only styles you really need to use are the built in heading styles - there are a few others that are optional.

| Headings | Use word's built in styles Heading 1 ... n or H1,Hn - WordDown creates sections automatically|
|:---------|:---------------------------------------------------------------------------------------------|
| Block Quotes | Any indent greater than the minimum for other paragraphs in the document will trigger a quote. Additional quanta of indenting will make things nest deeper |
| Lists  | Use any list formatting you like - the tool will try to detect the list type and it will nest lists correctly - styles not required but it will not hurt to use them |
| Code samples |Use courier or a monospaced font (Courier is recognized, you may need to add to the config to deal with others) - or the a paragraph style starting with 'Code' or 'Pre' (not case sensitive) |
| Inline Bold, italic etc | Just use Word's formatting or a style - but note that if you format a whole paragraph as bold the formatting **will** be discarded. |


# Semantics #
WordDown handles embedded HTML5 semantics. It can turn 'microformat' cues in documents into embedded semantic markup. Originally this was implemented using microdata but this has now changed to RDFa 1.1 Lite as this appears to be a better supported format for academic work.

**To mark up a Microdata Type**, use a link on a heading, or in a table:
For example if you mark up heading with a link to http://schema.org/Person then WordDown will create HTML5 like this:
```
<section <section vocab="http://schema.org/" typeof="http://schema.org/Person">>
<h1>All about me</h1>
```

(At the moment this only works for Schema.org types. TODO: the microformat will change to make it both more robust and more generic. The new way of doing this will be something like this, which if resolved will show a page that explains what is going on:
```
http://ontologize.me/?itemtype=http://schema.org/Person&triplink)
```

**To mark up a microdata property** use a style such as 'p-itemprop-name' or Normal-itemprop-name (character or paragraph styles both work, but paragraph styles are more robust if you are building a template for people to fill out). So if you add a paragraph after the heading then you will get this:

```
<section itemscope itemtype="http://schema.org/Person">
<h1>All about me</h1>
<p itemprop="name">Bootsy</p>
```

# Slides #
To embed a slide, use a heading with style h$n-Slide where $n is 1-5. If you do this in 'free text' the slide will end at the next heading of the same level - so h3-Slide will create a slide up to the next h3 whether it is a slide or not.

If you put a h1-Slide and susequent slide content in a single-cell table then that will turn into a slide as well.

WordDown creates markup like this, identifiying slides using the Bibo Bibliographic ontology:

```

<section typeof="http://purl.org/ontology/bibo/Slide">

</section>

```

# Citations and references #
WordDown originally worked with Zotero 3 to add citation data to HTML5 documents. If you use Zotero to insert citations WordDown creates in-text citations that can be machine-processed to do interesting things such as reformat the paper to use a particular citation style that suits the reader. This functionality will be removed and replaced with  something simpler. Dicsussion on the JISCHTML5 project concluded that embedding citation data is only important where there are no good sources to look up references, ideally citation should be by URI.



TODO: More examples.